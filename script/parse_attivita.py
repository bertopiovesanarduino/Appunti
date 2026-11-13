import argparse
import html
import json
import re
from collections import OrderedDict
from datetime import date
from html.parser import HTMLParser
from pathlib import Path


MONTHS = {
    "Gen": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "Mag": 5,
    "Giu": 6,
    "Lug": 7,
    "Ago": 8,
    "Set": 9,
    "Ott": 10,
    "Dic": 12,
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12,
}
FIELDS = ("data", "ora", "docente", "materia", "descrizione")


def clean_text(value: str, *, preserve_newlines: bool = False) -> str:
    lines = [re.sub(r"\s+", " ", line).strip() for line in value.splitlines()]
    lines = [line for line in lines if line]
    return "\n".join(lines) if preserve_newlines else " ".join(lines)


def parse_date(heading: str) -> str:
    match = re.search(r",\s*(\d{1,2})\s+([A-Za-z]{3})\s+(\d{4})", heading)
    if not match:
        raise ValueError(f"Data non riconosciuta nell'intestazione: {heading!r}")

    day, month_name, year = match.groups()
    month = MONTHS.get(month_name.title())
    if month is None:
        raise ValueError(f"Mese non riconosciuto nell'intestazione: {heading!r}")
    return date(int(year), month, int(day)).isoformat()


class ActivityParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.activities: list[dict[str, str]] = []
        self.current_date: str | None = None
        self._heading_text: list[str] | None = None
        self._cells: list[str] | None = None
        self._cell_text: list[str] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "h2":
            self._heading_text = []
        elif tag == "tr":
            self._cells = []
        elif tag == "td" and self._cells is not None:
            self._cell_text = []

    def handle_data(self, data: str) -> None:
        if self._heading_text is not None:
            self._heading_text.append(data)
        if self._cell_text is not None:
            self._cell_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "h2" and self._heading_text is not None:
            self.current_date = parse_date(clean_text("".join(self._heading_text)))
            self._heading_text = None
        elif tag == "td" and self._cell_text is not None:
            assert self._cells is not None
            self._cells.append("".join(self._cell_text))
            self._cell_text = None
        elif tag == "tr" and self._cells is not None:
            if self._cells:
                if len(self._cells) != 4:
                    raise ValueError(
                        f"Riga attività non valida: attesi 4 campi, trovati {len(self._cells)}"
                    )
                if self.current_date is None:
                    raise ValueError("Riga attività trovata prima di una data")
                self.activities.append(
                    {
                        "data": self.current_date,
                        "ora": clean_text(self._cells[0]),
                        "docente": clean_text(self._cells[1]),
                        "materia": clean_text(self._cells[2]),
                        "descrizione": clean_text(self._cells[3], preserve_newlines=True),
                    }
                )
            self._cells = None


def activity_key(activity: dict[str, str]) -> tuple[str, ...]:
    return tuple(activity[field] for field in FIELDS)


def load_existing(json_path: Path) -> list[dict[str, str]]:
    if not json_path.exists():
        return []

    existing = json.loads(json_path.read_text(encoding="utf-8"))
    if not isinstance(existing, list):
        raise ValueError(f"{json_path} deve contenere un array JSON")

    records: list[dict[str, str]] = []
    for index, item in enumerate(existing):
        if not isinstance(item, dict) or any(
            not isinstance(item.get(field), str) for field in FIELDS
        ):
            raise ValueError(
                f"Record JSON non valido all'indice {index}: richiesti i campi {FIELDS}"
            )
        records.append({field: item[field] for field in FIELDS})
    return records


def render_markdown(activities: list[dict[str, str]]) -> str:
    grouped: OrderedDict[str, list[dict[str, str]]] = OrderedDict()
    for activity in activities:
        grouped.setdefault(activity["data"], []).append(activity)

    sections = ["# Attività svolte"]
    for activity_date, records in grouped.items():
        sections.extend(
            [
                "",
                f"## {activity_date}",
                "",
                "| Ora | Docente | Materia | Descrizione |",
                "| --- | --- | --- | --- |",
            ]
        )
        for record in records:
            cells = [
                record["ora"],
                record["docente"],
                record["materia"],
                record["descrizione"],
            ]
            escaped = [
                html.escape(value, quote=False)
                .replace("|", r"\|")
                .replace("\n", "<br>")
                for value in cells
            ]
            sections.append("| " + " | ".join(escaped) + " |")
    return "\n".join(sections) + "\n"


def main() -> None:
    default_dir = Path(__file__).resolve().parent
    arg_parser = argparse.ArgumentParser(
        description="Estrae le attività dall'HTML e le aggiunge senza duplicati."
    )
    arg_parser.add_argument("--input", type=Path, default=default_dir / "INPUT.TXT")
    arg_parser.add_argument("--json", type=Path, default=default_dir / "attivita.json")
    arg_parser.add_argument(
        "--markdown", type=Path, default=default_dir / "attivita.md"
    )
    args = arg_parser.parse_args()

    parser = ActivityParser()
    parser.feed(args.input.read_text(encoding="utf-8"))
    parser.close()

    activities = load_existing(args.json)
    seen = {activity_key(activity) for activity in activities}
    new_activities = []
    for activity in parser.activities:
        key = activity_key(activity)
        if key not in seen:
            seen.add(key)
            new_activities.append(activity)
    activities.extend(new_activities)

    args.json.write_text(
        json.dumps(activities, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    args.markdown.write_text(render_markdown(activities), encoding="utf-8")
    print(
        f"Attività lette: {len(parser.activities)}; "
        f"nuove: {len(new_activities)}; totali: {len(activities)}"
    )


if __name__ == "__main__":
    main()

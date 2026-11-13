import argparse
import json
import re
import unicodedata
from collections import defaultdict
from datetime import date
from pathlib import Path


REQUIRED_FIELDS = ("data", "ora", "materia", "descrizione")


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_text.casefold()).strip("-")
    return slug or "materia"


def load_activities(input_path: Path) -> list[dict[str, str]]:
    data = json.loads(input_path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError(f"{input_path} deve contenere un array JSON")

    activities = []
    for index, item in enumerate(data):
        if not isinstance(item, dict) or any(
            not isinstance(item.get(field), str) for field in REQUIRED_FIELDS
        ):
            raise ValueError(
                f"Attività non valida all'indice {index}: "
                f"richiesti i campi {REQUIRED_FIELDS}"
            )
        date.fromisoformat(item["data"])
        activities.append(item)
    return activities


def hour_number(value: str) -> int:
    match = re.match(r"\s*(\d+)", value)
    return int(match.group(1)) if match else 0


def render_subject_markdown(
    subject: str, activities: list[dict[str, str]]
) -> str:
    ordered = sorted(
        activities,
        key=lambda activity: (
            -date.fromisoformat(activity["data"]).toordinal(),
            hour_number(activity["ora"]),
        ),
    )
    lines = [f"# Attività di {subject}", ""]
    for activity in ordered:
        day = date.fromisoformat(activity["data"]).strftime("%d/%m/%Y")
        description = activity["descrizione"].replace("\r\n", "\n").replace("\r", "\n")
        description = description.replace("\n", "\n  ")
        lines.append(f"- **{day} ({activity['ora']}):** {description}")
    return "\n".join(lines) + "\n"


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(
        description="Crea un file Markdown con le attività per ogni materia."
    )
    parser.add_argument("--input", type=Path, default=base_dir / "attivita.json")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=base_dir / "ARGOMENTI_PER_MATERIA",
    )
    args = parser.parse_args()

    by_subject: dict[str, list[dict[str, str]]] = defaultdict(list)
    for activity in load_activities(args.input):
        subject = activity.get("materia")
        if not isinstance(subject, str) or not subject.strip():
            raise ValueError("Trovata un'attività senza materia")
        by_subject[subject.strip()].append(activity)

    slugs: dict[str, str] = {}
    for subject in by_subject:
        slug = slugify(subject)
        if slug in slugs:
            raise ValueError(
                f"Conflitto tra i nomi file per {slugs[slug]!r} e {subject!r}"
            )
        slugs[slug] = subject

    args.output_dir.mkdir(parents=True, exist_ok=True)
    for slug, subject in slugs.items():
        output_path = args.output_dir / f"{slug}.md"
        output_path.write_text(
            render_subject_markdown(subject, by_subject[subject]),
            encoding="utf-8",
        )

    print(
        f"Create {len(slugs)} file per {sum(map(len, by_subject.values()))} attività "
        f"in {args.output_dir}"
    )


if __name__ == "__main__":
    main()

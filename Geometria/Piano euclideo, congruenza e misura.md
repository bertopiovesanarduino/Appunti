# Piano euclideo, congruenza e misura

## Passaggio dal metodo induttivo al metodo deduttivo

### Impostazione assiomatico-deduttiva della geometria

Fino ad ora sei stato abituato a vedere i concetti di geometria e a comprenderli utilizzando il metodo induttivo. Da ora in poi la geometria verrà studiata utilizzando il metodo deduttivo. 👈

#### Ragionamento induttivo 

🤔 Spieghiamo il metodo con un esempio: Consideriamo alcune terne di numeri consecutive: 

$ 1+2+3 = 6 $ oppure $ 2+3+4 = 9 $ oppure ancora $ 3+4+5 = 12 $

Dall'osservazione di alcuni casi possiamo quindi ipotizzare che la somma di terne di numeri successivi sarà darà come risultato un multiplo di tre. Questo tipo di ragionamento è chiamato **induttivo** e il ragionamento fatto ha prodotto una **congettura**. ⚠️ La congettura è un osservazione che con buona probabilità è vera, ma non è dimostrata.

#### Ragionamento deduttivo 👈

Il metodo induttivo ci permette di scoprire delle nuove proprietà (**formulare congettura**), ma non ci permette di **dimostrare**.

Il metodo deduttivo è il metodo con cui studieremo la gemoetria, più in particolare il metodo **assiomatico-deduttivo**.

🎯 Si basa su quattro concetti *fondamentali*: 

1. **Concetti primitivi**: Concetti assunti senza che ne sia data una definizione (punto di partenza) che saranno il punto di partenza per le definizioni.
2. **Assiomi** o **Postulati**: Proposizioni (affermazioni) accettate come **vere** senza giustificazioni.
3. La **definizione** di un nuovo oggetto avviene facendo uso **SOLO** di **concetti primitivi** e **assiomi** o **postulati**.
4. Mediante regionamento di tipo deduttivo chiamato **dimostrazione** si deducono altre preposizioni dette ✅ teoremi.


## Cosa è la geometria?
- La geometria è la branca della matematica che studia le figure geometriche
## Cosa sono i concetti primitivi?
- Si assumono alcuni concetti come primitivi, senza, cioè senza darne una definizione; la necessità di assumere dei concetti primitivi deriva dal fatto che ogni definizione deve contenere termini di cui si conosce già il significato, ossia termini di cui sono già state date le definizioni. anche queste definizioni contengono dei termini che devono essere defini e così via, per questo motivo ci siamo posti alla base dei concetti primitivi
## Gli assiomi
- Si assumono alcune proposizioni, dette assiomi (o postulati), che si decide di accettare come vere, senza darne giustificazioni
## Ogni nuovo oggetto si definisce attraverso delle definizioni
- Che facciano uso solo dei concetti primitivi o di altre espressioni di cui si sia già stabilito il significato.
## Le dimostrazioni
- Chiamiamo dimostrazioni un insieme di ragionamenti di tipo deduttivo, chiamato dimostrazione, si deducono altre proposizioni, detti teoremi. Un teorema è un enunciato vero, che viene dimostrato.

## esempio pratico
### gioco del tris
- parole chiavi del gioco: concetti primitivi
- regole del gioco: assiomi
- Un teorema potrebbe essere questo:

| &nbsp; | &nbsp; | &nbsp; |
|:---:|:---:|:---:|
| x | x |   |
| o | x |   |
|   |   | o |

- "Se il mio simbolo è x e se ci troviamo nella situazione descritta nella figura sopra allora ho vinto

- Una *dimostrazione* di questo teorema è la seguente:
  «Il mio avversario porrà il suo simbolo **o** in una delle due posizioni in cui minaccio di chiudere (in alto a destra o in basso al centro); ma, in ciascuno dei due casi, potrò comunque vincere ponendo il simbolo **x** nell'altra posizione libera».

  **Caso 1** (L'avversario gioca in alto a destra, io vinco in basso al centro):
  
  | &nbsp; | &nbsp; | &nbsp; |
  |:---:|:---:|:---:|
  | x | x | **o** |
  | o | x | &nbsp; |
  | &nbsp; | **x** | o |

  **Caso 2** (L'avversario gioca in basso al centro, io vinco in alto a destra):
  
  | &nbsp; | &nbsp; | &nbsp; |
  |:---:|:---:|:---:|
  | x | x | **x** |
  | o | x | &nbsp; |
  | &nbsp; | **o** | o |

  # I concetti primitivi
  - come concetti primitivi consideriamo i concetti di: punto, retta e piano
  - I punti vanno assegnati con le lettere maiuscole dell' alfabeto
  - Le rette con le lettere minuscole dell' alfabeto
  - I piani con le lettere minuscole dell'alfabeto greco

## Assioma 1
- Ogni piano è un insieme di punti. Ogni retta è un sottoinsieme del piano

## assioma 2
- Assiomi di appartenenza alla retta
- Ad ogni retta appartengono almeno due punti distinti
- Dati due punti distinti, esiste una e una sola retta alla quale appartengono entrambi
- Data una retta nel piano, esiste almeno un punto del piano che non appartiene a essa
- due rette distinte possono avere in comune solo un punto: infatti se avessero 2 o più punti in comune coinciderebbero
- tre ounti che appartengono a una medesima retta vengono detti *ALLINEATI*
- la retta può essere percorsa in due versi
    - quando si fissa un verso di percorrenza la retta viene detta *ORIENTATA* e, dati due punti distinti A e B sulla retta è possibile stabilire se A precede o segue B

## assioma 3
 - dati due punti distinti A e B, tali che A precede B, esiste sempre un punto C compreso tra A e B (cioè tale che A precede C e C precede B)
 - dato un punto P, esistono sempre due punti A e B, tali che A precede P e P precede B

## definizione fascio di rette
 - L'insieme delle rette che passano per un punto del piano si chiama fascio proprio di rette; il punto per cui passano tutte le rette del fascio si chiama centro del fascio

## Definizione semiretta
 - Data una retta e un suo punto, si chiama semiretta la figura costituita dal punto e da una delle due parti in cui la retta è divisa dal punto stesso. Il punto si dice origine della semiretta

## Definizione di segmento
 - Dati due punti A e B su di una retta, chiamiamo segmento AB l'insieme costituito dai due punti A e B e da tutti i punti compresi tra A e B e da tutti i  punti compresi tra A e B
 - I punti A e B si dicono estremi del segmento; i punti del segmento diversi dagli estremi si dicono interni al segmento

## Definizione di segmenti consecutivi e segmenti adiacenti
 - Due segmenti che hanno in comune uno e un solo estremo si dicono consecutivi
 - Due segmenti consecutivi che appartengono alla stessa retta si dicono adiacenti

## Poligonale
 - Si chiama poligonale la figura formata da un insieme formata da un insieme ordinato di segmenti, tali che:
    - Ciascun segmento e il suo successivo siano consecutivi ma non adiacenti;
    - Ciascun estremo dei segmenti sia in comune al massimo a due di essi. 
 - I segmenti si dicono lati della poligonale e i loro estremi vertici della poligonale.

## Figure convesse e concave
 - Una figura geometrica F si dice convessa se, comunque scelti due punti A, B (apparteneti a) F, il segmento AB è tutto contenuto in F. Una figura non convessa si dice concava.

## Assioma 4
 - Consideriamo una retta r nel piano. L'insieme dei punti del piano che non appartengono a r resta diviso da r in due sottoinsiemi disgiunti e convessi, (alfa) e (beta), tali che, se A appartiene a (alfa) e B appartiene a (beta), allora il segmento AB interseca la retta r in uno e un solo punto

 ## Definizione semipiano
  - Data una retta in un piano, si chiama semipiano la figura costituita dalla retta e da una delle due parti in cui il piano è diviso dalla retta stessa. La retta si dice origine (o frontiera) del semipiano.

 ## Definizione angolo
  - Date in un piano 2 semirette aventi la stessa origine, si chiama angolo la figura costituita dalle due semirette e da una delle due parti in cui il piano è diviso dalle semirette stesse. L'origine delle due semirette si chiama vertice dell' angolo e le due semirette si chiamano lati dell'angolo

 ## Definizioni angoli consecutivi e angoli adiacenti
  - Due angoli si dicono consecutivi se hanno lo stesso vertice e se hanno in comune soltanto i punti di un lato.
  - Due angoli si dicono adiacenti se sono consecutivi e se i lati non comuni appartengono alla stessa retta

 ## Definizioni angoli opposti al vertice
  - Due angoli si dicono opposti al vertice se sono convessi e i lati dell'uno sono i prolungamenti dei lati dell'altro

 ## Definizione poligono
  - Consideriamo una poligonale chiusa e non intrecciata. Chiamiamo poligono la figura formata dalla poligonale e dai punti interni ad essa. i vertici e i lati della poligonale si chiamano vertici e lati del poligono.

 ## Assioma 5 (primo assioma di congruenza)
  - Ogni figura è congruente a sé stessa (proprietà riflessiva)
  - Se la figura F1 è congruente alla figura F2 allora la figura F2 è congruente a F1 (proprietà simmetrica)
  - Se la figura F1 è congruente alla figura F2 e la figura F2 è congruente alla figura F3, allora F1 è congrunte a F3 (proprietà transitiva)

 ## Assioma 6 (congruenza di punti, semirette, piani e semipiani)
  - Tutti i punti sono congruenti fra loro, e così purele rette, le semirette, i piani e i semipiani
 
 ## Assioma 7 (trasporto dei segmenti e degli angoli)
  - Dato un segmento AB e una semiretta di origine O, esiste un unico punto P sulla semiretta, tale che AB è congruente a OP
  - Dato un angolo a^O^b e una semiretta a1 di origine O1, su ognuno dei due semipiani individiuali dalla retta cui appartiene la semiretta a1 esiste una unica semiretta b1, di originev=1, tale che a1^O^b1 è congruente ad a^O^b

 ## Definizione poligono regolare
  - Un poligono che ha tutti i lati congruenti e tutti gli angoli congruenti si dice regolare

 ## Definizione punto medio
  - Dato un segmento, si dice punto medio del segmento il punto che lo divide in due segmenti congruenti

## Domande per allenarsi a ripetere
1. Che cosa studia la geometria?
2. Che cosa sono i concetti primitivi e perché è necessario assumerli?
3. Che cosa sono gli assiomi o postulati?
4. Come si definisce un nuovo oggetto geometrico?
5. Che cosa sono una dimostrazione e un teorema?
6. Nell'esempio del tris, che cosa rappresentano le parole chiave e le regole del gioco?
7. Quali sono i concetti primitivi della geometria considerati in questi appunti? Come si indicano punti, rette e piani?
8. Che cosa afferma il primo assioma?

## Dimostrazioni sui segmenti
1. Ipotesi: assiomi riferiti al disegno a cui ci si basa nella dimostrazione
2. Disegno: disegno con tutti i dati visibili
3. Tesi: proposta da poi verificare
4. Dimostrazione: Dimostrazione della tesi
5. Quadrato nero (fine dimostrazione)
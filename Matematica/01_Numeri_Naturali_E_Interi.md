# Cap 1 - Numeri naturali e numeri interi
## Numeri naturali

Il loro insieme si indica con: 
 $$N = \{0,1,2,3, \dots\}$$
I numeri natuali possono essere rappresentati su una *semiretta ordinata*, con:
- un **origine** "O" 
- una freccia che rappresenta il **verso**.
- i segni sulla retta sono equidistanti tra loro di una distanza *unitaria*.

Essendo una retta ordinata possiamo definire le seguenti operazioni di confronto:

- minore
- maggiore
- minore o uguale
- maggiore o uguale

Possiamo quindi scrivere:

 $$ 7 \gt 2 $$ $$ 5 \gt 3 $$ $$ 8 \ge 1 $$

E definire il **concetti di**
 $$ precedente / successivo $$

Per ogni numero natuale esiste sempre il suo successivo $$ 1 \longrightarrow 2 \longrightarrow 3 $$

e per questo motivo non esiste un numero nel mezzo. L'insieme dei numeri natuali è si definisce come un insieme

 $$ discreto $$

## Proprietà delle operazioni in N

### Proprietà dell'addizione e della moltiplicazione

- Legge dell'annullamento del prodotto (a*b = 0 solo se a=0 o b=0)
- Proprietà commutativa dell'addizione (a+b = b+a)
- Proprietà commutativa della moltiplicazione (a*b = b*a)
- Proprietà associativa dell'addizione (a+b)+c = a+(b+c)
- Proprietà associativa della moltiplicazione (a*b)*c = a*(b*c)
- Proprietà distributiva della moltiplicazione rispetto all'addizione: 
    - a*(b+c) = a*b + a*c (semplificazione a sinistra)
    - (a+b)*c = a*c + b*c (semplificazione a destra)

### Properietà della sottrazione e della divisione

- Definizione sottrazione: 
    - Operazione inversa della addizione
    - a-b = d
        - a = minuendo
        - b = sottraendo
        - c = differenza
- Definizione divisione: 
    - Operazione inversa della moltiplicazione
    - a/b=q
        - a = dividendo
        - b = divisore
        - c = quoziente
    - Ogni divisione con divisore 0 viene considerata impossibile
    - Proprietà distributiva della moltiplicazione rispetto alla sottrazione: 
        - $ a \cdot (b - c) = a \cdot b - a \cdot c $ (semplificazione a sinistra)
        - $ (a - b) \cdot c = a \cdot c - b \cdot c $ (semplificazione a destra)
    - Proprietà distributiva della divisione rispetto all'addizione e alla sottrazione
    c != 0
        - $ (a + b) \div c = a \div c + b \div c $
        - $ (a - b) \div c = a \div c - b \div c $
    - Proprietà invariantiva della sottrazione
        - $ a - b = (a + c) - (b + c) $
        - $ a - b = (a - c) - (b - c) $
    - Proprietà invariantiva della divisione
        - $ a \div b = (a \cdot c) - (b \cdot c) $
        - $ a \div b = (a \div c) - (b \div c) $

## Proprietà delle potenze in N

### Prodotto di potenze con la stessa base
- Il prodotto di potenze con la stessa base è una potenza che ha la stessa base e come esponente la somma degli esponenti

$$a^m \cdot a^n = a^{m+n}$$
### Quoziente di potenze con la stessa base
- Il quoziente di potenze con la stessa base è una potenza che ha la stessa base e come esponente la differenza degli esponenti

$$a^m \div a^n = a^{m-n}$$
### Potenze di Potenze
- La potenza di una potenza è una potenza che ha la stessa base e come esponente il prodotto degli esponenti 

$$(a^m)^r = a^{m \dot r}$$
### Prodotto di potenze con lo stesso esponente
- Il prodotto di potenze con lo stesso esponente è una potenza che ha lo stesso esponente e come base il prodotto delle basi 

$$(a^m) \dot (b^m) = a \dot b^{m}$$
### Quoziente di potenze con lo stesso esponente
- Il quoziente di potenze con lo stesso esponente è una potenza che ha lo stesso esponente e come base il quoziente delle basi 
- Con b != da 0 e a divisibile per b
$$(a^m) \div (b^m) = a \div b^{m}$$
## Multipli divisori, MCD, mcm
### Multipli
- Un numero naturale $ a $ è multiplo di un numero naturale $ b $  se esiste un numero naturale $ q $ che moltiplicato per b dà a.
$$ a = q \dot b $$
### Divisori
- Un numero naturale $ b $, diverso da 0,è divisore di un altro numero naturale $ a $ se la divisione tra $ a $ e $ b $ è esatta, cioè ha resto 0. 
$$ a \div b = q $$
### MCD
- Il MCD è il prodotto dei fattori comuni, presi una sola volta, con l'esponente minore
### mcm
- Il mcm è il prodotto di tutti i fattori comuni e non comun, presi una sola volta, con l'esponente maggiore
### esempio MCD mcm
#### Trovare l'MCD e l'mcm di 120 e 140

- Scomposizione in fattori primi di 120:
  $$120 = 2^3 \cdot 3 \cdot 5$$

- Scomposizione in fattori primi di 140:
  $$140 = 2^2 \cdot 5 \cdot 7$$

- **MCD** (fattori comuni con l'esponente minore):
  $ \text{MCD}(120, 140) = 2^2 \cdot 5 = 20 $

- **mcm** (tutti i fattori, comuni e non comuni, con l'esponente maggiore):
  $ \text{mcm}(120, 140) = 2^3 \cdot 3 \cdot 5 \cdot 7 = 840 $


### Numero primo
- Un numero naturale diverso da 0 e da 1 è un numero primo se ha come divisori solo se stesso e 1

## Numeri interi
- Consideriamo numero intero ogni numero naturale diverso da zero facendo precedere il numero dal segno + e dal segno -. vengono indicati con Z (relativi)

## Operazioni in Z e proprietà
### somma di due numeri concordi
- segno uguale a quello degli addendi e valore assoluto uguale alla somma dei valori assoluti dei due numeri
### somma di due numeri discordi
- segno uguale a quello dell' addendo con valore assoluto maggiore, valore assoluto uguale alla differenza tra il valore assoluto maggiore e quello minore.
### differenza di due interi 
- somma del minuendo con l'opposto del sottraendo
### prodotto di due interi (diversi da 0)
- è un intero che ha segno positivo se i fattori sono concordi, segno negativo se sono discordi;
- valore assoluto uguale al prodotto dei valori assoluti dei fattori
### quoziente di due interi (diversi da 0)
- segno positivo se divisore e dividendo sono concordi, segno negativo se sono discordi
- valore assoluto uguale al quoziente dei valori assoluti del dividendo e del divisore
## Potenze in Z
# Vsebinski načrt:

## Opis aplikacije:

Na sredini okna bo igralna plošča, katera bo imela več vrstic z vžigalicami. Nad igralno ploščo bosta gumb za novo igro in gumb za razveljaviti zadnjo potezo (undo). V desnem kotu bo  napisano kdo je na potezi.  Desno od igralne plošče bo za izbirati, kako želiš igrati novo igro (računalnik- računalnik, človek- računalnik, človek-človek), kdo začne in težavnost (računalnik bo izbral število vrstic in vžigalic, glede na izbrano težavnost). 

Za igralno ploščo bova uporabila podatkovno strukturo seznam, ki bo imel enaka velikost kot število vrstic v igri, pri čemer vsako vrednost seznama nam pove število preostalih vžigalic v dani vrstici.

Igralec (človek) bo vžigalice vzel iz plošče s klikom na eno izmed vžigalic. S tem bodo iz igralne plošče izginile vse vžigalice desno od izbrane (vključno z njo). Poteza prejšnjega igralca bo pobarvana sivo, ko igralec na potezi klikne na vžigalico, se ta poteza pobarva sivo in prejšnja izbriše. 

Na koncu se bo pojavilo okno, ki bo naznanilo zmagovalca.

### Razredi

Vsi razredi so definirani v `nim.py`.

### Razred `Igra`
Razred, ki vsebuje trenutno stanje igre in zgodovino. Definirali sva naslednje metode: 

* `razveljavi(self)`: razveljavi zadnjo potezo
* `veljavne_poteze(self)`: Vrne nam seznam z vsemi moznimi potezi na vsaki vrstici
* `povleci_potezo(self,i,j)`: vzemi j vžigalic iz i-te vrstice 
* `stanje_igre(self)`: ugotovi, kakšno je trenutno stanje in vrne: ni konec, igralec_i (če je zmagal prvi igralec), igralec_ii (če je zmagal drugi igralec)

### Razred `Človek`

* `__init__(self, gui)`: konstruktorju podamo objekt `gui`, s katerim lahko dostopa do uporabniškega vmesnika in stanja igre
* `igraj(self)`: GUI pokliče to metodo, ko je igralec na potezi
* `klik(self, i, j)`: GUI pokliče to metodo, če je igralec na potezi in je uporabnik kliknil polje `(i,j)` na plošči

### Razred `PC`

* `__init__(self, gui)`
* `klik(self, i, j)`

### Razred `upvmesnik`
Razred, v katerem je definiran uporabniški vmesnik z metodami:

* `start_game(self, Igralec_i, Igralec_ii)`: začni igrati igro z danimi igralci
* `end_game(self, winner)`: končaj igro z danim zmagovalecem
* `izvrsi_potezo(self, i, j)`: igralec bo vzel j vžigalic iz i-te vrstice


# Časovni načrt

1. teden: načrtovanje projekta
2. teden: programiranje uporabniškega vmesnika
3. teden: programiranje podrazreda človek
4. teden: programiranje podrazreda računalnik
5. teden: dokumentacija in testiranje
6. teden: zadnji popravki, oddaja in priprava na zagovor

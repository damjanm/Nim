# Vsebinski načrt:

## Opis aplikacije:

Na sredini okna bo igralna plošča, katera bo imela več vrstic z vžigalicami. Nad igralno ploščo bo napisano kdo je na potezi. Igralec bo lahko v v prvem meniju z imenom Igra razveljavil potezo. V meniju Igralci bo imel na razpolago kako želi igrati novo igro (človek -človek, človek - računalnik, računalnik - človek ali računalnik - računalnik) in težavnost pri igri z računalnikom. Na voljo bo pa tudi meni Imena igralcev, kjer se bo ob kliku na "Doloci imena igralcev" odprlo okno in bo mogoče izbrati imena vseh igralcev.

Za igralno ploščo bova uporabila podatkovno strukturo seznam, ki bo imel enako velikost kot število vrstic v igri, pri čemer nam vsaka vrednost seznama pove število preostalih vžigalic v dani vrstici.

Igralec (človek) bo vžigalice vzel iz plošče s klikom na eno izmed vžigalic. S tem bodo iz igralne plošče izginile vse vžigalice desno od izbrane (vključno z njo). Ko bo miška na eni izmed vžigalic se bodo vse desno od nje (vključno z njo) razbarvale in tako pokazale, katere se bodo izbrisale, če igralec klikne na njo.

Na koncu se bo na sredini okna pojavil napis, ki bo naznanil zmagovalca.

### Razredi

Vsi razredi so definirani v `nim.py` in `tkSimpleDialog.py`.

### Razred `MyDialog`
Razred, ki nam pomaga v izbiranju imena vseh igralcev. Definirali sva naslednje metode: 

* `body(self, master, gui)`: Definiraj okvir okna, v katerem vpišemo imena igralcev.
* `apply(self)`: Shrani imena igralcev.

### Razred `Igra`
Razred, v katerem je definirana logika igre. 

* `__init__(self, igralec_1,igralec_2)`: Konstruktorju podamo objektov igralce_1/2.
* `shrani_pozicijo(self)`: Shrani trenutno pozicijo.
* `razveljavi(self)`: Razveljavi zadnjo potezo.
* `nasprotnik(self, igralec)`: Vrne nasprotnik igralca igralec.
* `veljavne_poteze(self)`: Vrne seznam z vsemi moznimi potezi v vsaki vrstici.
* `povleci_potezo(self,i,j)`: Vzame vse vžigalice od j-te desno (vključno z njo) iz i-te vrstice.
* `stanje_igre(self)`: Ugotovi, kakšno je trenutno stanje in vrne: ni konec ali igralec.

### Razred `Clovek`

* `__init__(self, gui, ime)`: Konstruktorju podamo objekt `gui`, s katerim lahko dostopa do uporabniškega vmesnika in stanja igre, ter ime.
* `igraj(self)`: GUI pokliče to metodo, ko je Clovek na potezi.
* `klik(self, i, j)`: GUI pokliče to metodo, če je igralec na potezi in je uporabnik kliknil polje `(i,j)` na plošči.

### Razred `PC`

* `__init__(self, gui, ime, tez)`: Podobno kot pri razredu Clovek podamo objekti `gui` in `ime`. Dodamo še tez, ki določi težavnost igre.
*`igraj(self)`: GUI pokliče to metodo, ko je PC na potezi.
*`strategija(self, tezavnost)`: Izračuna in vrne optimalno strategijo. 
*`pomozna_strategija(self, tezavnost, vrst, vzig)`: Pomožna metoda za izračun slučajne poteze. 


### Razred `upvmesnik`
Razred, v katerem je definiran uporabniški vmesnik z metodami:

*`__init__(self,master)`: Definiramo osnovne parametre in poženemo igro.
*`imena(self)`: Metoda, v katero shranimo imena igralcev.
* `start_game(self, igralec_1, igralec_2)`: Začni igrati igro z danimi igralci.
* `izvrsi_potezo(self, i, j)`: Zbriši vse vžigalice od j-te desno (vključno z njo) iz i-te vrstice.
* `razveljavi_potezo(self)`: Razveljavi zadnjo potezo.
* `plosca_klik(self, event)`: Skrbi, da igrico sprejme samo pravilne poteze.
* `osvetli(self,event)`: Osvetli vse vžigalice desno od tiste na katero je kazalec.
* `end_game(self, winner)`: Končaj igro z danim zmagovalecem.

### Razred `tkSimpleDialog.py`
Ta razred skupaj z razredom `MyDialog` smo jih najprej našli na `http://effbot.org/tkinterbook/tkinter-dialog-windows.htm` in adaptirali našemu programu. Uporabimo ga v izbiranju imena igralcev.

*`__init__(self, parent, gui, title = None)`: Definiramo parametre novega okna.
*`buttonbox(self)`: Definiramo gumbe.
*`ok(self, event=None)`: Definiramo gumb OK.
*`cancel(self, event=None)`: Definiramo gumb Cancel.


# Časovni načrt

1. teden: načrtovanje projekta
2. teden: programiranje uporabniškega vmesnika
3. teden: programiranje podrazreda človek
4. teden: programiranje podrazreda računalnik
5. teden: dokumentacija in testiranje
6. teden: zadnji popravki, oddaja in priprava na zagovor

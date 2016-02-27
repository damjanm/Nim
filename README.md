# Nim
Načrt za igro Nim

Pri igri Nim je igralna plošča sestavljena iz več vrstic. V vsaki vrstici so vžigalice. Igra poteka tako, da igralec, ki je na potezi, iz igralne plošče vzame vžigalice. V eni potezi lahko vzame poljubno število vžigalic iz ene vrstice. Zgubi tisti, ki vzame zadnjo vžigalico iz igralne plošče. 

Vsebinski načrt:

Na sredini okna bo igralna plošča, katera bo imela več vrstic z vžigalicami. Nad igralno ploščo bosta gumb za novo igro in gumb za razveljaviti zadnjo potezo (undo). V desnem kotu bo  napisano kdo je na potezi.  Desno od igralne plošče bo za izbirati, kako želiš igrati novo igro (računalnik- računalnik, človek- računalnik, človek-človek), kdo začne in težavnost (računalnik bo izbral število vrstic in vžigalic, glede na izbrano težavnost). 

Za igralno ploščo bova uporabila podatkovno strukturo matriko. V matriki bo v vsakem trenutku napisano trenutno stanje igre (kje so še vedno vžigalice). Ko bo računalnik izbral število vrstic in vžigalic, se bo ustvarila matrika velikosti št. vrstic krat max. št. vžigalic v vrstici. 

Igralec (človek) bo vžigalice vzel iz plošče s klikom na eno izmed vžigalic. S tem bodo iz igralne plošče izginile vse vžigalice desno od izbrane (vključno z njo). Poteza prejšnjega igralca bo pobarvana sivo, ko igralec na potezi klikne na vžigalico, se ta poteza pobarva sivo in prejšnja izbriše. 

Na koncu se bo pojavilo okno, ki bo naznanilo zmagovalca.

Najin program bo sestavljen iz  razredov  plošča in igralec. Igralec bo imel podrazreda človek in računalnik. 
Metoda igralca bo: določi potezo (človek klikne na vžigalico, računalnik pa izračuna)
Metoda plošče bo: izvedi potezo (dobi potezo igralca in glede na to odstrani vžigalico iz plošče (matrike))

Časovni načrt

1. teden: načrtovanje projekta
2. teden: programiranje uporabniškega vmesnika
3. teden: programiranje podrazreda človek
4. teden: programiranje podrazreda računalnik
5. teden: dokumentacija in testiranje
6. teden: zadnji popravki, oddaja in priprava na zagovor

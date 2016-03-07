from tkinter import *

##################################################################
## Igra

st_vrstic = 4 
st_vzigalic_po_vrsticah = [1,3,5,7] # Zaenkrat so konstante, kasneje bodo spremenljivke

#igralci:
igralec_i = "1"
igralec_ii = "2"

ni_konec = "ni konec"


clovek = "človek"
pc = "računalnik"


# Seznam dolžine 4 x 7 (v tem primeru), ki vsebuje enke in nicle, torej stevilo enk nam pove koliko vzigalic imamo v posamezni vrstici:
matrika=list()
for i in range(st_vrstic):
    matrika.append([1]*st_vzigalic_po_vrsticah[i] + [0]*(max(st_vzigalic_po_vrsticah) - st_vzigalic_po_vrsticah[i]))
    

def nasprotnik(igralec):
    if igralec == igralec_i:
        return igralec_ii
    else:
        return igralec_i

class Igra():
    def __init__(self):
        self.plosca=st_vzigalic_po_vrsticah
        self.na_potezi =  igralec_i
        self.zgodovina = [] # Zgodovino bomo rabili, da bi shranjevali kateri igralec je naredil ustrezno potezo.
        
    def shrani_pozicijo(self):
        q = [self.plosca[i] for i in range(len(self.plosca))] # Shranimo trenutno self.plosca
        self.zgodovina.append((q,self.na_potezi)) # Shranimo q in ne self.plosca, ker se self.plosca ves cas spreminja
        
    def razveljavi(self):
        (self.plosca, self.na_potezi) = self.zgodovina.pop()

    def veljavne_poteze(self):
        # Vrne nam seznam z vsemi moznimi potezi na vsaki vrstici
        poteze = []
        for i in range(len(self.plosca)):
            poteze.append([list(range(1, 1 + self.plosca[i])),i])
        return poteze

    def povleci_potezo(self,i,j):
        # Igralec bo vzel j vzigalic iz i-te vrstice
        if j not in self.veljavne_poteze()[i][0]:
            return None
        else:
            self.shrani_pozicijo()
            self.plosca[i] -= j
            if self.stanje_igre() == ni_konec:
                self.na_potezi = nasprotnik(self.na_potezi)
            return(self.stanje_igre())
            
    def stanje_igre(self):
        """Ugotovi, kakšno je stanje in vrne:
        -igralec_i, ce je zmagal prvi igralec
        -igralec_ii, ce je zmagal drugi igralec
        -ni_konec, ce igre se ni konec
        """
        if self.plosca != [0]*len(self.plosca):
            return(ni_konec)
        else:
            if self.zgodovina[len(self.zgodovina)-1][1]==igralec_i:
                return(igralec_ii)
            if self.zgodovina[len(self.zgodovina)-1][1]==igralec_ii:
                return(igralec_i)
            

##################################################################
## Igralec človek
            
class Clovek():
    def __init__(self, gui):
        self.gui = gui

    def igraj(self):
        pass

    def klik(self, i, j):
        self.gui.povleci_potezo(i, j)


##################################################################
## Igralec računalnik

class PC():
    def __init__(self, gui, algoritem):
        self.gui = gui
        self.algoritem = algoritem

    def klik(self, p):
        pass # Računalnik bo ignoriral klike

##################################################################
## Uporabniški vmesnik

class upvmesnik():
    # Meni
    def __init__(self,master):
        menu = Menu(master)
        master.config(menu=menu) # Dodamo glavni meni

        game_menu = Menu(menu)
        menu.add_cascade(label="Igra", menu=game_menu)
        game_menu.add_command(label="Nova igra", command=self.new_game)
        game_menu.add_command(label="Izhod iz igre", command=self.quit)
        
        player_menu = Menu(menu)
        menu.add_cascade(label="Igralca", menu=player_menu)
        player_menu.add_command(label="Človek proti človeku", command=self.start_game(clovek,clovek))
        player_menu.add_command(label="Človek proti računalniku", command=self.start_game(clovek,pc))
        player_menu.add_command(label="Računalnik proti človeku", command=self.start_game(pc,clovek))
        player_menu.add_command(label="Računalnik proti računalniku", command=self.start_game(pc,pc))

        # Napis, ki prikazuje stanje igre
        self.napis = StringVar(master, value="Dobrodošli v igri Nim")
        Label(master, textvariable=self.napis).grid(row=0, column=0)

        # Ustvarimo igralno ploščo
        self.plosca = Canvas(master, width = 150*max(st_vzigalic_po_vrsticah), height = 150*st_vrstic)

        
        # Igranje človeka bo upravljano s klikom
        self.plosca.bind("<Button-1>", self.plosca_klik)

        # Začne igro v načinu človek proti računalniku
        self.start_game(clovek,pc)

    def start_game(self, igralec_i, igralec_ii):
        # Pobrišemo platno
        self.plosca.delete(ALL)

        # Narišemo vžigalice
        for i in matrika:
            k=0
            for j in matrika[i]:
                if j==1:
                    self.plosca.create_line(50+k,50*i,50+k,100*i)
                    k+=100
                else:
                    k+=100
        
        # Ustvarimo novo igro
        self.igra=Igra()
        
        # Nastavimo igralca
        self.prvi = igralec_i
        self.drugi = igralec_ii

        # Človek je prvi na potezi
        self.napis.set("Na potezi je {0}".format(prvi))
        self.prvi.igraj()

    def izvrsi_potezo(self, i, j):
        # Igralec bo vzel j vzigalic iz i-te vrstice
        if j in Igra.veljavne_poteze()[i][0]:
            k = sum(matrika[i])
            matrika[i] = [1]*(k-j) + [0]*(max(st_vzigalic_po_vrsticah)-(k-j))
            l = matrika[i]
            for m in range(k,l):
                self.plosca.delete(50+k,50*i,50+k,100*i)
        else:
            continue

        
    def end_game(self, winner):
        self.napis.set("Zmagal je {0}".format(winner))
    


root = Tk()
root.title("Nim")
aplikacija = upvmesnik(root)
root.mainloop()

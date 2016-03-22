from tkinter import *

##################################################################
## Igra

st_vrstic = 4 
st_vzigalic_po_vrsticah = [1,3,5,7] # Zaenkrat so konstante, kasneje bodo spremenljivke

#igralci:
igralec_i = "Človek 1"
igralec_ii = "Človek 2"

ni_konec = "ni konec"


clovek = "človek"
pc = "računalnik"




class Igra():
    def __init__(self,igralec_1,igralec_2):
        self.plosca=st_vzigalic_po_vrsticah[:]
        self.na_potezi =  igralec_1
        self.igralec_1 =  igralec_1
        self.igralec_2 =  igralec_2
        self.zgodovina = [] # Zgodovino bomo rabili, da bi shranjevali kateri igralec je naredil ustrezno potezo.
        
    def shrani_pozicijo(self):
        self.zgodovina.append((self.plosca[:],self.na_potezi)) # Shranimo q in ne self.plosca, ker se self.plosca ves cas spreminja
        
    def razveljavi(self):
        (self.plosca, self.na_potezi) = self.zgodovina.pop()

    def nasprotnik(self,igralec):
        if igralec == self.igralec_1:
            return self.igralec_2
        else:
            return self.igralec_1

    def veljavne_poteze(self):
        # Vrne nam seznam z vsemi moznimi potezi na vsaki vrstici
        poteze = []
        for i in range(len(self.plosca)):
            poteze.append([i,list(range(self.plosca[i]))]) 
        return poteze

    def povleci_potezo(self,i,j):
        # Igralec bo vzel vse vžigalice od j-te desno, vključno z j-to iz i-te vrstice
        if j not in self.veljavne_poteze()[i][1]:
            return None
        else:
            self.shrani_pozicijo()
            self.plosca[i] = j
            if self.stanje_igre() == ni_konec:
                self.na_potezi = self.nasprotnik(self.na_potezi)
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
    def __init__(self, gui,ime):
        self.gui = gui
        self.ime = ime

    def igraj(self):
        pass

    def klik(self, i, j):
        self.gui.izvrsi_potezo(i, j)


##################################################################
## Igralec računalnik

class PC():
    def __init__(self, gui, ime):
        self.gui = gui
        self.ime= ime
        
    def igraj(self):        
        self.gui.izvrsi_potezo(self.strategija()[0],self.strategija()[1])

    def strategija(self):
        """Vrni seznam z vrstico iz katere bomo vzeli vse vzigalice od vzig desno"""
        
        # Najprej naredimo operacijo XOR (exlusive or) po vseh stevilah vzigalic in rezultat shranimo kot xor:        
        xor=self.gui.igra.plosca[0]
        for i in self.gui.igra.plosca[1:]:
            xor = xor^i
            
        # Naredimo ustrezno strategijo v odvisnosti od xor:
        if xor == 0:
            vrst = self.gui.igra.plosca.index(max(self.gui.igra.plosca))
            vzig = self.gui.igra.plosca[vrst]-1
        else:        
            for i,j in enumerate(self.gui.igra.plosca):
                if j^xor < j:
                    vrst = i
            vzig = self.gui.igra.plosca[vrst]^xor
            
            #S tem smo dolocili vrstico iz katere moramo vzeti ustrezno stevilo vzigalic.
            #Sedaj še popravimo strategijo v primeru, ko imamo po eno vžigalico v vsaki vrstici (ali pa je v maksimum eno vrstico več kot 1 vžigalica).
            #Naredimo tak korak, da bo ostalo liho število vrstic, kjer vsaka vrstica bo imela 1 vžigalico
            
            st=0
            for i,j in enumerate(self.gui.igra.plosca):
                if vrst == i:
                    kk = vzig
                else:
                    kk = j
                if kk>1:
                    st+=1
            if st == 0:
                vrst = self.gui.igra.plosca.index(max(self.gui.igra.plosca))
                st_enk = sum(i==1 for i in self.gui.igra.plosca)
                if st_enk%2!=1:
                    vzig = 1
                else:
                    vzig = 0    
        return [vrst,vzig] 
            
    def klik(self, i,j):
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
        game_menu.add_command(label="Nova igra", command=lambda:self.start_game(Clovek(self,"Clovek 1"),Clovek(self,"Clovek 2")))
        
        player_menu = Menu(menu)
        menu.add_cascade(label="Igralca", menu=player_menu)
        player_menu.add_command(label="Človek proti človeku", command=lambda:self.start_game(Clovek(self,"Clovek 1"),Clovek(self,"Clovek 2")))
        player_menu.add_command(label="Človek proti računalniku", command=lambda:self.start_game(Clovek(self,"Clovek"),PC(self,"Racunalnik")))
        player_menu.add_command(label="Računalnik proti človeku", command=lambda:self.start_game(PC(self,"Racunalnik"),Clovek(self,"Clovek")))
        player_menu.add_command(label="Računalnik proti računalniku", command=lambda:self.start_game(PC(self,"Racunalnik 1"),PC(self,"Racunalnik 2")))

        # Napis, ki prikazuje stanje igre
        self.napis = StringVar(master, value="Dobrodošli v igri Nim")
        Label(master, textvariable=self.napis).grid(row=0, column=0)

        # Ustvarimo igralno ploščo
        self.plosca = Canvas(master, width = 50*max(st_vzigalic_po_vrsticah)+50, height = 100*st_vrstic+50)
        self.plosca.grid()

        
        # Igranje človeka bo upravljano s klikom
        self.plosca.bind("<Button-1>", self.plosca_klik)

        # Začne igro v načinu človek proti človeku
        self.start_game(Clovek(self,"Clovek 1"),Clovek(self,"Clovek 2"))

    def start_game(self, igralec_1, igralec_2):
        # Pobrišemo platno
        self.plosca.delete(ALL)
        m=0
        sez1=list()
        # Narišemo vžigalice
        for i in range(st_vrstic):
            k=0
            sez2=list()
            for j in range(1,1+st_vzigalic_po_vrsticah[i]):
                i1=self.plosca.create_line(50+k,50*(i+1)+m,50+k,50*(i+1)+m+50)
                sez2.append(i1) #shranjujemo id vžigalic
                k+=50
            m+=50
            sez1.append(sez2)
        self.seznam=sez1    
        
        # Ustvarimo novo igro
        self.igra=Igra(igralec_1,igralec_2)
        
        # Nastavimo igralca
        self.prvi = igralec_1
        self.drugi = igralec_2

        # Človek je prvi na potezi
        self.napis.set("Na potezi je {0}".format(self.prvi.ime))
        #self.igralec= self.prvi
        self.prvi.igraj()

    def izvrsi_potezo(self, i, j):
        # Igralec bo vzel vse vžigalice od j-te desno, vključno z j-to iz i-te vrstice
        for a in self.seznam[i][j:]: 
            self.plosca.delete(a)
        self.seznam[i] = self.seznam[i][:j]         
        self.igra.povleci_potezo(i,j)
        if self.igra.na_potezi==self.prvi:
            self.prvi.igraj()
        else:
            self.drugi.igraj()
        self.napis.set("Na potezi je {0}".format(self.igra.na_potezi.ime))#self.igra.nasprotnik(self.igra.zgodovina[len(self.igra.zgodovina)-1][1]).ime))

        if self.igra.stanje_igre()!=ni_konec:
            self.end_game(self.igra.nasprotnik(self.igra.na_potezi).ime)
        else:
            pass

        
    def plosca_klik(self, event):
        vzigalica = (event.x+5)//50 -1 
        vrstica = (event.y-5)//100
        if 5<event.y%100<45:
            return
        if 5<event.x%50<45:
            return        
        if vrstica <0 or vrstica >=st_vrstic:
            return
        if vzigalica <0 or vzigalica >= self.igra.plosca[vrstica]:
            return
        
        if self.igra.na_potezi==self.prvi:
            self.prvi.klik(vrstica,vzigalica)
        else:
            self.drugi.klik(vrstica,vzigalica)
        
        
    
    def end_game(self,winner):
        self.napis.set("Zmagal je {0}".format(winner))



root = Tk()
root.title("Nim")
aplikacija = upvmesnik(root)
root.mainloop()

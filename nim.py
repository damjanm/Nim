from tkinter import *
from random import *
import tkSimpleDialog

##################################################################
## Igra

st_vzigalic_po_vrsticah = [1,3,5,7]
st_vrstic = len(st_vzigalic_po_vrsticah)

#igralci:
igralec_i = "Človek 1"
igralec_ii = "Človek 2"

ni_konec = "ni konec"


clovek = "človek"
pc = "računalnik"

tezavnost = 6

class MyDialog(tkSimpleDialog.Dialog):

    def body(self, master):
        
        Label(master, text="Človek 1:").grid(row=0)
        Label(master, text="Človek 2").grid(row=1)
        Label(master, text="Računalnik 1:").grid(row=2)
        Label(master, text="Računalnik 2:").grid(row=3)

        self.e1 = Entry(master)
        self.e1.insert(END, 'Maja')
        self.e2 = Entry(master)
        self.e2.insert(END, 'Damjan')
        self.e3 = Entry(master)
        self.e3.insert(END, 'Linux')
        self.e4 = Entry(master)
        self.e4.insert(END, 'Windows')

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)
        self.e4.grid(row=3, column=1)
        return self.e1

    def apply(self):
        c1 = str(self.e1.get())
        c2 = str(self.e2.get())
        pc1 = str(self.e3.get())
        pc2 = str(self.e4.get())
        self.imen = [c1,c2,pc1,pc2]
        
     


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
    def __init__(self, gui, ime, tez):
        self.gui = gui
        self.ime= ime
        self.tez=tez
        
    def igraj(self):
        
        a=self.strategija(self.tez)        
        #print(a,self.ime)
        self.gui.izvrsi_potezo(a[0],a[1])
        
    def strategija(self,tezavnost):
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


        #Težavnost: če je enaka 6 igra normalno, če je enaka 4 slučajno igra z verjetnostjo 1/3 in pravilno z verj. 2/3, če je 2 igra slučajno z verj. 1/2                      
        if tezavnost == 6:
            return [vrst,vzig]
        elif tezavnost == 4:
            slucaj = randint(1,3)
            if slucaj!=1:
                return [vrst,vzig]
            else:
                q=0
                for i in range(st_vrstic):
                    if self.gui.igra.veljavne_poteze()[i][1]!=[]:
                        q=i
                        break
                    
                return [q, randint(0,self.gui.igra.veljavne_poteze()[q][1][-1])]
        else:
            slucaj = randint(1,2)
            if slucaj==1:
                return [vrst,vzig]
            else:
                q=0
                for i in range(st_vrstic):
                    if self.gui.igra.veljavne_poteze()[i][1]!=[]:
                        q=i
                        break
                return [q, randint(0,self.gui.igra.veljavne_poteze()[q][1][-1])]       
                
            
    def klik(self, i,j):
        pass # Računalnik bo ignoriral klike

##################################################################
## Uporabniški vmesnik

class upvmesnik():
    # Meni
    def __init__(self,master):
        self.master=master
        menu = Menu(master)
        master.config(menu=menu) # Dodamo glavni meni
        self.ime_c1 = "Maja"
        self.ime_c2 = "Damjan"
        self.ime_pc1 = "Linux"
        self.ime_pc2 = "Windows"
        self.undo=[]

        game_menu = Menu(menu)
        menu.add_cascade(label="Igra", menu=game_menu)
        game_menu.add_command(label="Razveljavi potezo", command=lambda:self.razveljavi_potezo())

        player_menu = Menu(menu)
        menu_c_pc = Menu(player_menu)
        menu_pc_c = Menu(player_menu)
        menu_pc_pc = Menu(player_menu)
        
        menu.add_cascade(label="Igralci", menu=player_menu)
        player_menu.add_command(label="Človek proti človeku", command=lambda:self.start_game(Clovek(self,self.ime_c1),Clovek(self,self.ime_c2)))
        player_menu.add_cascade(label="Človek proti računalniku", menu=menu_c_pc)
        player_menu.add_cascade(label="Računalnik proti človeku", menu=menu_pc_c)
        player_menu.add_cascade(label="Računalnik proti računalniku", menu=menu_pc_pc)

        menu_c_pc.add_command(label="Lahko", command=lambda:self.start_game(Clovek(self,self.ime_c1),PC(self,self.ime_pc1,2)))
        menu_c_pc.add_command(label="Srednje", command=lambda:self.start_game(Clovek(self,self.ime_c1),PC(self,self.ime_pc1,4)))
        menu_c_pc.add_command(label="Težko", command=lambda:self.start_game(Clovek(self,self.ime_c1),PC(self,self.ime_pc1,6)))
        menu_pc_c.add_command(label="Lahko", command=lambda:self.start_game(PC(self,self.ime_pc1,2),Clovek(self,self.ime_c1)))
        menu_pc_c.add_command(label="Srednje", command=lambda:self.start_game(PC(self,self.ime_pc1,4),Clovek(self,self.ime_c1)))
        menu_pc_c.add_command(label="Težko", command=lambda:self.start_game(PC(self,self.ime_pc1,6),Clovek(self,self.ime_c1)))
        menu_pc_pc.add_command(label="Lahko", command=lambda:self.start_game(PC(self,self.ime_pc1,2),PC(self,self.ime_pc2,2)))
        menu_pc_pc.add_command(label="Srednje", command=lambda:self.start_game(PC(self,self.ime_pc1,4),PC(self,self.ime_pc2,4)))
        menu_pc_pc.add_command(label="Težko", command=lambda:self.start_game(PC(self,self.ime_pc1,6),PC(self,self.ime_pc2,6)))


        names_menu = Menu(menu)
        menu.add_cascade(label="Imena igralcev",menu=names_menu)
        names_menu.add_command(label="Doloci imena igralcev", command=self.imena)
      
        # Napis, ki prikazuje stanje igre
        self.napis = StringVar(master, value="Dobrodošli v igri Nim")
        Label(master, textvariable=self.napis,fg = "dark green",font=("Times",20,"bold italic")).grid(row=0, column=0)

        # Ustvarimo igralno ploščo
        self.plosca = Canvas(master, width = 50*max(st_vzigalic_po_vrsticah)+50, height = 100*st_vrstic+50,bg="papaya whip")
        self.plosca.grid()

        
        # Igranje človeka bo upravljano s klikom
        self.plosca.bind("<Button-1>", self.plosca_klik)

        #vžigalice se osvetlijo ko se miška premakne na njih
        self.plosca.bind("<Motion>", self.osvetli)

        # Začne igro v načinu človek proti človeku
        self.start_game(Clovek(self,self.ime_c1),Clovek(self,self.ime_c2))
        
    def imena(self):
        okno=MyDialog(self.master)        
        k=okno.imen
        self.ime_c1 = k[0]
        self.ime_c2 = k[1]
        self.ime_pc1 = k[2]
        self.ime_pc2 = k[3]

        
    
    def start_game(self, igralec_1, igralec_2):
        # Pobrišemo platno
        self.plosca.delete(ALL)
        m=0
        sez1=list()
        # Narišemo vžigalice
        self.sredina=(max(st_vzigalic_po_vrsticah)+1)//2
        for i in range(st_vrstic):
            k=0
            sez2=list()
            for j in range(st_vzigalic_po_vrsticah[i]):
                i1=self.plosca.create_rectangle(k+50*(self.sredina-i-min(st_vzigalic_po_vrsticah)//2)-2,50*(i+1)+m,k+50*(self.sredina-i-min(st_vzigalic_po_vrsticah)//2)+2,50*(i+1)+m+50, fill= "orange red")
                sez2.append(i1)
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
        if isinstance(self.prvi,PC):
            self.plosca.after(500,self.prvi.igraj)
        else:
            self.prvi.igraj()
    
    def izvrsi_potezo(self, i, j):
        # Igralec bo vzel vse vžigalice od j-te desno, vključno z j-to iz i-te vrstice
        if j not in self.igra.veljavne_poteze()[i][1]:
            return None
        else:
            self.undo.append([i,j,self.seznam[i][j:]])
            for a in self.seznam[i][j:]: 
                self.plosca.delete(a)
                
            self.seznam[i] = self.seznam[i][:j]
            self.igra.povleci_potezo(i,j)
            self.napis.set("Na potezi je {0}".format(self.igra.na_potezi.ime))#self.igra.nasprotnik(self.igra.zgodovina[len(self.igra.zgodovina)-1][1]).ime))
            if self.igra.stanje_igre()!=ni_konec:
                self.end_game(self.igra.nasprotnik(self.igra.na_potezi).ime)
                return
            else:
                pass
            if self.igra.na_potezi==self.prvi:                
                self.plosca.after(500,self.prvi.igraj)
            else:
                self.plosca.after(500,self.drugi.igraj)
            



    def razveljavi_potezo(self):
        if isinstance(self.prvi,PC) or isinstance(self.drugi,PC):
            q=2
        else:
            q=1
        for w in range(0,q):
            self.igra.razveljavi()
            undo=self.undo[-1]
            vrst=undo[0]
            vzig=undo[1]
            sezn=list()
            for j in range(vzig,st_vzigalic_po_vrsticah[vrst]):
                a=self.plosca.create_rectangle(50*(self.sredina-vrst-min(st_vzigalic_po_vrsticah)//2)-2+j*50,50*(vrst+1)+vrst*50,50*(self.sredina-vrst-min(st_vzigalic_po_vrsticah)//2)+2+j*50,50*(vrst+1)+vrst*50+50, fill= "orange red")
                sezn.append(a)
            self.seznam[vrst].extend(sezn)
            self.napis.set("Na potezi je {0}".format(self.igra.na_potezi.ime))
            self.undo.pop()
        
        
    def plosca_klik(self, event):
        vrstica = (event.y-5)//100
        vzigalica = (event.x+5-50*(4-vrstica))//50 
        if 5<event.y%100<45:
            return
        if 5<(event.x-50*(4-vrstica))%50<45:
            return        
        if vrstica <0 or vrstica >=st_vrstic:
            return
        if vzigalica <0 or vzigalica >= self.igra.plosca[vrstica]:
            return
        
        if self.igra.na_potezi==self.prvi:
            self.prvi.klik(vrstica,vzigalica)            
        else:
            self.drugi.klik(vrstica,vzigalica)
        

    def osvetli(self,event):
        for i in range(len(self.seznam)):
            for j in self.seznam[i]:
                self.plosca.itemconfig(j, fill="orange red")
        vrstica = (event.y-5)//100
        vzigalica = (event.x+5-50*(4-vrstica))//50 
        if 5<event.y%100<45:
            return
        if 5<(event.x-50*(4-vrstica))%50<45:
            return        
        if vrstica <0 or vrstica >=st_vrstic:
            return
        if vzigalica <0 or vzigalica >= self.igra.plosca[vrstica]:
            return
        for j in self.seznam[vrstica][vzigalica:]:
            self.plosca.itemconfig(j, fill="papaya whip")
        
    
    def end_game(self,winner):
        self.napis.set("")
        self.plosca.create_text((self.sredina*50), (100+(st_vrstic//2)*50), fill = "red4", font=("Times",30,"bold italic"), text = "Zmagal je {0}!".format(winner))



root = Tk()
root.title("Nim")
aplikacija = upvmesnik(root)
root.mainloop()

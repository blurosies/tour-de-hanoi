from turtle import*
from tkinter import*
from time import*
from copy import*


#Partie A
#configuration initiale du plateau
def init(n):
    #la liste plateau contient 3 listes, une par tour:
    #depart a l’indice 0, auxiliaire a l’indice 1, arrivee a l’indice 2
    tour0=[]
    tour1=[]
    tour2=[]
    plateau= [tour0,tour1,tour2]
    for i in range (n,0,-1):
        tour0.append(i)
    return plateau

#renvoie le nombre de disques sur cette tour pour une config donnee
def nbDisques(plateau, numtour):
    d= len(plateau[numtour])
    return d #d: nombre de disques
   
# Renvoie le numero du disque superieur de la tour choisie
def disqueSup(plateau, numtour):
    if len(plateau[numtour])>0:
        # temp = variable temporaire
        temp= plateau[numtour]
        # sup = disque superieur
        sup=temp[len(temp)-1]   
    # Si la tour est vide:
    else:
        sup= len(plateau[0]) + len(plateau[1]) + len(plateau[2])+1 
    return sup

# Nous donne la position du disque (dans quelle tour)
def posDisque(plateau,numdisque):
    for i in range (len(plateau)):
        if numdisque in plateau[i]:
            return i 
   
# Indique si le deplacement de nt1 a nt2 est authorisé    
def verifDepl(plateau, nt1, nt2):
    if nt1 != nt2 :
        bool= len(plateau [nt1])!= 0 and ((len(plateau [nt2])== 0) or (disqueSup(plateau, nt2)>disqueSup(plateau, nt1)))
    else:
        bool= 'Aucun disque a été déplacé'
    # Si bool= True alors le dep est authorisé, sinon, il ne l'est pas
    return bool    

# Verifie s'il y a une victoire
def verifVictoire(plateau, n):
    #modele de la tour2 pour une victoire:
    tourVic=[] 
    for i in range (n,0,-1):
        tourVic.append(i)  
    #Comparaison de la tour2 du plateau avec le modele precedant:
    victoire=(plateau[2]==tourVic) and len(plateau[0])==0 and len(plateau[1])==0
    return victoire

#Partie B
#Distances
x=-300
y=-200
largeurP=30
longeurT=30
largeurT=8

def posi(x,y):
    penup()
    setpos(x , y)
    pendown() 

#config. de turtle
hideturtle()
speed('fastest')
posi(x,y)
    
########################################
#Fonction tracé d'un rectangle pour faciliter les choses
def rect(longeur, largeur):
    for i in range (4):
        if i%2==0:
            fd(longeur)
            left(90)
        else:
            fd(largeur)
            left(90)

#Fonction pour determiner ls coordonnées des disques
def coords(nd, plateau, n):
    #Quelle tour
    k=len(plateau)
    for i in range(k):
        if nd in plateau[i]:
            tour=i
        else:
            i+=1
    #Quelle position
    na=plateau[tour]
    l=len(na)
    for j in range(l):
        if nd == na[j]:
            posit=j
        else:
            j+=1
    #Coordonnées
    espaceT=(40+30*n)+20
    y=(25*posit)-170
    if tour==0:
        x=(espaceT/2)*(tour+1)+4-((40+30*(nd-1))/2)-300
    else:
        x=(espaceT)*(tour)+(espaceT/2)+4-((40+30*(nd-1))/2)-300
    return x,y
        
#TRACER LE PLATEAU
def dessinePlateau(n,couleur):
    fillcolor(couleur)
    pencolor(couleur)
    longeurP=((40+largeurP*n)+25)*3
    posi(-300,-200)
    begin_fill()
    rect(longeurP, largeurP)
    end_fill()
    #Tracé des tours vides
    if n<2:
        return
    else:
        espaceT=(40+30*n)+20
        x2=((((longeurP+x)+x)/2)-largeurT)-espaceT
        posi(x2, y+largeurP)
    t=0
    while t<=3:
        begin_fill()
        rect(largeurT, longeurT*n)
        t+=1
        end_fill()
        posi(x2+espaceT*(t-1) , y+largeurP)

#Dessine un disque précis
def dessineDisque(nd, plateau, n): 
    fillcolor(dis)
    pencolor(dis)    
    disque=coords(nd,plateau,n)
    penup()
    goto(disque)
    pendown()
    begin_fill()
    rect(40+(30*(nd-1)),20)
    end_fill()

#Effacer le disque
def effaceDisque(nd, plateau, n):
    disque=coords(nd,plateau,n)
    penup()
    goto(disque)
    pendown()
    pencolor(bgd)
    fillcolor(bgd)
    begin_fill()
    rect(40+(30*(nd-1)),20)
    end_fill()

#Dessin final des disques
def dessineConfig(plateau,n):
    for d in range (1,n+1):
        dessineDisque(d,plateau,n)

#vider le plateau
def effaceTout(plateau,n):
    for di in range (1,n+1):
        effaceDisque(di,plateau,n)
    posi(-300,-200)
    dessinePlateau(n,pl)


# Partie C
# Renvoie les coordonnees de la tour de depart et d'arrivee
#-------------------------------------------------------------------------------------------------------------------
#cette fonction est utilisée si l'utilisateur choisi de jouer en utilisant le terminal
def lireCoords(plateau):
    # dep = depart
    dep=int(input('tour de depart?'))
    while (dep < -1 or dep > 2) :
        dep = int(input("Cette tour de depart n'existe pas, essaye encore une fois (entre 0 et 2) : "))
    while (len(plateau[dep])== 0) and dep!=-1:
        dep = int(input("Cette tour de depart est vide, essaye encore une fois : "))     
    # arr = arrivee
    arr=int(input("tour d'arrivee?"))
    while (arr < -1 or arr > 2) :
        arr = int(input("Cette tour de d'arrivee n'existe pas, essaye encore une fois (entre 0 et 2) : "))
    while disqueSup(plateau, arr)< disqueSup(plateau, dep):
        arr = int(input("Cette tour ne peut pas etre choisie, essaye encore une fois : "))
    # Les coordonneees seront renvoyees sous forme de liste nommee 'listecoords'
    listecoords=[]
    listecoords.append(dep)
    listecoords.append(arr)
    return listecoords

def coupsmax(n): #Plus le niveau est difficile, moin il y a des coups
    ch=["f","n","d"]
    coups=0
    choix=textinput("Message","Niveau Facile, Normal ou Difficile? (f/n/d): ") 
    while choix not in ch:
        choix=textinput("Message","Veuillez choisir un niveau disponible (f/n/d): ")
    if choix=="f":
        coups=2**(n+1)
    if choix=="n":
        coups=int(2**(n+0.5)//1)
    if choix=="d":
        coups=2**n-1 #ceci est le nombre de coup utilisé dans une partie optimale
    return coups

#------------------------------------------------------------------------------------------------
#Cette partie utilise des bouttons pour jouer au lieu d'écrire dans le terminal. c'est beaucoup plus long et moin efficace à codé et utilise bcp de variables globale dans les fonction
#On note aussi que dans cette partie plusieures règles du jeu initiale ne sont pas codés (plus grand disque sur petit disque)
listecoords=[]
disques = int(textinput("Message","Combien de disques?"))
while disques<2:
    disques = int(textinput("Message","Impossible d'avoir moin que deux disques..."))
lim=coupsmax(disques)
count=0


def tourun(plateau, disques): #Bouton tour 0 (tour 1 dans l'interface pour moin de confusion)
    global count
    if len(listecoords) >=2:
        listecoords.clear()
        
    listecoords.append(0)
    
    if(len(listecoords) == 2): #En utilisant des boutons, nous ne pouvons plus utiliser la boucle du jeu initialement crée, donc il a fallu réecrire une boucle dans chaque bouton.
        jouerUnCoupBout(plateau, disques, listecoords)
        count+=1
        if verifVictoire(plateau,disques)==True:
            up()
            home()
            pencolor("yellow")
            write("vous avez gagne!!!",font="16", align="center")     
        else:
            if count==lim:
                up()
                home()
                pencolor("yellow")
                write("Perdu...vous avez epuiser le nombre de coups.",font="16", align="center")
    
    return listecoords
    
def tourde(plateau, disques): #Bouton tour 1
    global count
    if len(listecoords) >=2:
        listecoords.clear()
        
    listecoords.append(1)
    
    if(len(listecoords) == 2):
        jouerUnCoupBout(plateau, disques, listecoords)
        count+=1
        if verifVictoire(plateau,disques)==True:
            up()
            home()
            pencolor("yellow")
            write("vous avez gagne!!!",font="16", align="center")     
        else:
            if count==lim:
                up()
                home()
                pencolor("yellow")
                write("Perdu...vous avez epuiser le nombre de coups.",font="16", align="center")
    
    return listecoords
    
def tourtr(plateau, disques): #Bouton tour 2
    global count
    if len(listecoords) >=2:
        listecoords.clear()
        
    listecoords.append(2)
    
    if(len(listecoords) == 2):
        
        jouerUnCoupBout(plateau, disques, listecoords)
        count+=1
        if verifVictoire(plateau,disques)==True:
            up()
            home()
            pencolor("yellow")
            write("vous avez gagne!!!",font="16", align="center")     
        else:
            if count==lim:
                up()
                home()
                pencolor("yellow")
                write("Perdu...vous avez epuiser le nombre de coups.",font="16", align="center")
    
    return listecoords


def tracetour(tour,dis): #retrace la tour a la partie manquante
    pencolor(pl)
    fillcolor(pl)
    longeurP=((40+largeurP*dis)+25)*3
    espaceT=(40+30*dis)+20
    x2=((((longeurP+x)+x)/2)-largeurT)-espaceT
    posi(x2+espaceT*(tour) , y+largeurP)
    begin_fill()
    rect(largeurT, longeurT*dis)
    end_fill()
    

#jouer un coup unique
def jouerUnCoupBout(plateau,n, coup): #pour les boutons
    pencolor(pl)
    dep=coup[0]
    arr=coup[1]
    tourD=plateau[dep]
    tourA=plateau[arr]
    effaceDisque(tourD[-1],plateau,n)
    tourA.append(tourD[-1])
    tourD.pop(-1)
    tracetour(int(dep),n)
    temp=deepcopy(plateau)
    coups.append(temp)
    dessineConfig(plateau,n)

def jouerUnCoup(plateau,n):#pour le terminal
    pencolor(pl)
    coords=lireCoords(plateau)
    dep=coords[0]
    arr=coords[1]
    tourD=plateau[dep]
    tourA=plateau[arr]
    effaceDisque(tourD[-1],plateau,n)
    tourA.append(tourD[-1])
    tourD.pop(-1)
    tracetour(int(dep),n)
    coups.append(plateau)
    dessineConfig(plateau,n)

#jeu principale, utilisé si l'utilisateur joue dans le terminal
def boucleJeu(plateau,n):
    
    coupsMax=lim
    count=0
    if count<coupsMax:
        #input coup
        
        jouerUnCoup(plateau,n)
        count+=1
            
        if verifVictoire(plateau,n)==True:
                print("vous avez gagne!!!")     
        else:
            if count==coupsMax:
                print("Perdu...vous avez epuiser le nombre de coups.")
    print("vous avez utiliser",str(count),"coups")
  
#Partie D

def dernierCoup (coups):
    coup=liste_to_dic(coups)
    P=[1,2]
    listek= list(coup.keys())
    Dconfig= coup[listek[-1]]
    Daconfig= coup[listek[-2]]
    a=nbDisques(Dconfig,0) - nbDisques(Daconfig,0)
    b=nbDisques(Dconfig,1) - nbDisques(Daconfig,1)
    c=nbDisques(Dconfig,2) - nbDisques(Daconfig,2)
    # Pour tour 0
    if a==1: #donc arrivee
        P.append(0) 
        P.remove(2)
    elif a== -1: #donc depart
        P.insert(0,0)
        P.remove(1)
    # Pour tour 1
    if b==1: #donc arrivee
        P.append(1) 
        P.remove(2)
    elif b== -1: #donc depart
        P.insert(0,1)
        P.remove(1)
    # Pour tour 2
    if c==1: #donc arrivee
        P.append(2) 
        P.remove(2)
    elif c== -1: #donc depart
        P.insert(0,2)
        P.remove(1)
    return P[0],P[1]


def annulerDernierCoup (coups,n):
    global count
    de,ar=dernierCoup (coups)
    # enleve derniere config
    coups.pop(de)
    # retranche du compteur
    count-=1
    # retrace la config en inversant le dep et l'arr
    dep=ar
    arr=de
    tourD=plateau[dep]
    tourA=plateau[arr]
    effaceDisque(tourD[-1],plateau,n)
    tourA.append(tourD[-1])
    tourD.pop(-1)
    tracetour(int(dep),n)
    dessineConfig(plateau,n)


#Partie E


#Partie F
#Solution du jeu automatique utilisant un algorithme récursif
def automat(disques, depart, arrive):
    mouv=[]
    def listesol(dep,arr): #cette fonction sert a mettre la solution dans une liste
        mouv.append((dep,arr))   
    def solu(disques,depart,arrive):
        milieu=3-(depart+arrive) #car nos tours sont numerotées 0 1 et 2
        if disques==1:
            listesol(depart , arrive)
        else:
            solu(disques-1 , depart , milieu)
            listesol(depart , arrive)
            solu(disques-1 , milieu , arrive)
    solu(disques,depart,arrive)
    return mouv
    

def solutionjeu(plateau,n,dep,arr): #dessine la solution
    sol=automat(n,dep,arr)
    coups=[init(disques)] 
    i=0
    while i<len(sol):
        coup=sol[i]
        dep=coup[0]
        arr=coup[1]
        tourD=plateau[dep]
        tourA=plateau[arr]
        effaceDisque(tourD[-1],plateau,n)
        tourA.append(tourD[-1])
        tourD.pop(-1)
        temp=deepcopy(plateau)
        coups.append(temp)
        tracetour(int(dep),n)
        dessineConfig(plateau,n)
        i+=1

#ces valeurs changes dépendant de l'utilisateur
bgd = "white"
dis = "gray"
pl = "black"
coups=[init(disques)] 


def liste_to_dic(liste):
    coups={}
    for i in range (len(liste)):
        coups[i]=liste[i]
    return coups  
 
def faire(): #fonction pour le boutton solution
    global plateau, disques
    effaceTout(plateau,disques)
    plateau=init(disques)
    dessineConfig(plateau,disques)
    solutionjeu(plateau,disques,0,2)
    startbuttonB.destroy()
    startbuttonT.destroy()
    solbutton.destroy()
    
def restart():#recommence le jeu
    global plateau, disques,coups
    coups=[]
    effaceTout(plateau,disques)
    plateau=init(disques)
    dessineConfig(plateau,disques)
    boucleJeu(plateau,disques)    

def close():#quitte le jeu. quand l'utilisateur joue dans le terminal, ce bouton ne marche pas tout le temps
    root.quit()
   
def jour():#themes
    global bgd, dis, pl,disques
    bgcolor("white")
    pencolor("black")
    main()
    bgd="white"
    dis="gray"
    pl="black"
    return bgd,dis,pl

def nuit():
    global bgd, dis, pl,disques
    bgcolor("black")
    pencolor("white")
    main()
    bgd="black"
    dis="silver"
    pl="dark slate gray"
    return bgd,dis,pl

def noel():
    global bgd,dis,pl,disques
    bgcolor("maroon")
    pencolor("antique white")
    main()
    bgd="maroon"
    dis="dark olive green"
    pl="antique white"
    return bgd,dis,pl

def commencerBout():#Cette fonction permet de commencer le jeu en jouant purement dans l'interface sans utiliser le terminal
    global plateau,disques
    
    clear()
    
    startbuttonB.destroy()
    startbuttonT.destroy()
    exitbutton.place(relx=0.1, rely=0.1, anchor=CENTER)
    solbutton = Button(root.master, text="Solution", command=lambda: faire() ,bg="white",activebackground="light gray",font=15)
    solbutton.pack()
    solbutton.place(relx=0.9, rely=0.099999, anchor=CENTER)
    recbutton = Button(root.master, text="Recommencer", command=lambda: restart() ,bg="white",activebackground="light gray",font=15)
    recbutton.pack()
    recbutton.place(relx=0.77, rely=0.099999, anchor=CENTER)
    annbutton = Button(root.master, text="Annuler", command=lambda: annulerDernierCoup(coups,disques) ,bg="white",activebackground="light gray",font=15)
    annbutton.pack()
    annbutton.place(relx=0.9, rely=0.2, anchor=CENTER)
    
    plateau=init(disques)
    dessinePlateau(disques,pl)
    dessineConfig(plateau,disques)
    tour1 = Button(root.master, text="Tour 1", command=lambda: tourun(plateau, disques), bg="white",font=20)
    tour2= Button(root.master, text="Tour 2", command=lambda: tourde(plateau, disques),bg="white",font=20)
    tour3= Button(root.master, text="Tour 3", command=lambda: tourtr(plateau, disques),bg="white",font=20)

    tour1.pack(side=LEFT,anchor='s')
    tour2.pack(side=LEFT,anchor='s')
    tour3.pack(side=LEFT,anchor='s')

    jour1.destroy()
    nuit1.destroy()
    noel1.destroy()
    
    return plateau,disques
 
def commencerTerm():#Jouer avec le terminal
    global plateau,disques
    
    clear()
    #réarrangement de l'interface
    startbuttonB.destroy()
    startbuttonT.destroy()
    exitbutton.place(relx=0.1, rely=0.1, anchor=CENTER)
    solbutton = Button(root.master, text="Solution", command=lambda: faire() ,bg="white",activebackground="light gray",font=15)
    solbutton.pack()
    solbutton.place(relx=0.9, rely=0.099999, anchor=CENTER)
    recbutton = Button(root.master, text="Recommencer", command=lambda: restart() ,bg="white",activebackground="light gray",font=15)
    recbutton.pack()
    recbutton.place(relx=0.77, rely=0.099999, anchor=CENTER)
    annbutton = Button(root.master, text="Annuler", command=lambda: annulerDernierCoup(coups,disques) ,bg="white",activebackground="light gray",font=15)
    annbutton.pack()
    annbutton.place(relx=0.9, rely=0.2, anchor=CENTER)
    jour1.destroy()
    nuit1.destroy()
    noel1.destroy()
    
    plateau=init(disques)
    dessinePlateau(disques,pl)
    dessineConfig(plateau,disques)
    boucleJeu(plateau,disques)
    return plateau,disques
 
def main():#interface main menu
    up()
    setpos(0,300)
    write('Tours', font=('Rubik',50,'bold'), align='center')
    setpos(0,220)
    write('De', font=('Rubik',50,'bold'), align='center')
    setpos(0,150)
    write('Hanoi', font=('Rubik',50,'bold'), align='center')
    setpos(0,110)
    write("Appuyer START pour commencer", font=('Rubik',10,'bold'), align='center')

#--------------------------------------------------------------------------------------------------    
#program commence ici
#--------------------------------------------------------------------------------------------------    
screen = Screen()
root=Tk()
canvas = getcanvas()    

main()

jour1 = Button(root.master, text="Jour", command=lambda: jour(), bg="white",font=15)
jour1.pack(side='right')

nuit1= Button(root.master, text="Nuit", command=lambda: nuit(),bg="white",font=15)
nuit1.pack(side='right')

noel1= Button(root.master, text="Noel", command=lambda: noel(),bg="white",font=15)
noel1.pack(side='right')

startbuttonB = Button(root.master, text="Start (B)", command=lambda: commencerBout(),bg="white",activebackground="light gray",font=15)
startbuttonB.pack()
startbuttonB.place(relx=0.45, rely=0.5, anchor=CENTER)

startbuttonT = Button(root.master, text="Start (T)", command=lambda: commencerTerm(),bg="white",activebackground="light gray",font=15)
startbuttonT.pack()
startbuttonT.place(relx=0.55, rely=0.5, anchor=CENTER)

solbutton = Button(root.master, text="Solution", command=lambda: faire() ,bg="white",activebackground="light gray",font=15)

exitbutton = Button(root.master, text=" Exit ", command=lambda: close() ,bg="white",activebackground="light gray",font=15)
exitbutton.pack()
exitbutton.place(relx=0.5, rely=0.6, anchor=CENTER)
 
root.mainloop()
#--------------------------------------------------------------------------------------------------    


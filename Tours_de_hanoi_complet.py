from turtle import*
from tkinter import*
from time import*
from copy import*
from pickle import*


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
    espaceT=(40+30*n)+20
    longeurP=((40+largeurP*n)+25)*3
    xt=-longeurP/2
    x2=((((longeurP+xt)+xt)/2)-largeurT)-espaceT
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
    
    y=(22*posit)-168
    if tour==0:
        x=x2+4-((40+30*(nd-1))/2)
    else:
        x=x2+(espaceT)*(tour)+4-((40+30*(nd-1))/2)
    return x,y
        
#TRACER LE PLATEAU
def dessinePlateau(n,couleur):
    fillcolor(couleur)
    pencolor(couleur)
    longeurP=((40+largeurP*n)+25)*3
    up()
    home()
    down()
    posi(-longeurP/2,-200)
    begin_fill()
    rect(longeurP, largeurP)
    end_fill()
    #Tracé des tours vides
    if n<2:
        return
    else:
        x=-longeurP/2
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
    opt=['0','1','2']
    # dep = depart
    dep=input('tour de depart?')
    while dep not in opt :
        dep =input("Cette tour de depart n'existe pas, essaye encore une fois (entre 0 et 2) : ")
    if dep in opt:
        dep=int(dep)
    while (len(plateau[dep])== 0):
        dep =input("Cette tour de depart est vide, essaye encore une fois : ")    
    # arr = arrivee
    arr=input("tour d'arrivee?")
    while arr not in opt:
        arr =input("Cette tour de d'arrivee n'existe pas, essaye encore une fois (entre 0 et 2) : ")
    if arr in opt:
        arr=int(arr)
    while disqueSup(plateau, arr)< disqueSup(plateau, dep):
        arr =input("Cette tour ne peut pas etre choisie, essaye encore une fois : ")
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
disques =int(textinput("Message","Combien de disques?"))
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
            pencolor("dark green")
            write("vous avez gagne!!!",font="20", align="center")     
        else:
            if count==lim:
                up()
                home()
                pencolor("dark green")
                write("Perdu...vous avez epuiser le nombre de coups.",font="20", align="center")
    
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
            pencolor("dark green")
            write("Vous avez gagné!!!",font="20", align="center")     
        else:
            if count==lim:
                up()
                home()
                pencolor("dark green")
                write("Perdu...vous avez epuiser le nombre de coups.",font="20", align="center")
    
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
            pencolor("dark green")
            write("vous avez gagne!!!",font="20", align="center")     
        else:
            if count==lim:
                up()
                home()
                pencolor("dark green")
                write("Perdu...vous avez epuiser le nombre de coups.",font="20", align="center")
    
    return listecoords


def tracetour(tour,dis): #retrace la tour a la partie manquante
    pencolor(pl)
    longeurP=((40+largeurP*dis)+25)*3
    x=-longeurP/2
    up()
    home()
    down()
    fillcolor(pl)
    espaceT=(40+30*dis)+20
    x2=((((longeurP+x)+x)/2)-largeurT)-espaceT
    posi(x2+espaceT*(tour) , y+largeurP)
    begin_fill()
    rect(largeurT, longeurT*dis)
    end_fill()
    

#jouer un coup unique
def jouerUnCoupBout(plateau,n, coup): #pour les boutons
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
    coords=lireCoords(plateau)
    dep=coords[0]
    arr=coords[1]
    tourD=plateau[dep]
    tourA=plateau[arr]
    effaceDisque(tourD[-1],plateau,n)
    tourA.append(tourD[-1])
    tourD.pop(-1)
    tracetour(int(dep),n)
    tempo=deepcopy(plateau)
    coups.append(tempo)
    dessineConfig(plateau,n)
count=0
#jeu principale, utilisé si l'utilisateur joue dans le terminal
def boucleJeu(plateau,n):
    global count
    coupsMax=lim
    while count<coupsMax:
        #input coup
        
        jouerUnCoup(plateau,n)
        count+=1
            
        if verifVictoire(plateau,n)==True:
                print("vous avez gagne!!!")  
                gagne= True 
                break 
        else:
            if count==coupsMax:
                print("Perdu...vous avez epuiser le nombre de coups.")
            gagne=False
    print("vous avez utiliser",str(count),"coups")
    return gagne
  
#Partie D

def dernierCoup (coups): #renvoie le dernier coups joué
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


def annulerDernierCoup (n):
    global count,coups
    de,ar=dernierCoup(coups)
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


# Module pickle

# output est le fichier de sortie avec l'extension .pickle et avec w en mode ecriture (binaire) et b en mode bytes
def save (coups):
    output= open("output.pickle","wb")
    dump(coups,output)
    output.close()
# le fichier a ete creer et le dictionnaire a ete sauvegarder

# pour reavoir acces a ce qui a ete sauvegarder: ( r en mode lecture)

def reload ():
    input= open("output.pickle","rb")
    coups= load(input)
    return coups


#Partie E
data={}
def sauvScore (n,nbcoups,temps): #enregistrer une partie quand l'utilisateur gagne
    global data
    
    score = ((nbcoups + temps) / n) 
    
    reponse= textinput("Message","voulez-vous enregistrer votre partie? (oui/non)")
    if reponse.lower() == 'non':
        print("D'accord, merci pour avoir joue !")
    
    elif reponse.lower() =='oui':
        nom=textinput("Message","Quel est votre nom? ")
        if nom not in data:
            data[nom]={'n':n,'nbcoups':nbcoups, 'temps':temps, 'score': score}
            return data
        elif nom in data :
            while nom in data:
                rip= textinput("Message","Ce nom est deja enregistre, voulez-vous changer les donnes de", nom, " (taper 'oui') ou voulez-vous changer de nom? (tapez 'changer')")
                if rip.lower() == 'oui':
                    data[nom]={'n':n,'nbcoups':nbcoups, 'temps':temps, 'score': score}
                    break
                elif rip.lower() == 'changer':
                    data[nom]={'n':n,'nbcoups':nbcoups, 'temps':temps, 'score': score}


#----------------------------------------------------------------------------------------------
def vainceurs_coups(joueurs):
    noms=[]
    coups=[]
    x = 10000
    no = ''
    
    for i in joueurs:
        noms.append(i)
        coups.append(joueurs[i]['nbcoups'])
            
    for sc in range (0,len(coups)):
        if coups[sc] < x: 
            x = coups[sc]
            no = noms[sc]
    return no , x

def filter_disque(joueurs, n): # filtre les joueurs par rapport au nombre de disques
    copie = {}
    for nom in joueurs :
        valeur = joueurs[nom]['n'] 
        if valeur == n :
            copie[nom] = joueurs[nom]
    return copie

#Pour le leaderboard

def filter_min(joueurs, cle):
    valeur_min = 100000000
    x = []
    n = []
    for nom in joueurs :
        valeur = joueurs[nom][cle] 
        if valeur < valeur_min :
            x.clear()
            n.clear()
            x.append(valeur)
            n.append(nom)
            valeur_min = valeur
        elif valeur == valeur_min :
            x.append(valeur)
            n.append(nom)
    return n, x

def trier(joueurs, cle):
    x=[]
    n=[]
    prov = deepcopy(joueurs)
    while len(prov) > 0 :
        nom,valeurs=filter_min(prov, cle)
        n.append(nom)
        x.append(valeurs)
        for i in nom :
          prov.__delitem__(i)
    return n,x
  

#----------------------------------------------------------------------------------------------
def vainceurs_temps(joueurs):
    noms=[]
    temps=[]
    x=1000
    no ='' 
    for i in joueurs:
        noms.append(i)
        if 'minutes' in joueurs[i]['temps']:
            lt=(joueurs[i]['temps']).split()
            temps.append(int(lt[0])*60+int(lt[3]))
        elif 'minutes' not in joueurs[i]['temps']:
            lt=(joueurs[i]['temps']).split()
            temps.append(int(lt[0]))
    for sc in range (0,len(temps)):
        if temps[sc] < x: 
            x= temps[sc]
            no =noms[sc]
    return no,x



#----------------------------------------------------------------------------------------------
def vainceurs_valeurs(joueurs,gagnants,temps_g,coups_g):
    t={}
    c={}
    v={}
    noms=[]
    valeurs22=[]
    x=1000
    no=''
    for i in range (len(gagnants)):
        t[gagnants[i]]=temps_g[i]
        c[gagnants[i]]=coups_g[i]
    for i in t:
        v[i]=t[i]+c[i]

    for i in range(len(joueurs)):
        noms.append(list(joueurs)[i])
        valeurs22.append(v[list(joueurs)[i]])
    for sc in range (0,len(valeurs22)):
        if valeurs22[sc] < x: 
            x= valeurs22[sc]
            no =noms[sc]
    return no,x



def dessine_tab(titre,valeurs,unite,gagnants,x,y): #dessine le leaderbord
    hideturtle()
    speed('fastest')

    # ecrire dans frame 1 
    speed('fastest')
    hideturtle()
    penup()
    goto(x+100,y-35)
    pendown()
    color("green")
    write(titre,font=('Ariel',15,'normal'))

    
    # rest of the frame
    for i in range (1,len(gagnants)+1):
        # writing in the rest of the frame 
    
        # Numbers
        speed('fastest')
        hideturtle()
        penup()
        goto(x+17,y-35+(-1*(21*(i-0.05))))
        pendown()
        color("black")
        write(str (i),font=('Ariel',12,'normal'))
    
        # Players
        speed('fastest')
        hideturtle()
        penup()
        goto(x+50,y-35+(-1*(21*(i-0.05))))
        pendown()
        color("black")
        write(gagnants[i-1],font=('Ariel',11,'normal'))
    
        # Points
        speed('fastest')
        hideturtle()
        penup()
        goto(x+250,y-35+(-1*(21*(i-0.05))))
        pendown()
        color("black")
        write(str(valeurs[i-1]) + unite,font=('Ariel',11,'normal'))


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
pencolor("black")
coups=[init(disques)] 

class fenetre(Tk): #Quelques boutons de l'interface on besoin de la création d'une nouvelle fenetre turtle, les foncitons ci dessous nous initialisent les fenetres 
    def __init__(wind, titre):
        super().__init__()
        wind.running = True
        wind.title(titre)
        wind.protocol("WM_DELETE_WINDOW", wind.destroy_window)
        wind.canvas = Canvas(wind)
        wind.canvas.pack(side=LEFT, expand=True, fill=BOTH)
        wind.turtle = RawTurtle(TurtleScreen(wind.canvas))

    def update_window(self):
        if self.running:
            self.update()

    def destroy_window(self):
        self.running = False
        self.destroy()

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
    global plateau, disques,coups,count
    clear()
    coups=[]
    count=0
    plateau=init(disques)
    dessinePlateau(disques,pl)
    dessineConfig(plateau,disques)
    ta=time()
    ga=boucleJeu(plateau,disques)
    tb=time() 
    sd =int(tb-ta)
    print('Temps de resolution:', sd, ' secondes.')
    blo= sd
    
    if ga==True:
        data=sauvScore (disques,count,blo)
        print(data)
    return plateau,disques
 
def lead():
    clear()
    gagnants1, coups_g = trier(data, "nbcoups") 
    gagnants2, temps_g = trier(data, "temps")
    gagnants2, valeur_g = trier(data, "score")
    
    
    dessine_tab("EFFICACITE : Coups",coups_g," coups                 ",gagnants1,-700,200)
    dessine_tab("EFFICACITE :  Temps", temps_g," secondes                  ",gagnants2,-250,200)
    dessine_tab("LEADERBOARD", valeur_g," points ",gagnants2,250,200)   
    

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
    reglebutton.destroy()
    exitbutton.place(relx=0.1, rely=0.1, anchor=CENTER)
    solbutton = Button(root.master, text="Solution", command=lambda: faire() ,bg="white",activebackground="light gray",font=15)
    recbutton = Button(root.master, text="Restart", command=lambda: restart() ,bg="white",activebackground="light gray",font=15)
    annbutton = Button(root.master, text="Annuler", command=lambda: annulerDernierCoup(disques) ,bg="white",activebackground="light gray",font=15)
    leadbutton = Button(root.master, text="Leaderboard", command=lambda: lead() ,bg="white",activebackground="light gray",font=15)
    solbutton.pack()
    annbutton.pack()
    recbutton.pack()
    leadbutton.pack()
    recbutton.place(relx=0.77, rely=0.099999, anchor=CENTER)
    solbutton.place(relx=0.9, rely=0.099999, anchor=CENTER)
    annbutton.place(relx=0.9, rely=0.2, anchor=CENTER)
    leadbutton.place(relx=0.9, rely=0.9, anchor=CENTER)
    
    plateau=init(disques)
    dessinePlateau(disques,pl)
    dessineConfig(plateau,disques)
    tour1 = Button(root.master, text="Tour 1", command=lambda: tourun(plateau, disques),bg="white",activebackground="light gray",font=20)
    tour2= Button(root.master, text="Tour 2", command=lambda: tourde(plateau, disques),bg="white",activebackground="light gray",font=20)
    tour3= Button(root.master, text="Tour 3", command=lambda: tourtr(plateau, disques),bg="white",activebackground="light gray",font=20)

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
    reglebutton.destroy()
    exitbutton.place(relx=0.1, rely=0.1, anchor=CENTER)
    solbutton = Button(root.master, text="Solution", command=lambda: faire() ,bg="white",activebackground="light gray",font=15)
    recbutton = Button(root.master, text="Restart", command=lambda: restart() ,bg="white",activebackground="light gray",font=15)
    annbutton = Button(root.master, text="Annuler", command=lambda: annulerDernierCoup(disques) ,bg="white",activebackground="light gray",font=15)
    leadbutton = Button(root.master, text="Leaderboard", command=lambda: lead() ,bg="white",activebackground="light gray",font=15)
    leadbutton.pack()
    solbutton.pack()
    recbutton.pack()
    annbutton.pack()
    solbutton.place(relx=0.9, rely=0.099999, anchor=CENTER)
    recbutton.place(relx=0.77, rely=0.099999, anchor=CENTER)
    annbutton.place(relx=0.9, rely=0.2, anchor=CENTER)
    leadbutton.place(relx=0.9, rely=0.9, anchor=CENTER)

    jour1.destroy()
    nuit1.destroy()
    noel1.destroy()
    
    plateau=init(disques)
    dessinePlateau(disques,pl)
    dessineConfig(plateau,disques)
    ta=time()
    ga=boucleJeu(plateau,disques)
    tb=time()
    sd =int(tb-ta)
    print('Temps de resolution:', sd, ' secondes.')
    blo=sd
    if ga==True:
        sauvScore (disques,count,blo)
        print(data)
    # gagnants1 = filter_min(data, "nbcoups") 
    # gagnants2 = filter_min(data, "temps")
    # gagnants,coups_g=filter(data)
    # gagnants1,temps_g=filtert(data)
    # gagnants2,valeur_g=filterv(data)
    # print(gagnants,coups_g)
    # print(gagnants1,temps_g)
    # print(gagnants2,valeur_g)
    return plateau,disques
 
def regle():
    fen1 = fenetre('Règles')
    t1=fen1.turtle
    t1.hideturtle()
    t1.up()
    t1.setpos(0,20)
    t1.write("On dispose de 3 piquets fixés sur un socle,",align='left') 
    t1.setpos(50,0)
    t1.write("et d'un nombre n de disques de diamètres différents. Les disques sont empilés sur un piquet,",align='left') 
    t1.setpos(50,-20)
    t1.write("en commençant du plus large au plus petit.Le nombre de disques peut varier.", align='left')
    t1.setpos(50,-40)
    t1.write("Plus il y a de disques au départ, plus le jeu est difficile.", align='left')
    t1.setpos(50,-60)
    t1.write(" il faut Déplacer les disques d'une tour de 'départ' à une tour 'd'arrivée'", align='left')
    t1.setpos(50,-80)
    t1.write("en passant par une tour 'intermédiaire', et ceci en un minimum de coups.", align='left')
    t1.setpos(50,-100)
    t1.write("- On ne déplace qu'un seul disque à la fois", align='left')
    t1.setpos(50,-120)
    t1.write("- Le disque déplacé ne doit pas être placé au-dessus d'un disque plus petit", align='left')
    t1.setpos(50,-140)
    t1.write("- On ne peut pas revenir en arrière deux fois d'affiler", align='left')
    
    while fen1.running:
        fen1.update_window()


def main():#interface main menu
    up()
    setpos(0,250)
    write('Tours', font=('Rubik',50,'bold'), align='center')
    setpos(0,170)
    write('De', font=('Rubik',50,'bold'), align='center')
    setpos(0,100)
    write('Hanoi', font=('Rubik',50,'bold'), align='center')
    setpos(0,60)
    write("Appuyer START pour commencer", font=('Rubik',10,'bold'), align='center')

#--------------------------------------------------------------------------------------------------    
#program commence ici
#--------------------------------------------------------------------------------------------------    
screen = Screen()
root=Tk()
canvas = getcanvas()    

main()

jour1 = Button(root.master, text="Jour", command=lambda: jour(), bg="white",font=15)
nuit1= Button(root.master, text="Nuit", command=lambda: nuit(),bg="white",font=15)
noel1= Button(root.master, text="Noel", command=lambda: noel(),bg="white",font=15)
startbuttonB = Button(root.master, text="Start (B)", command=lambda: commencerBout(),bg="white",activebackground="light gray",font=15)
startbuttonT = Button(root.master, text="Start (T)", command=lambda: commencerTerm(),bg="white",activebackground="light gray",font=15)
solbutton = Button(root.master, text="Solution", command=lambda: faire() ,bg="white",activebackground="light gray",font=15)
exitbutton = Button(root.master, text=" Exit ", command=lambda: close() ,bg="white",activebackground="light gray",font=15)
reglebutton = Button(root.master, text=" Règles ", command=lambda:regle() ,bg="white",activebackground="light gray",font=15)
jour1.pack(side='right')
nuit1.pack(side='right')
noel1.pack(side='right')
startbuttonB.pack()
startbuttonT.pack()
exitbutton.pack()
reglebutton.pack()
startbuttonB.place(relx=0.45, rely=0.5, anchor=CENTER)
startbuttonT.place(relx=0.55, rely=0.5, anchor=CENTER)
exitbutton.place(relx=0.5, rely=0.7, anchor=CENTER)
reglebutton.place(relx=0.5,rely=0.6, anchor=CENTER )

exitonclick()
root.mainloop()
#--------------------------------------------------------------------------------------------------    


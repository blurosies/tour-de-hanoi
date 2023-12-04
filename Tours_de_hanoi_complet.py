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
from turtle import*

#Distances
x=-300
y=-200
largeurP=30
longeurT=30
largeurT=8

def pos(x,y):
    penup()
    setpos(x , y)
    pendown() 

#config. de turtle
hideturtle()
speed('fastest')
pos(x,y)


    
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
            posi=j
        else:
            j+=1
    #Coordonnées
    espaceT=(40+30*n)+20
    y=(25*posi)-170
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
    if n<2:
        penup()
        home()
        write("Impossible d'avoir moin que 2 disques", font="16", align="center") 
    else:
        begin_fill()
        rect(longeurP, largeurP)
        end_fill()
    #Tracé des tours vides
    if n<2:
        return
    else:
        espaceT=(40+30*n)+20
        x2=((((longeurP+x)+x)/2)-largeurT)-espaceT
        pos(x2, y+largeurP)
    t=0
    while t<=3:
        begin_fill()
        rect(largeurT, longeurT*n)
        t+=1
        end_fill()
        pos(x2+espaceT*(t-1) , y+largeurP)

#Dessine un disque précis
def dessineDisque(nd, plateau, n): 
    fillcolor(dis)
    pencolor(dis)    
    if n<2: 
        return #return et pas return false pour que le type de sortie soit consistent
    else:
        disque=coords(nd,plateau,n)
        penup()
        goto(disque)
        pendown()
        begin_fill()
        rect(40+(30*(nd-1)),20)
        end_fill()

#Effacer le disque
def effaceDisque(nd, plateau, n):
    if n<2:
        return
    else:
        disque=coords(nd,plateau,n)
        penup()
        goto(disque)
        pendown()
    fillcolor(bgd)
    pencolor(bgd)
    begin_fill()
    rect(40+(30*(nd-1)),20)
    end_fill()

#Dessin final des disques
def dessineConfig(plateau,n):
    if n<2:
        return 
    else:
        for d in range (1,n+1):
            dessineDisque(d,plateau,n)

#vider le plateau
def effaceTout(plateau,n):
    if n<2:
        return 
    else:
        for di in range (1,n+1):
            effaceDisque(di,plateau,n)
    up()
    goto(-300,-200)
    down()
    dessinePlateau(n,pl)




#Partie C
# Renvoie les coordonnees de la tour de depart et d'arrivee
def lireCoords(plateau):
    # dep = depart
    dep=int(input('tour de depart?(-1 pour arreter)'))
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

def tracetour(tour,dis):
    pencolor(pl)
    fillcolor(pl)
    longeurP=((40+largeurP*dis)+25)*3
    espaceT=(40+30*dis)+20
    x2=((((longeurP+x)+x)/2)-largeurT)-espaceT
    pos(x2+espaceT*(tour) , y+largeurP)
    begin_fill()
    rect(largeurT, longeurT*dis)
    end_fill()
    
    

#joue un coup unique
def jouerUnCoup(plateau,n):
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
    dessineConfig(plateau,n)

#jeu principale
def boucleJeu(plateau,n):
  coups=0
  coupsMax=2**n +20
  while not verifVictoire(plateau,n) and coups<coupsMax:
    jouerUnCoup(plateau,n)
    coups+=1
  if verifVictoire:
      print("vous avez gagne!!!")
  if coups>coupsMax:
    print("Perdu...vous avez epuiser le nombre de coups.") 
  print("vous avez utiliser",str(coups),"coups")

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
    

def solutionjeu(n,dep,arr):
    sol=automat(n,dep,arr)
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
        tracetour(int(dep),n)
        dessineConfig(plateau,n)
        i+=1




#Début programme principale

print("Bienvenue dans les tours de Hanoi")


cou=["white","gray","black","blue","cyan","turquoise","green","yellow","gold","olive","brown","orange","red","pink","violet","purple","lavender"]

bgd=input("Choisir la couleur de fond d'éran (en anglais)")
while bgd not in cou:
    bgd=input("Couleur non disponible, veuillez réessayer")
if bgd in cou:
    bgcolor(bgd)
    
pl=input("Choisir la couleur du plateau (en anglais)")
while pl not in cou:
    pl=input("Couleur non disponible, veuillez réessayer")

dis=input("Choisir la couleur des disques (en anglais)")
while dis not in cou:
    dis=input("Couleur non disponible, veuillez réessayer")

disques=int(input("Combien de disques?"))
dessinePlateau(disques,pl)
plateau=init(disques)
dessineConfig(plateau,disques)
#boucleJeu(plateau,disques)
#solutionjeu(disques,0,2)

exitonclick()

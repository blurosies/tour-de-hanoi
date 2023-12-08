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
    posi(x2+espaceT*(tour) , y+largeurP)
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

def boucleJeu(plateau,n):
    coupsMax=coupsmax(n)
    count=0
    while count<coupsMax:
        jouerUnCoup(plateau,n)
        count+=1
    if verifVictoire==True:
        print("vous avez gagne!!!")      
    else:
        print("Perdu...vous avez epuiser le nombre de coups.")
    print("vous avez utiliser",str(count),"coups")

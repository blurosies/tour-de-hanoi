#Partie B
from turtle import*

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

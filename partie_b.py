#Partie B - Graphisme avec turtle
from turtle import*

#Distances
x=-300
y=-200
largeurP=30
longeurT=30
largeurT=8

#config. de turtle
hideturtle()
speed(1000000)
penup()
setpos(x , y)
pendown()

cou=["white","gray","black","blue","cyan","turquoise","green","yellow","gold","olive","brown","orange","red","pink","violet","purple","lavender"]

bgd=input("Choisir la couleur de fond d'éran (en anglais)")
while bgd not in cou:
    bgd=input("Couleur non disponible, veuillez réessayer")
if bgd in cou:
    bgcolor(bgd)
    

# pl=input("Choisir la couleur du plateau (en anglais)")
# while pl not in cou:
#     pl=input("Couleur non disponible, veuillez réessayer")
p1 = "red"
    
    
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
        penup()
        goto(x2, y+largeurP)
        pendown()
    
    t=0
    while t<=3:
        begin_fill()
        rect(largeurT, longeurT*n)
        t+=1
        end_fill()
        
        penup()
        goto(x2+espaceT*(t-1) , y+largeurP)
        pendown()

def dessineDisque(nd, plateau, n):
    dis=input("Choisir la couleur du disque "+ str(nd) +" (en anglais)")
    while dis not in cou:
        dis=input("Couleur non disponible, veuillez réessayer")
    if dis in cou:
        fillcolor(dis)
        pencolor(dis)
        
    if n<2:
        return
    else:
        disque=coords(nd,plateau,n)
        penup()
        goto(disque)
        pendown()
        begin_fill()
        rect(40+(30*(nd-1)),20)
        end_fill()

def effaceDisque(nd, plateau, n):
    if n<2:
        return False
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



def dessineConfig(plateau,n):
    if n<2:
        return 
    else:
        for d in range (1,n+1):
            dessineDisque(d,plateau,n)



def effaceTout(plateau,n):
    if n<2:
        return 
    else:
        for di in range (1,n+1):
            effaceDisque(di,plateau,n)
    up()
    goto(-300,-200)
    down()
    dessinePlateau(n,"red")







#Début programme principale



dessinePlateau(3,"red")
dessineConfig([[],[3,2],[1]], 3)
effaceTout([[],[3,2],[1]], 3)
exitonclick()

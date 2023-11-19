#Partie A


# Numero 1

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
    



#Numero 2

#renvoie le nombre de disques sur cette tour pour une config donnee
def nbDisques(plateau, numtour):
    d= len(plateau[numtour])
    return d #d: nombre de disques



#Numero 3
    
# Renvoie le numero du disque superieur de la tour choisie
def disqueSup(plateau, numtour):
    
    if len(plateau[numtour])>0:
        
        # temp = variable temporaire
        temp= plateau[numtour]
        
        # sup = disque superieur
        sup=temp[len(temp)-1]
        
    # Si la tour est vide:
    else:
        sup= 'Tour vide, pas de disque superieur'
        
    return sup



#Numero 4

# Nous donne la position du disque (dans quelle tour)
def posDisque(plateau,numdisque):
    for i in range (len(plateau)):
        if numdisque in plateau[i]:
            return i 



#Numero 5
    
# Indique si le deplacement de nt1 a nt2 est authorisé    
def verifDepl(plateau, nt1, nt2):
    if nt1 != nt2 :
        bool= len(plateau [nt1])!= 0 and ((len(plateau [nt2])== 0) or (disqueSup(plateau, nt2)>disqueSup(plateau, nt1)))
    else:
        bool= 'Aucun disque a été déplacé'
    # Si bool= True alors le dep est authorisé, sinon, il ne l'est pas
    return bool    



#Numero 6

# Verifie s'il y a une victoire
def verifVictoire(plateau, n):
    
    #modele de la tour2 pour une victoire:
    tourVic=[] 
    for i in range (n,0,-1):
        tourVic.append(i)
        
    #Comparaison de la tour2 du plateau avec le modele precedant:
    victoire=(plateau[2]==tourVic) and len(plateau[0])==0 and len(plateau[1])==0
    return victoire

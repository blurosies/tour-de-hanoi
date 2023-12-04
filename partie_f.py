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
    while i <=len(sol):
        coup=sol[i]
        dep=coup[0]
        arr=coup[1]
        tourD=plateau[dep]
        tourA=plateau[arr]
        effaceDisque(tourD[-1],plateau,n)
        tourA.append(tourD[-1])
        tourD.pop(-1)
        pos(-300,-200)
        dessinePlateau(n,pl)
        dessineConfig(plateau,n)
        i+=1

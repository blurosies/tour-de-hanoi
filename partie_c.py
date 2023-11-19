def jouerUnCoup(plateau,n):
    lireCoords(plateau)
    tourD=plateau[dep]
    tourA=plateau[arr]
    effaceDisque(tourD[-1],plateau,n)
    tourA.append(tourD[-1])
    tourD.pop(-1)
    dessineDisque(tourA[-1],plateau,n)




    

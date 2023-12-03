#Solution du jeu automatique utilisant un algorithme récursif
def automat(disques, depart, arrive):
    if disques==1:
        print(depart , arrive)
    else:
        tourmilieu= 3-(depart+arrive)
        automat(disques-1 , depart , tourmilieu)
        print(depart , arrive)
        automat(disques-1 , tourmilieu , arrive)

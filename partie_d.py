def derniersCoups(coups):
    paire = coups.values()
    coupsLi = list(paire)
    return coupsLi[-1]

#hay whe tenye idk ayyeha btezbat aktr bs laeanno ha tshuf b question 2 awwal whde brke taamellak mshkle

def derniersCoup(coups):
    paire = coups.keys()
    coupsLi = list(paire)
    dep=coupsLi[0]
    arr=coupsLi[1]
    return dep , arr

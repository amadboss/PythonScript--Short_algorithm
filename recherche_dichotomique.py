tab = [2,5,17,19,32]
rec = int(input("le chiffre a chercher"))
x = len(tab)
debut = 0
fin = len(tab)-1

def recherche (tab, rec, debut, fin):
    found = False
    while(debut <= fin and found == False):
        i_pivo = (fin + debut) // 2
        if tab[i_pivo] == rec:
            found = True
        elif tab[i_pivo] < rec :
            debut = i_pivo + 1
        else:
            fin = i_pivo - 1
        if (found == True):
            print(rec, "trouver dans le tableau")
            exit()
        elif (debut > fin):
            print("chiffre non trouvée")
            exit()
        else:
            recherche(tab, rec,debut,fin)
recherche(tab, rec,debut,fin)

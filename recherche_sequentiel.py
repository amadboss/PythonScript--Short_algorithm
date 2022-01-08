tab = [1,4,5,12,17,21]
rec = 22
def tri (tab, rec):
    for i in range(len(tab)):
        if tab[i] == rec:
            print(rec, "trouvé dans le tableau")
            exit()
        elif (tab[i] > rec):
            print(rec, "non trouvé dans le tableau")
        else:
            print(rec, "non trouvé dans le tableau")
            exit()
tri(tab, rec)


tab = [23,51,7,78,0,8,-12000]
print(tab)
def triRapide (tab, debut, fin):
    if debut < fin:
        i_pivo = (debut + fin)//2
        i_pivoOrigine = i_pivo
        i = debut
        while (i < i_pivo):
            if tab[i] > i_pivo:
                tmp = tab[i]
                i = j
                while(j < i_pivo):
                    tab[j] = tab[j+1]
                    j = j + 1
                tab[j] = tmp
                i_pivo = i_pivo - 1
                i = i - 1
            i=i+1
        for(i in range(i_pivoOrigine+1, fin + 1):
            if tab[i] < i_pivo:
                tmp = tab[i]
                j = i
                while(j > i_pivo):
                    tab[j] = tab[j-1]
                    j = j - 1
                tab[j] = tmp
                i_pivo = i_pivo + 1
    triRapide(tab,debut,i_pivo - 1)
    triRapide(tab,i_pivo + 1,fin)
    return tab
triRapide(tab, debut, fin)
print(tab)

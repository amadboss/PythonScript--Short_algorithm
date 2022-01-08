#tab = [2,7-9,18,26,4]
tab = [56,32,1,7,17,-9,17,0,2]

for j in range(1,len(tab)):
    tmp = tab[j]
    i = j
    while(i>0 and tab[i-1] > tmp):
        tab[i] = tab[i-1]
        i = i-1
    tab[i] = tmp
print(tab)

#tab = [56,32,1,7,17,-9,17,0,2]
tab = [1,2,3,4,5]
def toprint():
    for i in range(len(tab)):
        print(tab[i]," ", end='')
toprint()
print()


for j in range(len(tab)-1):
    tri = True
    for i in range(len(tab)-1-j):
        if tab[i] > tab[i+1]:
            tmp = tab[i+1]
            tab[i+1] = tab[i]
            tab[i] = tmp
            tri = False
        if tri == True:
            toprint()
            exit()
toprint()

from random import randint
N = 3
M = 5
lst=[[randint(2, 11) for i in range(N)] for i in range(M)]
for i in lst:
    print()
    for j in i:
        print (j, end=" ")
kol=0 
num_str=0
for i in range(M): 
    for j in range(N):
        kol_new=lst[i].count(lst[i][j]) 
        if kol_new>kol: 
            kol=kol_new 
            num_str=i   
print()
print("Номер строки: ", num_str)

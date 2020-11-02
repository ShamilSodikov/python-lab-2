print ("Введите какой сейчас час и сколько прошло секунд с начала дня")
X=int(input())
X=X//1
X=X*60*60
N=int(input())
T= N-X
T=T//60
print(T)

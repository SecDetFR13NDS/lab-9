from random import random, randrange, randint
k=[]
for num in range(6):
    x=float(input('Введіть число:'))
    k.append(x)

arr = []
for x in range(1, 10):
    arr.append(randint(1, 100))

C=set(arr)
D=set(k)
sum1=sum(C)
sum2=sum(D)
sum=sum2+sum1
print(sum)
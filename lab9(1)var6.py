import math
X=(11.4,10.5)
O=[0.0,0.0]
Y=(1.4,5.5)
Z=(8.4,3.5)
a=[]
vidsX= math.sqrt(((O[0]-X[0])**2)+((O[1]-X[1])**2))
vidsY= math.sqrt(((O[0]-Y[0])**2)+((O[1]-Y[1])**2))
vidsZ= math.sqrt(((O[0]-Z[0])**2)+((O[1]-Z[1])**2))
a.append(vidsX)
a.append(vidsY)
a.append(vidsZ)
print (a)
if a[0] == min(a):
    print(X)
elif a[1] == min(a):
    print(Y)
elif a[2] == min(a):
    print(Z)
if a[0] == max(a):
    print(X)
elif a[1] == max(a):
    print(Y)
elif a[2] == max(a):
    print(Z)



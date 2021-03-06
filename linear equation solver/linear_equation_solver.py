#to use this code modify the linear_equations.txt with the linear equation

#v and u are lists that imitate a vector
#a is just a float
#the functions bellow are vector operations as their names suggests
from functools import reduce


def vec_sum (u: list,v: list):
    return list (map(lambda x,y:x+y,u,v))

def vec_mult (u: list,a: float):
    return list(map(lambda x: x*a,u))
def vec_div (u: list,a: float):
    return list(map(lambda x: x/a if a!=0 else 10**3,u))

LL = []
a=open("linear equation solver\linear_equations.txt","r")

while L:=a.readline():
    L = L.split()
    for i in range(len(L)):
        L[i] = float(L[i])
    LL.append(L)

for i in range (len(LL)):
    if ((LL[0][0]) == 0):
        LL[0], LL[1] = LL[1], LL[0]
    if ((LL[1][1]) == 0 and len(LL)>2):
        LL[1], LL[2] = LL[2], LL[1]
    if (len(LL)>2):
        LL[2],LL[len(LL)-1]=LL[len(LL)-1],LL[2]
    if (((LL[0][0])*(LL[1][1])-(LL[0][1])*(LL[1][0]))>0):
        break

for i in range(len(LL)):
    LL[i] = vec_div(LL[i], LL[i][i])
    for j in range(0, i):
        LL[j] = vec_sum(LL[j], vec_mult(LL[i], -(LL[j][i])))
    for a in range(i + 1, len(LL)):
        LL[a] = vec_sum(LL[a], vec_mult(LL[i], -(LL[a][i])))
for k in range(len(LL)):
    print (f'X{k+1} = {LL[k][-1]}')


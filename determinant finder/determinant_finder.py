from functools import reduce

#modify the determinant.txt with the matrix ixi

#some vector operation functions
def vec_sum (u: list,v: list):
    return list (map(lambda x,y:x+y,u,v))
def vec_mult (u: list,a: float):
    return list(map(lambda x: x*a,u))
def vec_div (u: list,a: float):
    return list(map(lambda x: x/a if a!=0 else 10**3,u))
def vec_dot_excludingxindex (u: list,v: list,x: int):
    multipliedlist=list(map (lambda a,b: a*b,u,v))
    multipliedlist.pop(x)
    return reduce (lambda a,b: a+b,multipliedlist)
LL = []
a=open("determinant finder\determinant.txt","r")
L = a.readline()
for i in range (len(L.split())):
    L = L.split()
    for i in range(len(L)):
        LL.append( float(L[i]))
    L = a.readline()

tam=len(LL)
tam_sqrt=int (tam**0.5)
U={}
L={}

for i in range (tam_sqrt):
    u,l=[],[]
    for j in range (tam_sqrt):
        if i>=j:
            u.append(10)
        else:
            u.append(0)
        if i==j:
            l.append (1)
        elif i>j:
            l.append(10)
        else:
            l.append(0)
    U[i]=u
    L[i]=l
atuaU,linha,linhat=0,0,0
for x in range (tam):
    if linha!=(x//(tam_sqrt)):
        linhat=0
    linha=x//(tam_sqrt)
    if  ((x%tam_sqrt)==0) and (x>=tam_sqrt):
        atuaU=0
    if  linhat!=linha:
        L[linha][linhat]=(LL[x]-(vec_dot_excludingxindex((L[linha]),(U[atuaU]),linhat) ) )/(U[linhat][linhat])
        linhat = linhat + 1
    else:
        U[atuaU][linha]=(LL[x]-(vec_dot_excludingxindex(U[atuaU],L[linha],linha)))/L[linha][linha]
    atuaU+=1
determinante=1
for y in range(tam_sqrt):
    determinante=(U[y][y])*determinante
print('determinant =',determinante)
def vec_sum (a,b):
    a=list (a)
    for i in range (len(a)):
        a[i]+=b[i]
    return a
def vec_mult (a,v):
    a=list (a)
    for i in range (len(a)):
        a[i]=a[i]*v
    return a
def vec_div (a,x):
    a=list (a)
    if (x==0):
        return 1
    else:
        for i in range (len (a)):
            a[i]/=x
        return a
def prodvec_no0 (u,v,x):
    suma=0
    for i in range (0,len(u)):
        if x==i:
            continue
        suma+=(u[i]*v[i])
    return suma

LL = []
a=open("determinante.txt","r")
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
#print (tam_sqrt)
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
        L[linha][linhat]=(LL[x]-(prodvec_no0((L[linha]),(U[atuaU]),linhat) ) )/(U[linhat][linhat])
        linhat = linhat + 1
    else:
        U[atuaU][linha]=(LL[x]-(prodvec_no0(U[atuaU],L[linha],linha)))/L[linha][linha]
    atuaU+=1
determinante=1
for y in range(tam_sqrt):
    determinante=(U[y][y])*determinante
print('determinante =',determinante)
#to use this code modify the sistemaslineares.txt with the 

#v and u are lists that imitate a vector
#a is just a float
#some of the code is commented for me to remember old methods :(
def vec_sum (u,v):
    """
    u=list (u)
    for i in range (len(u)):
        u[i]+=v[i]
    return u
    """
    return list (map(lambda x,y:x+y,u,v))

def vec_mult (u,a):
    """
    u=list (u)
    for i in range (len(u)):
        u[i]=u[i]*a
    return u
    """
    return list(map(lambda x: x*a,u))
def vec_div (u,a):
    """
    u=list (u)
    if (a==0):
        return 1
    else:
        for i in range (len (u)):
            u[i]/=a
        return u
    """
    return list(map(lambda x: x/a if a!=0 else 10**3,u))

LL = []
a=open("sistemaslineares.txt","r")
L = a.readline()
while L != '---':
    L = L.split()
    for i in range(len(L)):
        L[i] = float(L[i])
    LL.append(L)
    L = a.readline()

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
    #for k in range(len(LL)):
    #    print(LL[k])
    #print('\n')

for k in range(len(LL)):
    print (f'X{k+1} = {LL[k][-1]}')


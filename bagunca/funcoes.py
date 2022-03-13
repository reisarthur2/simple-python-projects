import json
#Constantes
pi=3.1415926535898
e=(1+1/12000)**12000
dx=0.0001
potencios={'mx':1,'cx':10,'dx':100,'x':1000}
#=alterar função =====================================

def func (x):
    return sqrt (3-4*x*x)
def funcd (x):
    return 1
#=====================================================
#dicionario
def addicionario_txt (k,v,txt):
    with open(txt,'r') as ovo:
        raizes=ovo.readline()
        raizes=raizes.replace("'",'"')
        raizes=json.loads(raizes)
    with open(txt,'w') as ovo:
        if k not in raizes:
            raizes[str(k)]=v
        ovo.write(str (raizes))
#funcoes basicas
def facto(x):
    if x<=1:
        return 1
    else:
        return x*facto(x-1)

def exp(x):
    return e**x

def sqrt(x):
    return x**0.5

def ln (x):
    resp=0
    if (x==1):
        return 0
    elif (x<(e+0.3) and x>(e-0.2)):
        return 1
    else:
        x-=1
        if (x<=-0.8):
            resp=345.362831724+(x*371.7163843714)
        elif (x<=0.75):
            resp=(x-(x**2)/2+(x**3)/4-(x**4)/5+
                (x**5)/6-(x**6)/7+(x**7)/8-
                (x**8)/9+(x**9)/10-(x**10)/11+
                (x**11)/12-(x**12)/13+(x**13)/14-
                (x**14)/15)
        elif (x<=3):
            resp=0.3595041322*x+0.3260485214
        elif (x<=6.1):
            resp=0.182221382*x+0.88415291943
        elif (x<=10.5):
            resp=0.1180169*x+1.2416843323
        elif (x<=33):
            resp=0.049521391*x+1.970851054
        elif (x<=96):
            resp=0.01594862*x+3.09135807624
        else:
            resp=4.8
        return resp

def cos (teta):
    sas=0
    for n in range (40):
        sas+=((((-1)**n)*((teta)**(2*n)))/(facto(2*n)))
    sas=round (sas,3)
    return sas

def sin (teta):
    sas=0
    for n in range (40):
        sas+=(((-1)**n)*(teta**(2*n+1)))/(facto(2*n+1))
    sas=round (sas,3)
    return sas

def deg (teta):
    return ((pi*teta)/180)
#print (sin (deg(30)))
#=====================================================
def gaussiana (m,v,x):
    return (exp(-0.5*((x-m)/v)))/(v*sqrt(2*pi))

#metodos
def reguFalsi (a,b,c):
    x,y=func (a),func(b)
    c=(a*y-b*x)/(y-x)
    #if (abs(c-a)/c)<0.000001 or abs((c-b)/c)<0.000001:
    #   return -c
    if (func(c))<0.000001:
        return (c)
    else:
        return reguFalsi(b,c,1)

def Menew (b):
    b= b-(func(b)/funcd(b))
    if abs (func(b))<=0.00001:
        return b
    else:
         return Menew (b)

def integrnum (a,b):
    suma=0
    while a<=b:
        suma+=(dx*func(a))
        a+=dx
    return suma

def intg (a,b):
    suma=0
    bolo=a
    while a<=b:
        suma=suma+func (a)
        a+=dx
    suma*=2
    return (dx/2)*(suma+func(bolo)+func(b))

def derivNum (x):
    a= (func(x+dx)-func(x))/dx
    if (a<0):
        return a+dx
    elif (a>0):
        return a-dx
    else:
        return a

def retg (x):
    b=func(x)-derivNum(x)*x
    return 'y =',derivNum(x),'*','x','+',b

def vec_proj(u,v):
    return vec_mult((vec_produto_esc(u,v)/vec_produto_esc(u,v)),v)

def prodvec_no0 (u,v,x):
    suma=0
    for i in range (0,len(u)):
        if x==i:
            continue
        suma+=(u[i]*v[i])
    return suma

def det (list_cont_de_matriz):
    LL=list_cont_de_matriz
    tam = len(LL)
    tam_sqrt = int(tam ** 0.5)
    U = {}
    L = {}
    for i in range(tam_sqrt):
        u, l = [], []
        for j in range(tam_sqrt):
            if i >= j:
                u.append(10)
            else:
                u.append(0)
            if i == j:
                l.append(1)
            elif i > j:
                l.append(10)
            else:
                l.append(0)
        U[i] = u
        L[i] = l
    atuaU, linha, linhat = 0, 0, 0
    for x in range(tam):
        if linha != (x // (tam_sqrt)):
            linhat = 0
        linha = x // (tam_sqrt)
        if ((x % tam_sqrt) == 0) and (x >= tam_sqrt):
            atuaU = 0
        if linhat != linha:
            L[linha][linhat] = (LL[x] - (prodvec_no0((L[linha]), (U[atuaU]), linhat))) / (U[linhat][linhat])
            linhat = linhat + 1
        else:
            U[atuaU][linha] = (LL[x] - (prodvec_no0(U[atuaU], L[linha], linha))) / L[linha][linha]
        atuaU += 1
    determinante = 1
    for y in range(tam_sqrt):
        determinante = (U[y][y]) * determinante
    return (determinante)
#======================================================
#interpolador
def newpoler (lisx,lisy):
    if (len(lisx))==1:
        return lisy[0]
    elif (len(lisx))<1:
        return 0
    else:
        return ((newpoler((lisx[1:]),(lisy[1:])))-(newpoler((lisx[:(len(lisx)-1)]),(lisy[:(len(lisx)-1)]))))/((lisx[(len(lisx)-1)])-(lisx[0]))

# Funçoes uteis
def listr_lisfloat (list):
    for i in range (len (list)):
        list[i]=float (list[i])
    return list

def raiz (n,a):
    n = 1 / 2 * (n + a / n)
    if (a==0):
        return 0
    elif abs ((n*n)-a)<=0.00000000000001:
        return n
    else:
        return raiz(n,a)

"""def fact (x):
    if x==1 or x==0:
        return x
    else:
        return x*fact(x-1)
"""
def media_LN (lista_num):
    a,n=0,0
    zuz=lista_num#.split ()
    for x in zuz:
        x=float(x)
        x+=a
        a=x
        n+=1
    return a/n

def pos (u,i,j):
  return u+str(i+1)+str(j+1)

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
#modificado
def vec_div (a,x):
    a=list (a)
    if (x==0):
        return 1
    else:
        for i in range (len (a)):
            a[i]/=x
        return a
#modificado
def vec_produto_esc (u,v):
    if (len (u)==len (v)):
        ps=0
        for i in range (len(u)):
            ps+=(u[i]*v[i])
        return ps
    else:
        return 1

def vec_produto_vetorial (u,v):
    if (len(u)==2):
        u.append(0)
        v.append(0)
    if (len(u)==len(v) and len(u)==3):
        return [(u[1]*v[2])-(u[2]*v[1]),(u[2]*v[0])-(u[0]*v[2]),(u[0]*v[1])-(u[1]*v[0])]

def vec_proj(u,v):
    return vec_mult((vec_produto_esc(u,v)/vec_produto_esc(u,v)),v)

def modulo (v):
    v=list (v)
    res=0
    for i in v:
        res+=(i**2)
    return sqrt (res)

def vec_versor (p1,p2):
    p=vec_sum (p2,vec_mult(p1,-1))
    return vec_div (p, modulo(p))

def det_2 (a,b):
    return a[0]*b[1]-a[1]*b[0]

def det_3 (a,b,c):
    a[0]*b[1]*c[2]+a[1]*b[2]*c[0]+a[2]*b[0]*c[1]-c[0]*b[1]*a[2]-c[1]*b[2]*a[0]-c[2]*b[0]*a[1]

def bahskara (a,b,c,p):
    if a<0:
        a,b,c=-a,-b,-c
    deltar=raiz (1,(b**2)-4*a*c)
    x1=(deltar-b)/(2*a)
    x2=(-b-deltar)/(2*a)
    if p=='p':
        if (x1<=0):
            return x2
        else:
            return x1
    else:
        return (x1,x2)



def grafico_barra(x, y, z):
  plt.bar(x, y)
  plt.title(z[1:])
  plt.xlabel('numero/letra')
  plt.ylabel('Quantidade')
  plt.savefig(z+'.png')
  plt.close()
contador=1

def ln (x):
    i=0
    while True:
        y=exp(i)
        if abs (y-x)<0.02:
            return i
            break
        elif y>x:
            i-=0.05
        elif y<x:
            i+=0.05
#print (modulo([1/2,sqrt(2/3),sqrt(3)/6]))
"""k=1/((10**-9)/9)

a=[21*(sqrt(3)/2),10.5,0]
b=[0,21,0]
c=[0,0,0]
d=[6.0622,10.5,7*sqrt(6)]
deiz=10**-9
Q1,Q2,Q3,Q4=-12*deiz,-5*deiz,9*deiz,27*deiz

f41=vec_mult (vec_versor(a,d),Q1)
f42=vec_mult (vec_versor(b,d),Q2)
f43=vec_mult (vec_versor(c,d),Q3)
print (modulo(aa:=[sqrt(3)*14/3,7,-8*sqrt(6)/3]),'\n')

print (a,'\n')
print (sus:=vec_sum(vec_sum(f41,f42),f43),'\n')
bla=(k*Q4)/(.21**2)
#print (bla)
print ("\naaa", 5.51*sqrt((196/3)+128/3))

resp=modulo(sus)*bla
#print (resp)
print ("{:e}".format(resp*10**8))"""




"""fa=(k*20*-15*10**-18)/(4)
fb=((k*20*25*10**-18)/8)*(sqrt(2)/2)
sus=sqrt ((fb)**2+(fb+fa)**2)
print ("{:e}".format(sus))"""
"""falhas
def cos_rad (x):
    if (abs (x)>=2*pi):
        a=x//pi
        x=abs(x)-pi*a
    result=1-(x**2)/2+(x**4)/24-(x**6)/720+(x**8)/40320-(x**10)/3628800+(x**12)/47001600-(x**14)/87178291200
    if (-0.0001<=result<=0.0001):
        return 0
    elif (0.9999<=result<=1.0001):
        return 1
    elif (abs (result+1)<0.1):
        return -1
    else:
        return result

def ln (x):
    y=1+x
    res=0
    for n in range (1,20):
        res+=(((-1)**(n+1))*((y**n)/(n)))
    return res
        """

a=[-4,6,0]
b=[-4,6,0]

print (modulo (vec_produto_vetorial (a,b)))
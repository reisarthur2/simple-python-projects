

"""


def achadorpontox (a,b):
	return [a[0]+(((1-func(a,''))*(b[0]-a[0]))/(func(b,'')-func(a,''))),b[1]]

def achadorpontoy (a,b):
	inicio=a[1]
	fim=b[1]
	return [b[0],(inicio+((1-func(a,""))*(fim-inicio))/(func(b,'')-func(a,'')))]

def absoluto (n):
	if n<0:
		return -n
	else:
		return n
def ponto_medio (a,b):
	return [(a[0]+b[0])/2,(a[1]+b[1])/2]
def achadorpontox (a,b):
	inicio=a[0]
	fim=b[0]

	return [(inicio+((1-func(a,""))*(fim-inicio))/(func(b,'')-func(a,''))),b[1]]

def achadorpontoy (a,b):
	inicio=a[1]
	fim=b[1]
	return [b[0],(inicio+((1-func(a,""))*(fim-inicio))/(func(b,'')-func(a,'')))]

def fazedorlinha (a,b):
	saidax=[]
	saiday=[]
	cor=[]
	vetor=[-b[0]+a[0],-b[1]+a[1]]
	cont=0
	while cont<=1:
		saidax.append(b[0]+vetor[0]*cont)
		saiday.append(b[1]+vetor[1]*cont)
		cor.append ("#ff0000")
		cont+=0.1
	return saidax,saiday,cor

def doisde (x, y,c):
  plt.scatter(x, y,marker='.',color=c)
  plt.title('rate')
  plt.xlabel('rate')
  plt.ylabel('pop')
  plt.show()

def func (a,b):
	if (type(a)==int or type(a)==float):
		x,y=a,b
	else:
		x,y=a[0],a[1]

	return x**2+y**2-9
	#return x**3+y**3-6*x*y

"""


"""from errno import EILSEQ
from ssl import PROTOCOL_TLSv1_1
import matplotlib.pyplot as plt
import matplotlib
from random import randint

def doisde (x, y,c):
  plt.scatter(x, y,marker='.',color=c)
  #plt.grid ()
  plt.title('rate')
  plt.xlabel('rate')
  plt.ylabel('pop')
  #matplotlib.lines.Line2D(d,e,linewidth=2)
  plt.show()

def fazedorlinha (a,b):
	saidax=[]
	saiday=[]
	cor=[]
	vetor=[-b[0]+a[0],-b[1]+a[1]]
	cont=0
	while cont<=1:
		saidax.append(b[0]+vetor[0]*cont)
		saiday.append(b[1]+vetor[1]*cont)
		cor.append ("#ff0000")
		cont+=0.01
	return saidax,saiday,cor

def func (a,b):
	return a**3+b**3-6*a*b
xis=[]
yis=[]
cores=[]

cormenor='#00001E'
cormaior='#00E100'

for i in range (1000):
	x=randint(0,10)
	y=randint(0,10)
	if (func(x,y)<0):
		cores.append(cormenor)
	else:
		cores.append(cormaior)
	yis.append (y)
	xis.append (x)
doisde (xis,yis,cores)"""
"""
def absoluto (n):
	if n<0:
		return -n
	else:
		return n
#print (type (round (0.0000000000000001,20)))
#a[0],a[1],b[0],b[1]=round(a[0],3),round(a[1],3),round(b[0],3),round(b[1],3)
def func (a,b):
	if (type(a)==int or type(a)==float):
		x,y=a,b
	else:
		x,y=a[0],a[1]
	#print (x**2+y**2-9)
	return x**2+y**2-9
	

def achadorpontox (a,b):
	if (round(a[0])==0) or (round(a[1])==0) or (round(b[0])==0) or (round(b[1])==0):
		inicio=a[0]
		fim=b[0]
		erro=0.3
		while (func (inicio,b[1])<erro):
			inicio+= absoluto ((a[0]-b[0])/10)
		return [inicio,b[1]]
	else:
		return [a[0]+(((1-func(a,''))*(b[0]-a[0]))/(func(b,'')-func(a,''))),b[1]]

def achadorpontoy (a,b):
	inicio=a[1]
	fim=b[1]
	if (round(a[0])==0) or (round(a[1])==0) or (round(b[0])==0) or (round(b[1])==0):
		erro=0.3
		while (func (b[0],inicio)<erro):
			inicio+= absoluto ((a[1]-b[1])/10)
		return [b[0],inicio]
	else:
		return [b[0],(inicio+((1-func(a,""))*(fim-inicio))/(func(b,'')-func(a,'')))]

cima1,cima2=[-0.33333333333333365, 3.333333333333333] ,[-3.3306690738754696e-16, 3.333333333333333]
baixo1,baixo2=[-0.33333333333333365, 2.9999999999999996] ,[-3.3306690738754696e-16, 2.9999999999999996]

print (achadorpontox(baixo1,baixo2))"""


from ssl import PROTOCOL_TLSv1_1


dx=0.01
def derivNumx (x,y):
    a= (func(x+dx,y)-func(x,y))/dx
    return a

def derivNumy (x,y):
    a= (func(x,y+dx)-func(x,y))/dx
    return a

def achadorpontoy (a,b):
	return Menewy (a[0],(b[1]+a[1])/2)
	
def Menewy (x,y):
	print (y)
	y= y-(func(x,y)/derivNumy(x,y))
	if abs (func(x,y))<=0.01:
		return y
	else:
		return Menewy (x,y)

def Menewx (x,y):
	x= x-(func(x,y)/derivNumx(x,y))
	if abs (func(x,y))<=0.1:
		return x
	else:
		return Menewx (x,y)

def func (a,b):
	if (type(a)==int or type(a)==float):
		x,y=a,b
	else:
		x,y=a[0],a[1]

	return (x**2+y**2)-16

def achadorpontox (a,b):
	return Menewx ((a[0]+b[0])/2,b[1])

def achadorpontoy (a,b):
	return Menewy (a[0],(b[1]+a[1])/2)

"""pt1=[3,2]
pt2=[4,2]

pt3=[2,3]
pt4=[2,4]"""
#
#pt1=[-2,-3]
#pt2=[-1,-3]
#pt3=[-2,-4]
#pt4=[-1,-4]
#
#print (achadorpontoy(pt2,pt4))

import math
t=56.66
ac=0.52709/4
print (t*math.tan(ac))


for i in range (10**10):
	print ("geraste",i,"sexos")
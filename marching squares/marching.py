from cmath import sin, sqrt
from errno import EILSEQ
import matplotlib.pyplot as plt
from random import randint
dx=0.01

grade_geral=0 #1 se quiser grade colorida, 0 se nao
#codigo ainda instavel para alguns limites e funcoes

#funcao principal que sera plotada no final, alterar o return e por a funcao
#no formato f(x,y)=0 sem o = 0
def func (a,b):
	if (type(a)==complex):
		a=a.real
	if (type(a)==int or type(a)==float	):
		x,y=a,b
	else:
		x,y=a[0],a[1]
	return x*x-y**0.5+2 #=0
	#return x*y-y-8

#alterar pontos para mudar o tanto de pontos que cada linha e coluna
#tera a partir do (0,0) para as quatro direcoes (total de (2*pontos)+1)
#em cada linha/coluna

#alterar os limites para mudar a area de plot (mesmo para os limites negativos
# use valores positivos)
#nao alterar ainda os limites, ta um pouco quebrado :(=======================================================
pontos=100

limxpos=5
limxneg=5
limypos=5
limyneg=5

#metodos de newton para achar raizes usando x e y, respectivamente, como variaveis
#e y e x, respectivamente, como constantes (float, float)-->float
def Menewx (x,y):
	if (type(x)==complex):
		x=x.real
	if (x>limxpos):
		return limxpos
	if (x<-limxneg):
		return -limxneg
	try:
		x= x-(func(x,y)/derivNumx(x,y))
	except:
		x+=dx
		x= x-(func(x,y)/derivNumx(x,y))
	if abs (func(x,y))<=0.1:
		return x
	else:
		return Menewx (x,y)
def Menewy (x,y):
	if (type(y)==complex):
		y=y.real
	
	if (y>limypos):
		return limypos
	if (y<-limyneg):
		return -limyneg
	try:
		y= y-(func(x,y)/derivNumy(x,y))
	except:
		y+=dx
		y= y-(func(x,y)/derivNumy(x,y))
	if abs (func(x,y))<=0.1:
		return y
	else:
		return Menewy (x,y)

#derivadas numericas em relacao a x e y com a outra variavel como constante (float,float)-->float
def derivNumx (x,y):
    a= (func(x+dx,y)-func(x,y))/dx
    return a
def derivNumy (x,y):
    a= (func(x,y+dx)-func(x,y))/dx
    return a

#funcoes que encontram o ponto da borda da funcao principal, cujo valor
#eh 0, que esta entre dois pontos (list[2],list[2])-->list[2]
def achadorpontox (a,b):
	return [Menewx ((a[0]+b[0])/2,b[1]),b[1]]
def achadorpontoy (a,b):
	return [a[0],Menewy (a[0],(b[1]+a[1])/2)]

#mesmas funcoes anteriores, mas apresentam algum defeito no algoritimo
#reparar futuramente :(
"""
def achadorpontox (a,b):
	return [a[0]+(((1-func(a,''))*(b[0]-a[0]))/(func(b,'')-func(a,''))),b[1]]
def achadorpontoy (a,b):
	inicio=a[1]
	fim=b[1]
	return [b[0],(inicio+((1-func(a,""))*(fim-inicio))/(func(b,'')-func(a,'')))]
"""
#funcao que cria linha entre dois pontos, qtde de pontos pode ser alterada diretamente
#na funcao na variavel pontos, (list[2],list[2])--> list (list(coordx),list(coordy),list(cor '#ff0000'))
def fazedorlinha (a,b):
	saidax=[]
	saiday=[]
	cor=[]
	vetor=[-b[0]+a[0],-b[1]+a[1]]
	tamanho_vetor=((vetor[0])**2+(vetor[1])**2)**.5

	distancia_entre_pontos=50

	adicionador=1/(distancia_entre_pontos*tamanho_vetor)
	if (type(adicionador)==complex):
		adicionador=adicionador.real
	cont=0
	while cont<=1:
		saidax.append(b[0]+vetor[0]*cont)
		saiday.append(b[1]+vetor[1]*cont)
		cor.append ("#ff0000")
		cont+=adicionador
	return saidax,saiday,cor

#plotador de grafico do tipo scatter (list (coordx),list(coordy),list(cores))-->void
def doisde (x, y,c):
  plt.scatter(x, y,marker='.',color=c)
  plt.title('rate')
  plt.xlabel('rate')
  plt.ylabel('pop')
  plt.show()

#funcoes uteis (float)-->float
def facto(x):
    if x<=1:
        return 1
    else:
	    return x*facto(x-1)

malhax=[]
malhay=[]
cores=[]

listapontos=[]

resolucaoxy=(limxpos+limxneg)/pontos

y=-limyneg
auxiliary=0
while (y<=limypos or auxiliary<=(pontos)):
	x=-limxneg
	auxiliarx=0
	while (x<=limxpos or auxiliarx<=(pontos)):
		listapontos.append ([round (x,2),round(y,2)])
		
		if (grade_geral==1):
			malhax.append(x)
			malhay.append(y)
			try:
				if (func(x,y)<0):
					cores.append ('#0000ff')
				else:
					cores.append ("#00ff00")
			except:
				cores.append('#000000')
		auxiliarx+=1
		x+=resolucaoxy
	y=y+resolucaoxy
	auxiliary+=1
cont=0
while True:
	try:
		cima2=listapontos[cont+auxiliarx+1]
	except:
		break
	baixo1=listapontos[cont]
	baixo2=listapontos[cont+1]
	cima1=listapontos[cont+auxiliarx]
	
	#verificador dos pontos      o o o->  cima1   cima  cima2
	#se estão dentro ou fora     o   o->   esq           dir
	#e inicio e fim da linha     o o o-> baixo1  baixo  baixo2
	
	try:
		teste=func(cima1,'')<=0
		teste=func(cima2,'')<=0
		teste=func(baixo1,'')<=0
		teste=func(baixo2,'')<=0
	except:
		
		if (cima2[0]==(limxpos)):
			cont+=2
		else:
			cont+=1
		continue
	#if ((func(cima1,"")<=0 and func(cima2,"")<=0)and(func(baixo1,"")<=0 and func(baixo2,"")<=0)):
	#	if (cima2[0]==(limxpos)):
	#		cont+=2
	#	else:
	#		cont+=1
	#	continue
	if (func(cima1,"")<=0 and func(cima2,"")<=0):
		if (func(baixo1,"")>=0 and func(baixo2,"")>=0):
			esq=achadorpontoy (cima1, baixo1)
			dir=achadorpontoy (cima2,baixo2)
			linhax_linhay_cores=fazedorlinha(esq,dir)
			malhax.extend(linhax_linhay_cores[0])
			malhay.extend(linhax_linhay_cores[1])
			cores.extend(linhax_linhay_cores[2])
		elif (func(baixo1,"")<=0 and func(baixo2,"")>=0):
			cima=achadorpontox (baixo1,baixo2)
			esq= achadorpontoy (cima2,baixo2)
			linhax_linhay_cores=fazedorlinha(esq,cima)
			malhax.extend(linhax_linhay_cores[0])
			malhay.extend(linhax_linhay_cores[1])
			cores.extend(linhax_linhay_cores[2])	
		elif (func(baixo1,"")>=0 and func(baixo2,"")<=0):
			cima=achadorpontox(baixo1,baixo2)
			dir=achadorpontoy (cima1,baixo1)
			linhax_linhay_cores=fazedorlinha(cima,dir)
			malhax.extend(linhax_linhay_cores[0])
			malhay.extend(linhax_linhay_cores[1])
			cores.extend(linhax_linhay_cores[2])
	elif (func(baixo1,"")<=0 and func(baixo2,"")<=0):
		if (func(cima1,"")>=0 and func(cima2,"")>=0):
			esq=achadorpontoy (baixo1,cima1)
			dir=achadorpontoy (baixo2,cima2)
			linhax_linhay_cores=fazedorlinha(esq,dir)
			malhax.extend(linhax_linhay_cores[0])
			malhay.extend(linhax_linhay_cores[1])
			cores.extend(linhax_linhay_cores[2])
		elif (func(cima1,"")<=0 and func(cima2,"")>=0):
			dir=achadorpontoy(cima2,baixo2)
			cima=achadorpontox (cima1,cima2)
			linhax_linhay_cores=fazedorlinha(dir,cima)
			malhax.extend(linhax_linhay_cores[0])
			malhay.extend(linhax_linhay_cores[1])
			cores.extend(linhax_linhay_cores[2])
		elif (func(cima1,"")>=0 and func(cima2,"")<=0):
			esq=achadorpontoy(cima1,baixo1)
			cima=achadorpontox (cima1,cima2)
			linhax_linhay_cores=fazedorlinha(esq,cima)
			malhax.extend(linhax_linhay_cores[0])
			malhay.extend(linhax_linhay_cores[1])
			cores.extend(linhax_linhay_cores[2])
	elif (((func (cima1,'')<=0)and(func(baixo1,'')<=0))or((func(baixo2,'')<=0)and(func (cima2,'')<=0))):
		cima=achadorpontox(cima1,cima2)
		baixo=achadorpontox(baixo1,baixo2)
		linhax_linhay_cores=fazedorlinha(cima, baixo)
		malhax.extend(linhax_linhay_cores[0])
		malhay.extend(linhax_linhay_cores[1])
		cores.extend(linhax_linhay_cores[2])
	elif ((func(cima1,"")<=0) and (func(baixo2,'')<=0)):
		dir=achadorpontoy(cima2,baixo2)
		cima=achadorpontox(cima1,cima2)
		linhax_linhay_cores=fazedorlinha(dir,cima)
		malhax.extend(linhax_linhay_cores[0])
		malhay.extend(linhax_linhay_cores[1])
		cores.extend(linhax_linhay_cores[2])
		esq=achadorpontoy(cima1,baixo1)
		baixo=achadorpontox(baixo1,baixo2)
		linhax_linhay_cores=fazedorlinha(esq,baixo)
		malhax.extend(linhax_linhay_cores[0])
		malhay.extend(linhax_linhay_cores[1])
		cores.extend(linhax_linhay_cores[2])
	elif ((func(cima2,"")<=0) and (func(baixo1,'')<=0)):
		esq=achadorpontoy(cima1,baixo1)
		cima=achadorpontox(cima1,cima2)
		linhax_linhay_cores=fazedorlinha(esq,cima)
		malhax.extend(linhax_linhay_cores[0])
		malhay.extend(linhax_linhay_cores[1])
		cores.extend(linhax_linhay_cores[2])
		dir=achadorpontoy(cima2,baixo2)
		baixo=achadorpontox(baixo1,baixo2)
		linhax_linhay_cores=fazedorlinha(dir,baixo)
		malhax.extend(linhax_linhay_cores[0])
		malhay.extend(linhax_linhay_cores[1])
		cores.extend(linhax_linhay_cores[2])
	elif (func(cima1,"")<=0):
		esq=achadorpontoy(cima1,baixo1)
		cima=achadorpontox(cima1,cima2)
		linhax_linhay_cores=fazedorlinha(esq,cima)
		malhax.extend(linhax_linhay_cores[0])
		malhay.extend(linhax_linhay_cores[1])
		cores.extend(linhax_linhay_cores[2])
	elif (func(cima2,"")<=0):
		dir=achadorpontoy(cima2,baixo2)
		cima=achadorpontox(cima1,cima2)
		linhax_linhay_cores=fazedorlinha(dir,cima)
		malhax.extend(linhax_linhay_cores[0])
		malhay.extend(linhax_linhay_cores[1])
		cores.extend(linhax_linhay_cores[2])
	elif (func(baixo1,"")<=0):
		esq=achadorpontoy(cima1,baixo1)
		baixo=achadorpontox(baixo1,baixo2)
		linhax_linhay_cores=fazedorlinha(esq,baixo)
		malhax.extend(linhax_linhay_cores[0])
		malhay.extend(linhax_linhay_cores[1])
		cores.extend(linhax_linhay_cores[2])
	elif (func(baixo2,"")<=0 and (func(baixo1,'')>=0)):
		dir=achadorpontoy(cima2,baixo2)
		baixo=achadorpontox(baixo1,baixo2)
		linhax_linhay_cores=fazedorlinha(dir,baixo)
		malhax.extend(linhax_linhay_cores[0])
		malhay.extend(linhax_linhay_cores[1])
		cores.extend(linhax_linhay_cores[2])
	#print (cima1,cima2)
	#print (baixo1,baixo2,'\n')
	if (cima2[0]==(limxpos)):
		cont+=2
	else:
		cont+=1
			

doisde (malhax,malhay,cores)

#ignorar, versao antiga baseada em pinceladas aleatorias em um canvas
#torcendo para que saia uma obra de arte
"""
def func (x,y):
	return (x-50)**2+(y-50)**2-400
xis=[]
yis=[]
cores=[]

cormenor='#00001E'
cormaior='#00E100'

for i in range (1000):
	x=randint(0,100)
	y=randint(0,100)
	if (func(x,y)<0):
		cores.append(cormenor)
	else:
		cores.append(cormaior)
	yis.append (y)
	xis.append (x)
doisde (xis,yis,cores)
"""
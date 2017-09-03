"""
TO-DO:

22/08/2017
Estado: pendiente
	-Completar los encabezados de clases


22/08/2017
Estado: pendiente
	-Coherencia entre los nombres de funciones
	por ejemplo, hay una funcion llamada rot_center y otra sumarAngulo
	o la llamamos rotCenter (a mi me gusta esta notacion) 
	o la llamamos sumar_angulo (mmm notacion FEA)

22/08/2017
Estado: pendiente
	-Pasar por parametro la superficie donde se va a imprimir EN TODAS LAS CLASES


22/08/2017
Estado: pendiente
	-Revisar la generacion de planetas, poner condiciones para que no se superpongan

MINUTAS Fuckkk
hay que hablar seriamente sobre coordenadas absolutas y relativas
por que ya voy mareado con este tema de lo que se mueve y lo que no

"""

import pygame, sys, math
from Estrella import Estrella
from Nave import Nave
from Enemigo import Enemigo
from Planeta import Planeta
from Pantalla import Pantalla
from Agujero import Agujero
from Laser import Laser
from Texto import Texto
import random
from pygame.locals import * 

"""
Constantes de configuracion
"""
AREA_MAXIMA = 20000
DIVIDIR_AREA = 5
AREA = AREA_MAXIMA/DIVIDIR_AREA
VELOCIDAD_MINIMA = 0.1
VELOCIDAD_MAXIMA = 20
VELOCIDAD_LASER = 10

OBJETOS_MAXIMOS = 600
DISTANCIA_MINIMA = 550
ESTRELLA_MAXIMO = 75
LASER_MAXIMO = 10

"""
Funciones
"""

def generarObjetos(OBJETOS_MAXIMOS, AREA_MAXIMA, DISTANCIA_MINIMA):
	listaObjetos = []
	for i in range(OBJETOS_MAXIMOS):
		opc = random.randint(0,10)
		if opc == 10:
			listaObjetos.append(Agujero("Recursos/AgujeroNegro.png", 2, listaObjetos, AREA_MAXIMA, DISTANCIA_MINIMA))
		elif opc <= 5:
			listaObjetos.append(Planeta("Recursos/Planeta2.png", listaObjetos, AREA_MAXIMA, DISTANCIA_MINIMA))	
		else:
			listaObjetos.append(Planeta("Recursos/Planeta.png", listaObjetos, AREA_MAXIMA, DISTANCIA_MINIMA))		
	return listaObjetos
	
def generarLaser(LASER_MAXIMO):
	listaLaser = []
	for i in range(LASER_MAXIMO):			
		listaLaser.append(Laser("Recursos/laser2.png", pantalla, 0, 0, True))
	return listaLaser

def generarSectores(DIVIDIR_AREA):
	return [[] for i in range(math.trunc(math.pow(DIVIDIR_AREA, 2)))]
		
def agregarObjetoASector(listaSector, objeto, X, Y, AREA, DIVIDIR_AREA):
	listaSector[getIndiceSector(X, Y, AREA, DIVIDIR_AREA)].append(objeto)

def getIndiceSector(X, Y, AREA, DIVIDIR_AREA):
	return math.trunc(((X//AREA)*DIVIDIR_AREA ) + (Y//AREA))
	
"""
Inicializacion de variables
"""
pygame.init()
		
pantalla = Pantalla(0,0)

nave = Nave("Recursos/Chico.png", "Recursos/kaboom.png", 0, 0.1, VELOCIDAD_MINIMA, VELOCIDAD_MAXIMA, (0,0))

enemigo = Enemigo("Recursos/Enemigo.png", 550, 550, 1)

lobjetos = generarObjetos(OBJETOS_MAXIMOS, AREA_MAXIMA, DISTANCIA_MINIMA)

lsector = generarSectores(DIVIDIR_AREA)

for i in lobjetos:
	agregarObjetoASector(lsector, i, i.getCentroX(), i.getCentroY(), AREA, DIVIDIR_AREA)	
	
lestrella = []
for i in range(ESTRELLA_MAXIMO):
	lestrella.append(Estrella())
	
llaser = generarLaser(LASER_MAXIMO)	

intro = True

recargaLaser = 200

pasolaser = 12

clock = pygame.time.Clock()
clockLaser = pygame.time.Clock()
		
"""
Texto 
"""
fsize = 12
fuente = pygame.font.Font("Recursos/arial.ttf", fsize)
text21 = Texto("Recursos/arial.ttf",12)
text21.setTexto("PUTOOO")
text22 = Texto("Recursos/arial.ttf",12)
text22.setTexto("PE:")
text23 = Texto("Recursos/arial.ttf",12)
text23.setTexto("PN:")


"""
Bucle Principal 
"""
while intro:

	pantalla.display.fill((29,21,13))
	
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == K_ESCAPE:
				intro = False
			
			if event.key == K_m:
				fsize += 1
				fuente = pygame.font.Font("Recursos/arial.ttf", fsize)
				pasolaser += 1
			if event.key == K_n:
				fsize -= 1
				fuente = pygame.font.Font("Recursos/arial.ttf", fsize)
				pasolaser -= 1
			"""
			if event.key == K_k:
				for i in llaser:
					if i.laserLibre == True:
						i.setLaser(pantalla, VELOCIDAD_LASER, nave.angulo, False)
						break
			"""
						
		if event.type == pygame.QUIT:
			intro = False
	
	#Lectura de TECLAS
	keys = pygame.key.get_pressed()
	if keys[K_a]:
		nave.sumarAngulo(2)
		
	if keys[K_d]:
		nave.sumarAngulo(-2)
		
	if keys[K_w]:
		nave.sumarVelocidad(0.02)

	if keys[K_s]:
		nave.sumarVelocidad(-0.1)
	
	if keys[K_k]:
		if recargaLaser >= pasolaser:
			recargaLaser = 0
			for i in llaser:
				if i.laserLibre == True:
					i.setLaser(pantalla, VELOCIDAD_LASER, nave.angulo, False)
					break
		else:
			recargaLaser += 1
		
	#Impresion
	pantalla.mover(nave.X, nave.Y)
	
	for i in lestrella:
		i.imprimir(pantalla)
	
	# No se en que clase ponerlos, sirven para saber en que sector esta la nave
	supIZQ = getIndiceSector(pantalla.X-800,pantalla.Y-600, AREA, DIVIDIR_AREA)
	supDER = getIndiceSector(pantalla.X+800,pantalla.Y-600, AREA, DIVIDIR_AREA)
	infIZQ = getIndiceSector(pantalla.X-800,pantalla.Y+600, AREA, DIVIDIR_AREA)
	infDER = getIndiceSector(pantalla.X+800,pantalla.Y+600, AREA, DIVIDIR_AREA)
	
	# Si a alguien se le ocurre una mejor manera de comprobar que sector imprimir bienvenido sea
	for i in lsector[supIZQ]:
		i.imprimir(pantalla, nave)
	if supIZQ != supDER:
		for i in lsector[supDER]:
			i.imprimir(pantalla, nave)
	if supIZQ != infIZQ:
		for i in lsector[infIZQ]:
			i.imprimir(pantalla, nave)
		if infIZQ != infDER:
			for i in lsector[infDER]:
				i.imprimir(pantalla, nave)
				
	#pygame.display.set_caption("Coord X:" + str(pantalla.X))
	pygame.draw.line(pantalla.display,pygame.Color(255,255,255,255),[0-pantalla.X,0-pantalla.Y],[AREA_MAXIMA-pantalla.X,0-pantalla.Y],5)
	pygame.draw.line(pantalla.display,pygame.Color(255,255,255,255),[0-pantalla.X,0-pantalla.Y],[0-pantalla.X,AREA_MAXIMA-pantalla.Y],5)
	pygame.draw.line(pantalla.display,pygame.Color(255,255,255,255),[AREA_MAXIMA-pantalla.X,0-pantalla.Y],[AREA_MAXIMA-pantalla.X,AREA_MAXIMA-pantalla.Y],5)
	pygame.draw.line(pantalla.display,pygame.Color(255,255,255,255),[0-pantalla.X,AREA_MAXIMA-pantalla.Y],[AREA_MAXIMA-pantalla.X,AREA_MAXIMA-pantalla.Y],5)
	
	for i in llaser:
		if i.laserLibre == False:
			i.imprimir(nave.X, nave.Y, pantalla)
	nave.imprimir(pantalla)
	enemigo.imprimir(nave, pantalla)
	
	pantalla.imprimir()
	
	texto1 = fuente.render("X: " + str(int(pantalla.X+pantalla.getCentroX())), True, (0, 0, 255))
	texto2 = fuente.render("Y: " + str(int(pantalla.Y+pantalla.getCentroY())), True, (0, 0, 255))
	texto3 = fuente.render("Tamaño: " + str(fsize), True, (0, 0, 255))
	texto4 = fuente.render("FPS: " + str(clock.get_fps()), True, (0, 0, 255))
	texto5 = fuente.render("Velocidad: " + str(nave.velocidad), True, (0, 0, 255))
	#lock 125
	pantalla.display.blit(texto1, (665,45))
	pantalla.display.blit(texto2, (665,60))
	pantalla.display.blit(texto3, (665,75))
	pantalla.display.blit(texto4, (665,90))
	pantalla.display.blit(texto5, (665,105))
	text21.setTexto("C Laser: ", )
	text21.imprimir(pantalla,665,130)
	text22.setTexto("Nave: " + str(nave.getPos()), )
	text22.imprimir(pantalla,665,145)
	text23.setTexto("Enemigo: " + str(enemigo.getPos()), )
	text23.imprimir(pantalla,665,160)
	
	pygame.display.update()

	clock.tick(60)
"""
Prueba merge 1... Finalizado el test
"""
"""
Finalizacion
"""

pygame.quit()
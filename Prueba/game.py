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
import Funciones
from Explosion import Explosion

from Estrella import Estrella
from Nave import Nave
from Enemigo import Enemigo
from Pantalla import Pantalla
from Mapa import Mapa
from Laser import Laser
from Texto import Texto
from Planeta import Planeta


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

VELOCIDAD_MINIMA = 0.2
VELOCIDAD_MAXIMA = 15
VELOCIDAD_LASER = 10

OBJETOS_MAXIMOS = 200
DISTANCIA_MINIMA = 550
ESTRELLA_MAXIMO = 75
LASER_MAXIMO = 10

BLANCO = (255,255,255)

"""
Funciones
"""
	
def generarLaser(LASER_MAXIMO):
	listaLaser = []
	for i in range(LASER_MAXIMO):			
		listaLaser.append(Laser("Recursos/laser.png", nave, 0, 0, True))
	return listaLaser
	
"""
Inicializacion de variables
"""

pygame.init()

pantalla = Pantalla()

mapa = Mapa(20000, 5, OBJETOS_MAXIMOS, DISTANCIA_MINIMA)

lobjtmp = mapa.getListaObjetos()

nave = Nave("Recursos/Nave", "Recursos/kaboom.png", 0, 0.1, VELOCIDAD_MINIMA, VELOCIDAD_MAXIMA, (0,0), pantalla)

enemigo = Enemigo("Recursos/Enemigo.png", "Recursos/kaboom.png", 550, 550, 1)	

#explosion = Explosion("Recursos/Explosion1.png")

lestrella = []
for i in range(ESTRELLA_MAXIMO):
	lestrella.append(Estrella())
	
llaser = generarLaser(LASER_MAXIMO)	

intro = True

recargaLaser = 200

pasolaser = 6

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

timepoLuegoDeExplosion = 0
tiempoDeSpawneo = 0
imprimirNave = True
laserEnemigo = Laser("Recursos/laserEnemigo.png",enemigo,VELOCIDAD_LASER+enemigo.velocidad,nave.angulo,False)
"""
Bucle Principal 
"""
while intro:
	if(nave.fueDestruidoPorCompleto()):
		timepoLuegoDeExplosion += 1
		imprimirNave = False
		if(timepoLuegoDeExplosion >=60):
			nave = Nave("Recursos/Nave", "Recursos/kaboom.png", 0, 0.1, VELOCIDAD_MINIMA, VELOCIDAD_MAXIMA, (0,0), pantalla)
			enemigo = Enemigo("Recursos/Enemigo.png", "Recursos/kaboom.png", 550, 550, 1)
			laserEnemigo = Laser("Recursos/laserEnemigo.png",enemigo,VELOCIDAD_LASER+enemigo.velocidad,nave.angulo,False)
			timepoLuegoDeExplosion = 0
			tiempoDeSpawneo += 1
			imprimirNave = True
	if(tiempoDeSpawneo>=1):
		tiempoDeSpawneo += 1
		if(tiempoDeSpawneo>=120):
			tiempoDeSpawneo = 0
			imprimirNave = True
	
	if enemigo.destruidoPorCompleto:
		enemigo = Enemigo("Recursos/Enemigo.png", "Recursos/kaboom.png", 550, 550, 1)
		laserEnemigo = Laser("Recursos/laserEnemigo.png",enemigo,VELOCIDAD_LASER+enemigo.velocidad,nave.angulo,False)
		enemigo.destruidoPorCompleto = False


	pantalla.display.fill((29,21,13))
	
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == K_ESCAPE:
				intro = False
			
			if event.key == K_m:
				print("Imprimimos, la lista de obketos")
				cplan = 0
				for i in lobjtmp:
					if(isinstance(i, Planeta)):
						cplan += 1
						print("soy un planetin")
				print("Conte " + str(cplan) + "planetas entre " + str(len(lobjtmp)))
			if event.key == K_n:
				fsize -= 1
				fuente = pygame.font.Font("Recursos/arial.ttf", fsize)
				pasolaser -= 1
						
		if event.type == pygame.QUIT:
			intro = False
	
	#Lectura de TECLAS
	keys = pygame.key.get_pressed()
	if(nave.colision == False):
		if keys[K_a]:
			nave.sumarAngulo(3)
			
		if keys[K_d]:
			nave.sumarAngulo(-3)
			
		if keys[K_w]:
			nave.sumarVelocidad(0.06)
	
		if keys[K_s]:
			nave.sumarVelocidad(-0.2)
		
		if keys[K_k]:
			if recargaLaser >= pasolaser:
				recargaLaser = 0
				for i in llaser:
					if i.laserLibre == True:
						
						i.setLaser(nave, VELOCIDAD_LASER, nave.angulo, False)
						break
			else:
				recargaLaser += 1
		
	#Movimiento
	nave.mover(mapa)
	
	#Impresion
	for i in lestrella:
		i.imprimir(pantalla, nave)
	
	# Si a alguien se le ocurre una mejor manera de comprobar que sector imprimir bienvenido sea
	if nave.supIZQ <= 25:
		for i in mapa.listaSector[nave.supIZQ]:
			i.imprimir(pantalla, nave, llaser)
	if nave.supDER != nave.supIZQ and nave.supDER <= 25:
		for i in mapa.listaSector[nave.supDER]:
			i.imprimir(pantalla, nave, llaser)
	if nave.infIZQ != nave.supIZQ and nave.infIZQ <= 25:
		for i in mapa.listaSector[nave.infIZQ]:
			i.imprimir(pantalla, nave, llaser)
	if (nave.infDER != nave.infIZQ and nave.infDER != nave.supDER) and nave.infDER <= 25:
		for i in mapa.listaSector[nave.infDER]:
			i.imprimir(pantalla, nave, llaser)
			
	
	pygame.draw.line(pantalla.display,BLANCO,[0-nave.AX,0-nave.AY],[mapa.areaMaxima-nave.AX,0-nave.AY],5)
	pygame.draw.line(pantalla.display,BLANCO,[0-nave.AX,0-nave.AY],[0-nave.AX,mapa.areaMaxima-nave.AY],5)
	pygame.draw.line(pantalla.display,BLANCO,[mapa.areaMaxima-nave.AX,0-nave.AY],[mapa.areaMaxima-nave.AX,mapa.areaMaxima-nave.AY],5)
	pygame.draw.line(pantalla.display,BLANCO,[0-nave.AX,mapa.areaMaxima-nave.AY],[mapa.areaMaxima-nave.AX,mapa.areaMaxima-nave.AY],5)
	
	for i in llaser:
		if i.laserLibre == False:
			i.imprimir(nave, pantalla)
			if(Funciones.hayColision(enemigo, i) == True):
				enemigo.setVida (enemigo.getVida() - 10 )
				i.laserLibre = True
	"""
	Logica movimientos y colisiones

	"""
	
	
	

	#
	#
	### ENEMIGO COLISIONA CON ALGUN PLANETA?
	#
	#
	contadorObjetos = 0
	colision = False
	while(not colision and contadorObjetos < len(lobjtmp)):
		if(type(lobjtmp[contadorObjetos]) is Planeta):
			#colision = pygame.sprite.collide_rect(lobjtmp[contadorObjetos], enemigo)
			colision = Funciones.hayColision(lobjtmp[contadorObjetos], enemigo)
		if(not colision): 
			contadorObjetos += 1
	#
	# SI NO COLISIONA SE MUEVE HACIA LA NAVE, Y SI COLISIONA, ESQUIVA EL PLANETA
	#
	if(not colision):
		print("No hay colision de enemigo.")
		#Aca iria el enemigo.mover(nave) pero se buguea.
	else:
		print("ENEMIGO COLISIONÓ contra lobjtmp[" + str(int(contadorObjetos))+"] de tipo"+ str(type(lobjtmp[contadorObjetos])))
		#enemigo.evitarColision(nave, lobjtmp[contadorObjetos])
	
	
	enemigo.mover(nave)
	if laserEnemigo.laserLibre == False:
		laserEnemigo.imprimir(nave, pantalla)
	else:
		laserEnemigo.setLaser(enemigo, VELOCIDAD_LASER+enemigo.velocidad, laserEnemigo.traerAnguloLaserEnemigo(enemigo,pantalla), False)
	enemigo.imprimir(nave, pantalla, llaser)
	
	
	#nave.imprimir(pantalla)
	#explosion.imprimir(pantalla)
	pantalla.display.blit(pantalla.fondo1, (650,0))
	pantalla.display.blit(pantalla.fondo2, (0,475))
	if(timepoLuegoDeExplosion == 0):
		if((tiempoDeSpawneo//10)%2 !=0):
			imprimirNave = False
		else: 
			imprimirNave = True
	if(imprimirNave):
			nave.imprimir(pantalla, laserEnemigo)
	
	texto1 = fuente.render("X: " + str(int(nave.getACentroX())), True, (0, 0, 255))
	texto2 = fuente.render("Y: " + str(int(nave.getACentroY())), True, (0, 0, 255))
	texto3 = fuente.render("Puntos: " + str(enemigo.getPuntos()), True, (0, 0, 255))
	texto4 = fuente.render("FPS: " + str(clock.get_fps()), True, (0, 0, 255))
	texto5 = fuente.render("Velocidad: " + str(int(nave.velocidad)), True, (0, 0, 255))

	#lock 125
	pantalla.display.blit(texto1, (665,45))
	pantalla.display.blit(texto2, (665,60))
	pantalla.display.blit(texto3, (665,75))
	pantalla.display.blit(texto4, (665,90))
	pantalla.display.blit(texto5, (665,105))
	text21.setTexto("Recarga Laser: " + str(recargaLaser),)
	text21.imprimir(pantalla,665,130)
	text22.setTexto("Nave: " + str(nave.getAPos()), )
	text22.imprimir(pantalla,665,145)
	text23.setTexto("Laser[0]: " + str(llaser[0].getCoordenadas()) )
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
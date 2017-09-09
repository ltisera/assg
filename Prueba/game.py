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
from Pantalla import Pantalla
from Mapa import Mapa
from Laser import Laser
from Texto import Texto
from pygame.locals import * 

"""
Constantes de configuracion
"""

VELOCIDAD_MINIMA = 0.1
VELOCIDAD_MAXIMA = 20
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

nave = Nave("Recursos/Chico.png", "Recursos/kaboom.png", 0, 0.1, VELOCIDAD_MINIMA, VELOCIDAD_MAXIMA, (0,0), pantalla)

enemigo = Enemigo("Recursos/Enemigo.png", 550, 550, 1)	
	
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
					i.setLaser(VELOCIDAD_LASER, nave, False)
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
			i.imprimir(pantalla, nave)
	if nave.supDER != nave.supIZQ and nave.supDER <= 25:
		for i in mapa.listaSector[nave.supDER]:
			i.imprimir(pantalla, nave)
	if nave.infIZQ != nave.supIZQ and nave.infIZQ <= 25:
		for i in mapa.listaSector[nave.infIZQ]:
			i.imprimir(pantalla, nave)
	if (nave.infDER != nave.infIZQ and nave.infDER != nave.supDER) and nave.infDER <= 25:
		for i in mapa.listaSector[nave.infDER]:
			i.imprimir(pantalla, nave)
			
	
	pygame.draw.line(pantalla.display,BLANCO,[0-nave.AX,0-nave.AY],[mapa.areaMaxima-nave.AX,0-nave.AY],5)
	pygame.draw.line(pantalla.display,BLANCO,[0-nave.AX,0-nave.AY],[0-nave.AX,mapa.areaMaxima-nave.AY],5)
	pygame.draw.line(pantalla.display,BLANCO,[mapa.areaMaxima-nave.AX,0-nave.AY],[mapa.areaMaxima-nave.AX,mapa.areaMaxima-nave.AY],5)
	pygame.draw.line(pantalla.display,BLANCO,[0-nave.AX,mapa.areaMaxima-nave.AY],[mapa.areaMaxima-nave.AX,mapa.areaMaxima-nave.AY],5)
	
	for i in llaser:
		if i.laserLibre == False:
			i.imprimir(nave, pantalla)
			
	nave.imprimir(pantalla)
	enemigo.imprimir(nave, pantalla)
	
	pantalla.display.blit(pantalla.fondo1, (650,0))
	pantalla.display.blit(pantalla.fondo2, (0,475))

	
	texto1 = fuente.render("X: " + str(int(nave.getACentroX())), True, (0, 0, 255))
	texto2 = fuente.render("Y: " + str(int(nave.getACentroY())), True, (0, 0, 255))
	texto3 = fuente.render("Tamaño: " + str(fsize), True, (0, 0, 255))
	texto4 = fuente.render("FPS: " + str(clock.get_fps()), True, (0, 0, 255))
	texto5 = fuente.render("Velocidad: " + str(nave.velocidad), True, (0, 0, 255))
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
	text23.setTexto("Enemigo: " + str(enemigo.getAPos()), )
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
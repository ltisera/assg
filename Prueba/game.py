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

import pygame, sys, math, random, time
import Funciones, Menu
from Explosion import Explosion

from Estrella import Estrella
from Nave import Nave
from Enemigo import Enemigo
from Pantalla import Pantalla
from Mapa import Mapa
from Laser import Laser
from Texto import Texto
from Barra import Barra
from Planeta import Planeta

from pygame.locals import * 

"""
Constantes de configuracion
"""

VELOCIDAD_MINIMA = 0.1
VELOCIDAD_MAXIMA = 200
VELOCIDAD_LASER = 10

VIDAS = 3

OBJETOS_MAXIMOS = 200
DISTANCIA_MINIMA = 550
ESTRELLA_MAXIMO = 75
LASER_MAXIMO = 10

BLANCO = (255,255,255)
COLOR_TEXTO = (0,255,0)

PASO_LASER = 100
DAÑO_LASER = 10

VELOCIDAD_ENEMIGO = 1
DAÑO_ENEMIGO = 10
VIDA_ENEMIGO = 100 
PUNTOS_ENEMIGO = 100
VELOCIDAD_LASER_ENEMIGO = VELOCIDAD_LASER-7
MAXIMO_ENEMIGOS_ACTIVOS = 15

"""
Funciones
"""
	
def generarLaser(LASER_MAXIMO, DAÑO_LASER, nave):
	listaLaser = []
	for i in range(LASER_MAXIMO):			
		listaLaser.append(Laser("Recursos/laser.png", nave, 0, 0, True, DAÑO_LASER, VELOCIDAD_LASER))
	return listaLaser
	
"""
Juego
"""

pygame.init()

pantalla = Pantalla()

fsize = 12
fuente = pygame.font.Font("Recursos/arial.ttf", fsize)

intro, reset = Menu.main(pantalla)

"""
Bucle Principal 
"""
while intro:

	"""
	Inicializacion de variables
	"""
	if reset:
		mapa = Mapa(20000, 5, OBJETOS_MAXIMOS, DISTANCIA_MINIMA)

		lobjtmp = mapa.getListaObjetos()

		nave = Nave("Recursos/Nave", 0, 0.1, VELOCIDAD_MINIMA, VELOCIDAD_MAXIMA, (0,0), pantalla, 8, 161, (183, 509), (183, 535), (383, 509), VIDAS)

		boss = Enemigo("Recursos/boss.png", "Recursos/laser2.png", random.randint(int(nave.getACentroX()-300), int(nave.getACentroX()+300)), random.randint(int(nave.getACentroY()-400), int(nave.getACentroY()+400)), VELOCIDAD_ENEMIGO, DAÑO_ENEMIGO, 1000, PUNTOS_ENEMIGO)

		lenemigo = []

		dificultad = 0

		lestrella = []
		for i in range(ESTRELLA_MAXIMO):
			lestrella.append(Estrella())
			
		llaser = generarLaser(LASER_MAXIMO, DAÑO_LASER, nave)	

		intro = True
		cheats = False
		peleaBoss = False

		recargaLaser = Barra(((255,0,0),(255,0,0)), 0, PASO_LASER, PASO_LASER, 8, 161, 383, 535) 

		pasolaser = 0

		clock = pygame.time.Clock()
		clockLaser = pygame.time.Clock()
		cadencia = time.clock()
		timeEnemigo = time.clock() #Timer de generacion de enemigo

		reset = False

	pantalla.display.fill((29,21,13))
	
	for event in pygame.event.get():

		if event.type == pygame.KEYDOWN:

			if event.key == K_ESCAPE:
				Menu.pausa(pantalla)

			if cheats == True:
			
				if event.key == K_m:
					print("Imprimimos, la lista de objetos")
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

				if event.key == K_o:
					for i in lenemigo:
						i.destruirEnemigo()
						
		if event.type == pygame.QUIT:
			intro = False
	
	#Lectura de TECLAS
	keys = pygame.key.get_pressed()

	if keys[K_LCTRL] and keys[K_LSHIFT] and keys[K_c]:
		if cheats == False:
			cheats = True
			print("Cheats Mode ON")

	if keys[K_LCTRL] and keys[K_LSHIFT] and keys[K_x]:
		if cheats == True:
			cheats = False
			print("Cheats Mode Off")

	if keys[K_a]:
		nave.sumarAngulo(4)
		
	if keys[K_d]:
		nave.sumarAngulo(-4)
		
	if keys[K_w]:
		nave.sumarVelocidad(0.07)

	if keys[K_s]:
		nave.sumarVelocidad(-0.1)
	
	if keys[K_k]:
		if pasolaser > 0:
			recargaLaser.setValor(0)
			for i in llaser:
				if i.getLibre() == True:
					i.setLaser(VELOCIDAD_LASER, nave.getAngulo(), nave, False)
					break
		
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
		if i.getLibre() == False:
			i.imprimir(pantalla, nave)
			for e in lenemigo:
				if(Funciones.hayColision(e, i) == True):
					e.reduceVida(i.getDaño())
					i.setLibre(True)
			if(Funciones.hayColision(boss, i) == True):
				boss.reduceVida(i.getDaño())
				i.setLibre(True)
	"""
	Logica movimientos y colisiones

	"""
	pasolaser = recargaLaser.sumarValor(10) 
	
	for i in lenemigo:	
		i.imprimir(pantalla, nave, VELOCIDAD_LASER_ENEMIGO, lenemigo)
		if(i.fueDestruidoPorCompleto()):
			dificultad += 1
			lenemigo.remove(i) #Destruye al enemigo muerto

	if nave.gameOver():
		#intro = False
		#if Menu.gameOver(pantalla) == true: #Si no continua vuelve a la pantalla original
		Menu.gameOver(pantalla, nave.getPuntos())
		intro, reset = Menu.main(pantalla)
	else:
		nave.imprimir(pantalla)
	#explosion.imprimir(pantalla)
	pantalla.display.blit(pantalla.fondo1, (625,0))
	pantalla.display.blit(pantalla.fondo2, (0,475))
	nave.imprimirBarras(pantalla)
	recargaLaser.imprimir(pantalla)
	pantalla.display.blit(pantalla.fondo3, (0,475))

	texto1 = fuente.render("X: " + str(int(nave.getACentroX())), True, COLOR_TEXTO)
	texto2 = fuente.render("Y: " + str(int(nave.getACentroY())), True, COLOR_TEXTO)
	texto3 = fuente.render("Tamaño: " + str(fsize), True ,COLOR_TEXTO)
	texto4 = fuente.render("FPS: " + str(int(clock.get_fps())), True, COLOR_TEXTO)
	texto5 = fuente.render("Velocidad: " + str(nave.velocidad), True, COLOR_TEXTO)
	texto6 = fuente.render("Nave: " + str(nave.getAPos()), True, COLOR_TEXTO)
	texto7 = fuente.render("Laser[0]: " + str(llaser[0].getCoordenadas()), True, COLOR_TEXTO)
	texto8 = fuente.render("PUNTOS: " + str(nave.getPuntos()), True, COLOR_TEXTO)

	pantalla.display.blit(texto1, (645,45))
	pantalla.display.blit(texto2, (645,60))
	pantalla.display.blit(texto3, (645,75))
	pantalla.display.blit(texto4, (645,90))
	pantalla.display.blit(texto5, (645,105))
	pantalla.display.blit(texto6, (645,130))
	pantalla.display.blit(texto7, (645,145))
	pantalla.display.blit(texto8, (645,500))

	#Clock de generacion de enemigos y boss
	
	if (dificultad >= 20):
		if(peleaBoss == False):
			for i in lenemigo:
				i.destruirEnemigo()
			boss.reset(random.randint(int(nave.getACentroX()-300), int(nave.getACentroX()+300)), random.randint(int(nave.getACentroY()-400), int(nave.getACentroY()+400)), VELOCIDAD_ENEMIGO, DAÑO_ENEMIGO, 1000, PUNTOS_ENEMIGO)
			peleaBoss = True
		else:
			if(boss.fueDestruidoPorCompleto()):
				Menu.ganaste(pantalla, nave.getPuntos())
				intro, reset = Menu.main(pantalla)
			else:
				boss.imprimir(pantalla, nave, VELOCIDAD_LASER_ENEMIGO, lenemigo)	
	else:
		if (time.clock()-timeEnemigo >= 1):
			if(len(lenemigo) <= dificultad and len(lenemigo) <= MAXIMO_ENEMIGOS_ACTIVOS):
				timeEnemigo = time.clock()
				lenemigo.append(Enemigo("Recursos/Enemigo.png", "Recursos/laser2.png", random.randint(int(nave.getACentroX()-300), int(nave.getACentroX()+300)), random.randint(int(nave.getACentroY()-400), int(nave.getACentroY()+400)), VELOCIDAD_ENEMIGO, DAÑO_ENEMIGO, VIDA_ENEMIGO, PUNTOS_ENEMIGO))

	if (time.clock()-cadencia >= 1.1):
		cadencia = time.clock()
		for i in lenemigo:
			i.setDisparar()
	
	pygame.display.update()
	clock.tick(60)


pygame.quit()
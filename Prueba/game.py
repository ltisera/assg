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

import random
from pygame.locals import * 



"""
Constantes de configuracion
"""

VELOCIDAD_MINIMA = 0.1
VELOCIDAD_MAXIMA = 20

PLANETA_MAXIMO = 30
ESTRELLA_MAXIMO = 2000

"""
Funciones
"""
def generarPlanetas():
	listaPlaneta = []
	for i in range(PLANETA_MAXIMO):
		listaPlaneta.append(Planeta("Recursos/Planeta.png", listaPlaneta))
		listaPlaneta.append(Planeta("Recursos/Planeta2.png", listaPlaneta))
	return 0

	
def rot_center(image, angle):
	orig_rect = image.get_rect()
	rot_image = pygame.transform.rotate(image, angle)
	rot_rect = orig_rect.copy()
	rot_rect.center = rot_image.get_rect().center
	rot_image = rot_image.subsurface(rot_rect).copy()
	return rot_image

class Pantalla:
	def imprimir(self):
		pantalla.display.blit(self.fondo1, (650,0))
		pantalla.display.blit(self.fondo2, (0,475))
	def mover(self, X, Y):
		self.X += X
		self.Y += Y
	def __init__(self):
		self.display = pygame.display.set_mode((800,600))
		pygame.display.set_caption("ASSG")
		self.X = 0
		self.Y = 0
		self.fondo1 = pygame.image.load("Recursos/1.png").convert_alpha()
		self.fondo2 = pygame.image.load("Recursos/2.png").convert_alpha()
		self.centroX = 325
		self.centroY = 237.5

class Agujero:
	def sumarAngulo(self, sumarAngulo):
		self.angulo += sumarAngulo
		if self.angulo >= 360:
			self.angulo -= 360
	def imprimir(self, X, Y):
		pantalla.display.blit(rot_center(self.imagen, self.angulo), (-X+self.origenX,Y-self.origenY))
		self.sumarAngulo(self.velocidad)
	def __init__(self, directorio, origenX, origenY, velocidad):
		self.imagen = pygame.image.load(directorio).convert_alpha()
		self.origenX = origenX
		self.origenY = origenY
		self.angulo = 0
		self.velocidad = velocidad

"""
Inicializacion de variables
"""
pygame.init()
		
pantalla = Pantalla()

nave = Nave("Recursos/Chico.png", 270, 0.1, VELOCIDAD_MINIMA, VELOCIDAD_MAXIMA)

enemigo = Enemigo("Recursos/Enemigo.png", 200, 100, 1)

lplaneta = []
for i in range(PLANETA_MAXIMO):
	if random.choice([1,2]) == 1:
		lplaneta.append(Planeta("Recursos/Planeta.png", lplaneta))
	else:
		lplaneta.append(Planeta("Recursos/Planeta2.png", lplaneta))

	
#Imprimo la lista de planetas para ver los centros
print("Lista creada con: ", len(lplaneta))
n = 1
for i in lplaneta:
	print("planeta: " , n , " Centro en: ", i.getCentro())
	
	n += 1

agujero = Agujero("Recursos/AgujeroNegro.png", -400, -600, 2)

lestrella = []
for i in range(ESTRELLA_MAXIMO):
	lestrella.append(Estrella())
	
intro = True

clock = pygame.time.Clock()
		
"""
Texto 
"""
fsize = 12
fuente = pygame.font.Font("Recursos/arial.ttf", fsize)

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
			if event.key == K_n:
				fsize -= 1
				fuente = pygame.font.Font("Recursos/arial.ttf", fsize)

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
	#Impresion
	pantalla.mover(nave.X, nave.Y)
	
	for i in lestrella:
		i.imprimir(pantalla)
	
	for i in lplaneta:
		i.imprimir(pantalla)
	
	#pygame.display.set_caption("Coord X:" + str(pantalla.X))
	pygame.draw.line(pantalla.display,pygame.Color(255,255,255,255),[0-pantalla.X,0+pantalla.Y],[60000-pantalla.X,0+pantalla.Y],5)
	pygame.draw.line(pantalla.display,pygame.Color(255,255,255,255),[0-pantalla.X,0+pantalla.Y],[0-pantalla.X,60000+pantalla.Y],5)
	pygame.draw.line(pantalla.display,pygame.Color(255,255,255,255),[60000-pantalla.X,0+pantalla.Y],[60000-pantalla.X,60000+pantalla.Y],5)
	pygame.draw.line(pantalla.display,pygame.Color(255,255,255,255),[0-pantalla.X,60000+pantalla.Y],[60000-pantalla.X,60000+pantalla.Y],5)
	agujero.imprimir(pantalla.X, pantalla.Y)
	nave.imprimir(pantalla.centroX, pantalla.centroY, pantalla)
	enemigo.imprimir(nave.X, nave.Y, pantalla)
	pantalla.imprimir()
	
	
	texto1 = fuente.render("X: " + str(int(pantalla.X)), True, (0, 0, 255))
	texto2 = fuente.render("Y: " + str(int(pantalla.Y)), True, (0, 0, 255))
	texto3 = fuente.render("Tamaño: " + str(fsize), True, (0, 0, 255))
	texto4 = fuente.render("FPS: " + str(clock.get_fps()), True, (0, 0, 255))
	texto5 = fuente.render("Velocidad: " + str(nave.velocidad), True, (0, 0, 255))
	#lock 125
	pantalla.display.blit(texto1, (665,45))
	pantalla.display.blit(texto2, (665,60))
	pantalla.display.blit(texto3, (665,75))
	pantalla.display.blit(texto4, (665,90))
	pantalla.display.blit(texto5, (665,105))
	
	pygame.display.update()
	
	
	clock.tick(120)
"""
Prueba merge 1
"""
"""
Finalizacion
"""

pygame.quit()
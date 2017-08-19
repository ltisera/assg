import pygame, sys, math
from pygame.locals import *    # Nuevo en la version 0.03
pygame.init()

pantalla = pygame.display.set_mode((800,600))
pygame.display.set_caption("ASSG")

nave = pygame.image.load("Recursos/Chico.png")
nave = pygame.transform.rotate(nave, 270)

planeta1 = pygame.image.load("Recursos/Planeta.png")
planeta12 = pygame.image.load("Recursos/Planeta2.png")


fondo1 = pygame.image.load("Recursos/1.png")
fondo2 = pygame.image.load("Recursos/2.png")
moverX = 0
moverY = 0
X = 0
Y = 0
intro = True
aceleracion = 1
velocidad = 0.1
angulo = 0
clock = pygame.time.Clock()
tiempo = 0


moverY = math.sin(math.radians(angulo))*velocidad
moverX = math.cos(math.radians(angulo))*velocidad
		
while intro:

	pantalla.fill((255,255,255))
	
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()
		if event.type == pygame.QUIT:
			pygame.quit()
	
	#Lectura de TECLAS
	keys = pygame.key.get_pressed()
	if keys[K_w]:
		angulo +=2 
		if angulo >= 360:
			angulo -= 360
		elif angulo < 0:
			angulo += 360	
		moverY = math.sin(math.radians(angulo))*velocidad
		moverX = math.cos(math.radians(angulo))*velocidad
		
	if keys[K_s]:
		angulo -=2
		if angulo >= 360:
			angulo -= 360
		elif angulo < 0:
			angulo += 360	
		moverY = math.sin(math.radians(angulo))*velocidad
		moverX = math.cos(math.radians(angulo))*velocidad
	
	if keys[K_m]:
		if velocidad >= 20:
			velocidad = 20
		else:
			velocidad += 0.1
		moverY = math.sin(math.radians(angulo))*velocidad
		moverX = math.cos(math.radians(angulo))*velocidad
	if keys[K_n]:
		if velocidad <= 0.6:
			velocidad = 0.1
		else:
			velocidad -= 0.5
		if velocidad <= 0:
			velocidad = 0.1
		
		moverY = math.sin(math.radians(angulo))*velocidad
		moverX = math.cos(math.radians(angulo))*velocidad

	X += moverX
	Y += moverY
	
	pantalla.blit(planeta1, (-X+10,Y+10))
	pantalla.blit(planeta12, (-X+300,Y+350))
	pantalla.blit(planeta12, (-X-500,Y+100))
	pantalla.blit(pygame.transform.rotate(nave, angulo), (225,300))
	pantalla.blit(fondo1, (700,0))
	pantalla.blit(fondo1, (650,0))
	pantalla.blit(fondo2, (0,475))
	pygame.display.update()
	clock.tick(30)
	#print(clock)
	tiempo += 1

import pygame, sys, math
from pygame.locals import *    # Intento de clases
pygame.init()

class Nave:
	def sumarAngulo(self, sumarAngulo):
		self.angulo += sumarAngulo
		if self.angulo >= 360:
			self.angulo -= 360
		elif self.angulo < 0:
			self.angulo += 360
		self.mover()
	def sumarVelocidad(self, sumar):
		self.velocidad = self.velocidad + sumar
		if self.velocidad <= (self.minVelocidad):
			self.velocidad = self.minVelocidad
		elif self.velocidad >= (self.maxVelocidad):
			self.velocidad = self.maxVelocidad
		self.mover()
	def mover(self):
		self.X = math.cos(math.radians(self.angulo))*self.velocidad
		self.Y = math.sin(math.radians(self.angulo))*self.velocidad
	def imprimir(self, centroX, centroY):
		pantalla.display.blit(pygame.transform.rotate(self.imagen, self.angulo), (centroX-38,centroY-27))
	def __init__(self, directorio, anguloOrigen, velocidad, minVelocidad, maxVelocidad):
		self.imagen = pygame.image.load(directorio)
		self.imagen = pygame.transform.rotate(self.imagen, anguloOrigen)
		self.X = 0
		self.Y = 0
		self.maxVelocidad = maxVelocidad
		self.minVelocidad = minVelocidad
		self.angulo = 0
		self.velocidad = 0
		self.sumarVelocidad(velocidad)

class Pantalla:
	def imprimir(self):
		#pantalla.display.blit(self.fondo1, (700,0))
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
		self.fondo1 = pygame.image.load("Recursos/1.png")
		self.fondo2 = pygame.image.load("Recursos/2.png")
		self.centroX = 325
		self.centroY = 237.5

class Enemigo:
	def mover(self, X, Y, centroX, centroY):
		self.X -= X
		self.Y += Y
		if self.X < centroX-50:
			self.X += self.velocidad
		elif self.X > centroX-50:
			self.X -= self.velocidad
		if self.Y < centroY-28:
			self.Y += self.velocidad
		elif self.Y > centroY-28:
			self.Y -= self.velocidad
	def imprimir(self, X, Y, centroX, centroY):
		self.mover(X, Y, centroX, centroY)
		pantalla.display.blit(self.imagen, (self.X,self.Y))
	def __init__(self, directorio, X, Y, velocidad):
		self.imagen = pygame.image.load(directorio)
		self.X = X
		self.Y = Y
		self.velocidad = velocidad

class Planeta:
	def imprimir(self, X, Y):
		pantalla.display.blit(self.imagen, (-X+self.origenX,Y+self.origenY))
	def __init__(self, directorio, origenX, origenY):
		self.imagen = pygame.image.load(directorio)
		self.origenX = origenX
		self.origenY = origenY

pantalla = Pantalla()		
		
nave = Nave("Recursos/Chico.png", 270, 0.1, 0.1, 20)

enemigo = Enemigo("Recursos/Enemigo.png", 200, 100, 2)

planeta1 = Planeta("Recursos/Planeta.png", 10,10)
planeta2 = Planeta("Recursos/Planeta2.png", 300,350)
planeta3 = Planeta("Recursos/Planeta2.png", -500,100)

intro = True

clock = pygame.time.Clock()
		
while intro:

	pantalla.display.fill((229,221,213))
	
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()
		if event.type == pygame.QUIT:
			pygame.quit()
	
	#Lectura de TECLAS
	keys = pygame.key.get_pressed()
	if keys[K_w]:
		nave.sumarAngulo(2)
		
	if keys[K_s]:
		nave.sumarAngulo(-2)
		
	if keys[K_m]:
		nave.sumarVelocidad(0.1)

	if keys[K_n]:
		nave.sumarVelocidad(-0.5)
	
	#Impresion
	pantalla.mover(nave.X, nave.Y)
	planeta1.imprimir(pantalla.X, pantalla.Y)
	planeta2.imprimir(pantalla.X, pantalla.Y)
	planeta3.imprimir(pantalla.X, pantalla.Y)
	nave.imprimir(pantalla.centroX, pantalla.centroY)
	enemigo.imprimir(nave.X, nave.Y, pantalla.centroX, pantalla.centroY)
	pantalla.imprimir()
	pygame.display.update()
	
	
	clock.tick(30)
	#print(clock)


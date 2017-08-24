import pygame, random
from Funciones import distancia
class Planeta:
	def getCentro(self):
		return self.centro
	def getCentroX(self):
		return self.centro[0]
	def getCentroY(self):
		return self.centro[1]
	def setX(self, x):
		self.origenX = x
	def setY(self, y):
		self.origenX = x
	def libre(self, lplaneta):
		libre = True
		for i in lplaneta:
			if (distancia(self.getCentroX(), i.getCentroX(), self.getCentroY(), i.getCentroY()) <= 600):
				libre = False
		return libre
	def imprimir(self, pantalla):
		#Esto estaria mal, deberiamos pasarle por argumento
		#La superficie en donde queremos que haga el blit
		#Tambien se puede ver si esta o no EN CAMARA
		#ahora como esta IMPRIME TODO por mas que no lo veamos
		if (-pantalla.X+self.getCentroX() >= -400 and -pantalla.X+self.getCentroX() <= 1400) and (-pantalla.Y+self.getCentroY() >= -400 and -pantalla.Y+self.getCentroY() <= 1400):
			pantalla.display.blit(self.imagen, (-pantalla.X+self.origenX,pantalla.Y-self.origenY))	
	def __init__(self, directorio, lplaneta):
		self.imagen = pygame.image.load(directorio).convert_alpha()
		asignado = False
		while not asignado:
			self.origenX = random.randint(-2000,2000)
			self.origenY = random.randint(-2000,2000)
			#defino el centro de la imagen
			self.centro = ((self.imagen.get_width()/2) + self.origenX, (self.imagen.get_height()/2) + self.origenY)
			asignado = self.libre(lplaneta)
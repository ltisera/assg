import pygame, random
from Funciones import rotarCentro, sumarAngulo, lugarLibre, colision
import Pantalla
from Texto import Texto

class Agujero:
	def getAX(self):
		return self.AX
		
	def getAY(self):
		return self.AY
		
	def getAPos(self):
		return(int(self.AX),int(self.AY))
	
	def getACentro(self):
		return self.ACentro
		
	def getACentroX(self):
		return self.ACentro[0]
		
	def getACentroY(self):
		return self.ACentro[1]
	
	def getRX(self):
		return self.RX
		
	def getRY(self):
		return self.RY
		
	def getRPos(self):
		return(int(self.RX),int(self.RY))

	def getRCentro(self):
		return self.RCentro
		
	def getRCentroX(self):
		return self.RCentro[0]
		
	def getRCentroY(self):
		return self.RCentro[1]
		
	def mover(self,nave):
		self.angulo = sumarAngulo(self.angulo, self.velocidad)
		self.RX = self.AX - nave.getAX()
		self.RY = self.AY - nave.getAY()
		self.RCentro = ((self.imagen.get_width()/2) + self.RX, (self.imagen.get_height()/2) + self.RY)
		
	def imprimir(self, pantalla, nave):
		self.mover(nave)
		if ((self.getRCentroX() >= -400 and self.getRCentroX() <= 1400) and (self.getRCentroY() >= -400 and self.getRCentroY() <= 1400)):
			pantalla.display.blit(rotarCentro(self.imagen, self.angulo), (self.RX,self.RY))
			colision(self, nave)
		
	def __init__(self, directorio, velocidad, lobjeto, AREA_MAXIMA, DISTANCIA_MINIMA):
		self.imagen = pygame.image.load(directorio).convert_alpha()
		self.velocidad = velocidad
		self.RX = 0
		self.RY = 0
		self.RCentro = 0
		self.angulo = 0
		asignado = False
		while not asignado:
			self.AX = random.randint(10,AREA_MAXIMA-self.imagen.get_width())
			self.AY = random.randint(10,AREA_MAXIMA-self.imagen.get_height())
			self.ACentro = ((self.imagen.get_width()/2) + self.AX, (self.imagen.get_height()/2) + self.AY)
			asignado = lugarLibre(self, lobjeto, DISTANCIA_MINIMA)
		
		
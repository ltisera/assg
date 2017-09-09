import pygame, random
import Funciones
<<<<<<< HEAD
from Pantalla import Pantalla
from Texto import Texto

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
		self.origenY = Y
			
	def imprimir(self,camara,nave):
		if ((self.getCentroX()-camara.getX() >= -400 and self.getCentroX()-camara.getX() <= 1400) and (self.getCentroY()-camara.getY() >= -400 and self.getCentroY()-camara.getY() <= 1400)):
			camara.display.blit(self.imagen, (self.origenX-camara.getX(),self.origenY-camara.getY()))
			Funciones.colision(self, camara,nave)		
			
=======
import Pantalla
from Texto import Texto

class Planeta:
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
		self.RX = self.AX - nave.getAX()
		self.RY = self.AY - nave.getAY()
		self.RCentro = ((self.imagen.get_width()/2) + self.RX, (self.imagen.get_height()/2) + self.RY)
		
	
	def imprimir(self, pantalla, nave):
		self.mover(nave)
		cp1 = self.getRCentro()
		if Funciones.posicionValida(self.getRCentroX(),-100,800,self.getRCentroY(),-100,800):
			pantalla.display.blit(self.imagen, (self.RX,self.RY))
			Funciones.colision(self, nave)	
		
		
>>>>>>> Test-coordenadas
	def __init__(self, directorio, lplaneta, AREA_MAXIMA, DISTANCIA_MINIMA):
		self.imagen = pygame.image.load(directorio).convert_alpha()
		self.RX = 0
		self.RY = 0
		self.RCentro = 0
		asignado = False
		while not asignado:
<<<<<<< HEAD
			self.origenX = random.randint(10,AREA_MAXIMA-self.imagen.get_width())
			self.origenY = random.randint(10,AREA_MAXIMA-self.imagen.get_width())
			self.centro = ((self.imagen.get_width()/2) + self.origenX, (self.imagen.get_height()/2) + self.origenY)
=======
			self.AX = random.randint(10,AREA_MAXIMA-self.imagen.get_width())
			self.AY = random.randint(10,AREA_MAXIMA-self.imagen.get_height())
			self.ACentro = ((self.imagen.get_width()/2) + self.AX, (self.imagen.get_height()/2) + self.AY)
>>>>>>> Test-coordenadas
			asignado = Funciones.lugarLibre(self, lplaneta, DISTANCIA_MINIMA)
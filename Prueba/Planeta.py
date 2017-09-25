import pygame, random
import Funciones
import Pantalla
import Laser

from Texto import Texto

class Planeta:
	def getWidth(self):
		return self.width

	def getHeight(self):
		return self.height

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
		
	
	def imprimir(self, pantalla, nave, llaser):
		self.mover(nave)
		cp1 = self.getRCentro()
		if Funciones.posicionValida(self.getRCentroX(),-200,800,self.getRCentroY(),-200,800):
			pantalla.display.blit(self.imagen, (self.RX,self.RY))
			Funciones.colision(self, nave)
			#Funciones.colision(self, enemigo)
			for i in llaser:
				if i.laserLibre == False:
					Funciones.colision(self, i)	
		
		
	def __init__(self, directorio, lplaneta, AREA_MAXIMA, DISTANCIA_MINIMA):
		self.imagen = pygame.image.load(directorio).convert_alpha()
		self.width = self.imagen.get_width()
		self.height = self.imagen.get_height()
		self.RX = 0
		self.RY = 0
		self.RCentro = 0
		asignado = False
		while not asignado:
			self.AX = random.randint(10,AREA_MAXIMA-self.imagen.get_width())
			self.AY = random.randint(10,AREA_MAXIMA-self.imagen.get_height())
			self.ACentro = ((self.imagen.get_width()/2) + self.AX, (self.imagen.get_height()/2) + self.AY)
			asignado = Funciones.lugarLibre(self, lplaneta, DISTANCIA_MINIMA)
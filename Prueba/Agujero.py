import pygame, random
<<<<<<< HEAD
from Funciones import rotarCentro, sumarAngulo, lugarLibre, colision
from Pantalla import Pantalla
from Texto import Texto

class Agujero:
	def getCentro(self):
		return self.centro
	def getCentroX(self):
		return self.centro[0]
	def getCentroY(self):
		return self.centro[1]
	def imprimir(self, camara,nave):
		self.angulo = sumarAngulo(self.angulo, self.velocidad)
		if (self.getCentroX()-camara.getX() >= -400 and self.getCentroX()-camara.getX() <= 1400) and (self.getCentroY()-camara.getY() >= -400 and self.getCentroY()-camara.getY() <= 1400):
			camara.display.blit(rotarCentro(self.imagen, self.angulo), (self.origenX-camara.getX(),self.origenY-camara.getY()))
			colision(self, camara, nave)
			
	def __init__(self, directorio, velocidad, lobjeto, AREA_MAXIMA, DISTANCIA_MINIMA):
		self.imagen = pygame.image.load(directorio).convert_alpha()
		self.velocidad = velocidad
		self.angulo = 0
		asignado = False
		while not asignado:
			self.origenX = random.randint(10,AREA_MAXIMA-self.imagen.get_width())
			self.origenY = random.randint(10,AREA_MAXIMA-self.imagen.get_width())
			self.centro = ((self.imagen.get_width()/2) + self.origenX, (self.imagen.get_height()/2) + self.origenY)
			asignado = lugarLibre(self, lobjeto, DISTANCIA_MINIMA)
=======
import Funciones
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
		self.angulo = Funciones.sumarAngulo(self.angulo, self.velocidad)
		self.RX = self.AX - nave.getAX()
		self.RY = self.AY - nave.getAY()
		self.RCentro = ((self.imagen.get_width()/2) + self.RX, (self.imagen.get_height()/2) + self.RY)
		
	def imprimir(self, pantalla, nave):
		self.mover(nave)
		if Funciones.posicionValida(self.getRCentroX(),-100,800,self.getRCentroY(),-100,800):
			pantalla.display.blit(Funciones.rotarCentro(self.imagen, self.angulo), (self.RX,self.RY))
			Funciones.colision(self, nave)
		
	def __init__(self, directorio, velocidad, lobjeto, AREA_MAXIMA, DISTANCIA_MINIMA):
		self.imagen = pygame.image.load(directorio).convert_alpha()
		self.velocidad = velocidad
		self.RX = 0
		self.RY = 0
		self.RCentro = 0
		self.angulo = 0
		self.gravedad = 4
		asignado = False
		while not asignado:
			self.AX = random.randint(10,AREA_MAXIMA-self.imagen.get_width())
			self.AY = random.randint(10,AREA_MAXIMA-self.imagen.get_height())
			self.ACentro = ((self.imagen.get_width()/2) + self.AX, (self.imagen.get_height()/2) + self.AY)
			asignado = Funciones.lugarLibre(self, lobjeto, DISTANCIA_MINIMA)
>>>>>>> Test-coordenadas
		
		
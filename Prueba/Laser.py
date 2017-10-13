import math, pygame
import Funciones
from Pantalla import Pantalla


class Laser:
	def getRX(self):
		return self.RX
		
	def getRY(self):
		return self.RY
		
	def getRCentroX(self):
		return self.RCentro[0]
		
	def getRCentroY(self):
		return self.RCentro[1]

	def getWidth(self):
		return self.width

	def getHeight(self):
		return self.height

	def getCoordenadas(self):
		return (int(self.AX), int(self.AY))

	def mover(self, nave):
		cosAngulo = math.cos(math.radians(self.angulo))
		sinAngulo = math.sin(math.radians(self.angulo))

		self.RX += cosAngulo * self.velocidad
		self.RY += -sinAngulo * self.velocidad
		self.AX += cosAngulo * self.velocidad
		self.AY += -sinAngulo * self.velocidad

	def imprimir(self, nave, pantalla):
		
		self.mover(nave)
		#
		if Funciones.posicionValida(self.RX,0,650,self.RY,0,475):
			pantalla.display.blit(pygame.transform.rotate(self.imagen, self.angulo), (self.RX - 3.5,self.RY - 3.5))
		else:
			self.laserLibre = True
			
	def setLaser(self, velocidad, nave, libre):
		self.velocidad = velocidad
		self.angulo = nave.angulo
		self.RX = nave.getRCentroX()
		self.RY = nave.getRCentroY()
		self.AX = nave.getACentroX()
		self.AY = nave.getACentroY()
		self.laserLibre = libre
		
	def __init__(self, directorio, nave, velocidad, angulo, libre):
		self.imagen = pygame.image.load(directorio).convert_alpha()
		self.width = self.imagen.get_width()
		self.height = self.imagen.get_height()
		self.angulo = angulo
		self.velocidad = velocidad
		
		self.RX = nave.getRCentroX()
		self.RY = nave.getRCentroY()
		self.AX = nave.getACentroX()
		self.AY = nave.getACentroY()

		self.RCentro = (self.RX + (self.imagen.get_width()/2),self.RY + (self.imagen.get_height()/2))
		
		self.laserLibre = libre
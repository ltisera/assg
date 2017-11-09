import math, pygame
import Funciones
from Pantalla import Pantalla


class Laser:
	def getRX(self):
		return self.RX
		
	def getRY(self):
		return self.RY

	def getAX(self):
		return self.AX
		
	def getAY(self):
		return self.AY

	def getRCentro(self):
		return self.RCentro
		
	def getRCentroX(self):
		return self.RCentro[0]
		
	def getRCentroY(self):
		return self.RCentro[1]

	def getACentro(self):
		return self.ACentro
		
	def getACentroX(self):
		return self.ACentro[0]
		
	def getACentroY(self):
		return self.ACentro[1]

	def getWidth(self):
		return self.width

	def getHeight(self):
		return self.height

	def getCoordenadas(self):
		return (int(self.AX), int(self.AY))

	def getLibre(self):
		return self.laserLibre	

	def setLibre(self, libre):
		self.laserLibre = libre

	def getDaño(self):
		return self.daño

	def setDaño(self, daño):
		self.daño = daño

	def mover(self, nave):

		#EL LASER AHORA ANDA BIEN!
		cosAngulo = math.cos(math.radians(self.angulo))
		sinAngulo = math.sin(math.radians(self.angulo))

		if self.velocidadAumento > 0:
			self.velocidad = nave.getVelocidad() + self.velocidadAumento

		self.AX += cosAngulo * self.velocidad
		self.AY += -sinAngulo * self.velocidad

		self.RX = self.AX - nave.getAX()
		self.RY = self.AY - nave.getAY()

		self.ACentro = (self.RX + (self.imagen.get_width()/2),self.RY + (self.imagen.get_height()/2))
		self.RCentro = (self.RX + (self.imagen.get_width()/2),self.RY + (self.imagen.get_height()/2))
		

	def imprimir(self, pantalla, nave):
		
		self.mover(nave)
		#
		if Funciones.posicionValida(self.RX,0,800,self.RY,0,600):
			pantalla.display.blit(pygame.transform.rotate(self.imagen, self.angulo), (self.RX - 4.5,self.RY - 4.5))
		else:
			self.laserLibre = True
			
	def setLaser(self, velocidad, angulo, objeto, libre):
		self.velocidad = velocidad
		self.angulo = angulo
		self.RX = objeto.getACentroX()
		self.RY = objeto.getACentroY()
		self.AX = objeto.getACentroX()
		self.AY = objeto.getACentroY()
		self.ACentro = (self.RX + (self.imagen.get_width()/2),self.RY + (self.imagen.get_height()/2))
		self.RCentro = (self.RX + (self.imagen.get_width()/2),self.RY + (self.imagen.get_height()/2))
		self.laserLibre = libre
		
	def __init__(self, directorio, objeto, velocidad, angulo, libre, daño, velocidadAumento = 0):
		self.imagen = pygame.image.load(directorio).convert_alpha()
		self.width = self.imagen.get_width()
		self.height = self.imagen.get_height()
		self.angulo = angulo
		self.velocidad = velocidad
		self.velocidadAumento = velocidadAumento
		self.RX = objeto.getACentroX()
		self.RY = objeto.getACentroY()
		self.AX = objeto.getACentroX()
		self.AY = objeto.getACentroY()

		self.ACentro = (self.RX + (self.imagen.get_width()/2),self.RY + (self.imagen.get_height()/2))
		self.RCentro = (self.RX + (self.imagen.get_width()/2),self.RY + (self.imagen.get_height()/2))
		
		self.laserLibre = libre
		self.daño = daño
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
		
		self.velocidad = nave.getVelocidad() + 10 

		self.AX += cosAngulo * self.velocidad
		self.AY += -sinAngulo * self.velocidad

		self.RX = self.AX - nave.getAX()
		self.RY = self.AY - nave.getAY()
		

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
		self.RX = objeto.getRCentroX()
		self.RY = objeto.getRCentroY()
		self.AX = objeto.getACentroX()
		self.AY = objeto.getACentroY()
		self.laserLibre = libre
		
	def __init__(self, directorio, objeto, velocidad, angulo, libre, daño):
		self.imagen = pygame.image.load(directorio).convert_alpha()
		self.width = self.imagen.get_width()
		self.height = self.imagen.get_height()
		self.angulo = angulo
		self.velocidad = velocidad
		
		self.RX = objeto.getRCentroX()
		self.RY = objeto.getRCentroY()
		self.AX = objeto.getACentroX()
		self.AY = objeto.getACentroY()

		self.RCentro = (self.RX + (self.imagen.get_width()/2),self.RY + (self.imagen.get_height()/2))
		
		self.laserLibre = libre
		self.daño = daño
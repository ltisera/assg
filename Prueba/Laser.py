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

		self.AX += (cosAngulo * self.velocidad) 
		self.AY -= (sinAngulo * self.velocidad) 
		self.RX = self.AX - nave.AX
		self.RY = self.AY - nave.AY 

	def imprimir(self, nave, pantalla):
		
		self.mover(nave)
		#
		if Funciones.posicionValida(self.RX,0,650,self.RY,0,475):
			pantalla.display.blit(pygame.transform.rotate(self.imagen, self.angulo),(self.RX - 3.5,self.RY - 3.5))
		else:
			self.laserLibre = True
			
	def setLaser(self, objeto, velocidad, angulo, libre):
		self.velocidad = velocidad
		self.angulo = angulo
		self.RX = objeto.getRCentroX()
		self.RY = objeto.getRCentroY()
		self.AX = objeto.getACentroX()
		self.AY = objeto.getACentroY()
		self.laserLibre = libre
		
		
		
		
		
	def __init__(self, directorio, objeto, velocidad, angulo, libre):
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
	
	def  traerAnguloLaserEnemigo(self,enemigo, camara):
		objetivoX = camara.getCentroX()
		objetivoY = camara.getCentroY()
		if (enemigo.RX > objetivoX and enemigo.RY <= objetivoY):
			if(objetivoY==enemigo.RY):
				self.angulo = 0
			else:
				self.angulo = 270-math.degrees(math.atan((enemigo.RX - objetivoX)/(objetivoY - enemigo.RY)))
		elif (enemigo.RX > objetivoX and enemigo.RY >= objetivoY):
			if(objetivoY==enemigo.RY):
				self.angulo = 270
			else:
				self.angulo = 90+ math.degrees(math.atan((enemigo.RX - objetivoX)/(enemigo.RY - objetivoY)))
		elif (enemigo.RX < objetivoX) and (enemigo.RY >= objetivoY):
			if(objetivoY==enemigo.RY):
				self.angulo= 180
			else:
				self.angulo = 90- math.degrees(math.atan((objetivoX - enemigo.RX)/(enemigo.RY - objetivoY)))
		else:
			if(objetivoY==enemigo.RY):
				self.angulo = 90
			else:
				self.angulo = 360-(90- math.degrees(math.atan((objetivoX - enemigo.RX)/(objetivoY - enemigo.RY))))
		return self.angulo
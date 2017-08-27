import math, pygame
from Enemigo import Enemigo
from Pantalla import Pantalla

class Laser:		
	def mover(self):
		self.X += math.cos(math.radians(self.angulo))*self.velocidad
		self.Y -= math.sin(math.radians(self.angulo))*self.velocidad

	def imprimir(self, camara):
		self.mover()
		if (self.X >= 0 and self.X <= 650) and (self.Y >= 0 and self.Y <= 475) and (self.X!=camara.getCentroX() and self.Y!=camara.getCentroY()):
			camara.display.blit(pygame.transform.rotate(self.imagen, self.angulo), (self.X,self.Y))
		else:
			self.laserLibre = True
		
	def  traerAnguloLaserEnemigo(self,enemigo, camara):
		objetivoX = camara.getCentroX()
		objetivoY = camara.getCentroY()
		if (enemigo.X > objetivoX and enemigo.Y <= objetivoY):
			if(objetivoY==enemigo.Y):
				self.angulo = 0
			else:
				self.angulo = 270-math.degrees(math.atan((enemigo.X - objetivoX)/(objetivoY - enemigo.Y)))
		elif (enemigo.X > objetivoX and enemigo.Y >= objetivoY):
			if(objetivoY==enemigo.Y):
				self.angulo = 270
			else:
				self.angulo = 90+ math.degrees(math.atan((enemigo.X - objetivoX)/(enemigo.Y - objetivoY)))
		elif (enemigo.X < objetivoX) and (enemigo.Y >= objetivoY):
			if(objetivoY==enemigo.Y):
				self.angulo= 180
			else:
				self.angulo = 90- math.degrees(math.atan((objetivoX - enemigo.X)/(enemigo.Y - objetivoY)))
		else:
			if(objetivoY==enemigo.Y):
				self.angulo = 90
			else:
				self.angulo = 360-(90- math.degrees(math.atan((objetivoX - enemigo.X)/(objetivoY - enemigo.Y))))
		return self.angulo
		
	def setLaser(self, x,y, velocidad, angulo, libre):
		self.angulo = angulo
		self.velocidad = velocidad
		self.X = x
		self.Y = y
		self.laserLibre = libre
	def __init__(self, directorio, camara, velocidad, angulo, libre):
		self.imagen = pygame.image.load(directorio).convert_alpha()
		self.angulo = angulo
		self.velocidad = velocidad
		self.X = camara.getCentroX()
		self.Y = camara.getCentroY()
		self.laserLibre = libre
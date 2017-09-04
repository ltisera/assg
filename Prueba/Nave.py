import pygame, math
from Funciones import rotarCentro, sumarAngulo

class Nave:
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
	
	def sumarAngulo(self, sumAngulo):
		self.angulo = sumarAngulo(self.angulo, sumAngulo)
	
	def sumarVelocidad(self, sumar):
		self.velocidad = self.velocidad + sumar
		if self.velocidad <= (self.minVelocidad):
			self.velocidad = self.minVelocidad
		elif self.velocidad >= (self.maxVelocidad):
			self.velocidad = self.maxVelocidad
		
	def boom(self):
		self.colision = True
		
	def mover(self, pantalla):
		self.AX += math.cos(math.radians(self.angulo))*self.velocidad
		self.AY += -math.sin(math.radians(self.angulo))*self.velocidad
		self.ACentro = (self.AX + self.getRCentroX(), self.AY + self.getRCentroY())
		self.supIZQ = pantalla.getIndiceSector(self.getAX()-800,self.getAY()-600)
		self.supDER = pantalla.getIndiceSector(self.getAX()+800,self.getAY()-600)
		self.infIZQ = pantalla.getIndiceSector(self.getAX()-800,self.getAY()+600)
		self.infDER = pantalla.getIndiceSector(self.getAX()+800,self.getAY()+600)
		
	def imprimir(self, pantalla):
		pantalla.display.blit(rotarCentro(self.imagen, self.angulo), (self.RX, self.RY))
		if self.colision:
			pantalla.display.blit(self.imagenColision, (self.RX + (self.imagenColision.get_width()/2), self.RY + (self.imagenColision.get_height()/2)))
			self.colision = False
		
	def __init__(self, directorio,directorio2, anguloOrigen, velocidad, minVelocidad, maxVelocidad, origen, camara):
		self.imagen = pygame.image.load(directorio).convert_alpha()
		self.imagenColision = pygame.image.load(directorio2).convert_alpha()
		self.colision = False
		self.imagen = pygame.transform.rotate(self.imagen, anguloOrigen)
		self.RX = camara.getCentroX() - (self.imagen.get_width()/2)
		self.RY = camara.getCentroY() - (self.imagen.get_height()/2)
		self.RCentro = (camara.getCentroX(),camara.getCentroY())
		self.AX = origen[0]
		self.AY = origen[1]
		self.ACentro = (self.AX + self.getRCentroX(), self.AY + self.getRCentroY())
		self.supIZQ = 0
		self.supDER = 0
		self.infIZQ = 0
		self.infDER = 0
		self.maxVelocidad = maxVelocidad
		self.minVelocidad = minVelocidad
		self.angulo = 0
		self.velocidad = 0
		self.sumarVelocidad(velocidad)
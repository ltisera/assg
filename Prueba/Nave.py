import pygame, math
import Funciones

FRAMES = 4 #Para la animacion del fuego

class Nave:
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
	def getPuntos(self):
		return self.puntos
	def setPuntos(self, puntosNuevo):
		self.puntos = puntosNuevo
	def sumarAngulo(self, sumAngulo):
		self.angulo = Funciones.sumarAngulo(self.angulo, sumAngulo)
	
	def sumarVelocidad(self, sumar):
		self.velocidad = self.velocidad + sumar
		if self.velocidad <= (self.minVelocidad):
			self.velocidad = self.minVelocidad
		elif self.velocidad >= (self.maxVelocidad):
			self.velocidad = self.maxVelocidad
	
	def sumarContador(self):
		self.contador += 1
		if self.contador > 7*FRAMES:
			self.contador = 0	
		
	def boom(self):
		self.colision = True
		
	def mover(self, mapa):
		self.AX += math.cos(math.radians(self.angulo))*self.velocidad
		self.AY += -math.sin(math.radians(self.angulo))*self.velocidad
		self.ACentro = (self.AX + self.getRCentroX(), self.AY + self.getRCentroY())
		self.supIZQ = mapa.getIndiceSector(self.getAX()-800,self.getAY()-600)
		self.supDER = mapa.getIndiceSector(self.getAX()+800,self.getAY()-600)
		self.infIZQ = mapa.getIndiceSector(self.getAX()-800,self.getAY()+600)
		self.infDER = mapa.getIndiceSector(self.getAX()+800,self.getAY()+600)
		
	def imprimir(self, pantalla):
		if self.velocidad < 0.5:
			pantalla.display.blit(Funciones.rotarCentro(self.imagen, self.angulo), (self.RX, self.RY))
		elif self.velocidad < 4:
			pantalla.display.blit(Funciones.rotarCentro(self.lento[int(self.contador/FRAMES)], self.angulo), (self.RX, self.RY))
		elif self.velocidad < 7:
			pantalla.display.blit(Funciones.rotarCentro(self.normal[int(self.contador/FRAMES)], self.angulo), (self.RX, self.RY))
		elif self.velocidad < 10:
			pantalla.display.blit(Funciones.rotarCentro(self.rapido[int(self.contador/FRAMES)], self.angulo), (self.RX, self.RY))
		else:
			pantalla.display.blit(Funciones.rotarCentro(self.turbo[int(self.contador/FRAMES)], self.angulo), (self.RX, self.RY))
		if self.colision:
			pantalla.display.blit(self.imagenColision, (self.RX + (self.imagenColision.get_width()/2), self.RY + (self.imagenColision.get_height()/2)))
			self.colision = False
		self.sumarContador()
	def sumarPuntos(self, puntosS):
		self.puntos += puntosS
		
	def getPuntos(self):
		return self.puntos
	def __init__(self, directorio,directorio2, anguloOrigen, velocidad, minVelocidad, maxVelocidad, origen, pantalla):
		self.puntos = 0
		self.imagen = pygame.image.load(directorio+'/Nave.png').convert_alpha()
		self.lento = []
		for i in range(8):
			self.lento.append(pygame.image.load(directorio+'/Lento{}.png'.format(i+1)).convert_alpha())
		self.normal = []
		for i in range(8):
			self.normal.append(pygame.image.load(directorio+'/Normal{}.png'.format(i+1)).convert_alpha())
		self.rapido = []
		for i in range(8):
			self.rapido.append(pygame.image.load(directorio+'/Rapido{}.png'.format(i+1)).convert_alpha())
		self.turbo = []
		for i in range(8):
			self.turbo.append(pygame.image.load(directorio+'/Turbo{}.png'.format(i+1)).convert_alpha())
		self.contador = 0
		self.imagenColision = pygame.image.load(directorio2).convert_alpha()
		self.width = self.imagen.get_width()
		self.height = self.imagen.get_height()
		self.colision = False
		self.imagen = pygame.transform.rotate(self.imagen, anguloOrigen)
		self.RX = pantalla.getCentroX() - (self.imagen.get_width()/2)
		self.RY = pantalla.getCentroY() - (self.imagen.get_height()/2)
		self.RCentro = (pantalla.getCentroX(),pantalla.getCentroY())
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
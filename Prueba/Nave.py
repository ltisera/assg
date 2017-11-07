import pygame, math
import Funciones
from Explosion import Explosion

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
	
	def sumarAngulo(self, sumAngulo):
		self.angulo = Funciones.sumarAngulo(self.angulo, sumAngulo)
	
	def sumarVelocidad(self, sumar):
		self.velocidad = self.velocidad + sumar
		if self.velocidad <= (self.minVelocidad):
			self.velocidad = self.minVelocidad
		elif self.velocidad >= (self.maxVelocidad):
			self.velocidad = self.maxVelocidad
	
	def reduceVida(self, cantidad):
		if(self.vida > cantidad):
			self.vida -= cantidad
		else:
			self.vida = 0
			self.explotando = True
			
		
	def impBarraVida(self, vida, pantalla):
		colorBarra = (255,0,0)
		if(vida >= 33):
			colorBarra = (255,255,0)
		if(vida >=66):
			colorBarra = (0,255,0)
		pygame.draw.rect(pantalla.display, colorBarra, (0, 475, (vida * 650) / 100, 10))
	
	def sumarContador(self):
		self.contador += 1
		if self.contador > 7*FRAMES:
			self.contador = 0	
		
	def boom(self):
		self.colision = True
	
	def fueDestruidoPorCompleto(self):
		return self.exploto
		
	def mover(self, mapa):
		self.AX += math.cos(math.radians(self.angulo))*self.velocidad
		self.AY += -math.sin(math.radians(self.angulo))*self.velocidad
		self.ACentro = (self.AX + self.getRCentroX(), self.AY + self.getRCentroY())
		self.supIZQ = mapa.getIndiceSector(self.getAX()-800,self.getAY()-600)
		self.supDER = mapa.getIndiceSector(self.getAX()+800,self.getAY()-600)
		self.infIZQ = mapa.getIndiceSector(self.getAX()-800,self.getAY()+600)
		self.infDER = mapa.getIndiceSector(self.getAX()+800,self.getAY()+600)

	def imprimir(self, pantalla, laserEnemigo):
		if(self.explotando == False):
			self.imprimirNave(pantalla, laserEnemigo)
		else:
			#Efecto de explosion
			self.velocidad = 0.1
			if(self.explotaNave.imprimir(pantalla,self.getRX()+(self.imagen.get_width()/2)-10, self.getRY()+(self.imagen.get_height()/2)-10) == 0):
				self.explotando = False
				self.exploto = True
				self.vida = 100
				
	def imprimirNave(self, pantalla, laserEnemigo):
		colisionLaserEnemigo = False
		self.impBarraVida(self.vida, pantalla)
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
		if not self.colision and Funciones.hayColision(self, laserEnemigo):
			self.reduceVida(5)
			laserEnemigo.laserLibre = True
		if self.colision:
			if self.exploto:
				self.tiempoChoque = 40
				self.exploto = False
			pantalla.display.blit(self.imagenColision, (self.RX + (self.imagenColision.get_width()/2), self.RY + (self.imagenColision.get_height()/2)))
			if(self.tiempoChoque==0): 
				self.reduceVida(math.fabs((self.velocidad*100)/15))
				self.velocidad = -(self.velocidad/2)
				
			self.tiempoChoque += 1
			if(self.tiempoChoque >=40):
				self.tiempoChoque =0
				self.colision = False
		self.sumarContador()
		
	def __init__(self, directorio,directorio2, anguloOrigen, velocidad, minVelocidad, maxVelocidad, origen, pantalla):
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
		self.tiempoChoque = 0
		self.vida = 100
		self.explotaNave = Explosion("Recursos/Explosion1.png")
		self.exploto = False
		self.explotando = False
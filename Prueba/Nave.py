import pygame, math
import Funciones
from Barra import Barra
from Explosion import Explosion


FRAMES = 4 #Para la animacion del fuego
TIEMPO_DE_ESPERA_DEL_ESCUDO = 300
CANT_MIN_INICIAR_TURBO = 10

class Nave:
	def getWidth(self):
		return self.width

	def getHeight(self):
		return self.height

	def getAngulo(self):
		return self.angulo

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
	
	def getVelocidad(self):
		return self.velocidad

	def sumarVelocidad(self, sumar):
		self.velocidad = self.velocidad + sumar
		if self.velocidad <= (self.minVelocidad):
			self.velocidad = self.minVelocidad
		elif self.velocidad >= (self.maxVelocidad):
			self.velocidad = self.maxVelocidad
		if self.velocidad >= 9.9:
			if self.turboActivo == False and self.cargaturbo.getValor() < CANT_MIN_INICIAR_TURBO:
				if self.velocidad-sumar <= 9.9:
					self.velocidad = 9.9
			else:
				self.turboActivo = True

	def reduceVida(self, cantidad):
		self.ultimoGolpe = 0
		if (self.vida.sumarValor(self.escudo.sumarValor(-cantidad)) < 0): 
			self.explotando = True

	def sumarContador(self):
		self.contador += 1
		if self.contador > 7*FRAMES:
			self.contador = 0	
		
	def boom(self):
		self.colision = True

	def imprimir(self, pantalla):
		if(self.explotando == False):
			self.imprimirNave(pantalla)
		else:
			#Efecto de explosion
			self.velocidad = 0.1
			if(self.explotaNave.imprimir(pantalla,self.getRX()+(self.imagen.get_width()/2)-10, self.getRY()+(self.imagen.get_height()/2)-10) == 0):
				self.explotando = False
				self.exploto = True
				self.vida.setValor(100)
		
	def mover(self, mapa):
		self.AX += math.cos(math.radians(self.angulo))*self.velocidad
		self.AY += -math.sin(math.radians(self.angulo))*self.velocidad
		self.ACentro = (self.AX + self.getRCentroX(), self.AY + self.getRCentroY())
		self.supIZQ = mapa.getIndiceSector(self.getAX()-800,self.getAY()-600)
		self.supDER = mapa.getIndiceSector(self.getAX()+800,self.getAY()-600)
		self.infIZQ = mapa.getIndiceSector(self.getAX()-800,self.getAY()+600)
		self.infDER = mapa.getIndiceSector(self.getAX()+800,self.getAY()+600)
		
	def imprimirBarras(self, pantalla):
		self.vida.imprimir(pantalla)
		self.escudo.imprimir(pantalla)
		self.cargaturbo.imprimir(pantalla)	

	def imprimirNave(self, pantalla):
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
			if self.turboActivo == True:
				if self.cargaturbo.sumarValor((-self.velocidad/100)-0.06) < 0:
					self.turboActivo = False
			else:
				self.velocidad -= 0.1
		self.cargaturbo.sumarValor(0.06)
		if self.colision:
			if self.exploto:
				self.tiempoChoque = 40
				self.exploto = False
			if(self.tiempoChoque==0): 
				self.reduceVida(math.fabs((self.velocidad*100)/15))
				self.velocidad = -(self.velocidad/2)
			self.tiempoChoque += 1
			if(self.tiempoChoque >=40):
				self.tiempoChoque =0
				self.colision = False
		if self.ultimoGolpe > TIEMPO_DE_ESPERA_DEL_ESCUDO:
			self.escudo.sumarValor(0.06)
		self.ultimoGolpe += 1
		self.sumarContador()

	def sumarPuntos(self, puntos):
		self.puntos += puntos
		
	def getPuntos(self):
		return self.puntos

	def __init__(self, directorio, anguloOrigen, velocidad, minVelocidad, maxVelocidad, origen, pantalla, barraHeight, barraWidth, vida, escudo, turbo):
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
		self.vida = Barra(((255,0,0),(255,255,0),(0,255,0)), 0, 100, 100, barraHeight, barraWidth, vida[0], vida[1])
		self.escudo = Barra(((0,76,153),(0,102,204),(0,128,255),(51,153,255),(102,178,255)), 0, 100, 0, barraHeight, barraWidth, escudo[0], escudo[1])
		self.cargaturbo = Barra(((0,76,153),(0,102,204),(0,128,255),(51,153,255),(102,178,255)), 0, 100, 0, barraHeight, barraWidth, turbo[0], turbo[1])
		self.explotaNave = Explosion("Recursos/Explosion1.png")
		self.exploto = False
		self.explotando = False
		self.ultimoGolpe = 0
		self.turboActivo = False
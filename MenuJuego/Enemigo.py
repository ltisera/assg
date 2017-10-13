#	Clase Enemigo:
# 	- Genera un enemigo que ataca con un rayo laser, persigue al personaje
# 	principal hasta una distancia de 1000 pixeles.
#	- si distancia <= 500 ataque mele
#	- si distancia > 500 && distancia <= 1000 Dispara laser
#	- si distancia > 1000 Vuelve a su Origen!
#
#	Atributos:
#		-imagen: (sprite en un futuro) 
#		-origenX: 
#		-origenY: Coordenadas de origen del enemigo
#		-posX:
#		-posY: Coordenadas actuales del enemigo
#
#	Metodos:
#		+mover(self, nave)
#		+imprimir(self, X, Y, camara)
#	
#

import pygame, math
from Pantalla import Pantalla
import Funciones 
from Explosion import Explosion
class Enemigo:
	def destruirEnemigo(self):
		self.destruido = True

	def getVida(self):
		return self.vida

	def setVida(self, cuantaVida):
		self.vida = cuantaVida
		if (self.vida <= 0):
			self.sonido.play()
			self.destruirEnemigo()

	def setPuntos(self, puntos):
		self.puntos += puntos

	def getPuntos(self):
		return self.puntos

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

	def boom(self):
		self.colision = True
		
	def mover(self, nave):
		self.RX -= math.cos(math.radians(nave.angulo))*nave.velocidad
		self.RY -= -math.sin(math.radians(nave.angulo))*nave.velocidad
		self.RCentro = (self.RX + (self.imagen.get_width()/2),self.RY + (self.imagen.get_height()/2))
		if Funciones.distancia(self.getRCentroX(),nave.getRCentroX(),self.getRCentroY(),nave.getRCentroY()) > 100:
			if self.getRCentroX() < nave.getRCentroX()-(self.imagen.get_width()/2):
				self.RX += self.velocidad
			elif self.getRCentroX() > nave.getRCentroX()-(self.imagen.get_width()/2):
				self.RX -= self.velocidad
			if self.getRCentroY() < nave.getRCentroY()-(self.imagen.get_height()/2):
				self.RY += self.velocidad
			elif self.getRCentroY() > nave.getRCentroY()-(self.imagen.get_height()/2):
				self.RY -= self.velocidad
		else:
			if self.getRCentroX() < nave.getRCentroX()-(self.imagen.get_width()/2):
				self.RX -= self.velocidad
			elif self.getRCentroX() > nave.getRCentroX()-(self.imagen.get_width()/2):
				self.RX += self.velocidad
			if self.getRCentroY() < nave.getRCentroY()-(self.imagen.get_height()/2):
				self.RY -= self.velocidad
			elif self.getRCentroY() > nave.getRCentroY()-(self.imagen.get_height()/2):
				self.RY += self.velocidad

	def impBarraVida(self, vida, pantalla):
		colorBarra = (255,0,0)
		if(vida >= 33):
			colorBarra = (255,255,0)
		if(vida >=66):
			colorBarra = (0,255,0)

		pygame.draw.rect(pantalla.display, colorBarra, (self.RX + 10, self.RY -10, (vida * 30) / 100, 3))

	def reduceVida(self, cantidad):
		self.vida -= cantidad

	def imprimir(self, nave, pantalla, llaser):
		if(self.destruido == False):
			self.mover(nave)
			Funciones.colisonVieja(self, nave)
			self.impBarraVida(self.vida, pantalla)
			for i in llaser:
				if i.laserLibre == False:
					Funciones.colisonVieja(self, i)

			if (self.colision):
				pantalla.display.blit(self.imagenColision, (self.RX,self.RY))
			else: 
				pantalla.display.blit(self.imagen, (self.RX,self.RY))
		else:
			#Efecto de explosion
			print("Explota")
			if(self.explotaEnemigo.imprimir(pantalla,self.getRX(), self.getRY()) == 0):
				self.destruido = False
				self.vida = 100
				self.RX = -200
				self.RY = -200
				self.setPuntos(100)
	
	def __init__(self, directorio, directorio2, X, Y, velocidad):
		self.sonido = pygame.mixer.Sound("Recursos/Musica/explosion.wav")
		self.explotaEnemigo = Explosion("Recursos/Explosion1.png")
		self.imagen = pygame.image.load(directorio).convert_alpha()
		self.imagenColision = pygame.image.load(directorio2).convert_alpha()
		self.colision = False
		self.width = self.imagen.get_width()
		self.height = self.imagen.get_height()
		self.AX = X
		self.AY = Y
		self.ACentro = (self.AX + (self.imagen.get_width()/2),self.AY + (self.imagen.get_height()/2))
		self.RX = X 
		self.RY = Y
		self.RCentro = (self.RX + (self.imagen.get_width()/2),self.RY + (self.imagen.get_height()/2))
		self.velocidad = velocidad
		self.vida = 100
		self.destruido = False
		self.puntos = 0

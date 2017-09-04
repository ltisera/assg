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

class Enemigo:
	def getAX(self):
		return self.AX
		
	def getAY(self):
		return self.AY
		
	def getAPos(self):
		return(int(self.AX),int(self.AY))
	
	def getRX(self):
		return self.RX
		
	def getRY(self):
		return self.RY
		
	def getRPos(self):
		return(int(self.RX),int(self.RY))
	
	def mover(self, nave):
		self.RX -= math.cos(math.radians(nave.angulo))*nave.velocidad
		self.RY -= -math.sin(math.radians(nave.angulo))*nave.velocidad
		if self.RX < nave.getRCentroX()-(self.imagen.get_width()/2):
			self.RX += self.velocidad
		elif self.RX > nave.getRCentroX()-(self.imagen.get_width()/2):
			self.RX -= self.velocidad
		if self.RY < nave.getRCentroY()-(self.imagen.get_height()/2):
			self.RY += self.velocidad
		elif self.RY > nave.getRCentroY()-(self.imagen.get_height()/2):
			self.RY -= self.velocidad
			
	def imprimir(self, nave, pantalla):
		self.mover(nave)
		pantalla.display.blit(self.imagen, (self.RX,self.RY))
		
	def __init__(self, directorio, X, Y, velocidad):
		self.imagen = pygame.image.load(directorio).convert_alpha()
		self.AX = X - (self.imagen.get_width()/2)
		self.AY = Y - (self.imagen.get_height()/2)
		self.RX = X 
		self.RY = Y 
		self.velocidad = velocidad
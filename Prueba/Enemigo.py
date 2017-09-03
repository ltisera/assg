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


import pygame
from Pantalla import Pantalla

class Enemigo:
	def mover(self, nave):
		
		if self.X < nave.getX()+200:
			self.X += self.velocidad
		elif self.X > nave.getX()+200:
			self.X -= self.velocidad
		if self.Y < nave.getY()+175:
			self.Y += self.velocidad
		elif self.Y > nave.getY()+175:
			self.Y -= self.velocidad
			
	def getX(self):
		return self.X
	def getY(self):
		return self.Y
	def getPos(self):
		return(self.X,self.Y)
			
	def imprimir(self, nave, camara):
		self.mover(nave)
		camara.display.blit(self.imagen, (self.X,self.Y))
	def __init__(self, directorio, X, Y, velocidad):
		self.imagen = pygame.image.load(directorio).convert_alpha()
		self.X = X
		self.Y = Y
		self.velocidad = velocidad
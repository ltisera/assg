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
import Funciones
from Pantalla import Pantalla
from Planeta import Planeta

class Enemigo:
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
		
	def evitarColision(self, planeta, nave):
		if self.getRCentroX() < planeta.getRCentroX()-(self.imagen.get_width()/2):
			self.RX -= self.velocidad
		elif self.getRCentroX() > planeta.getRCentroX()-(self.imagen.get_width()/2):
			self.RX += self.velocidad
		if self.getRCentroY() < planeta.getRCentroY()-(self.imagen.get_height()/2):
			self.RY -= self.velocidad
		elif self.getRCentroY() > planeta.getRCentroY()-(self.imagen.get_height()/2):
			self.RY += self.velocidad
		
		
		if self.getRCentroX() < nave.getRCentroX()-(self.imagen.get_width()/2):
			if self.getRCentroY() < nave.getRCentroY()-(self.imagen.get_height()/2):
				self.RY -= self.velocidad	#Enemigo SupIzq Nave infDer
			elif self.getRCentroY() > nave.getRCentroY()-(self.imagen.get_height()/2):
				self.RY += self.velocidad	#Enemigo InfIzq Nave SupDer
		elif self.getRCentroX() > nave.getRCentroX()-(self.imagen.get_width()/2):
			if self.getRCentroY() < nave.getRCentroY()-(self.imagen.get_height()/2):
				self.RX += self.velocidad	#Enemigo SupDer Nave InfIzq
			elif self.getRCentroY() > nave.getRCentroY()-(self.imagen.get_height()/2):
				self.RX -= self.velocidad	#Enemigo infDer Nave SupIzq
	
			
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
			
	def imprimir(self, nave, pantalla):
		self.mover(nave)
		pantalla.display.blit(self.imagen, (self.RX,self.RY))
		if self.colision:
			pantalla.display.blit(self.imagenColision, (self.getRCentroX() - (self.imagenColision.get_width()/2), self.getRCentroY() - (self.imagenColision.get_height()/2)))
			self.colision = False
		
	def __init__(self, directorio, directorio2, X, Y, velocidad):
		self.imagen = pygame.image.load(directorio).convert_alpha()
		self.imagenColision = pygame.image.load(directorio2).convert_alpha()
		self.colision = False
		self.AX = X
		self.AY = Y
		self.ACentro = (self.AX + (self.imagen.get_width()/2),self.AY + (self.imagen.get_height()/2))
		self.RX = X 
		self.RY = Y
		self.RCentro = (self.RX + (self.imagen.get_width()/2),self.RY + (self.imagen.get_height()/2))
		self.velocidad = velocidad
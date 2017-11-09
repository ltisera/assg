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
from Barra import Barra
from Pantalla import Pantalla
import Funciones 
from Explosion import Explosion
from Laser import Laser

class Enemigo:
	def destruirEnemigo(self):
		self.explotando = True

	def getVida(self):
		return self.vida.getValor()

	def fueDestruidoPorCompleto(self):
		return self.exploto

	def getWidth(self):
		return self.width

	def getHeight(self):
		return self.height

	def getAX(self):
		return self.AX

	def setAX(self, X, minX, maxX):
		self.AX = Funciones.setValor(X, minX+50, maxX-100)

	def getAY(self):
		return self.AY
		
	def setAY(self, Y, minY, maxY):
		self.AY = Funciones.setValor(Y, minY+50, maxY-50)

	def setCordenadas(self, nave, AX, AY, maximo):
		self.setAX(AX,0,maximo)
		self.setAY(AY,0,maximo)
		self.ACentro = (self.AX + (self.imagen.get_width()/2),self.AY + (self.imagen.get_height()/2))
		self.RX = self.AX - nave.getAX()
		self.RY = self.AY - nave.getAY()
		self.RCentro = (self.RX + (self.imagen.get_width()/2),self.RY + (self.imagen.get_height()/2))
		
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
		return
		
	def mover(self, nave):
		if Funciones.distancia(self.getRCentroX(),nave.getRCentroX(),self.getRCentroY(),nave.getRCentroY()) > 100:
			if self.getRCentroX() < nave.getRCentroX()-(self.imagen.get_width()/2):
				self.AX += self.velocidad
			elif self.getRCentroX() > nave.getRCentroX()-(self.imagen.get_width()/2):
				self.AX -= self.velocidad
			if self.getRCentroY() < nave.getRCentroY()-(self.imagen.get_height()/2):
				self.AY += self.velocidad
			elif self.getRCentroY() > nave.getRCentroY()-(self.imagen.get_height()/2):
				self.AY -= self.velocidad
		else:
			if self.getRCentroX() < nave.getRCentroX()-(self.imagen.get_width()/2):
				self.AX -= self.velocidad
			elif self.getRCentroX() > nave.getRCentroX()-(self.imagen.get_width()/2):
				self.AX += self.velocidad
			if self.getRCentroY() < nave.getRCentroY()-(self.imagen.get_height()/2):
				self.AY -= self.velocidad
			elif self.getRCentroY() > nave.getRCentroY()-(self.imagen.get_height()/2):
				self.AY += self.velocidad

	def reduceVida(self, cantidad):
		if (self.vida.sumarValor(-cantidad) < 0):
			self.destruirEnemigo()

	def reset(self, X, Y, velocidad, daño, vida, puntos):
		self.exploto = False
		self.explotando = False
		self.AX = X
		self.AY = Y
		self.ACentro = (self.AX + (self.imagen.get_width()/2),self.AY + (self.imagen.get_height()/2))
		self.RX = 0 
		self.RY = 0
		self.RCentro = (self.RX + (self.imagen.get_width()/2),self.RY + (self.imagen.get_height()/2))
		self.vida.setMaximo(vida)
		self.vida.setValor(vida)
		self.laser.setDaño(daño)
		self.puntos = puntos

	def setDisparar(self):
		self.disparar = True
	
	def cercaDeOtroEnemigo(self, lenemigo):
		cerca = False
		for i in lenemigo:
			if(Funciones.distancia(self.getACentroX(), i.getACentroX(), self.getACentroY(), i.getACentroY()) <= 100 and (self.ACentro != i.ACentro)):
				cerca = True
				
				if(self.AX > i.AX and self.AY > i.AY):
					self.AX += self.velocidad
					self.AY += self.velocidad
					
				if(self.AX < i.AX and self.AY > i.AY):
					self.AX -= self.velocidad
					self.AY += self.velocidad

				if(self.AX > i.AX and self.AY < i.AY):
					self.AX += self.velocidad
					self.AY -= self.velocidad

				if(self.AX < i.AX and self.AY < i.AY):
					self.AX -= self.velocidad
					self.AY -= self.velocidad
				
				if(self.AX == i.AX and self.AY > i.AY):
					self.AY += self.velocidad
				
				if(self.AX > i.AX and self.AY == i.AY):
					self.AX -= self.velocidad
				
				if(self.AX == i.AX and self.AY < i.AY):
					self.AY -= self.velocidad
				
				if(self.AX < i.AX and self.AY == i.AY):
					self.AX += self.velocidad

		return cerca

	def imprimir(self, pantalla, nave, VELOCIDAD_LASER, lenemigo):
		if(self.explotando == False):
			if(not self.cercaDeOtroEnemigo(lenemigo)):
				self.mover(nave)
			self.setCordenadas(nave, self.AX, self.AY, pantalla.getAreaMaxima())
			pantalla.display.blit(self.imagen, (self.RX,self.RY))
			self.vida.imprimir(pantalla, self.RX + 10, self.RY -10)
			
			if self.laser.getLibre() == False:
				self.laser.imprimir(pantalla, nave)
				if Funciones.hayColisionA(self.laser, nave) == True:
					nave.reduceVida(self.laser.getDaño())
					self.laser.setLibre(True)
		
			else:
				if(self.disparar == True):
					self.disparar = False
					self.laser.setLaser(VELOCIDAD_LASER+self.velocidad, Funciones.calcularAnguloEntrePuntos(self.getACentroX(), self.getACentroY(), nave.getACentroX(), nave.getACentroY()), self, False)
		
		else:
			#Efecto de explosion
			self.laser.setLibre(True)
			if(self.explotaEnemigo.imprimir(pantalla,self.AX - nave.getAX(), self.AY - nave.getAY()) == 0):
				self.explotando = False
				self.exploto = True
				nave.sumarPuntos(self.puntos)

	def __init__(self, directorio, directorio2, X, Y, velocidad, daño, vida, puntos):
		self.explotaEnemigo = Explosion("Recursos/Explosion1.png")
		self.imagen = pygame.image.load(directorio).convert_alpha()
		self.exploto = False
		self.explotando = False
		self.width = self.imagen.get_width()
		self.height = self.imagen.get_height()
		self.AX = X
		self.AY = Y
		self.ACentro = (self.AX + (self.imagen.get_width()/2),self.AY + (self.imagen.get_height()/2))
		self.RX = X 
		self.RY = Y
		self.RCentro = (self.RX + (self.imagen.get_width()/2),self.RY + (self.imagen.get_height()/2))
		self.velocidad = velocidad
		self.vida = Barra(((255,0,0),(255,255,0),(0,255,0)), 0, vida, vida, 3, 30)
		self.laser = Laser(directorio2, self, 0, 0, True, daño)
		self.puntos = puntos
		self.disparar = False



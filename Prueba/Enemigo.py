import pygame

class Enemigo:
	def mover(self, X, Y, centroX, centroY):
		self.X -= X
		self.Y += Y
		if self.X < centroX-50:
			self.X += self.velocidad
		elif self.X > centroX-50:
			self.X -= self.velocidad
		if self.Y < centroY-28:
			self.Y += self.velocidad
		elif self.Y > centroY-28:
			self.Y -= self.velocidad
	def imprimir(self, X, Y, pantalla):
		self.mover(X, Y, pantalla.centroX, pantalla.centroY)
		pantalla.display.blit(self.imagen, (self.X,self.Y))
	def __init__(self, directorio, X, Y, velocidad):
		self.imagen = pygame.image.load(directorio).convert_alpha()
		self.X = X
		self.Y = Y
		self.velocidad = velocidad
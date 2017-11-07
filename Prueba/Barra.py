import pygame
from Pantalla import Pantalla

class Barra:
	def getValor(self):
		return self.valor

	def setValor(self, valor):
		self.valor = valor
		diferencia = 0
		if (self.valor <= self.minimo):
			diferencia = self.valor - self.minimo - 0.1
			self.valor = self.minimo
		if (self.valor >= self.maximo):
			diferencia = self.valor - self.maximo + 0.1
			self.valor = self.maximo	
		return diferencia

	def sumarValor(self, sumar):
		return self.setValor(self.valor+sumar)
	
	def getColor(self):
		i = int(self.valor/(self.maximo/len(self.color)))		
		if (i >= len(self.color)):
			i = len(self.color)-1
		return self.color[i]

	def imprimir(self, pantalla, X = 0, Y = 0):
		if X == 0:
			X = self.X
		if Y == 0:
			Y = self.Y
		pygame.draw.rect(pantalla.display, self.getColor(), (X, Y, (self.valor*self.width)/100 , self.height))

	def __init__(self, color, minimo, maximo, valorInicial, height, width, X = 0, Y = 0):
		self.color = []
		for i in color:
			self.color.append(i)
		self.minimo = minimo
		self.maximo = maximo
		self.valor = valorInicial
		self.height = height
		self.width = width
		self.X = X
		self.Y = Y

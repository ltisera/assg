import pygame
import math
from Planeta import Planeta
from Agujero import Agujero
import random

class  Mapa:
	def getAreaMaxima(self):
		return self.areaMaxima
		
	#Devuelve la lista de objetos generada para cada sector
	def generarObjetos(self, OBJETOS_MAXIMOS, DISTANCIA_MINIMA):
		self.listaObjetos = []
		for i in range(OBJETOS_MAXIMOS):
			opc = random.randint(0,10)
			if opc == 10:
				self.listaObjetos.append(Agujero("Recursos/AgujeroNegro.png", 2, self.listaObjetos, self.areaMaxima, DISTANCIA_MINIMA))
			elif opc < 5:
				self.listaObjetos.append(Planeta("Recursos/Planeta2.png", self.listaObjetos, self.areaMaxima, DISTANCIA_MINIMA))	
			else:
				self.listaObjetos.append(Planeta("Recursos/Planeta.png", self.listaObjetos, self.areaMaxima, DISTANCIA_MINIMA))
	
	def getListaObjetos(self):
		return self.listaObjetos
	
	def agregarObjetoASector(self, objeto):
		self.listaSector[self.getIndiceSector(objeto.getACentroX(), objeto.getACentroY())].append(objeto)

	def getIndiceSector(self, X, Y):
		if (X >= 0 and X <= self.areaMaxima) and (Y >= 0 and Y <= self.areaMaxima):
			return math.trunc(((X//self.area)*self.dividirArea ) + (Y//self.area))
		else:
			return self.cantidadAreas+1
			
	def __init__(self, areaMaxima, dividirArea, OBJETOS_MAXIMOS, DISTANCIA_MINIMA):
		self.areaMaxima = areaMaxima
		self.dividirArea = dividirArea
		self.area = self.areaMaxima/self.dividirArea
		self.cantidadAreas = math.trunc(math.pow(self.dividirArea, 2))
		self.listaSector = [[] for i in range(self.cantidadAreas)]
		self.generarObjetos(OBJETOS_MAXIMOS, DISTANCIA_MINIMA)
		for i in self.listaObjetos:
			self.agregarObjetoASector(i)
		
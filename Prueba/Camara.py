import pygame
from Estrella import Estrella
from Nave import Nave
from Enemigo import Enemigo
from Planeta import Planeta
from Pantalla import Pantalla
from Agujero import Agujero
from Laser import Laser

class Camara:
	def getCentro(self):
		return self.centro
		
	def getCentroX(self):
		return self.centro[0]
		
	def getCentroY(self):
		return self.centro[1]
		
	def mover(self, pantalla, nave):
		nave.mover(pantalla)

	def imprimir(self, pantalla, lestrella, llaser, enemigo, nave):
		for i in lestrella:
			i.imprimir(pantalla, nave)
		
		# Si a alguien se le ocurre una mejor manera de comprobar que sector imprimir bienvenido sea
		if nave.supIZQ <= 25:
			for i in pantalla.listaSector[nave.supIZQ]:
				i.imprimir(pantalla, nave)
		if nave.supDER != nave.supIZQ and nave.supDER <= 25:
			for i in pantalla.listaSector[nave.supDER]:
				i.imprimir(pantalla, nave)
		if nave.infIZQ != nave.supIZQ and nave.infIZQ <= 25:
			for i in pantalla.listaSector[nave.infIZQ]:
				i.imprimir(pantalla, nave)
		if (nave.infDER != nave.infIZQ and nave.infDER != nave.supDER) and nave.infDER <= 25:
			for i in pantalla.listaSector[nave.infDER]:
				i.imprimir(pantalla, nave)
		
		pygame.draw.line(pantalla.display,pygame.Color(255,255,255,255),[0-nave.AX,0-nave.AY],[pantalla.areaMaxima-nave.AX,0-nave.AY],5)
		pygame.draw.line(pantalla.display,pygame.Color(255,255,255,255),[0-nave.AX,0-nave.AY],[0-nave.AX,pantalla.areaMaxima-nave.AY],5)
		pygame.draw.line(pantalla.display,pygame.Color(255,255,255,255),[pantalla.areaMaxima-nave.AX,0-nave.AY],[pantalla.areaMaxima-nave.AX,pantalla.areaMaxima-nave.AY],5)
		pygame.draw.line(pantalla.display,pygame.Color(255,255,255,255),[0-nave.AX,pantalla.areaMaxima-nave.AY],[pantalla.areaMaxima-nave.AX,pantalla.areaMaxima-nave.AY],5)
		
		for i in llaser:
			if i.laserLibre == False:
				i.imprimir(nave, pantalla)
				
		nave.imprimir(pantalla)
		enemigo.imprimir(nave, pantalla)
		
		pantalla.display.blit(self.fondo1, (650,0))
		pantalla.display.blit(self.fondo2, (0,475))
		
	def __init__(self):
		self.fondo1 = pygame.image.load("Recursos/1.png").convert_alpha()
		self.fondo2 = pygame.image.load("Recursos/2.png").convert_alpha()
		self.centro = (325, 237.5)
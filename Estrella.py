import pygame, random
from Pantalla import Pantalla

class Estrella:
	def __init__(self):
		self.posX = random.randint(-200,850)
		self.posY = random.randint(-200,675)
		self.colorE = pygame.Color(255,255,255,255)
		self.rectPos = pygame.Rect(self.posX, self.posY,1,1)
	def imprimir(self, camara):
		self.rectPos.x = -camara.getX()+self.posX
		self.rectPos.y = camara.getY()+self.posY
		if (self.rectPos.x >= 0 and self.rectPos.x <= 650) and (self.rectPos.y >= 0 and self.rectPos.y <= 475):
			pygame.draw.rect(camara.display,self.colorE,self.rectPos,0)
		else:
			if self.rectPos.x < -200:
				self.posX += random.randint(850,1050)
			elif self.rectPos.x > 850:
				self.posX -= random.randint(850,1050)
			if self.rectPos.y < -200:
				self.posY += random.randint(675,875)
			elif self.rectPos.y > 675:
				self.posY -= random.randint(675,875)
			self.rectPos = pygame.Rect(self.posX, self.posY,1,1)
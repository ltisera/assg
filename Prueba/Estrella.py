import pygame, random

class Estrella:
	def __init__(self):
		self.posX = random.randint(-2000,2000)
		self.posY = random.randint(-2000,2000)
		self.colorE = pygame.Color(255,255,255,255)
		self.rectPos = pygame.Rect(self.posX, self.posY,1,1)


	def imprimir(self, camara):
		self.rectPos.x = -camara.X+self.posX
		self.rectPos.y = camara.Y+self.posY
		if (self.rectPos.x >= -100 and self.rectPos.x <= 900) and (self.rectPos.y >= -100 and self.rectPos.y <= 700):
			pygame.draw.rect(camara.display,self.colorE,self.rectPos,0)
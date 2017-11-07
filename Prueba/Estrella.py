import pygame, random
from Pantalla import Pantalla

class Estrella:
	def __init__(self):
		self.posX = random.randint(-200,1000)
		self.posY = random.randint(-200,800)
		self.colorE = pygame.Color(255,255,255,255)
		self.rectPos = pygame.Rect(self.posX, self.posY,1,1)
		
	def imprimir(self, pantalla, nave):
		self.rectPos.x = -nave.getAX()+self.posX
		self.rectPos.y = -nave.getAY()+self.posY
		if (self.rectPos.x >= 0 and self.rectPos.x <= 800) and (self.rectPos.y >= 0 and self.rectPos.y <= 600):
			pygame.draw.rect(pantalla.display,self.colorE,self.rectPos,0)
		else:
			if self.rectPos.x < -200:
				self.posX += random.randint(1000,1200)
			elif self.rectPos.x > 1000:
				self.posX -= random.randint(1000,1200)
			if self.rectPos.y < -200:
				self.posY += random.randint(800,1000)
			elif self.rectPos.y > 800:
				self.posY -= random.randint(800,1000)
			self.rectPos = pygame.Rect(self.posX, self.posY,1,1)
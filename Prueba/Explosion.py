"""
Medidas del sprite de prueba 480 * 288
matriz de 5 * 3
-----------  Tamaño de la imagen 96 * 96
|A|B|C|D|E|  medidas de A en teoria (0,0) (96,96)  
-----------
| | | | | |  
-----------
| | | | | |  
-----------
01234
56789
01214
"""

import pygame

class Explosion(pygame.sprite.Sprite):


	def imprimir(self, pantalla, RX, RY):
		
		if(self.current_frame < self.frames):
			self.current_frame += 1
		else:
			self.current_frame = 0
		self.retraso = 2
	
		ncolumna = 0
		nfila = 0
		for i in range(self.current_frame):
			if (ncolumna < self.columnas ):
				ncolumna += 1

			else:
				ncolumna = 0
				nfila += 1

		x0 = ncolumna * self.frame_width
		y0 = nfila * self.frame_heigth 
		x1 = self.frame_width
		y1 = self.frame_heigth 
		#print("Columna: " + str(ncolumna) + " Fila: " + str(nfila) )
		ractual = (x0, y0, x1, y1)
		#print(self.image.get_rect())
		pantalla.display.blit(self.image.subsurface(ractual), (RX-7,RY-19))
		#print("X= " + str(RX) + " Y= "+ str(RY))
		return self.current_frame

	def __init__(self, directorio):
		super().__init__()
		self.directorio = directorio
		self.image = pygame.image.load(directorio) 
		self.rect = self.image.get_rect()
		self.current_frame = 0
		self.frame_heigth = 64
		self.frame_width = 64
		self.filas = 5 - 1
		self.columnas = 5 - 1
		self.retraso = 5
		self.frames = self.filas * self.columnas - 1
        

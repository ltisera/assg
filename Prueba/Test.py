import pygame
from time import clock
from pygame.locals import * 

pygame.init()

screen = pygame.display.set_mode((800,600))
en_ejecucion = True

dpixel = pygame.image.load("Recursos/chico.png")

while en_ejecucion:
	for event in pygame.event.get():
		if event.type == QUIT:
			en_ejecucion = False
		if event.type == MOUSEBUTTONDOWN:
			
			screen.set_at(event.pos, (255,255,255))
	screen.blit(dpixel, (0,0))
			
	t_inicial = clock()
	screen.set_at((200,200),(255,255,255))
	print("punto: ", clock()- t_inicial) 
	
	t_inicial = clock()
	
	pygame.draw.rect(screen,(255,255,255),(200,100,1,1),0)
	print("cuadrado: ", clock()- t_inicial) 
	
	
	pygame.display.update()

pygame.quit()

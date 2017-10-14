import pygame

def creditos(pantalla):
	fondoc = pygame.image.load("Recursos/Menu/fondocreditos.jpg")
	pause = True
	while pause:
		for evento in pygame.event.get():
			if evento.type == pygame.KEYDOWN:
				if evento.key == pygame.K_RETURN:
					pause = False

		pantalla.blit(fondoc,(0,0))
		pygame.display.update()

def main():
    ancho = 800
    alto = 600
    navex = 285
    navey = 325
  
    pygame.init()
    pantalla = pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("NAVE")
    
    nave = pygame.image.load("Recursos/Menu/nave.png")
    fondo = pygame.image.load("Recursos/Menu/fondonombre.jpg")
    boton = [pygame.image.load("Recursos/Menu/botonjugar.png"), pygame.image.load("Recursos/Menu/botoncreditos.png"), pygame.image.load("Recursos/Menu/salir.png")]
    
    salir = False
    while not salir:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if navey == 325:
                        pass
                    else:
                        navey -= 70            
                elif event.key == pygame.K_DOWN:
                    if navey == 465:
                        pass
                    else:
                        navey += 70
                elif event.key == pygame.K_RETURN:
                    if navey == 325:
                    	salir = True
                    	import Game
                    if navey == 395:
                    	creditos(pantalla)
                    if navey == 465:
                        salir = True
        
        pantalla.blit(fondo,(0,0))
        pantalla.blit(boton[0],(ancho/2-118, 320))
        pantalla.blit(boton[1],(ancho/2-118, 390))
        pantalla.blit(boton[2],(ancho/2-118, 460))
        
        pantalla.blit(nave,(navex,navey))
        pygame.display.update()
    
main()
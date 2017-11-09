import pygame

def pausa(pantalla):
	pygame.mixer.music.pause()
	fondoPausa = pygame.image.load("Recursos/Menu/fondopausa.jpg")
	pause = True
	while pause:
		for evento in pygame.event.get():
			if evento.type == pygame.KEYDOWN:
				if evento.key == pygame.K_RETURN:
					pause = False
		pantalla.display.blit(fondoPausa,(0,0))
		pygame.display.update()

def creditos(pantalla):
	fondoc = pygame.image.load("Recursos/Menu/fondocreditos.jpg")
	pause = True
	while pause:
		for evento in pygame.event.get():
			if evento.type == pygame.KEYDOWN:
				if evento.key == pygame.K_RETURN:
					pause = False

		pantalla.display.blit(fondoc,(0,0))
		pygame.display.update()

def ganaste(pantalla):
	#Implementar menu o algo que diga ganaste
	creditos()

def gameOver():
	#Implementar continuar o volver a menu
	#Si coninua devolver False
	#Si NO continua mostrar creditos y devolver True
	return
	
def main(pantalla):
    ancho = 800
    alto = 600
    navex = 285
    navey = 325

    intro = False
    reset = False
    
    nave = pygame.image.load("Recursos/Menu/nave.png")
    fondo = pygame.image.load("Recursos/Menu/fondonombre.jpg")
    boton = [pygame.image.load("Recursos/Menu/botonjugar.png"), pygame.image.load("Recursos/Menu/botoncreditos.png"), pygame.image.load("Recursos/Menu/salir.png")]
    
    salir = False
    while not salir:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True
                intro = False
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
                    if navey == 325: #Juego
                    	salir = True
                    	reset = True
                    	intro = True
                    if navey == 395: #Creditos
                    	creditos(pantalla)
                    if navey == 465: #Salir del Juego
                    	intro = False
                    	salir = True                    	
                        
        pantalla.display.blit(fondo,(0,0))
        pantalla.display.blit(boton[0],(ancho/2-118, 320))
        pantalla.display.blit(boton[1],(ancho/2-118, 390))
        pantalla.display.blit(boton[2],(ancho/2-118, 460))
        
        pantalla.display.blit(nave,(navex,navey))
        pygame.display.update()
        
    return (intro, reset)
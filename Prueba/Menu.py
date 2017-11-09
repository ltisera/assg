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

def mostrarPuntos(pantalla, puntos):
	COLOR_TEXTO = (0,255,0)
	fuente = pygame.font.Font("Recursos/arial.ttf", 48)
	puntajeFinal = fuente.render("PUNTAJE FINAL: " + str(int(puntos)), True, COLOR_TEXTO)
	pantalla.display.blit(puntajeFinal, (50,300))

def pantallaFinal(pantalla, puntos, mensaje, posicionDeMensaje):
	fondoFinal = pygame.image.load("Recursos/Menu/fondoFinal.jpg")
	COLOR_TEXTO = (0,255,0)
	fuente = pygame.font.Font("Recursos/arial.ttf", 48)
	fuente2 = pygame.font.Font("Recursos/arial.ttf", 20)
	textoFinal = fuente.render(mensaje, True, COLOR_TEXTO)
	textoContinuar = fuente2.render("Presione la tecla ENTER...", True, COLOR_TEXTO)
	continuar = False
	while not continuar:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					continuar = True
		pantalla.display.blit(fondoFinal,(0,0))
		pantalla.display.blit(textoFinal, (posicionDeMensaje,50))
		pantalla.display.blit(textoContinuar, (50,500))
		mostrarPuntos(pantalla, puntos)
		pygame.display.update()
	creditos(pantalla)

def ganaste(pantalla, puntos):
	pantallaFinal(pantalla, puntos, "¡GANASTE!", 250)

def gameOver(pantalla, puntos):
	pantallaFinal(pantalla, puntos, "¡GAME OVER!", 200)
	
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
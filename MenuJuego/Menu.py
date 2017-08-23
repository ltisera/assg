import pygame

def main():
    ancho = 800
    alto = 600
    navex = 285
    navey = 255
    
    reloj = pygame.time.Clock()
    
    pygame.init()
    pantalla = pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("NAVE")
    
    pygame.mixer.music.load("Music.mp3")
    navesond = pygame.mixer.Sound("nave.wav")
    
    nave = pygame.image.load("nave.png")
    fondo = pygame.image.load("fondonombre.jpg")
    boton = [pygame.image.load("botonjugar.png"), pygame.image.load("botonopciones.png"), pygame.image.load("botoncreditos.png"), pygame.image.load("salir.png")]
    
    pygame.mixer.music.play(3)
    
    #volumen
    #pygame.mixer_music.set_volume(0.4) musica
    #navesond.set_volume(0.4) sonido
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if navey == 255:
                        pass
                    else:
                        navey -= 70
                        navesond.play()
                    
                elif event.key == pygame.K_DOWN:
                    if navey == 465:
                        pass
                    else:
                        navey += 70
                        navesond.play()
                elif event.key == pygame.K_RETURN:
                    if navey == 255:
                        pygame.mixer_music.set_volume(0.1)
                        import juego
                    if navey == 325:
                        print "opciones"
                    if navey == 395:
                        print "creditos"
                    if navey == 465:
                        pygame.quit()
                        quit()
                    
        
        
        pantalla.blit(fondo,(0,0))
       
        reloj.tick(20)
       
        pantalla.blit(boton[0],(ancho/2-118, 250))
        pantalla.blit(boton[1],(ancho/2-118, 320))
        pantalla.blit(boton[2],(ancho/2-118, 390))
        pantalla.blit(boton[3],(ancho/2-118, 460))
        
        pantalla.blit(nave,(navex,navey))
        pygame.display.update()
    
main()
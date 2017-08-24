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
    
    nave = pygame.image.load("nave.png")
    fondo = pygame.image.load("fondonombre.jpg")
    boton = [pygame.image.load("botonjugar.png"), pygame.image.load("botonopciones.png"), pygame.image.load("botoncreditos.png"), pygame.image.load("salir.png")]
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if navey == 255:
                        pass
                    else:
                        navey -= 70                    
                elif event.key == pygame.K_DOWN:
                    if navey == 465:
                        pass
                    else:
                        navey += 70
                elif event.key == pygame.K_RETURN:
                    if navey == 255:
                        import juego
                    if navey == 325:
                        print ("opciones")
                    if navey == 395:
                        print ("creditos")
                    if navey == 465:
                        pygame.quit()
        
        pantalla.blit(fondo,(0,0))
       
        reloj.tick(20)
       
        pantalla.blit(boton[0],(ancho/2-118, 250))
        pantalla.blit(boton[1],(ancho/2-118, 320))
        pantalla.blit(boton[2],(ancho/2-118, 390))
        pantalla.blit(boton[3],(ancho/2-118, 460))
        
        pantalla.blit(nave,(navex,navey))
        pygame.display.update()
    
main()
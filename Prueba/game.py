import pygame, sys, math

pygame.init()

pantalla = pygame.display.set_mode((800,600))
pygame.display.set_caption("Holis")

nave = pygame.image.load("Chico.png")
nave = pygame.transform.rotate(nave, 270)
planeta1 = pygame.image.load("Planeta.png")
planeta12 = pygame.image.load("Planeta2.png")
fondo1 = pygame.image.load("1.png")
fondo2 = pygame.image.load("2.png")
moverX = 0
moverY = 0
X = 0
Y = 0
intro = True
aceleracion = 1
velocidad = 2
angulo = 0
clock = pygame.time.Clock()
tiempo = 0

while intro:

	pantalla.fill((255,255,255))
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
	
		
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_w:
				angulo += 10
			if event.key == pygame.K_s:
				angulo -= 10
			if event.key == pygame.K_m:
				velocidad += 0.5
			if event.key == pygame.K_n:
				velocidad -= 0.25	
			if angulo >= 360:
				angulo -= 360
			elif angulo < 0:
				angulo += 360	
			moverY = math.sin(math.radians(angulo))*velocidad
			moverX = math.cos(math.radians(angulo))*velocidad
			print("Y:", moverY)
			print("X:", moverX)
			print("Angulo:", angulo)
		
	
	"""	
		if event.type == pygame.KEYDOWN:
			tiempo = 0
			if event.key == pygame.K_LEFT:
				velocidad += aceleracion * tiempo 
				moverX += velocidad
			elif event.key == pygame.K_RIGHT:
				velocidad += aceleracion * tiempo 
				moverX -= velocidad
			elif event.key == pygame.K_UP:
				velocidad += aceleracion * tiempo 
				moverY += velocidad
			elif event.key == pygame.K_DOWN:
				velocidad += aceleracion * tiempo 
				moverY -= velocidad
		if event.type == pygame.KEYUP:
			tiempo = 0
			if event.key == pygame.K_LEFT:
				velocidad -= aceleracion * tiempo 
				moverX = velocidad
			elif event.key == pygame.K_RIGHT:
				velocidad -= aceleracion * tiempo 
				moverX = -velocidad
			elif event.key == pygame.K_UP:
				velocidad -= aceleracion * tiempo 
				moverY = velocidad
			elif event.key == pygame.K_DOWN:
				velocidad -= aceleracion * tiempo 
				moverY = -velocidad
	"""
			
	X += moverX
	Y += moverY
	
	pantalla.blit(planeta1, (-X+10,Y+10))
	pantalla.blit(planeta12, (-X+300,Y+350))
	pantalla.blit(planeta12, (-X-500,Y+100))
	pantalla.blit(pygame.transform.rotate(nave, angulo), (225,300))
	pantalla.blit(fondo1, (700,0))
	pantalla.blit(fondo1, (650,0))
	pantalla.blit(fondo2, (0,475))
	pygame.display.update()
	clock.tick(30)
	#print(clock)
	tiempo += 1

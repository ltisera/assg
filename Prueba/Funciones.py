import math
import pygame
import random
import Planeta
<<<<<<< HEAD
=======
import Agujero
>>>>>>> Test-coordenadas

def distancia(X1, X2, Y1, Y2):
	return math.sqrt(math.pow((X1-X2),2)+math.pow((Y1-Y2),2))

def rotarCentro(image, angle):
	orig_rect = image.get_rect()
	rot_image = pygame.transform.rotate(image, angle)
	rot_rect = orig_rect.copy()
	rot_rect.center = rot_image.get_rect().center
	rot_image = rot_image.subsurface(rot_rect).copy()
	return rot_image

def sumarAngulo(angulo, anguloSumar):
	angulo += anguloSumar
	if angulo >= 360:
		angulo -= 360
	elif angulo < 0:
		angulo += 360
	return angulo
	
<<<<<<< HEAD
def lugarLibre(objeto, lobjeto, DISTANCIA_MINIMA):
	libre = True
	for i in lobjeto:
		if (distancia(objeto.getCentroX(), i.getCentroX(), objeto.getCentroY(), i.getCentroY()) <= DISTANCIA_MINIMA):
=======
def posicionValida(x,minX,maxX,y,minY,maxY):
		return ((x >= minX and x <= maxX) and (y >= minY and y <= maxY))
	
def lugarLibre(objeto, lobjeto, DISTANCIA_MINIMA):
	libre = True
	for i in lobjeto:
		if (distancia(objeto.getACentroX(), i.getACentroX(), objeto.getACentroY(), i.getACentroY()) <= DISTANCIA_MINIMA):
>>>>>>> Test-coordenadas
			libre = False
	return libre
		
			
<<<<<<< HEAD
def colision(objeto, camara, nave):
	if (type(objeto) is Planeta.Planeta):
		if (distancia(objeto.getCentroX(), camara.X+camara.getCentroX(), objeto.getCentroY(), camara.Y+camara.getCentroY()) <= (objeto.imagen.get_width()/2)+10):
			print("Aterrizaje forzoso")
=======
def colision(objeto, nave):
	if (type(objeto) is Planeta.Planeta):
		if (distancia(objeto.getRCentroX(), nave.getRCentroX(), objeto.getRCentroY(), nave.getRCentroY()) <= (objeto.imagen.get_width()/2)+10):
			nave.boom()
	if (type(objeto) is Agujero.Agujero):
		#if (distancia(objeto.getRCentroX(), nave.getRCentroX(), objeto.getRCentroY(), nave.getRCentroY()) <= (objeto.imagen.get_width()*1.5)+10):
			#Hacer que la nave se vaya acercando al centro del agujero
		if (distancia(objeto.getRCentroX(), nave.getRCentroX(), objeto.getRCentroY(), nave.getRCentroY()) <= (objeto.imagen.get_width()/4)+10):
>>>>>>> Test-coordenadas
			nave.boom()
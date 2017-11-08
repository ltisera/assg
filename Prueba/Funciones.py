import math
import pygame
import random
import Planeta
import Agujero
import Nave
import Enemigo
import Laser

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

def calcularAnguloEntrePuntos(XO, YO, X, Y):
	return math.atan2(-Y+YO,X-OX)*(180*math.pi)

"""
posicionValida(x, minX, maxX, y, minY, maxY):
	True si Xe Y se encuentran dentro del rango min - max
"""
def posicionValida(x,minX,maxX,y,minY,maxY):
		return ((x >= minX and x <= maxX) and (y >= minY and y <= maxY))
	
def lugarLibre(objeto, lobjeto, DISTANCIA_MINIMA):
	libre = True
	for i in lobjeto:
		if (distancia(objeto.getACentroX(), i.getACentroX(), objeto.getACentroY(), i.getACentroY()) <= DISTANCIA_MINIMA):
			libre = False
	return libre
		
			
def colisonVieja(objeto1, objeto2):
	
	if(isinstance(objeto1, Planeta.Planeta) and type(objeto2) is Nave.Nave):
		if (distancia(objeto1.getRCentroX(), objeto2.getRCentroX(), objeto1.getRCentroY(), objeto2.getRCentroY()) <= (objeto1.imagen.get_width()/2)+10):
			objeto2.boom()
	
	if (type(objeto1) is Agujero.Agujero and type(objeto2) is Nave.Nave):
		#if (distancia(objeto1.getRCentroX(), objeto2.getRCentroX(), objeto1.getRCentroY(), objeto2.getRCentroY()) <= (objeto1.imagen.get_width()*1.5)+10):
			#Hacer que la objeto2 se vaya acercando al centro del agujero
		if (distancia(objeto1.getRCentroX(), objeto2.getRCentroX(), objeto1.getRCentroY(), objeto2.getRCentroY()) <= (objeto1.imagen.get_width()/4)+10):
			objeto2.boom()

	if(type(objeto1) is Enemigo.Enemigo and type(objeto2) is Nave.Nave):
		if (distancia(objeto1.getRCentroX(), objeto2.getRCentroX(), objeto1.getRCentroY(), objeto2.getRCentroY()) <= (objeto1.imagen.get_width()/2)):
			objeto2.boom()

	if(type(objeto1) is Enemigo.Enemigo and type(objeto2) is Planeta.Planeta):
		if (distancia(objeto1.getRCentroX(), objeto2.getRCentroX(), objeto1.getRCentroY(), objeto2.getRCentroY()) <= (objeto1.imagen.get_width()/2)):
			objeto1.boom()
			print("Camila mala")

	if((isinstance(objeto1, Laser.Laser) and isinstance(objeto2, Planeta.Planeta)) 
		or (isinstance(objeto1, Planeta.Planeta) and isinstance(objeto2, Laser.Laser))):
		if (distancia(objeto1.getRCentroX(), objeto2.getRX(),objeto1.getRCentroY(), objeto2.getRY()) <= (objeto1.getWidth()/2)):
			if (isinstance(objeto2, Laser.Laser)):
				objeto2.setLibre(True)
			else:
				objeto1.setLibre(True)
"""
	if  ((isinstance(objeto1, Laser.Laser) and isinstance(objeto2, Enemigo.Enemigo)) 
		or (isinstance(objeto1, Enemigo.Enemigo) and isinstance(objeto2, Laser.Laser))):
		if (distancia(objeto1.getRCentroX(), objeto2.getRX(),objeto1.getRCentroY(), objeto2.getRY()) <= (objeto1.imagen.get_width()/2)):
			objeto2.setLibre(True)
"""
""" Esta es la nueva Colision que hay que usar
"""
def hayColision (objeto1, objeto2):
	#deberiamos testear si son objetos validos
	if (distancia(objeto1.getRCentroX(), objeto2.getRX() ,objeto1.getRCentroY(), objeto2.getRY()) <= (objeto1.imagen.get_width()/2)):
		return True
	return False
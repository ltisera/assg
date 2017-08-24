import math
import pygame
import random

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
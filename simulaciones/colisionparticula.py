#Esta es la simulacion de fisica, esta tiene que ver con la colision o comportamiento de varias particulas o pelotas colisionando elasticamente dentro de una caja
#esta es la primer version
import random 
#creacion de particulas

#suposiciones de la simulacion: conjunto de particulas que chocan elasticamente, con una aceleracion igual a 0 es decir velocidad constante 

#creamos una clase llamada particula que contendra los elementos necesarios para la simulacion
class Particula:
    def __init__(self):
        self.color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.pos_ini=[random.randint(0,800),random.randint(0,600)]
        self.velocidad_x=random.randint(0,10)/5
        self.velocidad_y=2-self.velocidad_x
        self.masa=random.randint(1,10)
     #este funcion que tiene cada particula nos ayudara a poder comprobar si una particula choca contra las paredes de la caja
    def colision_pared(self,tamano_x_ventana,tamano_y_ventana):
        #aqui compruebaremos si la particula choca con la pare derecha o izquierda de la pantalla
        if((self.pos_ini[0]+self.velocidad_x)<=self.masa or (self.pos_ini[0]+self.velocidad_x)>=tamano_x_ventana-self.masa):
            #si la particula choca con lo antes mencionado de la pantalla entonces 
            self.velocidad_x*=-1#cambia la direccion de el vector velocidad en la coordenada x en el signo 
            self.pos_ini[0]+=self.velocidad_x#sigue su movimiento la particula
        else:#si la particula no choca entonces
            self.pos_ini[0]+=self.velocidad_x#solo sigue su movimiento la particula
        #al igual que el if anterior este sirve para comprobar si la particula choca con las paredes, pero en este caso es la pared inferior y superior
        if((self.pos_ini[1]+self.velocidad_y)<=self.masa or (self.pos_ini[1]+self.velocidad_y)>=tamano_y_ventana-self.masa):
            self.velocidad_y*=-1
            self.pos_ini[1]+=self.velocidad_y
        else:
            self.pos_ini[1]+=self.velocidad_y
#pasamos a pygame

import pygame #importando el modulo de pygame para poder hacer la simulacion 
from pygame.locals import *

pygame.init()#inicializamos pygame
white = (0,0,0)#fondo de la ventana
particula1=Particula()#inicializamos la particula

#definimos el tamano de la pantalla
tamano_x_ventana=800
tamano_y_ventana=600

#definimos la pantalla que usameros
Display=pygame.display.set_mode((tamano_x_ventana,tamano_y_ventana))
pygame.display.update()
gameExit=False

clock=pygame.time.Clock()


while not gameExit:
    clock.tick(9000)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit=True
         #llamamos a la funcion que verifica si la particula choca contra las paredes de la caja    
        particula1.colision_pared(tamano_x_ventana,tamano_y_ventana)
        
    #fondo de la ventana
    Display.fill(white)

    #diibujamos la ventana
    pygame.draw.circle(Display,particula1.color,particula1.pos_ini,particula1.masa)
    #actualizamos 
    pygame.display.update()

pygame.quit()
quit()
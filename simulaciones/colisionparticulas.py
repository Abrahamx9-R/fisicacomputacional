#Esta es la simulacion de el choque elastico de n particulas dentro de una caja en 2 dimensiones , aun tiene algunos problemas, 
# por la cantidad de pixels que avanza cada vez que se ejecuta, falta corregir eso, pero esta es la vercion 1
#ademas de que en algunos casos las particulas se generan unas dentro de otras, por lo que al final estas se comportan como una sola,
#esto mismo pasa cuando se generan en la pared con una parte fuera de la pared, estas particulas se conportan como si estuvieran unidas a la pared

import random 

#suposiciones de la simulacion: conjunto de particulas que chocan elasticamente, con una aceleracion igual a 0 es decir velocidad constante 

#crearemos una clase llamada particula donde definiremos todas las propiedades necesarias para poder simular el choque entre particulas elastico 

class Particula:
    def __init__(self):#cada uno de los valores que debe tener una particula se generan aleatoriamente, y estas siempre son numeros enteros,
        #el valor de la velocidad de y sera dependiente de la velocidad de x esto solo es para poder apreciar mejor las particulas en movimiento
        #pero se puede cambiar por un valor aleatoria sin dependecia con la velocidad en x
        self.color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.pos_ini=[random.randint(0,800),random.randint(0,600)]
        self.velocidad_x=random.randint(0,10)/5
        self.velocidad_y=2-self.velocidad_x#o se puede cambiar por un valor random como todos los demas
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
    #esta funcion que tiene cada particula nos ayudara a poder poner en la ventana  cada particula
    def draw(self):
        pygame.draw.circle(Display,self.color,self.pos_ini,self.masa)

#pasamos a pygame

import pygame #importando el modulo de pygame para poder hacer la simulacion 
from pygame.locals import *

pygame.init()#inicializamos pygame
black = (0,0,0)#definimos el color de fondo de la pantalla

#cracion de particulas
num_particulas=200#definimos la cantidad de particulas
particulas=[Particula() for i in range(num_particulas)]#creamos una lista que contiene todas las particulas

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
        #la siguiente parte del codigo nos ayudara a comprobar si alguna particula colisona con otra, esta forma no es muy eficiente pero es lo mas rapido que se me ocurrio
        #si quieren saber mas metodos para poder hacer esta parte del codigo mas eficiente pueden ver el siguiente video
        # https://www.youtube.com/watch?v=eED4bSkYCB8
        for i in range(num_particulas-1):
            for j in range(i+1,num_particulas):
                #vemos que la distancia entre las dos particulas sea menor o igual a la suma de sus radios, para esto usamos una metrica euclidiana
                if pow(pow(particulas[i].pos_ini[0]-particulas[j].pos_ini[0],2)+pow(particulas[i].pos_ini[1]-particulas[j].pos_ini[1],2),0.5)<=(particulas[j].masa+particulas[j].masa)/2:
                    #para las ecuaciones de velocidad final se necesitan de las velocidades iniciales
                    v_ini_1_x=particulas[i].velocidad_x
                    v_ini_1_y=particulas[i].velocidad_y
                    v_ini_2_x=particulas[j].velocidad_x
                    v_ini_2_y=particulas[j].velocidad_y
                    #calculamos las velocidades finales con las ecuaciones ya conocidas 
                    particulas[i].velocidad_x=(v_ini_1_x*(particulas[i].masa-particulas[j].masa)+2*v_ini_2_x*particulas[j].masa)/(particulas[i].masa+particulas[j].masa)
                    particulas[i].velocidad_y=(v_ini_1_y*(particulas[i].masa-particulas[j].masa)+2*v_ini_2_y*particulas[j].masa)/(particulas[i].masa+particulas[j].masa)
                    particulas[j].velocidad_x=(v_ini_2_x*(particulas[j].masa-particulas[i].masa)+2*v_ini_1_x*particulas[i].masa)/(particulas[i].masa+particulas[j].masa)
                    particulas[j].velocidad_y=(v_ini_2_y*(particulas[j].masa-particulas[i].masa)+2*v_ini_1_y*particulas[i].masa)/(particulas[i].masa+particulas[j].masa)
        #esta parte es para hacer llamar a la funcion que comprobaba si una particula chocaba con la pared        
        for i in particulas:  
            i.colision_pared(tamano_x_ventana,tamano_y_ventana)      
    
    #fondo negro de la pantalla
    Display.fill(black)       
    #insertamos o dibujamos las particulas en la pantalla
    for i in particulas:
        i.draw()       
    
    #actualizamos la pantalla
    pygame.display.update()

pygame.quit()
quit()
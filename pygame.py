import pygame
import sys
import random

def actualizar():
    pygame.display.flip()
#Para ahorrar espacio y confusion

def fueradepantalla(a):
    if a >= 500:
        a -= 50
    if a <= -50:    
        a += 50
#Los ejes van de 0 a 500, recuerda eso

    return a

ANCHO_VENTANA = 500
ALTO_VENTANA = 500
#Lo dice el nombre

TABLERO = [
[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0],
[0,0,2,2,2,2,2,2,0,0,0,1,1,1,1,1,1,1,0,0],
[1,1,2,0,0,0,0,2,0,0,0,1,1,1,1,1,1,1,0,0],
[1,1,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,0,0],
[1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0],
[0,0,0,0,0,0,0,1,1,1,0,1,1,1,1,1,1,2,2,0],
[0,2,2,2,2,2,2,2,1,1,0,0,1,1,1,1,1,0,2,0],
[0,2,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,2,0],
[0,2,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,0],
[0,2,0,0,0,0,0,0,2,0,2,0,0,2,0,0,0,0,0,0],
[0,2,2,2,2,2,2,2,2,0,2,0,0,2,0,1,1,1,1,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,1,1,1,1,1],
[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,1],
[2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0],
[2,0,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0],
[2,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
[2,0,1,1,1,0,0,1,2,0,2,2,2,0,1,1,1,1,1,0],
[0,0,0,0,0,0,0,0,2,0,2,0,2,0,1,1,1,1,1,0],
[0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0]
]




def main ():
    
    pygame.init()
    #Inicio pygame

    ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Tutorial")
    ventana.fill((82,20,120))
    #Todo lo relacionado a /ventana/

    xRectangulo = 400
    yRectangulo = 200
    #Posicion Inicial de /rectangulo/

    rectangulo = pygame.draw.rect(ventana,(255,255,255), pygame.Rect(xRectangulo, yRectangulo, 50,50))
    #Define al /rectangulo/

    xEnemigo = ANCHO_VENTANA / 2
    yEnemigo = ALTO_VENTANA / 2

    rectangulo = pygame.draw.rect(ventana,(255,0,0), pygame.Rect(xEnemigo, yEnemigo, 50,50))

    actualizar()

    reloj = pygame.time.Clock()
    #FPS
    contadorMovimiento = 0
    #Va a decirle al enemigo cuando puede moverse

    while True:

        reloj.tick(60)

        ventana.fill((82,20,120))

        rectangulo = pygame.draw.rect(ventana,(255,255,255), pygame.Rect(xRectangulo, yRectangulo, 50,50))
        rectangulo = pygame.draw.rect(ventana,(255,0,0), pygame.Rect(xEnemigo, yEnemigo, 50,50))

        contadorMovimiento += 1

        if contadorMovimiento == 25:
            contadorMovimiento = 0
            if random.uniform(0,1) <= 0.6:
                #Horizontalmente

                if random.uniform(0,1) <= 0.6:
                    #Derecha
                    xEnemigo += 50
                    xEnemigo = fueradepantalla(xEnemigo)
                
                else:
                    #Izquierda
                    xEnemigo -= 50
                    xEnemigo = fueradepantalla(xEnemigo)

            else:
                #Verticalmente

                if random.uniform(0,1) <= 0.6:
                    #Arriba
                    yEnemigo -= 50
                    yEnemigo = fueradepantalla(yEnemigo)

                else:
                    #Abajo
                    yEnemigo += 50
                    yEnemigo = fueradepantalla(yEnemigo)

        for event in pygame.event.get():

            if (event.type == pygame.QUIT):
                sys.exit()
            #Para cerrar ventana
            
            if (event.type == pygame.KEYDOWN):
                tecla_presionada = pygame.key.name(event.key)

                if tecla_presionada == "w":
                    yRectangulo -= 50
                    yRectangulo = fueradepantalla(yRectangulo)
                
                if tecla_presionada == "a":
                    xRectangulo -= 50
                    xRectangulo = fueradepantalla(xRectangulo)

                if tecla_presionada == "s":
                    yRectangulo += 50
                    yRectangulo = fueradepantalla(yRectangulo)

                if tecla_presionada == "d":
                    xRectangulo += 50
                    xRectangulo = fueradepantalla(xRectangulo)

            #Para mover mi rectangulo
            

        actualizar()
        

main()

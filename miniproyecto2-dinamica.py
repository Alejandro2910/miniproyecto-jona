import matplotlib
import math
import numpy

masa_persona = 0
materiales = 0
masa_silla = 0
duracion_movimiento = 0
lp = 0.65
w2 = 0.0
#Probar módulo para reducir longitud
longitud_eslabones = numpy.array([1.14, 1.28, 1.14, 1.28])
masa_eslabones = numpy.zeros((1, 4))
peso_eslabones = numpy.zeros((1, 4))
momento_inercia_eslabones = numpy.zeros((1, 4))
#Por definir
ancho = 0
espesor = 0

def solicitud_datos_entrada():
    global masa_persona, materiales, masa_silla, duracion_movimiento
    entrada = 121.0
    while entrada > 120.0:
        entrada = input("Favor ingresar la masa de la persona, debe ser menor a 120kg")
        if entrada <= 120.0:
            #Caych float error
            masa_persona = float(entrada)
        else:
            print("El valor está fuera de los límites, favor ingresarlo de nuevo.")

    entrada = 0
    #Revisar materiales
    materiales = input("Seleccione el numero con los materiales que tendrá el mecanismo\n1. Aluminio\n2. Acero\n3. Titaneo")
    
    entrada = input("Seleccione la masa de la silla\n1. 14.5kg\n2. 17kg\n3. 24kg")

    if entrada == 1:
        masa_silla = 14.5
    elif entrada == 2:
        masa_silla = 17
    else:
        masa_silla = 24
    
    entrada = 0
    
    entrada = input("Seleccione la duracion del movimiento\n1. 70s(1 minuto y 10 segundos)\n2. 90s(1 minutos y 30 segundos)\n3. 120s(2 minutos)")
    
    if entrada == 1:
        duracion_movimiento = 70
    elif entrada == 2:
        duracion_movimiento = 90
    else:
        duracion_movimiento = 190

def calcule_w2(duracion_movimiento):
    global w2
    w2 = (2*math.pi)/duracion_movimiento

def calcule_masa_eslabones(materiales):
    global masa_eslabones
    densidad = 0
    
    if materiales == 1:
        densidad = 2700
    elif materiales == 2:
        densidad = 7850
    else:
        densidad = 4507

    for i in range(4):
        if i != 1:
            masa_eslabones[i] = densidad * ancho * espesor * longitud_eslabones[i]
        else:
            pass
            #masa_eslabones[i] = densidad * volumen

def calcule_peso_eslabones(masa_eslabones):
    global peso_eslabones
    gravedad = 9.81

    for i in range(4):
        peso_eslabones[i] = masa_eslabones[i] * gravedad

def calcule_momento_inercia(masa_eslabones, longitud_eslabones):
    global momento_inercia_eslabones

    for i in range(4):
        if i != 1:
            momento_inercia_eslabones[i] = (1/12)* masa_eslabones[i] * math.pow(longitud_eslabones[i], 2)
        else:
            pass
            #Es fija 
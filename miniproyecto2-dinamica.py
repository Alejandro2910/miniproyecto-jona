import matplotlib
import math
import numpy

masa_persona = materiales = masa_silla = duracion_movimiento = 0
lp = 0.65
alpha2 = w2 = w4 = theta2 = theta3 = theta4 = 0.0
#Probar módulo para reducir longitud
longitud_eslabones = numpy.array([1.14, 1.28, 1.14, 1.28])
masa_eslabones = numpy.zeros((1, 4))
peso_eslabones = numpy.zeros((1, 4))
momento_inercia_eslabones = numpy.zeros((1, 4))
ancho = 0.05
espesor = 0.02

def solicitud_datos_entrada():
    global masa_persona, materiales, masa_silla, duracion_movimiento
    entrada = 121.0
    while entrada > 120.0:
        entrada = input("Favor ingresar la masa de la persona, debe ser menor a 120kg")
        if entrada <= 120.0:
            #Catch float error
            masa_persona = float(entrada)
        else:
            print("El valor está fuera de los límites, favor ingresarlo de nuevo.")

    entrada = 0
    #Revisar materiales
    materiales = input("Seleccione el numero con los materiales que tendrá el mecanismo\n1. Acero inoxidable\n2. Acero A36\n3. Fibra de carbono(HEXCEL AS4C)\n4. Aleación de aluminio(5052-H38 BARRA (SS))\n5. Aleación de aliminio(5086-H32 BARRA (SS))")
    
    entrada = input("Seleccione la masa de la silla\n1. 17kg\n3. 24kg")

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
    global w2, w4
    w2 = (2*math.pi)/duracion_movimiento
    w4 = w2

def calcule_masa_eslabones(materiales):
    global masa_eslabones
    densidad = 0
    volumen = 0.01

    if materiales == 1:
        densidad = 7860
    elif materiales == 2:
        densidad = 7850
    elif materiales == 3:
        densidad = 1780
    elif materiales  == 4:
        densidad = 2680
    elif materiales == 5:
        densidad = 2660

    for i in range(4):
        if i != 1:
            masa_eslabones[i] = densidad * ancho * espesor * longitud_eslabones[i]
        else:
            pass
            masa_eslabones[i] = densidad * volumen

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
            momento_inercia_eslabones[i] = 1.24

def calcule_A(theta4, longitud_eslabones):
    return longitud_eslabones[2]*math.sin(theta4)

def calcule_B(theta3, longitud_eslabones):
    return longitud_eslabones[1]*math.sin(theta3)

def calcule_C(alpha2, w2, w3, w4, theta2, theta3, theta4, longitud_eslabones):
    return (longitud_eslabones[0]*alpha2*math.sin(theta2)) + (longitud_eslabones[0]*math.pow(w2, 2)*math.cos(theta2)) + (longitud_eslabones[1]*math.pow(w3, 2)*math.cos(theta3)) - (longitud_eslabones[2]*math.pow(w4, 2)*math.cos(theta4))

def calcule_D(theta4, longitud_eslabones):
    return longitud_eslabones[2]*math.cos(theta4)

def calcule_E(theta3, longitud_eslabones):
    return longitud_eslabones[1]*math.cos(theta3)

def calcule_F(alpha2, w2, w3, w4, theta2, theta3, theta4, longitud_eslabones):
    return (longitud_eslabones[0]*alpha2*math.cos(theta2)) - (longitud_eslabones[0]*math.pow(w2, 2)*math.sin(theta2)) - (longitud_eslabones[1]*math.pow(w3, 2)*math.sin(theta3)) + (longitud_eslabones[2]*math.pow(w4, 2)*math.sin(theta4))


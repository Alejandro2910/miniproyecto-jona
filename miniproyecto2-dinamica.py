import matplotlib
import math
import numpy as np

masa_persona = materiales = masa_silla = duracion_movimiento = 0
g = h = f = e = P = o = q = p = A = B = C = D = E = F = lg3 = rg3 = alpha2 = alpha3 = alpha4 = w2 = w3 = w4 = theta3 = 0.0
#Probar módulo para reducir longitud
longitud_eslabones = np.array([1.14, 1.28, 1.14, 1.28])
masa_eslabones = np.zeros((1, 4))
peso_eslabones = np.zeros((1, 4))
momento_inercia_eslabones = np.zeros((1, 4))
acel_cent = np.zeros((3,2), float)

ancho = 0.05
espesor = 0.02
theta2 = theta4 = 90.00
lp = 0.65
j = 0.56
i = 1.3
k = 0.1
n = 1.18

def solicitud_datos_entrada():
    global masa_persona, materiales, masa_silla, duracion_movimiento
    entrada = 121.0
    while entrada > 120.0:
        entrada = float(input("Favor ingresar la masa de la persona, debe ser menor a 120kg\nR: "))
        if entrada <= 120.0:
            masa_persona = entrada
        else:
            print("\nEl valor está fuera de los límites, favor ingresarlo de nuevo.")

    entrada = 0

    #Revisar materiales
    materiales = input("\nSeleccione el numero con los materiales que tendrá el mecanismo\n1. Acero inoxidable\n2. Acero A36\n3. Fibra de carbono(HEXCEL AS4C)\n4. Aleación de aluminio(5052-H38 BARRA (SS))\n5. Aleación de aliminio(5086-H32 BARRA (SS))\nR: ")
    
    entrada = input("\nSeleccione la masa de la silla\n1. 17kg\n2. 24kg\nR: ")

    if entrada == 1:
        masa_silla = 17
    elif entrada == 2:
        masa_silla = 24
    
    entrada = 0
    
    entrada = input("\nSeleccione la duracion del movimiento\n1. 70s(1 minuto y 10 segundos)\n2. 90s(1 minutos y 30 segundos)\n3. 120s(2 minutos)\nR: ")
    
    if entrada == 1:
        duracion_movimiento = 70
    elif entrada == 2:
        duracion_movimiento = 90
    else:
        duracion_movimiento = 190

def calcule_w2():
    global w2, w4
    w2 = (2*math.pi)/duracion_movimiento
    w4 = w2

def calcule_masa_eslabones():
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

def calcule_peso_eslabones():
    global peso_eslabones
    gravedad = 9.81

    for i in range(4):
        peso_eslabones[i] = masa_eslabones[i] * gravedad

def calcule_momento_inercia():
    global momento_inercia_eslabones

    for i in range(4):
        if i != 1:
            momento_inercia_eslabones[i] = (1/12)* masa_eslabones[i] * math.pow(longitud_eslabones[i], 2)
        else:
            pass
            momento_inercia_eslabones[i] = 1.24

def calcule_A():
    global A
    A = longitud_eslabones[2]*math.sin(math.radians(theta4))

def calcule_B():
    global B
    B = longitud_eslabones[1]*math.sin(math.radians(theta3))

def calcule_C():
    global C
    C = (longitud_eslabones[0]*alpha2*math.sin(math.radians(theta2))) + (longitud_eslabones[0]*math.pow(w2, 2)*math.cos(math.radians(theta2))) + (longitud_eslabones[1]*math.pow(w3, 2)*math.cos(math.radians(theta3))) - (longitud_eslabones[2]*math.pow(w4, 2)*math.cos(math.radians(theta4)))

def calcule_D():
    global D
    D = longitud_eslabones[2]*math.cos(math.radians(theta4))

def calcule_E():
    global E
    E = longitud_eslabones[1]*math.cos(math.radians(theta3))

def calcule_F():
    global F
    F = (longitud_eslabones[0]*alpha2*math.cos(math.radians(theta2))) - (longitud_eslabones[0]*math.pow(w2, 2)*math.sin(math.radians(theta2))) - (longitud_eslabones[1]*math.pow(w3, 2)*math.sin(math.radians(theta3))) + (longitud_eslabones[2]*math.pow(w4, 2)*math.sin(math.radians(theta4)))

def calcule_LG3():
    global lg3
    lg3 = (math.sqrt(809)/50)

def calcule_alpha3():
    global alpha3
    alpha3 = ((C*D) - (A*F))/((A*E) - (B*D))

def calcule_alpha4():
    global alpha4
    aplha4 = ((C*E) - (B*F))/((A*E) - (B*D))

def calcule_acel_cent(gamma):
    global acel_cent

    #Eslabón 2
    acel_cent[0][0] = (-math.pow(w2, 2))*(longitud_eslabones[0]/2)*math.cos(math.radians(theta2))
    acel_cent[0][1] = (-math.pow(w2, 2))*(longitud_eslabones[0]/2)*math.sin(math.radians(theta2))

    #Eslabón 3
    acel_cent[1][0] = ((-math.pow(w2, 2))*longitud_eslabones[0]*(math.cos(math.radians(theta2)))) - ((-math.pow(w3))*lg3*(math.cos(math.radians(gamma)))) - (alpha3 * lg3 * math.sin(math.radians(gamma)))
    acel_cent[1][1] = ((-math.pow(w2, 2))*longitud_eslabones[0]*(math.sin(math.radians(theta2)))) - ((-math.pow(w3))*lg3*(math.sin(math.radians(gamma)))) - (alpha3 * lg3 * math.cos(math.radians(gamma)))

    #Eslabón 4
    acel_cent[2][0] = ((-math.pow(w4, 2))*(longitud_eslabones[2] / 2)*(math.cos(math.radians(theta4)))) - (alpha4*(longitud_eslabones[2] / 2)*(math.sin(math.radians(theta4))))
    acel_cent[2][1] = ((-math.pow(w4, 2))*(longitud_eslabones[2] / 2)*(math.sin(math.radians(theta4)))) - (alpha4*(longitud_eslabones[2] / 2)*(math.cos(math.radians(theta4))))

def calcule_f(gamma):
    global f, e
    f = (longitud_eslabones[0]/2)*math.cos(math.radians(gamma))
    e = f

def calcule_g(gamma):
    global g, h
    g = (longitud_eslabones[0]/2)*math.sin(math.radians(gamma))
    g = h

def calcule_o():
    global o
    o = ((peso_eslabones[3] + (masa_eslabones[3]*acel_cent[2][0]))*f) + (masa_eslabones[3]*acel_cent[2][0]*h) - (momento_inercia_eslabones[3]*alpha4)

def calcule_p():
    global p
    p = (masa_eslabones[2]*acel_cent[1][1]*(g + h)) + (P + peso_eslabones[2] + masa_eslabones[2]*acel_cent[1][0])*(e + f)

def calcule_q():
    global q
    q = (P*rg3) - (momento_inercia_eslabones[2]*alpha3) + (masa_eslabones[2]*acel_cent[1][1]*n) + ((P+peso_eslabones[2]+(masa_eslabones[2]*acel_cent[1][0]))*j)

def calcule_PFuerza():
    global P
    P = ((masa_persona + masa_silla)/2)*9.81

def calcule_rg3():
    global rg3
    rg3 = (i / 2) - j

if __name__ == "__main__":
    global theta2, theta4

    solicitud_datos_entrada()
    calcule_w2()
    calcule_masa_eslabones()
    calcule_peso_eslabones()
    calcule_momento_inercia()

    #Descenso
    for gamma in np.arange(0.00, 38.00, 1.00):
        theta2 = theta2 + gamma
        theta4 = theta2

        calcule_A()
        calcule_B()
        calcule_C()
        calcule_D()
        calcule_E()
        calcule_F()

        calcule_alpha4()
        calcule_alpha3()

        calcule_LG3()
        calcule_acel_cent(gamma)

        calcule_f(gamma)
        calcule_g(gamma)
        calcule_o()
        calcule_PFuerza()
        calcule_p()
        calcule_rg3()
        calcule_q()

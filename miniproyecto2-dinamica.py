from matplotlib import pyplot as plt
import math
import numpy as np
from time import sleep as sl

#Inicialización de variables
masa_persona = materiales = masa_silla = duracion_movimiento = 0
g = h = f = e = P = o = q = p = A = B = C = D = E = F = lg3 = rg3 = w3 = w4 = mo = 0.00
lx = ly = mx = my = nx = ny = ox = oy = alpha2 = alpha3 = alpha4 = w2 = theta3 =  0.00
longitud_eslabones = np.array([1.14, 1.28, 1.14, 1.28])
masa_eslabones = np.array([0., 0., 0., 0.])
peso_eslabones = np.array([0., 0., 0., 0.])
momento_inercia_eslabones = np.array([0., 0., 0., 0.])
acel_cent = np.zeros((3,2), float)

delta = 79.875
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
    volumen = 0.00908
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
            if materiales == 1:
                momento_inercia_eslabones[i] = 5.4873
            elif materiales == 2:
                momento_inercia_eslabones[i] = 5.4803143
            elif materiales == 3:
                momento_inercia_eslabones[i] = 1.2426700
            elif materiales  == 4:
                momento_inercia_eslabones[i] = 1.8709863
            elif materiales == 5:
                momento_inercia_eslabones[i] = 1.8570237

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

    #Eslabón 2-a
    acel_cent[0][0] = (-math.pow(w2, 2))*(longitud_eslabones[0]/2)*math.cos(math.radians(theta2))
    acel_cent[0][1] = (-math.pow(w2, 2))*(longitud_eslabones[0]/2)*math.sin(math.radians(theta2))

    #Eslabón 3-b
    acel_cent[1][0] = ((-math.pow(w2, 2))*longitud_eslabones[0]*(math.cos(math.radians(theta2)))) - ((-math.pow(w3, 2))*lg3*(math.cos(math.radians(gamma)))) - (alpha3 * lg3 * math.sin(math.radians(delta)))
    acel_cent[1][1] = ((-math.pow(w2, 2))*longitud_eslabones[0]*(math.sin(math.radians(theta2)))) - ((-math.pow(w3, 2))*lg3*(math.sin(math.radians(gamma)))) - (alpha3 * lg3 * math.cos(math.radians(delta)))

    #Eslabón 4-c
    acel_cent[2][0] = ((-math.pow(w4, 2))*(longitud_eslabones[2] / 2)*(math.cos(math.radians(theta4)))) - (alpha4*(longitud_eslabones[2] / 2)*(math.sin(math.radians(theta4))))
    acel_cent[2][1] = ((-math.pow(w4, 2))*(longitud_eslabones[2] / 2)*(math.sin(math.radians(theta4)))) - (alpha4*(longitud_eslabones[2] / 2)*(math.cos(math.radians(theta4))))

def calcule_f(gamma):
    global f, e
    f = (longitud_eslabones[0]/2)*math.cos(math.radians(gamma))
    e = f

def calcule_g(gamma):
    global g, h
    g = (longitud_eslabones[0]/2)*math.sin(math.radians(gamma))
    h = g

def calcule_o():
    global o
    o = ((peso_eslabones[2] + (masa_eslabones[2]*acel_cent[2][0]))*f) + (masa_eslabones[2]*acel_cent[2][1]*h) - (momento_inercia_eslabones[2]*alpha4)

def calcule_p():
    global p
    p = (masa_eslabones[1]*acel_cent[1][1]*(g + h)) + (P + peso_eslabones[1] + masa_eslabones[1]*acel_cent[1][0])*(e + f)

def calcule_q():
    global q
    q = (P*rg3) - (momento_inercia_eslabones[1]*alpha3) + (masa_eslabones[1]*acel_cent[1][1]*n) + ((P+peso_eslabones[1]+(masa_eslabones[1]*acel_cent[1][0]))*j)

def calcule_PFuerza():
    global P
    P = ((masa_persona + masa_silla)/2)*9.81

def calcule_rg3():
    global rg3
    rg3 = (i / 2) - j

def calcule_L_actual():
    global lx, ly
    lx = (1 / (e + f))*(- o - p - ly * (g + h))
    ly = (-q)/(k + n)
    return math.sqrt(math.pow(lx, 2) + math.pow(ly, 2))

def calcule_M_actual():
    global mx, my
    mx = - P - lx - peso_eslabones[1] - masa_eslabones[1] * acel_cent[1][0]
    my = - ly - masa_eslabones[1] * acel_cent[1][1]
    return math.sqrt(math.pow(mx, 2) + math.pow(my, 2)) 

def calcule_N_actual():
    global nx, ny
    nx = mx - peso_eslabones[2] - masa_eslabones[2] * acel_cent[2][0]
    ny = my - masa_eslabones[2] * acel_cent[2][1]
    return math.sqrt(math.pow(nx, 2) + math.pow(ny, 2))  

def calcule_O_actual():
    global ox, oy
    ox = peso_eslabones[0] + masa_eslabones[0] * acel_cent[0][0] - lx
    oy = masa_eslabones[0]*acel_cent[0][1] - ly
    return math.sqrt(math.pow(ox, 2) + math.pow(oy, 2))

def calcule_momento_entrada_actual():
    return (lx * e) + (ly * g) - (ox * f) - (oy * h)  

def imprima_valores_actuales(gamma, theta2, L, M, N, O, M0):
    print("Para el valor actual de gamma {} y theta2 {}".format(gamma, theta2))
    print()
    """print("AC-Ax: {}".format(acel_cent[0][0]))
    print("AC-Ay: {}".format(acel_cent[0][1]))
    print("AC-Bx: {}".format(acel_cent[1][0]))
    print("AC-By: {}".format(acel_cent[1][1]))
    print("AC-Cx: {}".format(acel_cent[2][0]))
    print("AC-Cy: {}".format(acel_cent[2][1]))
    print()
    """
    print("f: {}".format(f))
    print("g: {}".format(g))
    print()
    print("o: {}".format(o))
    print("p: {}".format(p))
    print("q: {}".format(q))
    print()
    print("M0: {}".format(M0))
    print("L: {}".format(L))
    print("M: {}".format(M))
    print("N: {}".format(N))
    print("O: {}".format(O))

#Main
m0_desc = np.zeros(39)
L_desc = np.zeros(39)
M_desc = np.zeros(39)
N_desc = np.zeros(39)
O_desc = np.zeros(39)
gamma_values = np.arange(0.00, 39.00, 1.00)

solicitud_datos_entrada()
calcule_w2()
calcule_masa_eslabones()
calcule_peso_eslabones()
calcule_momento_inercia()

#Descenso
for gamma in gamma_values:
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

    m0_desc[int(gamma)] = calcule_momento_entrada_actual()
    L_desc[int(gamma)] = calcule_L_actual()
    M_desc[int(gamma)] = calcule_M_actual()
    N_desc[int(gamma)] = calcule_N_actual()
    O_desc[int(gamma)] = calcule_O_actual()
    #imprima_valores_actuales(gamma, theta2, L_desc, M_desc, N_desc, O_desc, m0_desc)
    theta2 = theta2 + 1
    theta4 = theta2

    #sl(1)

plt.plot(gamma_values, L_desc, label = 'L')
plt.plot(gamma_values, M_desc, label = 'M')
plt.plot(gamma_values, N_desc, label = 'N')
plt.plot(gamma_values, O_desc, label = 'O')
plt.plot(gamma_values, m0_desc, label = 'M0')
plt.legend()
plt.show()

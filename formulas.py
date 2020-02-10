# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import math
import numpy as np

#Inicialización de variables
masa_persona = materiales = masa_silla = duracion_movimiento = 0
g = h = f = e = P = o = q = p = A = B = C = D = E = F = lg3 = rg3 = w3 = w4 = mo = 0.00
lx = ly = mx = my = nx = ny = ox = oy = alpha2 = alpha3 = alpha4 = w2 = theta3 =  0.00
longitud_eslabones = np.array([1.14, 1.28, 1.14, 1.28])
masa_eslabones = np.array([0., 0., 0., 0.])
peso_eslabones = np.array([0., 0., 0., 0.])
momento_inercia_eslabones = np.array([0., 0., 0., 0.])
acel_cent = np.zeros((3,2), float)
m0_desc = np.zeros(39)
L_desc = np.zeros(39)
M_desc = np.zeros(39)
N_desc = np.zeros(39)
O_desc = np.zeros(39)

m0_asc = np.zeros(39)
L_asc = np.zeros(39)
M_asc = np.zeros(39)
N_asc = np.zeros(39)
O_asc = np.zeros(39)
lmno = np.zeros(5)

gamma_values_desc = np.arange(-38.00, 1.00, 1.00)
gamma_values_asc = np.arange(0.00, 39.00, 1.00)

#Constantes
delta = 79.875
ancho = 0.05
espesor = 0.02
theta2 = theta4 = 90.00
lp = 0.65
j = 0.56
i = 1.3
k = 0.1
n = 1.18

def asigne_valores(mp, ms, mas, dm):
    global duracion_movimiento, masa_silla, masa_persona, materiales
    masa_persona = mp
    materiales = ms
    masa_silla = mas
    duracion_movimiento = dm

def calcule_w2():
    global w2, w4
    w2 = (2*math.pi)/duracion_movimiento
    w4 = w2

def calcule_masa_eslabones():
    global masa_eslabones
    densidad = 0
    volumen = 0.00908
    if materiales == 1:
        densidad = 7860.0
    elif materiales == 2:
        densidad = 7850.0
    elif materiales == 3:
        densidad = 1780.0
    elif materiales  == 4:
        densidad = 2680.0
    elif materiales == 5:
        densidad = 2660.0

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
            momento_inercia_eslabones[i] = (1.0/12.0)* masa_eslabones[i] * math.pow(longitud_eslabones[i], 2)
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
    C = (longitud_eslabones[0]*alpha2*math.sin(math.radians(theta2))) + (longitud_eslabones[0]*math.pow(w2, 2.0)*math.cos(math.radians(theta2))) + (longitud_eslabones[1]*math.pow(w3, 2)*math.cos(math.radians(theta3))) - (longitud_eslabones[2]*math.pow(w4, 2.0)*math.cos(math.radians(theta4)))

def calcule_D():
    global D
    D = longitud_eslabones[2]*math.cos(math.radians(theta4))

def calcule_E():
    global E
    E = longitud_eslabones[1]*math.cos(math.radians(theta3))

def calcule_F():
    global F
    F = (longitud_eslabones[0]*alpha2*math.cos(math.radians(theta2))) - (longitud_eslabones[0]*math.pow(w2, 2.0)*math.sin(math.radians(theta2))) - (longitud_eslabones[1]*math.pow(w3, 2.0)*math.sin(math.radians(theta3))) + (longitud_eslabones[2]*math.pow(w4, 2.0)*math.sin(math.radians(theta4)))

def calcule_LG3():
    global lg3
    lg3 = (math.sqrt(809.0)/50.0)

def calcule_alpha3():
    global alpha3
    alpha3 = ((C*D) - (A*F))/((A*E) - (B*D))

def calcule_alpha4():
    global alpha4
    alpha4 = ((C*E) - (B*F))/((A*E) - (B*D))

def calcule_acel_cent(gamma):
    global acel_cent

    #Eslabón 2-a
    acel_cent[0][0] = (-math.pow(w2, 2.0))*(longitud_eslabones[0]/2.0)*math.cos(math.radians(theta2))
    acel_cent[0][1] = (-math.pow(w2, 2.0))*(longitud_eslabones[0]/2.0)*math.sin(math.radians(theta2))

    #Eslabón 3-b
    acel_cent[1][0] = ((-math.pow(w2, 2.0))*longitud_eslabones[0]*(math.cos(math.radians(theta2)))) - ((-math.pow(w3, 2.0))*lg3*(math.cos(math.radians(gamma)))) - (alpha3 * lg3 * math.sin(math.radians(delta)))
    acel_cent[1][1] = ((-math.pow(w2, 2.0))*longitud_eslabones[0]*(math.sin(math.radians(theta2)))) - ((-math.pow(w3, 2.0))*lg3*(math.sin(math.radians(gamma)))) - (alpha3 * lg3 * math.cos(math.radians(delta)))

    #Eslabón 4-c
    acel_cent[2][0] = ((-math.pow(w4, 2.0))*(longitud_eslabones[2] / 2.0)*(math.cos(math.radians(theta4)))) - (alpha4*(longitud_eslabones[2] / 2.0)*(math.sin(math.radians(theta4))))
    acel_cent[2][1] = ((-math.pow(w4, 2.0))*(longitud_eslabones[2] / 2.0)*(math.sin(math.radians(theta4)))) - (alpha4*(longitud_eslabones[2] / 2.0)*(math.cos(math.radians(theta4))))

def calcule_f(gamma):
    global f, e
    f = (longitud_eslabones[0]/2.0)*math.cos(math.radians(gamma))
    e = f

def calcule_g(gamma):
    global g, h
    g = (longitud_eslabones[0]/2.0)*math.sin(math.radians(gamma))
    h = g

def calcule_o():
    global o
    o = ((peso_eslabones[2] + (masa_eslabones[2]*acel_cent[2][0]))*f) + (masa_eslabones[2]*acel_cent[2][1]*h) - (momento_inercia_eslabones[2]*alpha4)

def calcule_p():
    global p
    p = (masa_eslabones[1]*acel_cent[1][1]*(g + h)) + (P + peso_eslabones[1] + masa_eslabones[1]*acel_cent[1][0])*(e + f)

def calcule_q():
    global q
    q = (P * rg3) - (momento_inercia_eslabones[1] * alpha3) + (masa_eslabones[1] * acel_cent[1][1] * n) + ((P + peso_eslabones[1] + (masa_eslabones[1] * acel_cent[1][0])) * j)

def calcule_PFuerza():
    global P
    P = ((masa_persona + masa_silla)/2.0)*9.81

def calcule_rg3():
    global rg3
    rg3 = (i / 2.0) - j

def calcule_L_actual():
    global lx, ly
    ly = (-q)/(k + n)
    lx = (1.0 / (e + f))*(- o - p - ly * (g + h))
    return math.sqrt(math.pow(lx, 2.0) + math.pow(ly, 2.0))

def calcule_M_actual():
    global mx, my
    mx = - P - lx - peso_eslabones[1] - masa_eslabones[1] * acel_cent[1][0]
    my = - ly - masa_eslabones[1] * acel_cent[1][1]
    return math.sqrt(math.pow(mx, 2.0) + math.pow(my, 2.0)) 

def calcule_N_actual():
    global nx, ny
    nx = mx - peso_eslabones[2] - masa_eslabones[2] * acel_cent[2][0]
    ny = my - masa_eslabones[2] * acel_cent[2][1]
    return math.sqrt(math.pow(nx, 2.0) + math.pow(ny, 2.0))  

def calcule_O_actual():
    global ox, oy
    ox = peso_eslabones[0] + masa_eslabones[0] * acel_cent[0][0] - lx
    oy = masa_eslabones[0]*acel_cent[0][1] - ly
    return math.sqrt(math.pow(ox, 2.0) + math.pow(oy, 2.0))

def calcule_momento_entrada_actual():
    return (lx * e) + (ly * g) - (ox * f) - (oy * h) 

def main():
    global m0_desc, L_desc, M_desc, N_desc, O_desc, theta2, theta4, gamma_values_desc, gamma_values_asc 
    
    calcule_w2()
    calcule_masa_eslabones()
    calcule_peso_eslabones()
    calcule_momento_inercia()
    
    #Descenso
    for gamma in range(0, 39):
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

        L_desc[int(gamma)] = calcule_L_actual()
        M_desc[int(gamma)] = calcule_M_actual()
        N_desc[int(gamma)] = calcule_N_actual()
        O_desc[int(gamma)] = calcule_O_actual()
        m0_desc[int(gamma)] = calcule_momento_entrada_actual()
        theta2 = theta2 + 1.0
        theta4 = theta2

    theta2 = 128.0
    
    #Ascenso
    for gamma in range(38, -1, -1):
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

        L_asc[38 - int(gamma)] = calcule_L_actual()
        M_asc[38 - int(gamma)] = calcule_M_actual()
        N_asc[38 - int(gamma)] = calcule_N_actual()
        O_asc[38 - int(gamma)] = calcule_O_actual()
        m0_asc[38 - int(gamma)] = calcule_momento_entrada_actual()
        theta2 = theta2 - 1.0
        theta4 = theta2
   
def graph_LMNO():
    plt.plot(gamma_values_desc, L_desc, label = 'L desc')
    plt.plot(gamma_values_desc, M_desc, label = 'M desc')
    plt.plot(gamma_values_desc, N_desc, label = 'N desc')
    plt.plot(gamma_values_desc, O_desc, label = 'O desc')

    plt.plot(gamma_values_asc, L_asc, label = 'L asc')
    plt.plot(gamma_values_asc, M_asc, label = 'M asc')
    plt.plot(gamma_values_asc, N_asc, label = 'N asc')
    plt.plot(gamma_values_asc, O_asc, label = 'O asc')

    plt.xlabel("Rango de movimiento(Grados)")
    plt.ylabel("Reacciones en los apoyos(N)")
    plt.legend()
    plt.show()

def graph_momento_entrada():
    plt.plot(gamma_values_asc, m0_asc, label = 'M0 asc')
    plt.plot(gamma_values_desc, m0_desc, label = 'M0 desc')

    plt.xlabel("Rango de movimiento(Grados)")
    plt.ylabel("Momento de entrada(Nm)")
    plt.legend()
    plt.show()

def get_point(theta):
    global lmno

    lmno[0] = L_desc[theta]
    lmno[1] = M_desc[theta]
    lmno[2] = N_desc[theta]
    lmno[3] = O_desc[theta]
    
    return lmno
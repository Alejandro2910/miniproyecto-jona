# -*- coding: utf-8 -*-
from Tkinter import *
from sys import exit
import formulas as minip
import numpy as np
import matplotlib.pyplot as plt


error = 0
materiales = {"Acero Inoxidable" : "1", 
              "Acero A36" : "2", 
              "Fibra de carbono(HEXCEL AS4C)" : "3", 
              "Aleación de aluminio(5052-H38 BARRA (SS))" : "4", 
              "Aleación de aliminio(5086-H32 BARRA (SS))" : "5"}
masa_silla = {"17kg" : 17, 
              "24kg" : 24}
duracion_movimiento = {"70s" : 70,
                       "90s" : 90,
                       "120s" : 120}


root = Tk()
root.geometry('500x450+450+150')
root.title('Miniproyecto B68011 B59181')

material_seleccionado = StringVar(root, value="1")
masa_seleccionada = IntVar(root, value=17)
duracion_movimiento_seleccionada = IntVar(root, value=70)
masa_persona = IntVar(root, value=80)
theta = IntVar(root, value=0)
lmno = np.zeros(5)

img = PhotoImage(file="C:\Users\\abena\Desktop\miniproyecto-jona\MecanismoInterfaz.gif")


#Afuera para poder cambiar el color
label1 = Label(root, text = 'Indique la masa de la persona, menor o igual a 120kg', font=('arial', 12))
l, m, n, o = 0, 0, 0, 0
opcion3 = 0

def all_children (window) :
    _list = window.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list

def check_weight():
    global masa_persona, material_seleccionado, masa_seleccionada, duracion_movimiento_seleccionada, label1, root
    try:
        mp = float(masa_persona.get())
    except Exception as ex:
        label1.config(foreground="red")
    else:
        if mp <= 120.0 and mp > 0.0:
            ms = int(material_seleccionado.get())
            mas = float(masa_seleccionada.get())
            dm = float(duracion_movimiento_seleccionada.get())

            widget_list = all_children(root)
            for item in widget_list:
                item.destroy()

            run_simulation(mp, ms, mas, dm)
        else:
            label1.config(foreground="red")
  
def request_data():
    global masa_persona, material_seleccionado, masa_seleccionada, duracion_movimiento_seleccionada, label1, root
    title = Label(root, text = 'Valores iniciales', font=('arial', 16, 'bold'))
    title.pack()

    label1.pack()

    masa = Entry(root, textvariable = masa_persona)
    masa.pack()

    label2 = Label(root, text = 'Seleccione el material del que será hecho el mecanismo', font=('arial', 12))
    label2.pack()

    for(material, valor) in materiales.items():
        Radiobutton(root, text=material,  variable=material_seleccionado, value=valor).pack()

    label3 = Label(root, text = 'Seleccione la masa de la silla', font=('arial', 12))
    label3.pack()

    for(masa, valor) in masa_silla.items():
        Radiobutton(root, text=masa, variable=masa_seleccionada , value=valor).pack()

    label4 = Label(root, text = 'Seleccione la duración del movimiento', font=('arial', 12))
    label4.pack()

    for(duracion, valor) in duracion_movimiento.items():
        Radiobutton(root, text=duracion, variable=duracion_movimiento_seleccionada, value=valor).pack()

    space = Label(root)
    space.pack()

    btn = Button(root, text="Aceptar", bg="green", command=check_weight)
    btn.pack()

def menu():
    global root, l, m, n, o, opcion3
    root.geometry('1000x520+200+120')
    
    label = Label(root, text= "Seleccione que desea hacer: ", font=('arial', 14))
    label.pack()

    photo = Label(root, image=img)
    photo.pack(side='right')

    opcion1 = Label(root, text="1. Ver la gráfica de las reacciones (en N) en los apoyos", font=('arial', 12))
    opcion1.pack()

    space = Label(root)
    space.pack()

    btn1 = Button(root, text="Reacciones", command=graph_reactions)
    btn1.pack()

    space1 = Label(root)
    space1.pack()

    opcion2 = Label(root, text="2. Ver la gráfica de los momentos de entrada (en Nm)", font=('arial', 12))
    opcion2.pack()

    space2 = Label(root)
    space2.pack()

    btn2 = Button(root, text="Entrada", command=graph_m0)
    btn2.pack()

    space3 = Label(root)
    space3.pack()

    opcion3 = Label(root, text="3. Valor puntual de las reacciones en funcion\n del rango de movimiento(0 a 38 grados)", font=('arial', 12))
    opcion3.pack()

    space4 = Label(root)
    space4.pack()

    theta_value = Entry(root, textvariable = theta)
    theta_value.pack()

    space5 = Label(root)
    space5.pack()

    l = Label(root, text="L: 0N", font=('arial', 12))
    l.pack() 

    m = Label(root, text="M: 0N", font=('arial', 12))  
    m.pack()

    n = Label(root, text="N: 0N", font=('arial', 12))
    n.pack()

    o = Label(root, text="O: 0N", font=('arial', 12))
    o.pack()
    
    space6 = Label(root)
    space6.pack()

    btn3 = Button(root, text="Calcular", command=search_point)
    btn3.pack()

    space7 = Label(root)
    space7.pack()

    salir = Button(root, text="Salir", bg="red", command=leave)
    salir.pack()

def leave():
    global root
    exit()

def run_simulation(mp, ms, mas, dm):
    minip.asigne_valores(mp, ms, mas, dm)
    minip.main()
    menu()

def graph_reactions():
    minip.graph_LMNO()

def graph_m0():
    minip.graph_momento_entrada()

def search_point():
    global theta
    try:
        tv = int(theta.get())
    except Exception as ex:
        opcion3.config(foreground="red")
    else:
        if tv <= 38 and tv >= 0:
            opcion3.config(foreground="black")
            lmno = minip.get_point(tv)

            l.config(text="L: {}N".format(lmno[0]))
            m.config(text="M: {}N".format(lmno[1]))
            n.config(text="N: {}N".format(lmno[2]))
            o.config(text="O: {}N".format(lmno[3]))

        else:
            opcion3.config(foreground="red")

request_data()
root.mainloop()
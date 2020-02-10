# -*- coding: utf-8 -*-
from Tkinter import *
from sys import exit
import formulas as minip
import numpy as np
import matplotlib.pyplot as plt

image = """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"""

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

#img = PhotoImage(file="C:\Users\\abena\Desktop\miniproyecto-jona\MecanismoInterfaz.gif")
img = PhotoImage(data=image)


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
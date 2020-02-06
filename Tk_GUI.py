# -*- coding: utf-8 -*-
from Tkinter import *
import Miniproyecto2 as minip

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

window = Tk()

material_seleccionado = StringVar(window, value="1")
masa_seleccionada = IntVar(window, value=17)
duracion_movimiento_seleccionada = IntVar(window, value=70)
masa_persona = IntVar(window, value=80)
label1 = Label(window, text = 'Indique la masa de la persona, menor o igual a 120kg', font=('arial', 12))

def check_weight():
    global masa_persona, material_seleccionado, masa_seleccionada, duracion_movimiento_seleccionada, label1, window
    try:
        mp = float(masa_persona.get())
    except Exception as ex:
        label1.config(foreground="red")
    else:
        if mp <= 120.0:
            ms = int(material_seleccionado.get())
            mas = float(masa_seleccionada.get())
            dm = float(duracion_movimiento_seleccionada.get())
            #print('Masa de la persona: {}\nMaterial seleccionado: {}\nMasa de la silla: {}\nDuracion del movimiento: {}'.format(mp, ms, mas, dm))
            widget_list = all_children(window)
            for item in widget_list:
                item.pack_forget()
            window.destroy()
            run_simulation(mp, ms, mas, dm)
        else:
            label1.config(foreground="red")
        
def all_children (window) :
    _list = window.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list        

def request_data():
    global masa_persona, material_seleccionado, masa_seleccionada, duracion_movimiento_seleccionada, label1
    window.geometry('500x450')
    window.title('Miniproyecto B68011 B59181')

    window_title_label = Label(window, text = 'Valores iniciales', font=('arial', 16, 'bold'))
    window_title_label.pack()

    #photo = PhotoImage(file="MecanismoInterfaz.png")
    #label0 = Label(window, image=photo)
    #label0.pack()

    label1.pack()

    masa = Entry(window, textvariable = masa_persona)
    masa.pack()

    label2 = Label(window, text = 'Seleccione el material del que será hecho el mecanismo', font=('arial', 12))
    label2.pack()

    for(material, valor) in materiales.items():
        Radiobutton(window, text=material,  variable=material_seleccionado, value=valor).pack()

    label3 = Label(window, text = 'Seleccione la masa de la silla', font=('arial', 12))
    label3.pack()

    for(masa, valor) in masa_silla.items():
        Radiobutton(window, text=masa, variable=masa_seleccionada , value=valor).pack()

    label4 = Label(window, text = 'Seleccione la duración del movimiento', font=('arial', 12))
    label4.pack()

    for(duracion, valor) in duracion_movimiento.items():
        Radiobutton(window, text=duracion, variable=duracion_movimiento_seleccionada, value=valor).pack()

    btn = Button(window, text="Aceptar", bg="green", command=check_weight)
    btn.pack()
    window.mainloop()

def run_simulation(mp, ms, mas, dm):
    minip.asigne_valores(mp, ms, mas, dm)
    minip.main()

request_data()
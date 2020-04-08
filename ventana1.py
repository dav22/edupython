from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def funcionPrueba():
    messagebox.showinfo(message=Asignaturas.get(), title="Asignatura Seleccionada")

ventana = Tk()

ventana.geometry('400x300')

ventana.configure(bg = '#483D8B')

ventana.title('eduPython')

btnSalir = Button(ventana, text='Salir',command=ventana.destroy).pack(side=BOTTOM)

Asignaturas = ttk.Combobox(ventana, values=["Aritmetica", "Programacion Basica","Geometria","Trigonometria","CoronaVirus"])

lbl = Label(ventana,text="Lista de Asignaturas",bg="#483D8B",fg="white",font=("Arial", 20))

btnSelec = Button(ventana,text="Seleccionar",command=funcionPrueba)

lbl.pack(side=TOP)

Asignaturas.pack()

btnSelec.pack()

Asignaturas.current(1)

ventana.mainloop()

def funcionPruebaTemas():
    messagebox.showinfo(message=Temas.get(), title="Tema Seleccionado")

ventanaDos = Tk()

ventanaDos.geometry('400x300')

ventanaDos.configure(bg = '#483D8B')

ventanaDos.title('eduPython')

btnSalir = Button(ventanaDos, text='Salir',command=ventanaDos.destroy).pack(side=BOTTOM)

Temas = ttk.Combobox(ventanaDos, values=["Sumas", "Python","Triangulos","Teorema de Pitágoras","Medidas de prevención"])

lbl = Label(ventanaDos,text="Lista de temas",bg="#483D8B",fg="white",font=("Arial", 20))

btnSelec = Button(ventanaDos,text="Seleccionar",command=funcionPruebaTemas)

lbl.pack(side=TOP)

Temas.pack()

btnSelec.pack()

Temas.current(1)

ventanaDos.mainloop()








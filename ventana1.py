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

Asignaturas = ttk.Combobox(ventana, values=["Aritmetica", "Programacion Basica","Geometria","Trigonometria","Algebra"])

lbl = Label(ventana,text="Lista de Asignaturas",bg="#483D8B",fg="white",font=("Arial", 20))

btnSelec = Button(ventana,text="Seleccionar",command=funcionPrueba)

lbl.pack(side=TOP)

Asignaturas.pack()

btnSelec.pack()

Asignaturas.current(1)

ventana.mainloop()




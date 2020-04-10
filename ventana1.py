from tkinter import *
from tkinter import ttk
from tkinter import messagebox
 

ventana = Tk()

ventana.geometry('400x300')

ventana.configure(bg = '#483D8B')

ventana.title('eduPython')

btnSalir = Button(ventana, text='Salir',command=ventana.destroy).pack(side=BOTTOM)

Asignaturas = ttk.Combobox(ventana, values=["Aritmetica", "Programacion Basica","Geometria","Trigonometria","CoronaVirus"])

lblAsignaturas = Label(ventana,text="Lista de Asignaturas",bg="#483D8B",fg="white",font=("Arial", 20))

def ventanaTemas():
    
    ventanaDos = Toplevel(ventana,bg='#483D8B')

    ventanaDos.geometry('400x300')
        
    btnSalir2 = Button(ventanaDos, text='Salir',command=ventanaDos.destroy).pack(side=BOTTOM)

    Temas = ttk.Combobox(ventanaDos, values=["Sumas", "Python","Triangulos","Teorema de Pitágoras","Medidas de prevención"])

    lblTemas = Label(ventanaDos,text="Lista de temas",bg="#483D8B",fg="white",font=("Arial", 20))

    btnSelec2 = Button(ventanaDos,text="Seleccionar")

    lblTemas.pack(side=TOP)

    Temas.pack()

    btnSelec2.pack()

    Temas.current(1)

    ventanaDos.mainloop()

btnSelec = Button(ventana,text="Seleccionar",command=ventanaTemas)

lblAsignaturas.pack(side=TOP)

Asignaturas.pack()

btnSelec.pack()

Asignaturas.current(1)

ventana.mainloop()








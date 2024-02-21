import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Pablo Jose
apellido: Fause Sarmiento
---
Ejercicio: while_01
---
Enunciado:
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert 
10 repeticiones con números ASCENDENTE desde el 1 al 10
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        Interaccion = 0
        while Interaccion < 10:
            alert("Informe", "Interaccion NRO: " + str(Interaccion + 1))
            Interaccion += 1
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
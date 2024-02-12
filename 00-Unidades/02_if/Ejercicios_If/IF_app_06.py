import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Pablo Jose
apellido: Fause Sarmiento
---
Ejercicio: if_06
---
Enunciado:
Al presionar el botón 'Calcular', se deberá obtener el contenido de la caja de texto txtEdad, 
transformarlo en número y calcular si es mayor, niño/a(menor de 10) o pre-adolescente 
(edad entre 10 y 13 años) o adolescente (edad entre 13 y 17 años) de edad, 
se deberá informar utilizando el Dialog alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        Edad = int(self.txt_edad.get())

        if Edad > 9 and Edad < 13:
            mensaje = "Sos pre-adolescente, anda a mirar videos en yutub 🤓" #Pre-adolescente
        elif Edad > 12 and Edad < 18:
            mensaje = "Sos adolescente, anda a estudiar wacho ☹️"#adolscente
        elif Edad > 17:
            mensaje = "Sos un adulto, lamentablemente 😞" #Mayor#Mayor
        else:
            mensaje = "Sos un niño chiquito que haces con computadora 😒" #Niño

        alert("Mensaje", mensaje)

        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
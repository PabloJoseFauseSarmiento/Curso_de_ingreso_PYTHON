import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Pablo Jose
apellido: Fause Sarmiento
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        suma_positivo = 0
        suma_negativo = 0
        cantidad_positivo = 0
        cantidad_negativo = 0
        cantidad_ceros = 0
        diferencia = 0
        alert("Aviso", "¡Ingresa la cantidad de numeros que quieras!")
        while True:
            numero = prompt("Ingrese", "Ingrese un valor")
            if numero == None or numero == "":
                break
            elif int(numero) == 0:
                cantidad_ceros += 1
            elif int(numero) < 0:
                cantidad_negativo += 1
                suma_negativo = suma_negativo + int(numero)
            elif int(numero) > 0:
                cantidad_positivo += 1
                suma_positivo = suma_positivo + int(numero)
        
        diferencia = suma_positivo + suma_negativo

        alert("Resultados", "Acumulacion de positivos:" + str(suma_positivo) + "\nAcumulacion de negativos: " + str(suma_negativo) + "\nCantidad de positivos: " + str(cantidad_positivo) + "\nCantidad de negativos: " + str(cantidad_negativo) + "\nCantidad de ceros: " + str(cantidad_ceros) + "\nDiferencia: " + str(diferencia))

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

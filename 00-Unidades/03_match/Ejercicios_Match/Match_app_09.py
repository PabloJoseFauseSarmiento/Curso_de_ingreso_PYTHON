import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Pablo Jose
apellido: Fause Sarmiento
---
Ejercicio: Match_09
---
Una agencia de viajes cobra $15.000 por cada estadía como base. 
Luego para calcular las tarifas total realiza el siguiente cálculo, 
en función de la estación del año y del destino elegido:
    Si es invierno: 
        Bariloche tiene un aumento del 20% 
        Cataratas y Córdoba tienen un descuento del 10%
        Mar del plata tiene un descuento del 20%
    Si es Verano:
        Bariloche tiene un descuento del 20%
        Cataratas y Cordoba tienen un aumento del 10%
        Mar del plata tiene un aumento del 20%
    Si es Primavera u Otoño:
        Bariloche tiene un aumento del 10%
        Cataratas tiene un aumento del 10%
        Mar del plata tiene un aumento del 10%
        Córdoba tiene precio sin descuento

'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.label_estaciones = customtkinter.CTkLabel(master=self, text="Estaciones")
        self.label_estaciones.grid(row=0, column=0, padx=20, pady=10)
        estaciones = ['Verano', 'Otoño', 'Invierno', 'Primavera']
        self.combobox_estaciones = customtkinter.CTkComboBox(master=self, values=estaciones)
        self.combobox_estaciones.grid(row=1, column=0, padx=20, pady=(10, 10))

        
        self.label_destinos = customtkinter.CTkLabel(master=self, text="Destinos")
        self.label_destinos.grid(row=2, column=0, padx=20, pady=10)
        destinos = ['Bariloche', 'Mar del plata', 'Cataratas', 'Cordoba']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=3, column=0, padx=20, pady=(10, 10))

        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        Estacion = self.combobox_estaciones.get()
        Destino = self.combobox_destino.get()

        match Estacion, Destino:
            case "Invierno", "Bariloche":
                Aumento = 0.20
                Descuento = 0

            case "Invierno", "Cataratas"|"Cordoba":
                Aumento = 0
                Descuento = 0.10

            case "Invierno", "Mar del plata":
                Aumento = 0
                Descuento = 0.20

            case "Verano", "Bariloche":
                Aumento = 0
                Descuento = 0.20

            case "Verano", "Cataratas"|"Cordoba":
                Aumento = 0.10
                Descuento = 0

            case "Verano", "Mar del plata":
                Aumento = 0.20
                Descuento = 0

            case "Primavera"|"Otoño", "Bariloche"|"Cataratas"|"Mar del plata":
                Aumento = 0.10
                Descuento = 0
            
            case "Primavera"|"Otoño", "Cordoba":
                Aumento = 0
                Descuento = 0

        Total_Calculado = 15000 + (15000 * Aumento)
        Total_Calculado = Total_Calculado - (Total_Calculado * Descuento)

        alert("Total", "El total calculado del viaje es de " + str(Total_Calculado) + "$")

            
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: Iluminación
---
Enunciado:
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        Marca = self.combobox_marca.get()
        Cantidad = int(self.combobox_cantidad.get())

        match Marca, Cantidad:
            case _, 6|7|8|9:
                Descuento = 0.5

                Total = Cantidad * 800
                Total_Con_Descuentos = Total - (Total * Descuento)

            case _, 10|11|12:
                Descuento = 0.5

                Total = Cantidad * 800
                Total_Con_Descuentos = Total - (Total * Descuento)
                Total_Con_Descuentos = Total_Con_Descuentos - (Total_Con_Descuentos * 0.05) #Se le agrega un 5% mas de descuento porque este es el unico caso que alcanza mas de 4000$


            case "ArgentinaLuz", 5:
                Descuento = 0.4

                Total = Cantidad * 800
                Total_Con_Descuentos = Total - (Total * Descuento)

            case _, 5:
                Descuento = 0.3

                Total = Cantidad * 800
                Total_Con_Descuentos = Total - (Total * Descuento)

            case "ArgentinaLuz"|"FelipeLamparas", 4:
                Descuento = 0.25

                Total = Cantidad * 800
                Total_Con_Descuentos = Total - (Total * Descuento)
            
            case _, 4:
                Descuento = 0.20

                Total = Cantidad * 800
                Total_Con_Descuentos = Total - (Total * Descuento)

            case "ArgentinaLuz", 3:
                Descuento = 0.15

                Total = Cantidad * 800
                Total_Con_Descuentos = Total - (Total * Descuento)

            case "FelipeLamparas", 3:
                Descuento = 0.10

                Total = Cantidad * 800
                Total_Con_Descuentos = Total - (Total * Descuento)

            case _, 3:
                Descuento = 0.05

                Total = Cantidad * 800
                Total_Con_Descuentos = Total - (Total * Descuento)
    
        alert("Factura", "El precio total de todas sus compras suman: " + str(Total_Con_Descuentos) + " $")

        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
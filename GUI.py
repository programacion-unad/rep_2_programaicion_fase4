import tkinter as tk
from tkinter import ttk  
from tkinter import messagebox
from coneccion import funciones_clientes

class AplicacionSJF(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Software FJ - Gestión de Servicios")
        self.geometry("700x600")
        
        self.func = funciones_clientes()
        
        # 1. Panel de pestañas 
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, expand=True, fill="both")

        # 2. Definición de las pestañas
        self.tab_clientes = ttk.Frame(self.notebook)
        self.tab_servicios = ttk.Frame(self.notebook)
        self.tab_reservas = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_clientes, text="Clientes")
        self.notebook.add(self.tab_servicios, text="Servicios")
        self.notebook.add(self.tab_reservas, text="Reservas")

        # Inicializar interfaces
        self.Registrar_clientes()
        self.Servicio_hotel()
        self.Servicio_transporte()
        self.Servicio_tour()

    def Registrar_clientes(self):
        # Interfaz de Clientes 
        ttk.Label(self.tab_clientes, text="Registro de Nuevo Cliente", font=('Arial', 12, 'bold')).pack(pady=10)
        frame_form = ttk.Frame(self.tab_clientes)
        frame_form.pack(pady=5)

        ttk.Label(frame_form, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
        self.ent_nombre = ttk.Entry(frame_form)
        self.ent_nombre.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame_form, text="Correo:").grid(row=1, column=0, padx=5, pady=5)
        self.ent_correo = ttk.Entry(frame_form)
        self.ent_correo.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(self.tab_clientes, text="Guardar Cliente", command=self.guardar_datos).pack(pady=20)

    def Servicio_hotel(self):
        # Interfaz para la clase Hotel 
        ttk.Label(self.tab_servicios, text="Servicio de Hotelería", font=('Arial', 12, 'bold')).pack(pady=10)
        
        frame_hotel = ttk.LabelFrame(self.tab_servicios, text="Calcular Costo Hotel")
        frame_hotel.pack(pady=10, padx=10, fill="x")

        ttk.Label(frame_hotel, text="Precio por noche:").grid(row=0, column=0, padx=5, pady=5)
        self.ent_precioNoche = ttk.Entry(frame_hotel)
        self.ent_precioNoche.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame_hotel, text="Número de noches:").grid(row=1, column=0, padx=5, pady=5)
        self.ent_numeroNoches = ttk.Entry(frame_hotel)
        self.ent_numeroNoches.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(frame_hotel, text="Calcular costo", command=self.calcular_hotel).grid(row=2, columnspan=2, pady=10)
    
    def Servicio_transporte(self):
        ttk.Label(self.tab_servicios, text="Servicio de Transporte", font=('Arial', 12, 'bold')).pack(pady=10)

        # Interfaz para la clase Transporte 
        frame_transporte = ttk.LabelFrame(self.tab_servicios, text="Gestión de Transporte")
        frame_transporte.pack(pady=10, padx=10, fill="x")

        ttk.Label(frame_transporte, text="Tarifa por KM:").grid(row=0, column=0, padx=5, pady=5)
        self.ent_tarifaKm = ttk.Entry(frame_transporte)
        self.ent_tarifaKm.grid(row=0, column=1, padx=5, pady=5)
        
        # calcular distancia
        ttk.Label(frame_transporte, text="Distancia (KM):").grid(row=1, column=0, padx=5, pady=5)
        self.ent_distancia = ttk.Entry(frame_transporte)
        self.ent_distancia.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(frame_transporte, text="Calcular Transporte", command=self.calcular_transporte).grid(row=2, columnspan=2, pady=10)

    def Servicio_tour(self):
        ttk.Label(self.tab_servicios, text="Servicio de Tour", font=('Arial', 12, 'bold')).pack(pady=10)

        # Interfaz para la clase Tour 
        frame_tour = ttk.LabelFrame(self.tab_servicios, text="Gestión de Tour")
        frame_tour.pack(pady=10, padx=10, fill="x")

      
        ttk.Label(frame_tour, text="Precio por Persona:").grid(row=0, column=0, padx=5, pady=5)
        self.ent_precioPersona = ttk.Entry(frame_tour)
        self.ent_precioPersona.grid(row=0, column=1, padx=5, pady=5)
        
       
        ttk.Label(frame_tour, text="Cantidad de Personas:").grid(row=1, column=0, padx=5, pady=5)
        self.ent_cantidadPersonas = ttk.Entry(frame_tour)
        self.ent_cantidadPersonas.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(frame_tour, text="Calcular Tour", command=self.calcular_tour).grid(row=2, columnspan=2, pady=10)

    #  manejo de excepciones 
    def calcular_transporte(self):
        try:
            tarifa = float(self.ent_tarifaKm.get())
            distancia = float(self.ent_distancia.get())
            total = tarifa * distancia 
            messagebox.showinfo("Costo Transporte", f"El costo total es: ${total}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos para transporte.")

    def calcular_tour(self):
        try:
            precio = float(self.ent_precioPersona.get())
            personas = int(self.ent_cantidadPersonas.get())
            total = precio * personas 
            messagebox.showinfo("Costo Tour", f"El costo total es: ${total}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos para el tour.")

    def calcular_hotel(self):
        # manejo de excepciones 
        try:
            precio = float(self.ent_precioNoche.get())
            noches = int(self.ent_numeroNoches.get())
            # Esto usa el método de la clase Hotel de tus compañeros 
            total = precio * noches 
            messagebox.showinfo("Costo Total", f"El costo del hospedaje es: ${total}")
        except ValueError:
            messagebox.showerror("Error de Datos", "Por favor ingrese valores numéricos válidos.")

    def guardar_datos(self):
        nombre = self.ent_nombre.get()
        correo = self.ent_correo.get()
        
        if nombre and correo:
            self.func.guadar_dt(nombre, correo)
            messagebox.showinfo("Éxito", f"Cliente {nombre} registrado correctamente.")
        else:
            messagebox.showwarning("Atención", "Todos los campos son obligatorios.")

if __name__ == "__main__":
    app = AplicacionSJF()
    app.mainloop()
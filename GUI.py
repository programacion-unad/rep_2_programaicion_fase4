import tkinter as tk
from tkinter import ttk  
from tkinter import messagebox
from coneccion import funciones_clientes
class AplicacionSJF(tk.Tk):
    
    func = funciones_clientes()
    
    def __init__(self):
        super().__init__()
        self.title("Software FJ")
        self.geometry("600x500")

        # 1. Creación del panel de pestañas 
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, expand=True, fill="both")

        # 2. Definición de las pestañas principales
        self.tab_clientes = ttk.Frame(self.notebook)
        self.tab_servicios = ttk.Frame(self.notebook)
        self.tab_reservas = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_clientes, text="Clientes")
        self.notebook.add(self.tab_servicios, text="Servicios")
        self.notebook.add(self.tab_reservas, text="Reservas")

        # Inicializar contenido de cada pestaña
        self.crear_interfaz_clientes()

    def crear_interfaz_clientes(self):
        #Etiquetas y campos de entrada
        ttk.Label(self.tab_clientes, text="Registro de Nuevo Cliente", font=('Arial', 12, 'bold')).pack(pady=10)
        
        frame_form = ttk.Frame(self.tab_clientes)
        frame_form.pack(pady=5)

        ttk.Label(frame_form, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
        self.ent_nombre = ttk.Entry(frame_form)
        self.ent_nombre.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(frame_form, text="Correo:").grid(row=1, column=0, padx=5, pady=5)
        self.ent_correo = ttk.Entry(frame_form)
        self.ent_correo.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(self.tab_clientes, text="Guardar Cliente", command=self.guardar_datos).pack(pady=20)

    def guardar_datos(self):
        
        nombre = self.ent_nombre.get()
        correo = self.ent_correo.get()
                
        self.func.guadar_dt(nombre, correo)               
        
        if nombre and correo:
            messagebox.showinfo("Éxito", f"Cliente {nombre} registrado localmente.")
        else:
            messagebox.showwarning("Atención", "El campo nombre es obligatorio.")

if __name__ == "__main__":
    app = AplicacionSJF()
    app.mainloop()
    
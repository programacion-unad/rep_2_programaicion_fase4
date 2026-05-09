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
        
        # Panel de pestañas 
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, expand=True, fill="both")

        # Pestañas (sin Reservas)
        self.tab_clientes = ttk.Frame(self.notebook)
        self.tab_servicios = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_clientes, text="Clientes")
        self.notebook.add(self.tab_servicios, text="Servicios")

        self.construir_tab_clientes()
        self.construir_tab_servicios()

    
    #              TAB CLIENTES
   

    def construir_tab_clientes(self):
        ttk.Label(self.tab_clientes, text="Registro de Nuevo Cliente", font=('Arial', 12, 'bold')).pack(pady=10)

        frame_form = ttk.Frame(self.tab_clientes)
        frame_form.pack(pady=5)

        # Nombre
        ttk.Label(frame_form, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
        self.ent_nombre = ttk.Entry(frame_form)
        self.ent_nombre.grid(row=0, column=1, padx=5, pady=5)

        # Correo
        ttk.Label(frame_form, text="Correo:").grid(row=1, column=0, padx=5, pady=5)
        self.ent_correo = ttk.Entry(frame_form)
        self.ent_correo.grid(row=1, column=1, padx=5, pady=5)

        # Tipo de servicio
        ttk.Label(frame_form, text="Servicio:").grid(row=2, column=0, padx=5, pady=5)
        self.combo_servicio = ttk.Combobox(frame_form, values=["Hotel", "Transporte", "Tour"], state="readonly")
        self.combo_servicio.grid(row=2, column=1, padx=5, pady=5)
        self.combo_servicio.bind("<<ComboboxSelected>>", self.actualizar_label_valor)

        # Valor del servicio (cambia según el tipo)
        self.lbl_valor = ttk.Label(frame_form, text="Valor:")
        self.lbl_valor.grid(row=3, column=0, padx=5, pady=5)
        self.ent_valor = ttk.Entry(frame_form)
        self.ent_valor.grid(row=3, column=1, padx=5, pady=5)

        ttk.Button(self.tab_clientes, text="Guardar Cliente", command=self.guardar_cliente).pack(pady=10)

        # Lista de clientes registrados
        ttk.Label(self.tab_clientes, text="Clientes Registrados:", font=('Arial', 10, 'bold')).pack()

        frame_lista = ttk.Frame(self.tab_clientes)
        frame_lista.pack(pady=5, fill="both", expand=True, padx=10)

        scrollbar = ttk.Scrollbar(frame_lista, orient="vertical")
        self.listbox_clientes = tk.Listbox(frame_lista, yscrollcommand=scrollbar.set, height=8)
        scrollbar.config(command=self.listbox_clientes.yview)

        self.listbox_clientes.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def actualizar_label_valor(self, event=None):
        """Cambia el texto de la etiqueta según el servicio seleccionado."""
        servicio = self.combo_servicio.get()
        if servicio == "Hotel":
            self.lbl_valor.config(text="Precio por noche:")
        elif servicio == "Transporte":
            self.lbl_valor.config(text="Tarifa por KM:")
        elif servicio == "Tour":
            self.lbl_valor.config(text="Precio por persona:")

    def guardar_cliente(self):
        nombre = self.ent_nombre.get().strip()
        correo = self.ent_correo.get().strip()
        tipo = self.combo_servicio.get()

        try:
            if not tipo:
                raise ValueError("Debe seleccionar un tipo de servicio.")
            valor = float(self.ent_valor.get())
            cliente = self.func.guardar_cliente(nombre, correo, tipo, valor)
            # Agregar a la listbox
            self.listbox_clientes.insert(tk.END, cliente.mostrar_info())
            # Actualizar combo de servicios
            self.actualizar_combo_clientes()
            messagebox.showinfo("Éxito", f"Cliente '{nombre}' registrado con servicio {tipo}.")
            # Limpiar campos
            self.ent_nombre.delete(0, tk.END)
            self.ent_correo.delete(0, tk.END)
            self.ent_valor.delete(0, tk.END)
            self.combo_servicio.set("")
            self.lbl_valor.config(text="Valor:")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

   
    #              TAB SERVICIOS
   

    def construir_tab_servicios(self):
        ttk.Label(self.tab_servicios, text="Calcular Costo por Cliente", font=('Arial', 12, 'bold')).pack(pady=10)

        frame_sel = ttk.Frame(self.tab_servicios)
        frame_sel.pack(pady=5)

        ttk.Label(frame_sel, text="Seleccionar cliente:").grid(row=0, column=0, padx=5, pady=5)
        self.combo_clientes = ttk.Combobox(frame_sel, state="readonly", width=40)
        self.combo_clientes.grid(row=0, column=1, padx=5, pady=5)
        self.combo_clientes.bind("<<ComboboxSelected>>", self.al_seleccionar_cliente)

        # Frame dinámico para el parámetro según servicio
        self.frame_calculo = ttk.LabelFrame(self.tab_servicios, text="Parámetro de cálculo")
        self.frame_calculo.pack(pady=10, padx=10, fill="x")

        self.lbl_param = ttk.Label(self.frame_calculo, text="")
        self.lbl_param.grid(row=0, column=0, padx=5, pady=5)
        self.ent_param = ttk.Entry(self.frame_calculo)
        self.ent_param.grid(row=0, column=1, padx=5, pady=5)

        ttk.Button(self.tab_servicios, text="Calcular Costo", command=self.calcular_costo_cliente).pack(pady=10)

        # Resultado
        self.lbl_resultado = ttk.Label(self.tab_servicios, text="", font=('Arial', 11))
        self.lbl_resultado.pack(pady=5)

    def actualizar_combo_clientes(self):
        """Refresca el combo de clientes en la tab de servicios."""
        clientes = self.func.get_clientes()
        nombres = [f"{i}: {c.get_nombre()} ({c.get_servicio().descripcion()})" for i, c in enumerate(clientes)]
        self.combo_clientes["values"] = nombres
        if nombres:
            self.combo_clientes.set(nombres[-1])
            self.al_seleccionar_cliente()

    def al_seleccionar_cliente(self, event=None):
        """Actualiza el label del parámetro según el servicio del cliente seleccionado."""
        seleccion = self.combo_clientes.get()
        if not seleccion:
            return
        try:
            indice = int(seleccion.split(":")[0])
            cliente = self.func.get_cliente_por_indice(indice)
            tipo = cliente.get_servicio().descripcion()
            if tipo == "Hotel":
                self.lbl_param.config(text="Número de noches:")
            elif tipo == "Transporte":
                self.lbl_param.config(text="Distancia (KM):")
            elif tipo == "Tour":
                self.lbl_param.config(text="Cantidad de personas:")
            self.ent_param.delete(0, tk.END)
            self.lbl_resultado.config(text="")
        except (IndexError, ValueError) as e:
            messagebox.showerror("Error", str(e))

    def calcular_costo_cliente(self):
        seleccion = self.combo_clientes.get()
        if not seleccion:
            messagebox.showwarning("Atención", "Seleccione un cliente primero.")
            return
        try:
            indice = int(seleccion.split(":")[0])
            cliente = self.func.get_cliente_por_indice(indice)
            param = float(self.ent_param.get())
            if param <= 0:
                raise ValueError("El parámetro debe ser mayor a 0.")
            costo = cliente.get_servicio().calcular_costo(param)
            self.lbl_resultado.config(
                text=f"Cliente: {cliente.get_nombre()} | Servicio: {cliente.get_servicio().descripcion()} | Costo total: ${costo:.2f}"
            )
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except IndexError as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    app = AplicacionSJF()
    app.mainloop()
from Clases import Cliente, Hotel, Transporte, Tour

# =============================================
#       Conexión entre lógica y GUI 
# =============================================

class funciones_clientes:

    def __init__(self):
        self.lista_clientes = []  # lista donde se guardan todos los clientes

    def guardar_cliente(self, nombre: str, correo: str, tipo_servicio: str, valor: float):
        """Crea un cliente con su servicio asignado y lo agrega a la lista."""
        try:
            if not nombre or not correo:
                raise ValueError("Nombre y correo son obligatorios.")
            if valor <= 0:
                raise ValueError("El valor del servicio debe ser mayor a 0.")

            if tipo_servicio == "Hotel":
                servicio = Hotel(valor)
            elif tipo_servicio == "Transporte":
                servicio = Transporte(valor)
            elif tipo_servicio == "Tour":
                servicio = Tour(valor)
            else:
                raise ValueError(f"Tipo de servicio no reconocido: {tipo_servicio}")

            cliente = Cliente(nombre, correo, servicio)
            self.lista_clientes.append(cliente)
            return cliente

        except ValueError as e:
            raise e

    def get_clientes(self):
        return self.lista_clientes

    def get_cliente_por_indice(self, indice: int):
        try:
            return self.lista_clientes[indice]
        except IndexError:
            raise IndexError("No existe un cliente con ese índice.")

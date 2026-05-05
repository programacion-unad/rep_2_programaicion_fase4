from servicio import Servicio

class Hotel(Servicio):
    def __init__(self, precio_noche):
        self.precio_noche = precio_noche

    def calcular_costo(self, noches=1):
        return self.precio_noche * noches
    
    def descripcion(self):
        return "servicio de hotel"
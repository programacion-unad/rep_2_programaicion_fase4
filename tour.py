from servicio import Servicio

class Tour(Servicio):
    def calcular_costo(self, personas):
        return personas * 50
    
    def descripcion(self):
        return "servicio turistico"
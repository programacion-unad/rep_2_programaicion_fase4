from servicio import Servicio

class Transporte(Servicio):
    def calcular_costo(self, distancia):
        return distancia * 2
    
    def descripcion(self):
        return "servicio de transporte"
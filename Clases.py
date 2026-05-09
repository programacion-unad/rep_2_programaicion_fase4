from abc import ABC, abstractmethod
from clase_general import System_P  


# =========================
# CLASE CLIENTE
# =========================

class Cliente(System_P):

    def __init__(self, nombre, correo, servicio):
        self.nombre = nombre
        self.correo = correo
        self.servicio = servicio  # objeto Hotel, Transporte o Tour

    def get_nombre(self):
        return self.nombre
    def set_nombre(self, nombre):
        self.nombre = nombre
        
    def get_correo(self):
        return self.correo
    def set_correo(self, correo):
        self.correo = correo

    def get_servicio(self):
        return self.servicio

    def mostrar_info(self):
        return f"Cliente: {self.nombre}, Correo: {self.correo}, Servicio: {self.servicio.descripcion()}"

    def reservas_equipos(self, hora, tipo):
        return f"Reserva realizada a las {hora}"
        
    def servicios(self, hora, tipo):
        return f"Servicio solicitado: {tipo}" 
    

# =========================
# SERVICIO HOTEL
# =========================

class Hotel(System_P):

    def __init__(self, precio_noche):
        self.precio_noche = precio_noche
        
    def get_precio_noche(self):
        return self.precio_noche
    def set_precio_noche(self, precio):
        self.precio_noche = precio

    def calcular_costo(self, noches=1):
        return self.precio_noche * noches

    def descripcion(self):
        return "Hotel"
    
    def reservas_equipos(self, hora, tipo):
        return f"Reserva realizada a las {hora}"
    
    def servicios(self, hora, tipo):
        return f"Servicio hotel: {tipo}"


# =========================
# SERVICIO TRANSPORTE
# =========================

class Transporte(System_P):

    def __init__(self, tarifa_km):
        self.tarifa_km = tarifa_km

    def get_tarifa_km(self):
        return self.tarifa_km
    def set_tarifa_km(self, tarifa):
        self.tarifa_km = tarifa

    def calcular_costo(self, distancia):
        return self.tarifa_km * distancia

    def descripcion(self):
        return "Transporte"

    def reservas_equipos(self, hora, tipo):
        return f"Reserva transporte a las {hora}"
    
    def servicios(self, hora, tipo):
        return f"Servicio transporte: {tipo}"
    
# =========================
# SERVICIO TOUR
# =========================

class Tour(System_P):

    def __init__(self, precio_persona):
        self.precio_persona = precio_persona

    def get_precio_persona(self):
        return self.precio_persona
    def set_precio_persona(self, precio):
        self.precio_persona = precio

    def calcular_costo(self, personas):    
        return self.precio_persona * personas

    def descripcion(self):
        return "Tour"

    def reservas_equipos(self, hora, tipo):
        return f"Reserva tour a las {hora}"
    
    def servicios(self, hora, tipo):
        return f"Servicio tour: {tipo}"


# =========================
# PRUEBAS DEL SISTEMA
# =========================

if __name__ == "__main__":
    hotel1 = Hotel(150)
    transporte1 = Transporte(5)
    tour1 = Tour(80)

    cliente1 = Cliente("Juan", "juan@gmail.com", hotel1)

    print(cliente1.mostrar_info())

    print(hotel1.descripcion(), "- Costo:", hotel1.calcular_costo(3))
    print(transporte1.descripcion(), "- Costo:", transporte1.calcular_costo(20))
    print(tour1.descripcion(), "- Costo:", tour1.calcular_costo(4))

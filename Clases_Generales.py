from abc import ABC, abstractmethod


# =========================
# CLASE CLIENTE
# =========================

class Cliente:

    def __init__(self, nombre, correo):

        if not nombre:
            raise ValueError("El nombre no puede estar vacío")

        if "@" not in correo:
            raise ValueError("Correo inválido")

        self.nombre = nombre
        self.correo = correo

    def mostrar_info(self):

        return f"Cliente: {self.nombre}, Correo: {self.correo}"


# =========================
# CLASE ABSTRACTA SERVICIO
# =========================

class Servicio(ABC):

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass


# =========================
# SERVICIO HOTEL
# =========================

class Hotel(Servicio):

    def __init__(self, precio_noche):

        if precio_noche <= 0:
            raise ValueError("El precio debe ser positivo")

        self.precio_noche = precio_noche

    def calcular_costo(self, noches=1):

        if noches <= 0:
            raise ValueError("Número de noches inválido")

        return self.precio_noche * noches

    def descripcion(self):

        return "Servicio de Hotel"


# =========================
# SERVICIO TRANSPORTE
# =========================

class Transporte(Servicio):

    def __init__(self, tarifa_km):

        if tarifa_km <= 0:
            raise ValueError("Tarifa inválida")

        self.tarifa_km = tarifa_km

    def calcular_costo(self, distancia):

        if distancia <= 0:
            raise ValueError("Distancia inválida")

        return self.tarifa_km * distancia

    def descripcion(self):

        return "Servicio de Transporte"


# =========================
# SERVICIO TOUR
# =========================

class Tour(Servicio):

    def __init__(self, precio_persona):

        if precio_persona <= 0:
            raise ValueError("Precio inválido")

        self.precio_persona = precio_persona

    def calcular_costo(self, personas):

        if personas <= 0:
            raise ValueError("Cantidad inválida")

        return self.precio_persona * personas

    def descripcion(self):

        return "Servicio de Tour"


# =========================
# PRUEBAS DEL SISTEMA
# =========================

try:

    cliente1 = Cliente("Juan", "juan@gmail.com")

    hotel1 = Hotel(150)

    print(cliente1.mostrar_info())

    print(hotel1.descripcion())

    print("Costo total:", hotel1.calcular_costo(3))

except Exception as e:

    print("Error:", e)
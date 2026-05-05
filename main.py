from cliente import Cliente
from hotel import Hotel

c = Cliente("juan", "juan@gmail.com")
h = Hotel(100)

print(c.mostrar_info())
print(h.calcular_costo(2))
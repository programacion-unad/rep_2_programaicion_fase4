class Cliente:
    def __init__(self, nombre, correo):
        if not nombre:
            raise ValueError("El nombre no puede estar vacio")
        if "@" not in correo:
            raise ValueError("El correo debe contener un @")
        
        self.nombre = nombre
        self.correo = correo

    def mostrar_info(self):
        return f"Cliente: {self.nombre}, Correo: {self.correo}"
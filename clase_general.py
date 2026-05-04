from abc import ABC, abstractmethod

class System_P(ABC):
    @abstractmethod
    def reservas_equipos(self, hora, tipo: str):
        pass
    
    @abstractmethod
    def servicios(self, hora, tipo: str):
        pass
    
    


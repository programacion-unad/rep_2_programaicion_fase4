# ==========================================
# EXCEPCIONES PERSONALIZADAS DEL SISTEMA
# ==========================================

class ErrorSistema(Exception):
    """Clase base para errores del sistema"""
    pass


# ==========================================
# EXCEPCIONES CLIENTE
# ==========================================

class ClienteInvalidoError(ErrorSistema):
    """Error cuando el cliente tiene datos inválidos"""
    pass


class CorreoInvalidoError(ErrorSistema):
    """Error cuando el correo es inválido"""
    pass


# ==========================================
# EXCEPCIONES SERVICIOS
# ==========================================

class ServicioInvalidoError(ErrorSistema):
    """Error cuando el servicio no existe"""
    pass


class ValorInvalidoError(ErrorSistema):
    """Error cuando el valor ingresado es incorrecto"""
    pass


# ==========================================
# EXCEPCIONES LISTAS / BÚSQUEDAS
# ==========================================

class ClienteNoEncontradoError(ErrorSistema):
    """Error cuando no existe el cliente"""
    pass
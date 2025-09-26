from .base import ValidadorBase

class ValidadorDatosContacto(ValidadorBase):
    def validar_email(self, email: str) -> bool:
        return "@" in email and "." in email

    def validar_celular(self, celular: str) -> bool:
        return self.validar_solo_numeros(celular) and len(celular) >= 9

    def validar_direccion(self, direccion: str) -> bool:
        return len(direccion.strip()) > 5

from .base import ValidadorBase

class ValidadorDatosPersonales(ValidadorBase):
    def validar_edad(self, edad: int) -> bool:
        return isinstance(edad, int) and 0 < edad < 120

    def validar_nombre(self, nombre: str) -> bool:
        return self.validar_solo_letras(nombre)

    def validar_documento_identidad(self, doc: str) -> bool:
        return self.validar_solo_numeros(doc) and len(doc) >= 6

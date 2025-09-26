from ..validators.datos_personales import ValidadorDatosPersonales
from ..validators.datos_contacto import ValidadorDatosContacto

class Persona:
    def __init__(self):
        self.nombre = None
        self.edad = None
        self.documento = None
        self.email = None
        self.celular = None
        self.direccion = None
        self.validador_personal = ValidadorDatosPersonales()
        self.validador_contacto = ValidadorDatosContacto()

    def set_nombre(self, nombre: str):
        if self.validador_personal.validar_nombre(nombre):
            self.nombre = nombre
        else:
            raise ValueError("Nombre inválido")
        return self

    def set_edad(self, edad: int):
        if self.validador_personal.validar_edad(edad):
            self.edad = edad
        else:
            raise ValueError("Edad inválida")
        return self

    def set_documento(self, documento: str):
        if self.validador_personal.validar_documento_identidad(documento):
            self.documento = documento
        else:
            raise ValueError("Documento inválido")
        return self

    def set_email(self, email: str):
        if self.validador_contacto.validar_email(email):
            self.email = email
        else:
            raise ValueError("Email inválido")
        return self

    def set_celular(self, celular: str):
        if self.validador_contacto.validar_celular(celular):
            self.celular = celular
        else:
            raise ValueError("Celular inválido")
        return self

    def set_direccion(self, direccion: str):
        if self.validador_contacto.validar_direccion(direccion):
            self.direccion = direccion
        else:
            raise ValueError("Dirección inválida")
        return self

    def build(self):
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "documento": self.documento,
            "email": self.email,
            "celular": self.celular,
            "direccion": self.direccion,
        }

class ValidadorBase:
    def validar_solo_numeros(self, valor: str) -> bool:
        return valor.isdigit()

    def validar_solo_letras(self, valor: str) -> bool:
        return valor.isalpha()

    def validar_alfanumerico(self, valor: str) -> bool:
        return valor.isalnum()

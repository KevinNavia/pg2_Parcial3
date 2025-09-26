# pg2_Parcial3
PONGAME 100 ING 
# Librería nombre_apellido_pg2_tecba

## Ejemplo de uso

```python
from nombre_apellido_pg2_tecba.core.persona import Persona

persona = (
    Persona()
    .set_nombre("Juan")
    .set_edad(25)
    .set_documento("12345678")
    .set_email("juan@mail.com")
    .set_celular("123456789")
    .set_direccion("Calle Falsa 123")
    .build()
)

print(persona)

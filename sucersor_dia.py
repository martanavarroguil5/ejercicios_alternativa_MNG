from enum import Enum

# Clase enum para los dia de la semana
class Dia(Enum):
    LUNES = 1
    MARTES = 2
    MIÉRCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SÁBADO = 6
    DOMINGO = 7

# Funcion sucesor que te devuelve qué día es mañana
def sucesor_dia_semana(dia_actual):
    # Si es sábado, el sucesor es lunes (de la semana siguiente)
    if dia_actual == Dia.DOMINGO:  
        return Dia.LUNES
    # Incrementar el día actual en 1 (dia siguiente) 
    else: 
        # Convertir el número del día actual a la enumeración correspondiente
        dia_siguiente = Dia(dia_actual.value + 1)
        return dia_siguiente

# Ejemplo de uso:
dia_actual = Dia.MIÉRCOLES  
sucesor = sucesor_dia_semana(dia_actual)

# Imprimir el sucesor tanto como número como nombre del día
print("El sucesor de", dia_actual.value, "es", sucesor.value)  
print("El sucesor de", dia_actual.name, "es", sucesor.name)


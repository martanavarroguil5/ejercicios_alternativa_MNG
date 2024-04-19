# Función que calcula el coste del viaje
def calcular_coste_viaje(cantidad_alumnos):

    # Determinar el coste del trayecto por alumno
    if cantidad_alumnos <= 25:
        coste_trayecto_por_alumno = 67.30
    else:
        coste_trayecto_por_alumno = 61.00
    
    # Coste de la comida por alumno
    coste_comida_por_alumno = 3.50
    
    # Determinar el coste del alojamiento por alumno
    if cantidad_alumnos < 30:
        coste_alojamiento_por_alumno = 4.75
    elif 31 <= cantidad_alumnos <= 35:
        coste_alojamiento_por_alumno = 4.00
    else:
        coste_alojamiento_por_alumno = 3.50

    # Calcular el precio de coste por alumno
    precio_coste_por_alumno = coste_trayecto_por_alumno + coste_comida_por_alumno + coste_alojamiento_por_alumno
    
    # Calcular el coste total del viaje
    coste_total_viaje = precio_coste_por_alumno * cantidad_alumnos

    return precio_coste_por_alumno, coste_total_viaje

# Ejemplo de uso:
cantidad_alumnos = 5 
precio_coste, coste_total = calcular_coste_viaje(cantidad_alumnos)
print("El precio de coste por alumno por día es de", precio_coste, "€")
print("El coste total del viaje por día es de", coste_total, "€")

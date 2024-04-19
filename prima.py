# Función que calcula la prima anual de un conductor
def calcular_prima_anual(accidentes, distancia_recorrida, antiguedad):
    
    # Determinar la prima por accidentes
    if accidentes == 0:
        prima_por_accidentes = 1.0
    elif accidentes == 1:
        prima_por_accidentes = 0.5
    elif accidentes == 2:
        prima_por_accidentes = 1.0 / 3
    elif accidentes == 3:
        prima_por_accidentes = 0.25
    else:
        prima_por_accidentes = 0
    
    # Calcular la prima de distancia
    prima_distancia = min(distancia_recorrida * 0.01, 400)
    
    # Calcular la prima de antigüedad
    if antiguedad >= 4:
        prima_antiguedad = 200 + (antiguedad - 4) * 20
    else:
        prima_antiguedad = 0
    
    # Calcular la prima anual total
    prima_anual = (prima_distancia + prima_antiguedad) * prima_por_accidentes

    return prima_anual

# Ejemplo de uso:
accidentes = 1
distancia_recorrida = 35000
antiguedad = 5
prima = calcular_prima_anual(accidentes, distancia_recorrida, antiguedad)
print("La prima anual que recibirá el conductor es de", prima, "€")

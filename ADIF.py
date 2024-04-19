# Función que calcula el descuento
def calcular_descuento(numero_niños):
    if numero_niños == 2:
        descuento = 0.10
    elif numero_niños == 3:
        descuento = 0.15
    elif numero_niños == 4:
        descuento = 0.18
    elif numero_niños > 4:
        descuento = 0.18 + (numero_niños - 4) * 0.01
    else:
        descuento = 0 
    
    return descuento

# Ejemplo de uso:
numero_niños = 560 
descuento = calcular_descuento(numero_niños)
print("El descuento aplicado es del", descuento * 100, "%")

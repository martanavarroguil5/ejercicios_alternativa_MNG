# Funcion que calcula el descuento según el número de piezas y el tipo de cliente
def calcular_descuento(cantidad_componentes, cliente):

    # Determinar el descuento base según la cantidad de componentes
    if 10000 <= cantidad_componentes <= 20000:
        descuento_base = 0.10
    elif 20001 <= cantidad_componentes <= 40000:
        descuento_base = 0.15
    elif cantidad_componentes > 40000:
        descuento_base = 0.20
    else:
        descuento_base = 0

    # Ajustar el descuento según el tipo de cliente
    if cliente == "COMMAQ":
        descuento_cliente = 0.02
    elif cliente == "BEL":
        descuento_cliente = 0.01
    else:
        descuento_cliente = 0

    # Calcular el descuento total
    descuento_total = descuento_base + descuento_cliente

    return descuento_total

# Ejemplo de uso:
cantidad_componentes = 25000  
cliente = "COMMAQ"  # Ejemplo de cliente
descuento = calcular_descuento(cantidad_componentes, cliente)
print("El descuento aplicado es del", descuento * 100, "%")

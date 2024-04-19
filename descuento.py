# Función que calcula el descuento
def calcular_descuento(importe_compra):
    
    # Descuento del 5% para precios entre 100 € y 500€
    if 100 <= importe_compra <= 500:
        descuento = importe_compra * 0.05
    
    # Descuento del 80% para precios superiores 
    elif importe_compra > 500:
        descuento = importe_compra * 0.08
    
    # No se aplica descuento si el importe es inferior a 100 €
    else:
        descuento = 0  
    
    return descuento

# Ejemplo de uso:
importe_compra = 600 
descuento = calcular_descuento(importe_compra)
print("El descuento aplicado es de:", descuento, "euros")


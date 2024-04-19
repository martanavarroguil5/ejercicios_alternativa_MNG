# Funcion que ordenará dos numeros, su suma y su producto de menor a mayor
def clasificar_numeros(a, b):
   
    # Se crea una lista con los dos valores.
    lista = [a, b]

    # Calcular la suma y el producto de los números dados
    suma = a + b
    producto = a * b

    # Añade dichos valores calculados a la lista
    lista.append(suma)
    lista.append(producto)

    # Con la funcion "sort" se ordena la lista de menor a mayor
    lista.sort()
    return lista

# Ejemplo de uso:
a = -15
b = 6

resultado = clasificar_numeros(a, b)
print("Los números clasificados respecto a su suma y producto son:", resultado)

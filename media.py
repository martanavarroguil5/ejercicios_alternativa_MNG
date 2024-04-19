# Clase alumno que recoge sus notas
class Alumno:
    def __init__(self, nota1, nota2, nota3, nota4):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4

    # Getters
    def get_nota1(self):
        if isinstance (self.nota1, float):
            return self.nota1
        else:
            raise TypeError("Debe ser un número con decimales")
        
    def get_nota2(self):
        if isinstance (self.nota2, float):
            return self.nota2
        else:
            raise TypeError("Debe ser un número con decimales")
        
    def get_nota3(self):
        if isinstance (self.nota3, float):
            return self.nota3
        else:
            raise TypeError("Debe ser un número con decimales")
    
    
    def get_nota4(self):
        if isinstance (self.nota4, float):
            return self.nota4
        else:
            raise TypeError("Debe ser un número con decimales")
    
    # Función que calcula la media de las cuatro notas
    def calcular_media(self):
       media = (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4
       return media
        
    
    # Funcion que indica si es un alumno con talento, con capacidad o si debe reorientarse.
    def obtener_evaluacion(self):
        media = self.calcular_media()
        if media > 15:
            return "Alumno con talento"
        elif 12 <= media <= 15:
            return "Alumno con capacidad"
        else:
            return "Debe reorientarse"

# Ejemplo de uso:
alumno = Alumno(14.75, 16, 18, 13)
media = alumno.calcular_media()
evaluacion = alumno.obtener_evaluacion()
print("La media del alumno es:", media)
print("Evaluación del alumno:", evaluacion)

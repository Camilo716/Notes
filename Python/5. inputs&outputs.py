# INPUTS I OUTPUTS

# Formateo de cadenas:

numero = 242
texto = 'Hola'
decimal = 1.2

print('El número es %d , el texto es %s y el decimal es %f' % (numero, texto, decimal))  # NO RECOMENDADA
# (Método antiguo)

print('El número es {} , el texto es {} y el decimal es {}'.format(numero, texto, decimal))  # MUY USADA

print(f'El número es {numero} , el texto es {texto} y el decimal es {decimal}')  # RECOMENDADA ('FStrings')


# Es el recomendado porque podemos ejecutar codigo python adentro de las llaves, sirve para tod0 y es mas flexible

# STR Y REPR
# Usaremos str() para salidas informales y repr() para salidas técnicas de desarrollo o depuración


class Juguete:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f'Mi nombre es {self.nombre} y mi precio es {self.precio}'
        # Sobrecargamos la función str para que tenga una salida informal


# Guardar mensajes o leerlos en un fichero:

open('nombredelfichero.txt', 'r')

# MODOS O PERMISOS:
# r :Lectura
# a: append
# w: Escritura
# x: create

# t: texto
# b: binary

# +


# SERIALIZACIÓN DE DATOS es convertir una representacion de un programa a  una secuencia de datos que podemos escribir
# en un fichero

# DESERIALIZACIÓN DE DATOS es coger una secuencia de datos y convertirlos a algo entendible en un programa

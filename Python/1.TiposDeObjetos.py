# TIPOS DE OBJETOS EN PYTHON--------------------------------

# Inmutables: Números, cadenas, tuplas
numero = 9
cadena = 'Hola'
tupla = (2, 'dfs', 5)

# Mutables: Listas, diccionarios,conjuntos-sets

lista = ['a', 'b', 'c']
lista.append('d')  # Agregar elementos a una lista
lista.remove('d')  # Quitar elementos de una lista

diccionario = {
    'clave1': 'valor1',
    'clave2': 'valor2',
    'clave3': 'valor3'
}
diccionario.pop('clave3')  # eliminar el valor

conjunto = {1, 2, 3, 1, 2, 3}
print(conjunto)  # {1,2,3} --- Los conjuntos no pueden tener valor duplicado
a = {0, 2, 4, 6, 8}
b = {1, 2, 3, 4, 5}
print(a | b)  # {0,1,2,3,4,5,6,8} --- Me da la unión de dos conjuntos sin repetir valores
print(a & b)  # {2,4} --- Me da la intersección de dos conjuntos
print(a - b)  # {0,8,6} Me da las diferencias de dos conjuntos (Valores que estan en uno menos los que ya están en otro)
print(a ^ b)  # {0,1,3,5,6,8} --- Me da la diferencia simétrica (Que valores son unicos entre los dos)

# Métodos de las cadenas

miTexto = "hola, este es mi textO"
miTexto.capitalize()  # "Hola, este es mi texto" --- Capitaliza la primera letra y el resto la pone en minúscula
miTexto.title()  # "Hola, Este Es Mi Texto" --- Capitaliza la primera letra de cada palabra
miTexto.lower()  # "hola, este es mi texto" --- Convierte en minúsculas
miTexto.upper()  # "HOLA, ESTE ES MI TEXTO" --- convierte en mayúsculas
miTexto.replace("a", "o")  # "Holo, este es mi textO" --- Reemplaza una cadena o caracter por otro
miTexto.find("este")  # 6 --- Devuelve el lugar en el que se posiciona la cadena puesta como parámetro

miTexto.split()  # ["hola,","este","es","mi","textO"] Se convierte en una lista y cada elemento se separa por un espacio
miTexto.split(
    ",")  # ["hola"," este es mi textO"] --- Se convierte en una lista y cada elemento se separa por el parámetro puesto

miTexto.replace(",", "").lower().split()  # ["hola", "este","es","mi", "texto"]

listaTexto = ["hola", "este", "es", "mi", "texto"]
" ".join(listaTexto)  # "hola este es mi texto"
"-".join(listaTexto)  # "hola-este-es-mi-texto"

# Operadores
# División => a//b
# Potenciación => a**b
# Modulo => a%b

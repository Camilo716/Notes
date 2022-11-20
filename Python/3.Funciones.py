# Funciones
# -El nombre de la funcion debe hacer referencia a lo que hace y su sintaxis es esta

def nombre():
    print('Camilo')


# Deben ser cargadas por el interprete antes de ser utilizada. Siempre se invocan despues de su definicion
nombre()

# Scope de variables

temp = 27.0  # Variable global


def temperatura():
    temp = 15.2  # Variable local
    print(temp)


temperatura()  # El valor sera 15.2
print(temp)  # El valor sera 27.0


# Si queremos crear una variable global dentro de una funcion usamo la palabra reservada "global"

# En una funcion podemos poner un valor por 'defecto' como parametro


def apellido(apellido='Gonzalez'):
    print('hola', apellido)


# asi si invocamos la funcion poniendo un parametro, este sera el usado por la funcion, de lo contrario, se usara el que
# definimos por defecto dentro de la misma. (Solo se puede aplicar a el ultimo o los ultimos parametros de la funcion)


# Uso de *args: Es una lista con un numero indefinido de valores

def suma(*args):
    resultado = 0
    for i in args:
        resultado += i
    print(resultado)
    print(args)  # (3, 4, 5, 5, 6, 7, 7, 1, 2, 3, 4, 5, 5)


suma(3, 4, 5, 5, 6, 7, 7, 1, 2, 3, 4, 5, 5)


# Al cambiar *args por '**kwargs' , la funcion representara los parametros a modo de diccionarios-objetos

def objeto(**kwargs):
    for key, value in kwargs.items():
        print(key, " = ", value)

    print(kwargs)  # {'Persona1': 'Julio', 'Persona2': 'Raul', 'Persona3': 'Samuel'}


objeto(Persona1='Julio', Persona2='Raul', Persona3='Samuel')

# Funcion lambda: Funcion anonima asignada a una variable

anonima = lambda: print('Hola', nombre)

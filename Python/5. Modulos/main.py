import operaciones as op  # Importar un módulo y darle una referencia mas corta para usar en el programa(Opcional)
import paquete.interactuar  # Importar un módulo de un paquete

# Los módulos son un fichero en el disco duro que contiene una serie de sentencias y definiciones varias en python

# Es una buena práctica crear los módulos de esta manera:

def main():
    # código principal del programa
    op.suma(2, 5)  # Así se llama una función de un módulo importado
    print(paquete.interactuar.saludo('Camilo')) # Asi se llama una función del módulo de un paquete

    print(__name__)  # El nombre del módulo principal siempre será main
    print(op.nombre())  # El nombre del resto de módulos importados será el mismo del nombre del mismo fichero


print(__name__)
if __name__ == '__main__':
    main()

# Así solo tendremos dos bloques de código en el ámbito global



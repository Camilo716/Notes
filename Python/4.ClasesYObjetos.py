from abc import abstractmethod


class Juguete:
    _encendido = True  # _ al comienzo del nombre de una variable o funcion es una convencion

    # que indica que no deberiamos manipularlo desde fuera de la clase

    def apaga(self):
        self._encendido = False  # Si no ponemos el self estariamos creando una variable local dentro de la funcion

    def enciende(self):
        self._encendido = True

    def isEncendido(self):
        return self._encendido


d = Juguete()  # Instanciar una clase / Crear un objeto
d.apaga()


# ----------HERENCIA

class Potato(Juguete):
    def quitarOreja(self):
        pass


# Lo que hacemos es crear una clase base con los metodos y propiedades comunes# y luego hacemos clases
# derivada que implemente la funcionalidad de esas clases

p1 = Potato()
dir(p1)  # Saber cuales metodos y funciones tiene nuestra instancia


# -----------CONSTRUCTOR

class Dino(Juguete):
    color = None
    nombre = None

    def __init__(self, nombre, color):  # Esto es un constructor
        self.color = color
        self.nombre = nombre


d1 = Dino('Verde', 'Max')

# ------------Clase abstracta
# Nos definen una serie de funciones que serán comunes en otras clases

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sonido(self):  # Al ser abstracto las clases 'hijas' lo deben implementar
        pass

    def diHola(self):  # Al no ser abstracta las clases hijas usarán esta implementación
        print('Hola')


class Perro(Animal):
    def sonido(self):
        print('Guau')


class Gato(Animal):
    def sonido(self):
        print('Miau')

# -------------COMPOSICIÓN
# Consiste de que una clase tiene una o mas instancias de otras clases y no hereda funciones

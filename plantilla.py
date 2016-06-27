#!/ usr/bin/python -tt
# -*- coding: utf-8 -*-
# Ronny Conde at Monkey from the Future

def posibles_desplazamientos(accion):
    """ Devuelve una lista de tuplas con los posibles desplazamientos y su
    probabilidad tras seleccionar accion (En esta funcion no puede ser 'EXIT'). 
    
    E.g. posibles_desplazamientos('W') devolvera [('W', 0.8), ('N', 0.1), ('S',
    0.1)]
    """
    pass

def siguiente_estado(estado, desplazamiento):
    """ Devuelve la celda en la que acabara el agente tras el desplazamiento
    desde estado. Los desplazamientos son deterministas. La componente
    estocastica se tuvo en cuenta en la funcion
    posibles_desplazamientos(accion). Hay que tener en cuenta el comportamiento
    ante los obstaculos y limites del laberinto.
    
    E.g. siguiente_estado((0, 1), 'E') devolvera (0, 2)
    """
    pass

def posibles_transiciones(estado, accion):
    """ Devuelve una lista de tuplas con los posibles estados tras seleccionar
    accion desde estado y sus probabilidades correspondientes. Si la accion es
    'EXIT' devolvera [(None, 1.0)].
    
    E.g. posibles_transiciones((0,0), 'W') devolvera [((0,0), 0.9), ((1,0),
    0.1)]
    """
    pass

def recompensa(estado, accion):
    """ Devuelve la recompensa que se recibira al abandonar estado tras
    seleccionar accion.
    
    E.g. recompensa((0,0), 'E') devolvera 0.0; recompensa((0,3), 'EXIT')
    devolvera 1.0
    """
    pass

def acciones_disponibles(estado):
    """ Devuelve una lista con las posibles acciones que el agente puede
    seleccionar desde estado.
    
    E.g. acciones_disponibles((0,0)) devolvera ['W', 'N', 'E', 'S'];
    acciones_disponibles((1,3)) devolvera ['EXIT']
    """
    pass

def paso(valores_estados, dicc_transiciones, gamma):
    """ Devuelve la version actualizada de valores_estados tras ejecutar un paso
    del algoritmo Value Iteration. El parametro gamma es el factor de
    descuento.
    """
    pass

def main():
    gamma = 0.9
    N = 100
  
    # Inicializamos valores_estados.
    # valores_estados es un diccionario que almacena cada posible estado, como
    # clave, asociado a su valor. El valor de un estado se define como la suma de
    # las recompensas que se recibiran hasta el final del episodio si se actua de
    # manera optima, teniendo en cuenta el factor de descuento gamma.
    # E.g. valores_estados se inicializara como {(0, 0): 0.0, (0, 1): 0.0, ... }


    # Inicializamos dicc_transiciones
    # Inicializar dicc_transiciones en la funcion main(). dicc_transiciones es un
    # diccionario con la siguiente especificacion:
    # - Claves. Tuplas con la combinacion de cada estado y sus acciones disponibles.
    # - Valores. Lista de tuplas con los posibles estados resultantes tras
    # seleccionar accion desde estado y sus probabilidades asociadas (salida de la
    # funcion posibles_transiciones). (estado, accion) es la clave asociada.
    # E.g. dicc_transiciones se inicializara como {((0,0), 'W'): [((0,0), 0.9),
    # ((1,0), 0.1)], ... }

    # Bucle para ejecutar la funcion paso N veces
    # E.g. Tras ejecutar 100 pasos el resultado tiene que ser: {(0, 1):
    # 0.7443801465395765, (1, 2): 0.5718590331455524, (0, 0):
    # 0.6449692376239595, (2, 1): 0.430844455827435, (0, 2): 0.8477662780034064,
    # (2, 0): 0.49068396358124544, (1, 3): -1.0, (2, 3): 0.27729583947027003,
    # (2, 2): 0.4754711304415913, (1, 0): 0.5663144525478669, (0, 3): 1.0}

if __name__ == "__main__":
  main()

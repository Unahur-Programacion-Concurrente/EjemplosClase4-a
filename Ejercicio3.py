"""
Ejercicio 3:

Modificar el ejercicio 2 de modo que el hilo B haga las iteraciones cada un tiempo aleatorio entre 1 y 4 hasta que todos los hilos B terminen.

Probar para verificar que no se dan condiciones de carrera con cualquier número de hilos A y B concurrentes..


"""


import random
import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

x = 0
lock1 = threading.Lock()
cantHilosActivos = 0

def hiloAFunc():
    global x
    global cantHilosActivos

    try:
        lock1.acquire()
        cantHilosActivos += 1
    finally:
        lock1.release()

    logging.info(f'Arranca hilo A {threading.current_thread().name} y el valor de x es {x}')
    numIterac = random.randint(10, 100)
    logging.info(f'Arranca hilo A {threading.current_thread().name} va a contar hasta {numIterac}')
    for iteraciones in range(numIterac):
        try:
            lock1.acquire()
            x += 1
        finally:
            lock1.release()
            time.sleep(random.randint(0,1))
    logging.info(f'Termina hilo A {threading.current_thread().name} y el valor de x es {x}')
    try:
        lock1.acquire()
        cantHilosActivos -= 1
    finally:
        lock1.release()

def hiloBFunc():

    global x
    global cantHilosActivos

    logging.info(f'Hilo B {threading.current_thread().name} arrancó')
    # Si no hay hilos A activos, espera
    while (cantHilosActivos == 0):
        pass

    while (cantHilosActivos != 0):
        try:
            lock1.acquire()
            logging.info(f'El valor de x es {x}, cantidad de hilos A es {cantHilosActivos}')
        finally:
            lock1.release()
            time.sleep(random.randint(1,4))

    logging.info(f'Hilo B {threading.current_thread().name} termino')


def main():
    hilos = []
    for hiloA in range(random.randint(5,10)):
        tA = threading.Thread(target=hiloAFunc)
        hilos.append(tA)

    for hiloB in range(random.randint(1,3)):
        tB = threading.Thread(target=hiloBFunc)
        hilos.append(tB)

    for hAB in hilos:
       hAB.start()

    for hAB in hilos:
        hAB.join()


if __name__ == '__main__':
    main()
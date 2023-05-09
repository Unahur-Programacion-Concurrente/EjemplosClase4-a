"""
Ejercicio 2:

Modificar el ejercicio 1 de modo que se lancen 3 hilos tipo A y uno tipo B y que no existan condiciones de carrera.

Probar para verificar que no se dan condiciones de carrera con cualquier número de hilos A y B concurrentes..

"""


import random
import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

x = 0
lock1 = threading.Lock()

def hiloAFunc():
    global x
    logging.info(f'Arranca {threading.current_thread().name} y el valor de x es {x}')
    numIterac = random.randint(10, 100)
    logging.info(f'Arranca {threading.current_thread().name} va a contar hasta {numIterac}')
    for iteraciones in range(numIterac):
        try:
            lock1.acquire()
            x += 1
        finally:
            lock1.release()
            time.sleep(random.randint(0,1))
    logging.info(f'Termina {threading.current_thread().name} y el valor de x es {x}')

def hiloBFunc():

    global x
    logging.info(f'{threading.current_thread().name} arrancó')

    for iteraciones in range(random.randint(10, 50)):
        try:
            lock1.acquire()
            logging.info(f'El valor de x es {x}')
        finally:
            lock1.release()
            time.sleep(random.randint(1,4))
    logging.info(f'Thread {threading.current_thread().name} termino')


def main():
    hilos = []
    for hiloA in range(3):
        tA = threading.Thread(target=hiloAFunc)
        hilos.append(tA)

    tB = threading.Thread(target=hiloBFunc)
    hilos.append(tB)

    for hAB in hilos:
       hAB.start()

    for hAB in hilos:
        hAB.join()


if __name__ == '__main__':
    main()
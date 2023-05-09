"""
Ejercicio 1:

Implemente un programa que lance dos hilos A y B, ambos con acceso a una variable X (global) inicializada en cero.

- El hilo A incrementa X en 1 hasta llegar a una cantidad aleatoria entre 50 y 100 intercalando un retardo aleatorio
 entre 0 y 1 segundo entre cada incremento de X.
- El hilo B hará una número aleatorio entre 10 y 100 iteraciones cada un tiempo aleatorio entre 1 y 2 segundos,
imprimiendo el valor de X en cada iteración.

- Tanto A como B deberán imprimir mensajes al arrancar y al terminar, identificando al hilo.

- El hilo A deberá también indicar el valor final de X en el mensajel final.

"""


import random
import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

x = 0

def hiloAFunc():
    global x
    logging.info(f'Arranca {threading.current_thread().name} y el valor de x es {x}')

    for iteraciones in range(random.randint(10, 100)):
        x += 1
        time.sleep(random.randint(0,1))
    logging.info(f'Termina {threading.current_thread().name} y el valor de x es {x}')

def hiloBFunc():

    global x
    logging.info(f'{threading.current_thread().name} arrancó')

    for iteraciones in range(random.randint(10, 50)):
        logging.info(f'El valor de x es {x}')
        time.sleep(random.randint(1,4))
    logging.info(f'Thread {threading.current_thread().name} termino')


def main():
    threadA1 = threading.Thread(target=hiloAFunc)
    threadB = threading.Thread(target=hiloBFunc)

    threadA1.start()
    threadB.start()

    threadA1.join()
    threadB.join()

if __name__ == '__main__':
    main()
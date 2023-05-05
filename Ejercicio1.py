import random
import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

x = 0

def hiloAFunc():
    global x
    logging.info(f'Soy {threading.current_thread().name} y el valor de x es {x}')
    while(x < random.randint(50, 100)):
        x += 1
        time.sleep(random.randint(0,1))
    logging.info(f'Soy {threading.current_thread().name} y el valor de x es {x}')

def hiloBFunc():

    global x
    logging.info(f'{threading.current_thread().name} arrancó')
    while(x < random.randint(10, 100)):
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
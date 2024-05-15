

import time

def contador(segundos):
    for i in range(segundos, 0, -1):
        print(i)
        time.sleep(1)

    print("¡Tiempo terminado!")

contador(10)  # Esto imprimirá un contador desde 20 hasta 1, esperando un segundo entre cada número
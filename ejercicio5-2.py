import time

def contador(segundos):
    for i in range(segundos, -1, -1):
        print(i)
        time.sleep(1)

    print("¡Tiempo terminado!")

contador(10) 

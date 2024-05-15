#Cree un programa en Python que imprima la hora del sistema, estado de memoria
#RAM y almacenamiento disponible en la partición montada en “/”

import psutil
import datetime

def obtener_informacion_sistema():
    # Obtener la hora del sistema
    hora_actual = datetime.datetime.now()
    print("Hora del sistema:", hora_actual)

    # Obtener estado de la memoria RAM
    estado_memoria = psutil.virtual_memory()
    print("Memoria RAM total:", round(estado_memoria.total / (1024 ** 3), 2), "GB")
    print("Memoria RAM disponible:", round(estado_memoria.available / (1024 ** 3), 2), "GB")
    print("Porcentaje de uso de la memoria RAM:", estado_memoria.percent, "%")

    # Obtener almacenamiento disponible en la partición "/"
    estado_almacenamiento = psutil.disk_usage('/')
    print("Almacenamiento total en la partición '/':", round(estado_almacenamiento.total / (1024 ** 3), 2), "GB")
    print("Almacenamiento disponible en la partición '/':", round(estado_almacenamiento.free / (1024 ** 3), 2), "GB")
    print("Porcentaje de uso de almacenamiento en la partición '/':", estado_almacenamiento.percent, "%")

# Llamar a la función para obtener la información del sistema
obtener_informacion_sistema()

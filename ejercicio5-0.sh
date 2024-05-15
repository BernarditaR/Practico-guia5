#Cree un programa en BASH, que invoque a tres programas en python, donde cada
#uno es un contador (con avance cada un segundo) hasta un número que se pase
#por entrada. Cada programa en python debe imprimir el contador
#segundo-a-segundo.
    #a. Identifique el PID de cada proceso python
    #b. ¿Los procesos de ejecutan de manera secuencial?, ¿Cómo hacer para que corran todos a la vez?


#!/bin/bash

read $1

python3 ejercicio5-1.py $1 &
pid1=$!
python3 ejercicio5-2.py $1 &
pid2=$!
python3 ejercicio5-3.py $1 &
pid3=$!

# Imprimir los PID de los procesos
echo "PID del script 1: $pid1"
echo "PID del script 2: $pid2"
echo "PID del script 3: $pid3"


#agregando & corren todos a la vez



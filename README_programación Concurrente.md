# Asignación de Programación Concurrente

Este proyecto aborda el problema de realizar tareas concurrentes en un programa de Python, utilizando hilos para ejecutar dos operaciones simultáneamente: obtener los precios actuales de acciones y calcular el factorial de un número.

## Descripción del Problema

El programa tiene como objetivo resolver dos problemas a la vez:
1. **Obtención de precios de acciones**: El programa consulta periódicamente los precios de una lista de acciones en tiempo real usando la librería `yfinance`.
2. **Cálculo de un factorial**: Se calcula el factorial de un número de manera recursiva, demostrando la ejecución de tareas simultáneas.

## Solución Propuesta

El programa utiliza **programación concurrente** mediante hilos (`threading`), donde cada hilo se encarga de obtener el precio de una acción mientras otro hilo calcula el factorial de un número. Este enfoque permite que ambas tareas se realicen sin bloquearse mutuamente, mejorando la eficiencia del programa.

### Funcionamiento del Programa

1. **Obtención de precios de acciones**: Se crea un hilo por cada acción en la lista `lista_acciones`. Cada hilo ejecuta la función `obtener_precio`, que obtiene y muestra el precio más reciente de la acción cada 10 segundos.
2. **Cálculo del factorial**: Independientemente de los hilos de obtención de precios, el programa calcula y muestra el factorial de un número utilizando una función recursiva.

### Librerías utilizadas

- `yfinance`: Para obtener los precios de las acciones desde Yahoo Finance.
- `time`: Para controlar las pausas de 10 segundos entre actualizaciones de precios.
- `threading`: Para manejar la ejecución concurrente de hilos.

## Uso

Para ejecutar el programa, primero asegúrate de tener instalada la librería `yfinance`:

```bash
pip install yfinance
Luego, ejecuta el programa:

bash
Copiar
Editar
Pogramacion_Concurrente.py

LINK DEL VIDEO EN YOUTUBE:
https://www.youtube.com/watch?v=GuuIJccN21w


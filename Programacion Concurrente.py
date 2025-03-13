import yfinance as yf
import time
import threading

def obtener_precio(accion):
    """
    Función que obtiene y muestra el precio actual de una acción específica.
    Se ejecuta en un bucle infinito con pausas de 10 segundos.
    """
    while True:
        stock = yf.Ticker(accion)
        precio = stock.history(period='1d').iloc[-1]['Close']
        print(f"{accion}: ${precio:.2f}")
        time.sleep(10)

def calcular_factorial(n):
    """
    Función recursiva para calcular el factorial de un número.
    """
    if n == 0 or n == 1:
        return 1
    return n * calcular_factorial(n - 1)

def main():
    lista_acciones = ["AAPL", "GOOGL", "MSFT", "AMZN"]  # Lista de símbolos de acciones
    threads = []
    
    # Creación de un hilo para cada acción
    for accion in lista_acciones:
        thread = threading.Thread(target=obtener_precio, args=(accion,))
        threads.append(thread)
        thread.start()
    
    # Ejemplo de recursión
    numero = 5  # Número para calcular el factorial
    print(f"El factorial de {numero} es: {calcular_factorial(numero)}")
    
    # Mantener los hilos en ejecución
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
import yfinance as yf
import time

def obtener_precio(acciones):
    while True:
        print("\nActualización de precios de acciones:")
        for accion in acciones:
            stock = yf.Ticker(accion)
            precio = stock.history(period='1d').iloc[-1]['Close']
            print(f"{accion}: ${precio:.2f}")
        time.sleep(10)  # Espera 10 segundos antes de actualizar

if __name__ == "__main__":
    lista_acciones = ["AAPL", "GOOGL", "MSFT", "AMZN"]  # Lista de símbolos de acciones
    obtener_precio(lista_acciones)
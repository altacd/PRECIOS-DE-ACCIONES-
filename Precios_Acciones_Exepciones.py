import yfinance as yf
import time

def obtener_precio(acciones):
    while True:
        print("\nActualización de precios de acciones:")
        for accion in acciones:
            try:
                stock = yf.Ticker(accion)
                historial = stock.history(period='1d')

                # Verificar si el historial tiene datos
                if historial.empty:
                    raise ValueError(f"No se encontraron datos para la acción {accion}")

                precio = historial.iloc[-1]['Close']
                print(f"{accion}: ${precio:.2f}")

            except ValueError as ve:
                print(f"Error de valor: {ve}")
            except KeyError:
                print(f"Error al acceder a los datos de {accion}.")
            except Exception as e:
                print(f"Error inesperado al obtener {accion}: {e}")

        time.sleep(10)  # Espera 10 segundos antes de actualizar

if __name__ == "__main__":
    lista_acciones = ["AAPL", "GOOGL", "MSFT", "AMZN", "XXXX"]  # "XXXX" es una acción inválida para probar excepciones
    obtener_precio(lista_acciones)
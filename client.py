'''
    ANGEL GABRIEL SOSA MORALES
    SISTEMAS OPERATIVOS I
    RPC - Cliente para Calcular Raíz Cuadrada

    Este script de cliente se utiliza para conectarse a un servidor RPC y calcular las raíces 
    de una ecuación cuadrática
    proporcionando los coeficientes a, b y c como argumentos de línea de comandos.

    Uso:
    python client.py 'a: int' 'b: int' 'c: int'

    Donde 'a', 'b' y 'c' son los coeficientes de la ecuación cuadrática
    de la forma ax^2 + bx + c = 0.

    Ejemplo:
    python client.py 1 2 -3

    Este ejemplo calculará las raíces de la ecuación x^2 + 2x - 3 = 0 y mostrará los resultados.

    Requiere que el servidor RPC esté en funcionamiento y accesible en la dirección proporcionada.
'''

from xmlrpc.client import ServerProxy
import sys

server = ServerProxy('http://192.168.0.192:5050', allow_none=True)
arguments = sys.argv

if __name__ == '__main__':
    if len(arguments) < 2:
        print("El formato debe ser python client.py 'a: int' 'b: int' 'c: int'")
    else:
        value = int(arguments[1])
        result = server.raiz(int(arguments[1]), int(arguments[2]), int(arguments[3]))
        print(f'<-- Resultados -->\n{result}')

'''
        Script cliente para calcular el perímetro y área de un cuadrado mediante RPC.

        Este script se utiliza para conectarse a un servidor RPC que proporciona
        dos métodos remotos, 'calc_perimetro' y 'calc_area', los cuales calculan
        el perímetro y el área de un cuadrado, respectivamente.

        Args:
            Se espera que se proporcione un argumento en la línea de comandos que
            represente el lado del cuadrado en forma de un número entero.

        Ejemplo de uso:
            Para calcular el perímetro y el área de un cuadrado con lado 5:
            $ python client.py 5
            Perimetro: 20
            Area: 25
'''

from xmlrpc.client import ServerProxy
import sys

s = ServerProxy('http://192.168.0.192:5000', allow_none=True)
arguments = sys.argv

if __name__ == '__main__':
    if len(arguments) < 2:
        print("El formato debe ser python client.py 'lado: int'")
    else:
        value = int(arguments[1])
        print(f'Perimetro: {s.calc_perimetro(value)}\nArea: {s.calc_area(value)}\n')

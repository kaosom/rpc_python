'''
    ANGEL GABRIEL SOSA MORALES 
    SISTEMAS OPERATIVOS I 
    RPC - Calcular raiz cuadrada
'''

from xmlrpc.server import SimpleXMLRPCServer
from math import sqrt

class RPC:
    '''
        Clase que almacena nuestro servidor simple usando SimpleXMLRPCServer
    '''
    def __init__(self, direccion, port):
        '''
        Constructor de la clase RPC.

        Parameters:
            direccion (str): La dirección en la que se va a iniciar el servidor.
            port (int): El número de puerto en el que se va a iniciar el servidor.
        '''
        self.server = SimpleXMLRPCServer((direccion, port), allow_none=True)
        self.server.register_function(getattr(self, 'raiz'))

    def is_real(self, a : int, b: int, c: int) -> bool:
        '''
        Comprueba si las raíces son números reales.

        Parameters:
            a (int): Coeficiente cuadrático.
            b (int): Coeficiente lineal.
            c (int): Término independiente.

        Returns:
            bool: True si las raíces son números reales, False en caso contrario.
        '''
        return ((b * b) - 4 * a * c) > 0

    def raiz(self, a: int, b: int, c: int) -> str:
        '''
        Calcula las raíces de una ecuación cuadrática y devuelve el resultado como una cadena.

        Parameters:
            a (int): Coeficiente cuadrático.
            b (int): Coeficiente lineal.
            c (int): Término independiente.

        Returns:
            str: Una cadena que representa las raíces de la ecuación cuadrática.
        '''
        if self.is_real(a, b, c):
            root1 = ((-1 * b) + sqrt((b * b) - 4 * a * c)) / (2 * a)
            root2 = ((-1 * b) - sqrt((b * b) - 4 * a * c)) / (2 * a)
            return f'x1 = {root1:.2f}\nx2 = {root2:.2f}'
        else:
            temp = ((b * b) - (4 * a * c)) * -1
            real_part = (-1 * b) / (2 * a)
            imaginary_part = (sqrt(temp)) / (2 * a)
            return f'x1 = {real_part} + {imaginary_part}i\nx2 = {real_part} - {imaginary_part}i'

    def run(self):
        '''
        Inicia el servidor RPC y lo pone en modo de espera para recibir solicitudes.
        '''
        self.server.serve_forever()
        print("Server iniciado")

if __name__ == '__main__':
    rpc = RPC('', 5050)
    print('Iniciando servidor...')
    rpc.run()

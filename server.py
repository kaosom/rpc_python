'''
    ANGEL GABRIEL SOSA MORALES 
    SISTEMAS OPERATIVOS I 
    RPC - Calcular Area y Perimetro

'''

from xmlrpc.server import SimpleXMLRPCServer
class RPC:
    '''
        Clase que implementa un servidor RPC simple para cálculo de área y perímetro.

        Esta clase utiliza la biblioteca SimpleXMLRPCServer
        para registrar métodos remotos que calculan el perímetro y el área de un cuadrado.

        Args:
            direccion (str): La dirección IP en la que se va a ejecutar el servidor.
            port (int): El puerto en el que se va a escuchar para las solicitudes RPC.

        Attributes:
            methods (list): Lista de nombres de métodos remotos disponibles en el servidor.

        Methods:
            calc_perimetro(a): Método remoto que calcula el perímetro de un cuadrado.
            calc_area(a): Método remoto que calcula el área de un cuadrado.
        '''
    methods = ['calc_perimetro', 'calc_area']
    def __init__(self, direccion, port):
        self.server = SimpleXMLRPCServer((direccion, port), allow_none=True)
        for method in self.methods:
            self.server.register_function(getattr(self, method))
    def calc_perimetro(self, a):
        '''
        Calcula el perímetro de un cuadrado.

        Este método toma un valor numérico 'a' que representa el lado del cuadrado
        y calcula el perímetro multiplicando el lado por 4.

        Args:
            a (float): El lado del cuadrado.

        Returns:
            float: El valor del perímetro del cuadrado.

        Ejemplo de uso:
            >>> rpc = RPC('', 5000)
            >>> rpc.calc_perimetro(5)
            20.0
        '''
        return 4 * a

    def calc_area(self, a):
        '''
        Calcula el área de un cuadrado.

        Este método toma un valor numérico 'a' que representa el lado del cuadrado
        y calcula el área multiplicando el lado por sí mismo (elevado al cuadrado).

        Args:
            a (float): El lado del cuadrado.

        Returns:
            float: El valor del área del cuadrado.

        Ejemplo de uso:
            >>> rpc = RPC('', 5000)
            >>> rpc.calc_area(5)
            25.0
        '''
        return a * a


    def run(self):
        '''
            run(): Inicia el servidor RPC y lo pone en modo de espera para recibir solicitudes.
        '''
        self.server.serve_forever()
        print("Server iniciado")
if __name__ == '__main__':
    rpc = RPC('', 5000)
    print('Iniciando servidor...')
    rpc.run()
    
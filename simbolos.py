from enum import Enum


class TIPO_DATO(Enum):
    NULL = 0
    ENTERO = 1
    FLOAT = 2
    STRING = 3
    BOOLEAN = 4
    CHAR = 5
    FUNCION = 10


class Simbolos():  # VALOR - NODO

    def __init__(self, id, tipo, valor, instrucciones=[], parametros=[], props={}, cte=0):
        self.id = id
        self.tipo = tipo
        self.valor = valor
        self.instrucciones = instrucciones
        self.parametros = parametros
        self.props = props
        self.cte = cte


class TablaSimbolos():

    def __init__(self, simbolos={}):
        self.simbolos = simbolos

    def agregar(self, simbolo):
        self.simbolos[simbolo.id] = simbolo

    def obtener(self, id):
        if not id in self.simbolos:
            print('Error: variable no definida')
        else:
            return self.simbolos[id]

    def actualizar(self, id, valor):
        if not id in self.simbolos:
            print('Nueva variable definida')
        else:
            self.simbolos[id].valor = valor

    def obtener_datos(self):
        # Obtener las claves (IDs) de los símbolos y ordenarlas
        claves_ordenadas = sorted(self.simbolos.keys())
        datos = ""
        # Recorrer las claves ordenadas y obtener los datos de los símbolos

        for clave in claves_ordenadas:
            simbolo = self.simbolos[clave]
            datos += f"ID: {simbolo.id}, Valor: {simbolo.valor} , Tipo: {simbolo.tipo}\n"
        return datos

from enum import Enum


class TIPO_DATO(Enum):
    ENTERO = 1
    STRING = 1
    FUNCION = 10


class Simbolos():  # VALOR - NODO

    def __init__(self, id, tipo, valor, instrucciones=[], parametros=[], props={}):
        self.id = id
        self.tipo = tipo
        self.valor = valor
        self.instrucciones = instrucciones
        self.parametros = parametros
        self.props = props


class TablaSimbolos():

    def __init__(self, simbolos={}):
        self.simbolos = simbolos

    def agregar(self, simbolo):
        self.simbolos[simbolo.id] = simbolo

    def obtener(self, id):
        if not id in self.simbolos:
            from interfaz import errores
            err = 'Error variable no definida'
            errores.append(err)
        else:
            return self.simbolos[id]

    def actualizar(self, id, valor):
        if not id in self.simbolos:
            from interfaz import errores
            err = 'Error variable no definida'
            errores.append(err)
        else:
            self.simbolos[id].valor = valor

    def obtener_datos(self):
        # Obtener las claves (IDs) de los símbolos y ordenarlas
        claves_ordenadas = sorted(self.simbolos.keys())
        datos = ""
        # Recorrer las claves ordenadas y obtener los datos de los símbolos
        for clave in claves_ordenadas:
            simbolo = self.simbolos[clave]
            datos += f"ID: {simbolo.id}, Valor: {simbolo.valor}\n"
        return datos

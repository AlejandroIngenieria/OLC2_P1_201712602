from enum import Enum


class OPERACION_ARITMETICA(Enum):
    MAS = 1
    MENOS = 2
    POR = 3
    DIVIDIDO = 4
    MODULO = 5


class OPERACION_LOGICA(Enum):
    MENORQUE = 0
    MENORIGUAL = 1
    MAYORIGUAL = 2
    MAYOR = 3
    IGUALQUE = 4
    DIFERENTE = 5
    IGUAL = 6
    AND = 7
    OR = 8
    NOT = 9


class ExpresionNumerica:
    '''
        Esta clase representa una expresión numérica
    '''


class ExpresionBinaria(ExpresionNumerica):

    def __init__(self, exp1, exp2, operador):
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador


class ExpresionLogica():
    def __init__(self, exp1, exp2, operador):
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador


class ExpresionNegativo(ExpresionNumerica):
    def __init__(self, val=0):
        self.val = val


class ExpresionNumero(ExpresionNumerica):

    def __init__(self, val=0):
        self.val = val
        

class ExpresionDecimal(ExpresionNumerica):

    def __init__(self, val=0.0):
        self.val = val
        

class ExpresionID(ExpresionNumerica):
    def __init__(self, id):
        self.id = id


class ExpresionAccesoInterface(ExpresionNumerica):
    def __init__(self, id, prop):
        self.id = id
        self.prop = prop


class ExpresionCadena:
    ''' Clase abstracta para cadenas'''


class ExpresionConsoleLog(ExpresionCadena):
    def __init__(self, val):
        #print("val", val)
        self.val = val


class ExpresionInterface:
    def __init__(self, id, props):
        self.id = id
        self.props = props

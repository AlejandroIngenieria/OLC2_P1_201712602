class Instruccion:
    '''Clase abs de instrucciones'''


class Imprimir(Instruccion):

    def __init__(self, cad):
        self.cad = cad


class Declaracion(Instruccion):
    def __init__(self, id, exp, tipo):
        self.id = id
        self.tipo = tipo
        self.exp = exp
        #print("declaracion ID: ", self.id, " Valor: ", self.exp, " Tipo: ",self.tipo)


class Constante(Instruccion):
    def __init__(self, id, exp, tipo):
        self.id = id
        self.exp = exp
        self.tipo = tipo
        print("Constante ID: ", self.id, " Valor: ",self.exp, " Tipo: ", self.tipo)


class Asignacion(Instruccion):
    def __init__(self, id, exp, sim):
        self.id = id
        self.exp = exp
        self.sim = sim
        print("id: ", self.id, " exp: "+str(self.exp.val)+" sim: "+self.sim)

class Ternario(Instruccion):
    def __init__(self, expLogica, valTrue, valFalse):
        print("Ternario")
        print("expLogica", expLogica.val)
        print("valTrue", valTrue.val)
        print("valFalse", valFalse.val)
        self.expLogica = expLogica
        self.valT = valTrue
        self.valF = valFalse

class If(Instruccion):
    def __init__(self, expLogica, instrucciones=[]):
        self.expLogica = expLogica
        self.instrucciones = instrucciones


class IfElse(Instruccion):
    def __init__(self, expLogica, instrIfVerdadero=[], instrIfFalso=[]):
        self.expLogica = expLogica
        self.instrIfVerdadero = instrIfVerdadero
        self.instrIfFalso = instrIfFalso


class Function(Instruccion):
    def __init__(self, id, ret_, parametros=[], instrucciones=[]):
        self.id = id
        self.parametros = parametros
        self.instrucciones = instrucciones


class CallFunction(Instruccion):
    def __init__(self, id, params=[]):
        self.id = id
        self.params = params

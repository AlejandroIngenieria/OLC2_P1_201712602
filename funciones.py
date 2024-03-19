from simbolos import TablaSimbolos, Simbolos, TIPO_DATO
from expresiones import *
from instrucciones import *


def procesar_imprimir(instr, ts):
    # print('>> ', resolver_expresion(instr.cad, ts))
    return resolver_expresion(instr.cad, ts)

def procesar_declaracion(instr, ts):
    from interfaz import errores
    id = instr.id
    tipo = instr.tipo
    exp = resolver_expresion(instr.exp, ts)
    if exp == "true" or exp == "false":
        tipo = "boolean"

    if tipo == "null":
        tipo = type(exp).__name__
        print("tipo: ", tipo)
        if tipo == "str":
            tipo = "string"
        elif tipo == "int":
            tipo = "number"
    else:
        valTipo = type(exp).__name__
        if valTipo == "str":
            valTipo = "string"
        elif valTipo == "int":
            valTipo = "number"
        if tipo != valTipo:
            errores.append(
                f"Error: no se puede asignar un {valTipo} a un {tipo}")
            return

    sim = ts.obtener(id)
    if sim:
        if sim.cte == 1:
            errores.append("Error: no se puede cambiar una constante")
            return
        if sim.tipo == tipo:
            simbolo = Simbolos(id, tipo, exp)
        else:
            errores.append(
                f"Error: no se puede asignar un {tipo} a un {sim.tipo}")
            return
    else:
        simbolo = Simbolos(id, tipo, exp)
    ts.agregar(simbolo)

def procesar_asignacion(instr, ts):
    id = instr.id
    exp = resolver_expresion(instr.exp, ts)
    ts.actualizar(id, exp)

def procesar_constante(instr, ts):
    from interfaz import errores
    id = instr.id
    tipo = instr.tipo
    exp = resolver_expresion(instr.exp, ts)
    if exp == "true" or exp == "false":
        tipo = "boolean"

    if tipo == "null":
        tipo = type(exp).__name__
        print("tipo: ", tipo)
        if tipo == "str":
            tipo = "string"
        elif tipo == "int":
            tipo = "number"
    else:
        valTipo = type(exp).__name__
        if valTipo == "str":
            valTipo = "string"
        elif valTipo == "int":
            valTipo = "number"
        if tipo != valTipo:
            errores.append(
                f"Error: no se puede asignar un {valTipo} a un {tipo}")
            return

    sim = ts.obtener(id)
    if sim:
        errores.append("Error: la variable ya existe")
        return
    else:
        simbolo = Simbolos(id, tipo, exp)
        simbolo.cte = 1
    ts.agregar(simbolo)

def procesar_if(instr, ts):
    expLog = resolver_expresion_logica(instr.expLogica, ts)
    if expLog:
        TablaLocal = TablaSimbolos(ts.simbolos.copy())
        return procesar_instrucciones(instr.instrucciones, TablaLocal)

def procesar_if_else(instr, ts):
    expLog = resolver_expresion_logica(instr.expLogica, ts)
    if expLog:
        TablaLocal = TablaSimbolos(ts.simbolos.copy())
        return procesar_instrucciones(instr.instrIfVerdadero, TablaLocal)
    else:
        TablaLocal = TablaSimbolos(ts.simbolos.copy())
        return procesar_instrucciones(instr.instrIfFalso, TablaLocal)

def resolver_expresion_aritmetica(expNum, ts):
    if isinstance(expNum, ExpresionBinaria):
        exp1 = resolver_expresion_aritmetica(expNum.exp1, ts)
        exp2 = resolver_expresion_aritmetica(expNum.exp2, ts)
        print("exp1: ", exp1)
        print("exp2: ", exp2)

        if expNum.operador == OPERACION_ARITMETICA.MAS:
            return exp1 + exp2
        if expNum.operador == OPERACION_ARITMETICA.MENOS:
            return exp1 - exp2
        if expNum.operador == OPERACION_ARITMETICA.POR:
            return exp1 * exp2
        if expNum.operador == OPERACION_ARITMETICA.DIVIDIDO:
            if type(exp1).__name__ == "int" and type(exp2).__name__ == "int":
                return int(exp1/exp2)
            return exp1 / exp2
        if expNum.operador == OPERACION_ARITMETICA.MODULO:
            return exp1 % exp2

    elif isinstance(expNum, ExpresionNumero):
        return expNum.val
    elif isinstance(expNum, ExpresionDecimal):
        return expNum.val
    elif isinstance(expNum, ExpresionConsoleLog):
        return expNum.val
    elif isinstance(expNum, ExpresionID):
        exp_id = ts.obtener(expNum.id)
        return exp_id.valor
    elif isinstance(expNum, ExpresionAccesoInterface):
        exp_id = ts.obtener(expNum.id)

        if expNum.prop in exp_id.props:
            return exp_id.props[expNum.prop]

        return None

def resolver_expresion_logica(expLog, ts):
    exp1 = resolver_expresion_aritmetica(expLog.exp1, ts)
    exp2 = resolver_expresion_aritmetica(expLog.exp2, ts)
    if expLog.operador == OPERACION_LOGICA.IGUALQUE:
        return exp1 == exp2
    if expLog.operador == OPERACION_LOGICA.DIFERENTE:
        return exp1 != exp2
    if expLog.operador == OPERACION_LOGICA.MAYOR:
        return exp1 > exp2
    if expLog.operador == OPERACION_LOGICA.MAYORIGUAL:
        return exp1 >= exp2
    if expLog.operador == OPERACION_LOGICA.MENORQUE:
        return exp1 < exp2
    if expLog.operador == OPERACION_LOGICA.MENORIGUAL:
        return exp1 <= exp2
    
def procesar_funcion(instr, ts):
    fun_ = ts.obtener(instr.id).instrucciones
    params_ = ts.obtener(instr.id).parametros
    if len(fun_) > 0:
        TablaLocal = TablaSimbolos(ts.simbolos.copy())
        for i in range(len(instr.params)):
            exp = resolver_expresion(instr.params[i], TablaLocal)
            TablaLocal.agregar(Simbolos(params_[i], TIPO_DATO.ENTERO, exp))
        procesar_instrucciones(fun_, TablaLocal)

        if fun_.ret_ is not None:
            # return resolver(exp)
            pass

def guardar_funcion(instr, ts):
    funcion_id = instr.id

    simbolo = Simbolos(funcion_id, TIPO_DATO.FUNCION,
                       instr.parametros, instr.instrucciones, instr.parametros)
    ts.agregar(simbolo)

def guardar_interface(instr, ts):
    interface_id = instr.id

    props = instr.props
    keys = list(props.keys())
    values = list(props.values())

    for i in range(len(keys)):
        instr.props[keys[i]] = resolver_expresion(values[i], ts)

    simbolo = Simbolos(interface_id, TIPO_DATO.FUNCION,
                       valor=None, props=instr.props)
    ts.agregar(simbolo)


def resolver_expresion(expCad, ts):
    if isinstance(expCad, ExpresionBinaria):
        exp = resolver_expresion_aritmetica(expCad, ts)
        return exp
    elif isinstance(expCad, ExpresionLogica):
        exp = resolver_expresion_logica(expCad, ts)
        return exp
    elif isinstance(expCad, ExpresionConsoleLog):
        return expCad.val
    elif isinstance(expCad, ExpresionID):
        exp_id = ts.obtener(expCad.id)
        if exp_id.valor is None:
            return exp_id.props

        return exp_id.valor
    elif isinstance(expCad, ExpresionAccesoInterface):
        exp_id = ts.obtener(expCad.id)

        if expCad.prop in exp_id.props:
            return exp_id.props[expCad.prop]

        return None
    elif isinstance(expCad, ExpresionNumero):
        return expCad.val
    elif isinstance(expCad, ExpresionDecimal):
        return expCad.val
    elif isinstance(expCad, ExpresionNegativo):
        return -expCad.val.val
    else:
        print('Error: Expresión cadena no válida')


def procesar_instrucciones(instrucciones, ts, save=False):
    from interfaz import resultados, errores
    for instr in instrucciones:
        if not save:
            if isinstance(instr, Imprimir):
                resultados.append(procesar_imprimir(instr, ts))
                # return procesar_imprimir(instr, ts)
            elif isinstance(instr, Declaracion):
                procesar_declaracion(instr, ts)
            elif isinstance(instr, Asignacion):
                procesar_asignacion(instr, ts)
            elif isinstance(instr, Constante):
                procesar_constante(instr, ts)
            elif isinstance(instr, If):
                resultados.append(procesar_if(instr, ts))
                # return procesar_if(instr, ts)
            elif isinstance(instr, IfElse):
                resultados.append(procesar_if_else(instr, ts))
                # return procesar_if_else(instr, ts)
            elif isinstance(instr, CallFunction):
                procesar_funcion(instr, ts)
            elif isinstance(instr, Function):
                pass
            elif isinstance(instr, ExpresionInterface):
                pass
            else:
                print('Error: instrucción no válida')
                errores.append('Error: instrucción no válida')
                return 'Error: instrucción no válida'
        else:
            '''OTRA VERIFICACION PARA LA CLASE FUNCION'''
            '''
                si tiene o no parametros
                lista_instruciones

                -> Primer recorrdio 
                    -> TS va a guardar ID -> {Valor}
            '''
            if isinstance(instr, Function):
                guardar_funcion(instr, ts)
            elif isinstance(instr, ExpresionInterface):
                guardar_interface(instr, ts)

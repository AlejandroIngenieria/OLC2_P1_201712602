import ply.lex as Lex
import ply.yacc as yacc
from instrucciones import *
from expresiones import *
from lexico import *

# ? ---------------------------------------------------------------------------- #
# ?                              ANALISIS SINTACTICO                             #
# ? ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
#                                    INICIO                                    #
# ---------------------------------------------------------------------------- #


def p_init(t):
    'init            : instrucciones'
    t[0] = t[1]

# ---------------------------------------------------------------------------- #
#                       RECURSIVIDAD DE LAS INSTRUCCIONES                      #
# ---------------------------------------------------------------------------- #


def p_instrucciones_lista(t):
    '''instrucciones    : instrucciones instruccion'''
    t[1].append(t[2])
    t[0] = t[1]

# ---------------------------------------------------------------------------- #
#                           LLAMADO DE LA INSTRUCCION                          #
# ---------------------------------------------------------------------------- #


def p_instrucciones_instruccion(t):
    'instrucciones    : instruccion '
    t[0] = [t[1]]

# ---------------------------------------------------------------------------- #
#                           LISTADO DE INSTRUCCIONES                           #
# ---------------------------------------------------------------------------- #


def p_instruccion(t):
    '''instruccion  : imprimir_instr PUNTOCOMA
                    | declaracion_instr PUNTOCOMA
                    | asignacion_instr PUNTOCOMA
                    | constante_instr PUNTOCOMA

    '''
    # | ternario_instr PUNTOCOMA
    # | if_instr PUNTOCOMA
    # | if_else_instr PUNTOCOMA
    # | funcion_instr
    # | call_funcion_instr
    # | interface_instr
    t[0] = t[1]
# ---------------------------------------------------------------------------- #
#                              IMPRIMIR EN CONSOLA                             #
# ---------------------------------------------------------------------------- #


def p_instruccion_console(t):
    '''imprimir_instr : CONSOLE PUNTO LOG PARIZQ expresionCadena PARDER'''
    t[0] = Imprimir(t[5])

# ---------------------------------------------------------------------------- #
#                                TIPOS DE DATOS                                #
# ---------------------------------------------------------------------------- #


def p_tipo_dato(t):
    """ tipo_dato : STRING
                  | NUMBER
                  | FLOAT
                  | BOOLEAN
                  | CHAR
    """
    t[0] = str(t[1])


# ---------------------------------------------------------------------------- #
#                           DECLARACION DE VARIABLES                           #
# ---------------------------------------------------------------------------- #

def p_instruccion_declaracion(t):
    '''declaracion_instr : LET ID IGUAL expresion
                        | VAR ID IGUAL expresion
                        | LET ID DOSPUNTOS tipo_dato
                        | VAR ID DOSPUNTOS tipo_dato
                        | LET ID DOSPUNTOS tipo_dato IGUAL expresion
                        | VAR ID DOSPUNTOS tipo_dato IGUAL expresion
                          '''
    if len(t) == 5:
        if t[4] in datos:
            t[0] = Declaracion(t[2], 0, t[4])
        else:
            t[0] = Declaracion(t[2], t[4], "null")
    else:
        t[0] = Declaracion(t[2], t[6], t[4])

# ---------------------------------------------------------------------------- #
#                            ASIGNACION DE VARIABLES                           #
# ---------------------------------------------------------------------------- #


def p_instruccion_asignacion(t):
    '''asignacion_instr : ID IGUAL expresion'''
    t[0] = Asignacion(t[1], t[3])

# ---------------------------------------------------------------------------- #
#                           DECLARACION DE CONSTANTES                          #
# ---------------------------------------------------------------------------- #


def p_instruccion_constantes(t):
    '''constante_instr : CONST ID IGUAL expresion
                        | CONST ID DOSPUNTOS tipo_dato IGUAL expresion
                          '''
    if len(t) == 5:
        t[0] = Constante(t[2], t[4], "null")
    else:
        t[0] = Constante(t[2], t[6], t[4])

# ---------------------------------------------------------------------------- #
#                               OPERADOR TERNARIO                              #
# ---------------------------------------------------------------------------- #


def ternario(t):
    '''ternario_instr : expresion QUESTION expresion DOSPUNTOS expresion'''
    t[0] = IfElse(t[1], t[3], t[5])


# ---------------------------------------------------------------------------- #
#                                INSTRUCCION IF                                #
# ---------------------------------------------------------------------------- #


def p_if_instr(t):
    'if_instr           : IF PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDER'
    t[0] = If(t[3], t[6])

# ---------------------------------------------------------------------------- #
#                              INSTRUCCION IF-ELSE                             #
# ---------------------------------------------------------------------------- #


def p_if_else_instr(t):
    'if_else_instr      : IF PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDER ELSE LLAVIZQ instrucciones LLAVDER'
    t[0] = IfElse(t[3], t[6], t[10])

# ---------------------------------------------------------------------------- #
#                            CREACION DE UNA FUNCION                           #
# ---------------------------------------------------------------------------- #


def p_funcion_instr(t):
    'funcion_instr      : FUNCTION ID PARIZQ ID COMA ID PARDER LLAVIZQ instrucciones LLAVDER PUNTOCOMA'
    params = [t[4], t[6]]
    t[0] = Function(t[2], parametros=params, instrucciones=t[9])

# ---------------------------------------------------------------------------- #
#                            LLAMADO DE UNA FUNCION                            #
# ---------------------------------------------------------------------------- #


def p_call_funcion_instr(t):
    'call_funcion_instr      : ID PARIZQ expresion COMA expresion PARDER PUNTOCOMA'
    params = [t[3], t[5]]
    t[0] = CallFunction(t[1], params=params)


# ---------------------------------------------------------------------------- #
#                           INTERFACE SIN PARAMETROS                           #
# ---------------------------------------------------------------------------- #


def p_instruccion_interface(t):
    '''interface_instr : INTERFACE ID LLAVIZQ interface_params PUNTOCOMA LLAVDER'''
    t[0] = ExpresionInterface(t[2], t[4])

# ---------------------------------------------------------------------------- #
#                           INTERFACE CON PARAMETROS                           #
# ---------------------------------------------------------------------------- #


def p_instruccion_interface_params(t):
    '''interface_params : interface_params PUNTOCOMA ID DOSPUNTOS expresion
                        | ID DOSPUNTOS expresion'''

    if (len(t) == 4):
        t[0] = {t[1]: t[3]}
    else:
        t[1][t[3]] = t[5]
        t[0] = t[1]

# ---------------------------------------------------------------------------- #
#                               EXPRESION BINARIA                              #
# ---------------------------------------------------------------------------- #


def p_expresion_binaria(t):
    '''expresion : expresion MAS expresion
                  | expresion MENOS expresion
                  | expresion POR expresion
                  | expresion DIVIDIDO expresion
                  | expresion MODULO expresion
                  '''
    if t[2] == '+':
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MAS)
    elif t[2] == '-':
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MENOS)
    elif t[2] == '*':
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.POR)
    elif t[2] == '/':
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.DIVIDIDO)
    elif t[2] == '%':
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MODULO)

# ---------------------------------------------------------------------------- #
#                               EXPRESION LOGICA                               #
# ---------------------------------------------------------------------------- #


def p_expresion_logica(t):
    '''expresion : expresion MAYOR expresion
                  | expresion MENORQUE expresion
                  | expresion IGUALQUE expresion
                  | expresion DIFERENTE expresion'''
    if t[2] == '==':
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.IGUAL)
    elif t[2] == '!=':
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.DIFERENTE)
    elif t[2] == '>':
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MAYOR)
    elif t[2] == '>=':
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MAYORIGUAL)
    elif t[2] == '<':
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MENORQUE)
    elif t[2] == '<=':
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MENORIGUAL)

# ---------------------------------------------------------------------------- #
#                              OPERADORES LOGICOS                              #
# ---------------------------------------------------------------------------- #


def p_operacion_logica(t):
    '''expresion : expresion AND expresion
                  | expresion OR expresion
                  | NOT expresion'''

    if len(t) == 3:
        t[0] = ExpresionNOT(t[2], OPERADORES_LOGICOS.NOT)
    else:

        t[0] = ExpresionLogica(t[1], t[3], t[2])

# ---------------------------------------------------------------------------- #
#                               EXPRESION UNARIA                               #
# ---------------------------------------------------------------------------- #


def p_expresion_unaria(t):
    'expresion : MENOS expresion %prec MENOSUNARIO'
    t[0] = ExpresionNegativo(t[2])

# ---------------------------------------------------------------------------- #
#                            EXPRESION DE AGRUPACION                           #
# ---------------------------------------------------------------------------- #


def p_expresion_agrupacion(t):
    'expresion : PARIZQ expresion PARDER'
    t[0] = t[2]

# ---------------------------------------------------------------------------- #
#                              EXPRESION NUMERICA                              #
# ---------------------------------------------------------------------------- #


def p_expresion_number(t):
    '''expresion    : ENTERO
                     '''
    t[0] = ExpresionNumero(t[1])

# ---------------------------------------------------------------------------- #
#                               EXPRESION DECIMAL                              #
# ---------------------------------------------------------------------------- #
def p_decimal(t):
    '''decimal : ENTERO PUNTO ENTERO'''
    t[1] = str(t[1]) + str(t[2]) + str(t[3])
    t[0] = t[1]

def p_expresion_decimal(t):
    '''expresion    : decimal
                     '''
    t[0] = ExpresionDecimal(float(t[1]))

# ---------------------------------------------------------------------------- #
#                              EXPRESION DE CADENA                             #
# ---------------------------------------------------------------------------- #


def p_expresion_cadenas(t):
    '''expresion : CADENA
                | TRUE
                | FALSE
    '''
    t[0] = ExpresionConsoleLog(t[1])


def p_expresion_cadena(t):
    '''expresionCadena : CADENA COMA expresionCadena2
    | CADENA
    | TRUE
    | FALSE
    | decimal
    | ENTERO
    '''
    try:
        t[1] = str(t[1]) + " " + str(t[3])
    except:
        None
    # print("cadena procesada: "+str(t[1]))
    t[0] = ExpresionConsoleLog(str(t[1]))


def p_expresion_cadena2(t):
    '''expresionCadena2 : CADENA
    | TRUE
    | FALSE
    | decimal
    | ENTERO
    '''
    t[0] = str(t[1])


# ---------------------------------------------------------------------------- #
#                                   PARSE INT                                  #
# ---------------------------------------------------------------------------- #


def p_parseInt(t):
    '''parseInt : PARSEINT PARIZQ expresionCadena PARDER PUNTOCOMA'''
    t[0] = int(t[3])

# ---------------------------------------------------------------------------- #
#                                  PARSE FLOAT                                 #
# ---------------------------------------------------------------------------- #


def p_parseFloat(t):
    '''parseFloat : PARSEFLOAT PARIZQ expresionCadena PARDER PUNTOCOMA'''
    t[0] = float(t[3])


# ---------------------------------------------------------------------------- #
#                                   TO STRING                                  #
# ---------------------------------------------------------------------------- #

def p_toString(t):
    '''toString : ID PUNTO TOSTRING PARIZQ PARDER'''

# ---------------------------------------------------------------------------- #
#                                 TO LOWER CASE                                #
# ---------------------------------------------------------------------------- #


def p_toLowerCase(t):
    '''toLowerCase : ID PUNTO TOLOWERCASE PARIZQ PARDER'''
# ---------------------------------------------------------------------------- #
#                                 TO UPPER CASE                                #
# ---------------------------------------------------------------------------- #


def p_toUpperCase(t):
    '''toUpperCase : ID PUNTO TOUPPERCASE PARIZQ PARDER'''
# ---------------------------------------------------------------------------- #
#                                    TYPEOF                                    #
# ---------------------------------------------------------------------------- #


def p_typeof(t):
    '''typeof : TYPEOF expresion
                | TYPEOF ID'''
# ---------------------------------------------------------------------------- #
#                                EXPRESION DE ID                               #
# ---------------------------------------------------------------------------- #


def p_expresion_id(t):
    '''expresion    : ID
                    | ID PUNTO ID'''
    if (len(t) == 2):
        t[0] = ExpresionID(t[1])
    else:
        t[0] = ExpresionAccesoInterface(t[1], t[3])

# ---------------------------------------------------------------------------- #
#                              ERRORES SINTACTICOS                             #
# ---------------------------------------------------------------------------- #


def p_error(p):
    from interfaz import errores
    if p:
        err = f"Error de sintaxis en línea {p.lineno}, columna {
            p.lexpos}: Token inesperado '{p.value}'"
        errores.append(err)
    else:
        err = "Error de sintaxis"
        errores.append(err)


lexer = Lex.lex()
parser = yacc.yacc()


def parse(input):
    return parser.parse(input)

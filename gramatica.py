import ply.lex as Lex
import ply.yacc as yacc
from simbolos import TIPO_DATO
from instrucciones import *
from expresiones import *

# ? ---------------------------------------------------------------------------- #
# ?                                ANALISIS LEXICO                               #
# ? ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
#                              PALABRAS RESERVADAS                             #
# ---------------------------------------------------------------------------- #
reservadas = {
    'console': 'CONSOLE',
    'log': 'LOG',
    'let': 'LET',
    'number': 'NUMBER',
    'string': 'STRING',
    'if': 'IF',
    'else': 'ELSE',
    'function': 'FUNCTION',
    'interface': 'INTERFACE',
    'array': 'ARRAY',
    'null': 'NULL',
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',
}

# ---------------------------------------------------------------------------- #
#                                LISTA DE TOKENS                               #
# ---------------------------------------------------------------------------- #
tokens = [
    'PARIZQ',
    'PARDER',
    'CORIZQ',
    'CORDER',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'MODULO',
    'MENORQUE',
    'MENORIGUAL',
    'MAYORIGUAL',
    'MAYOR',
    'IGUALQUE',
    'DIFERENTE',
    'MENOSUNARIO',
    'PUNTO',
    'PUNTOCOMA',
    'DOSPUNTOS',
    'TIPONUMBER',
    'TIPOFLOAT',
    'TIPOSTRING',
    'TIPOBOOLEAN',
    'TIPOCHAR',
    'CADENA',
    'ENTERO',
    'COMMENTBLOCK',
    'ID',
    'IGUAL',
    'LLAVIZQ',
    'LLAVDER',
    'COMA'
] + list(reservadas.values())

t_CONSOLE = r'console'
t_LOG = r'log'
t_LET = r'let'
t_IF = r'if'
t_TIPONUMBER = r'number'
t_TIPOFLOAT = r'float'
t_TIPOSTRING = r'string'
t_TIPOBOOLEAN = r'boolean'
t_TIPOCHAR = r'char'
t_DOSPUNTOS = r':'
t_IGUAL = r'='
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_DIVIDIDO = r'/'
t_MODULO = r'%'
t_MENORQUE = r'<'
t_MENORIGUAL = r'<='
t_MAYORIGUAL = r'>='
t_MAYOR = r'>'
t_IGUALQUE = r'=='
t_DIFERENTE = r'!='
t_MENOSUNARIO = r'\-'
t_PUNTO = r'\.'
t_PUNTOCOMA = r';'
t_LLAVIZQ = r'{'
t_LLAVDER = r'}'
t_COMA = r','
t_NULL = r'null'
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'

# ---------------------------------------------------------------------------- #
#                               IDENTIFICADORRES                               #
# ---------------------------------------------------------------------------- #


def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'  # El identificador debe comenzar con una letra
    if t.value.lower() in reservadas:  # Verificar si el identificador es una palabra reservada
        t.type = t.value.upper()  # Asignar el tipo de palabra reservada
    else:
        t.type = 'ID'  # Asignar el tipo ID
    return t

# ---------------------------------------------------------------------------- #
#                                    CADENAS                                   #
# ---------------------------------------------------------------------------- #


def t_CADENA(t):
    r'\"(.+?)\"'
    try:
        t.value = str(t.value)
    except ValueError:
        print("Error %d", t.value)
        t.value = ''
    return t

# ---------------------------------------------------------------------------- #
#                                NUMEROS ENTEROS                               #
# ---------------------------------------------------------------------------- #


def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


t_ignore = " \t"

t_ignore_COMMENTLINE = r'\/\/.*'

# ---------------------------------------------------------------------------- #
#                                  COMENTARIOS                                 #
# ---------------------------------------------------------------------------- #


def t_ignore_COMMENTBLOCK(t):
    r'\/\*[^*]*\*+(?:[^/*][^*]*\*+)*\/'
    t.lexer.lineno += t.value.count('\n')

# ---------------------------------------------------------------------------- #
#                                SALTO DE LINEA                                #
# ---------------------------------------------------------------------------- #


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# ---------------------------------------------------------------------------- #
#                                BARRA INVERTIDA                               #
# ---------------------------------------------------------------------------- #


def t_invert_bar(t):
    r'\\+'

# ---------------------------------------------------------------------------- #
#                               RETORNO DE CARRO                               #
# ---------------------------------------------------------------------------- #


def t_car_return(t):
    r'\\r+'

# ---------------------------------------------------------------------------- #
#                                  TABULACION                                  #
# ---------------------------------------------------------------------------- #


def tabulation(t):
    r'\\t+'

# ---------------------------------------------------------------------------- #
#                                ERRORES LEXICOS                               #
# ---------------------------------------------------------------------------- #


def t_error(t):
    from interfaz import errores
    err = "Error Léxico: '%s'" % t.value[0]
    errores.append(err)
    t.lexer.skip(1)


# ---------------------------------------------------------------------------- #
#                           PRECEDENCIA DE OPERADORES                          #
# ---------------------------------------------------------------------------- #
precedence = (
    ('left', 'MENORQUE', 'MENORIGUAL', 'MAYORIGUAL', 'MAYOR'),  # < <= >= >
    ('left', 'IGUALQUE', 'DIFERENTE'),  # == !=
    ('left', 'AND'),  # &&
    ('left', 'OR'),  # ||
    ('left', 'MAS', 'MENOS'),  # + -
    ('left', 'POR', 'DIVIDIDO', 'MODULO'),  # * / %
    ('right', 'MENOSUNARIO', 'NOT')  # - !
)

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
    '''instruccion      : imprimir_instr
                        | declaracion_instr
                        | asignacion_instr
                        | if_instr
                        | if_else_instr
                        | funcion_instr
                        | call_funcion_instr
                        | interface_instr
    '''
    t[0] = t[1]

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

# def p_tipo_dato(p):
#     """ tipo_dato : STRING
#                 | NUMBER """

#     if p.slice[1].type == 'STRING':
#         p[0] = TIPO_DATO.STRING
#     elif p.slice[1].type == 'NUMBER':
#         p[0] = TIPO_DATO.ENTERO

# ---------------------------------------------------------------------------- #
#                              IMPRIMIR EN CONSOLA                             #
# ---------------------------------------------------------------------------- #


def p_instruccion_console(t):
    '''imprimir_instr : CONSOLE PUNTO LOG PARIZQ expresion PARDER PUNTOCOMA'''
    t[0] = Imprimir(t[5])


# ---------------------------------------------------------------------------- #
#                           DECLARACION DE VARIABLES                           #
# ---------------------------------------------------------------------------- #
def p_instruccion_declaracion(t):
    '''declaracion_instr : LET ID IGUAL expresion PUNTOCOMA'''
    t[0] = Declaracion(t[2], t[4])

# ---------------------------------------------------------------------------- #
#                            ASIGNACION DE VARIABLES                           #
# ---------------------------------------------------------------------------- #


def p_instruccion_asignacion(t):
    '''asignacion_instr : ID IGUAL expresion PUNTOCOMA'''
    t[0] = Asignacion(t[1], t[3])

# ---------------------------------------------------------------------------- #
#                                INSTRUCCION IF                                #
# ---------------------------------------------------------------------------- #


def p_if_instr(t):
    'if_instr           : IF PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDER PUNTOCOMA'
    t[0] = If(t[3], t[6])

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
#                              INSTRUCCION IF-ELSE                             #
# ---------------------------------------------------------------------------- #


def p_if_else_instr(t):
    'if_else_instr      : IF PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDER ELSE LLAVIZQ instrucciones LLAVDER PUNTOCOMA'
    t[0] = IfElse(t[3], t[6], t[10])

# ---------------------------------------------------------------------------- #
#                               EXPRESION BINARIA                              #
# ---------------------------------------------------------------------------- #


def p_expresion_binaria(t):
    '''expresion : expresion MAS expresion
                  | expresion MENOS expresion
                  | expresion POR expresion
                  | expresion DIVIDIDO expresion'''
    if t[2] == '+':
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MAS)
    elif t[2] == '-':
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MENOS)
    elif t[2] == '*':
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.POR)
    elif t[2] == '/':
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.DIVIDIDO)

# ---------------------------------------------------------------------------- #
#                               EXPRESION LOGICA                               #
# ---------------------------------------------------------------------------- #


def p_expresion_logica(t):
    '''expresion : expresion MAYOR expresion
                  | expresion MENORQUE expresion
                  | expresion IGUALQUE expresion
                  | expresion DIFERENTE expresion'''
    if t[2] == '>':
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MAYOR_QUE)
    elif t[2] == '<':
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MENOR_QUE)
    elif t[2] == '==':
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.IGUAL)
    elif t[2] == '!=':
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.NO_IGUAL)

# ---------------------------------------------------------------------------- #
#                              OPERADORES LOGICOS                              #
# ---------------------------------------------------------------------------- #


# def p_operacion_logica(t):
#     '''expresion : expresion AND expresion
#                   | expresion OR expresion
#                   | NOT expresion'''

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
    '''expresion    : ENTERO'''
    t[0] = ExpresionNumero(t[1])

# ---------------------------------------------------------------------------- #
#                              EXPRESION DE CADENA                             #
# ---------------------------------------------------------------------------- #


def p_expresion_cadena(t):
    '''expresion    : CADENA'''
    t[0] = ExpresionDobleComilla(t[1])

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

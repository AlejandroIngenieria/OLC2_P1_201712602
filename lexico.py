datos = ["string", "float", "number", "boolean", "char", "null"]
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
    'var': 'VAR',
    'true': 'TRUE',
    'false': 'FALSE',
    'float': 'FLOAT',
    'string': 'STRING',
    'boolean': 'BOOLEAN',
    'char': 'CHAR',
    'null': 'NULL',
    'const': 'CONST',

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
    'AND',
    'OR',
    'NOT',
    'PUNTO',
    'PUNTOCOMA',
    'DOSPUNTOS',
    'CADENA',
    'ENTERO',
    'COMMENTBLOCK',
    'ID',
    'IGUAL',
    'LLAVIZQ',
    'LLAVDER',
    'COMA',
    'QUESTION',
    'PARSEINT',
    'PARSEFLOAT',
    'TOSTRING',
    'TOLOWERCASE',
    'TOUPPERCASE',
    'TYPEOF',
] + list(reservadas.values())
t_CONSOLE = r'console'
t_LOG = r'log'
t_LET = r'let'
t_VAR = r'var'
t_CONST = r'const'
t_IF = r'if'
t_NUMBER = r'number'
t_FLOAT = r'float'
t_STRING = r'string'
t_BOOLEAN = r'boolean'
t_CHAR = r'char'
t_NULL = r'null'
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
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_QUESTION = r'\?'
t_TRUE = r'true'
t_FALSE = r'false'
t_PARSEINT = r'parseInt'
t_PARSEFLOAT = r'parseFloat'
t_TOSTRING = r'toString'
t_TOLOWERCASE = r'toLowerCase'
t_TOUPPERCASE = r'toUpperCase'
t_TYPEOF = r'typeof'

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
    # Patrón para manejar cadenas con secuencias de escape y saltos de línea
    r'\"([^"\n\\]*(\\.[^"\n\\]*)*)\"'
    try:
        t.value = t.value[1:-1]  # Elimina las comillas al inicio y al final
        # Reemplaza las secuencias de escape \n por saltos de línea reales
        t.value = t.value.replace(r'\n', '\n')
        # Reemplaza las secuencias de escape \t por tabulaciones reales
        t.value = t.value.replace(r'\t', '\t')
        t.value = t.value.replace(
            r'\\', '\\')  # Reemplaza las secuencias de escape \\ por una sola \
        t.value = str(t.value)  # Convierte a cadena si no lo es
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

t_ignore_inverted_bar = r'\\'

t_ignore_car_return = r'\r'

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

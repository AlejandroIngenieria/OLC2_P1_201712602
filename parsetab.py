
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftMENORQUEMENORIGUALMAYORIGUALMAYORleftIGUALQUEDIFERENTEleftANDleftORleftMASMENOSleftPORDIVIDIDOMODULOrightMENOSUNARIONOTAND ARRAY BOOLEAN CADENA CHAR COMA COMMENTBLOCK CONSOLE CORDER CORIZQ DECIMAL DIFERENTE DIVIDIDO DOSPUNTOS ELSE ENTERO FALSE FLOAT FUNCTION ID IF IGUAL IGUALQUE INTERFACE LET LLAVDER LLAVIZQ LOG MAS MAYOR MAYORIGUAL MENORIGUAL MENORQUE MENOS MENOSUNARIO MODULO NOT NULL NUMBER OR PARDER PARIZQ PARSEFLOAT PARSEINT POR PUNTO PUNTOCOMA QUESTION STRING TOLOWERCASE TOSTRING TOUPPERCASE TRUE TYPEOF VARinit            : instruccionesinstrucciones    : instrucciones instruccioninstrucciones    : instruccion instruccion  : imprimir_instr PUNTOCOMA\n                    | declaracion_instr PUNTOCOMA\n    imprimir_instr : CONSOLE PUNTO LOG PARIZQ expresionCadena PARDER tipo_dato : STRING\n                  | NUMBER\n                  | FLOAT\n                  | BOOLEAN\n                  | CHAR\n    declaracion_instr : LET ID IGUAL expresion\n                        | VAR ID IGUAL expresion\n                        | LET ID DOSPUNTOS tipo_dato\n                        | VAR ID DOSPUNTOS tipo_dato\n                        | LET ID DOSPUNTOS tipo_dato IGUAL expresion\n                        | VAR ID DOSPUNTOS tipo_dato IGUAL expresion\n                          asignacion_instr : ID IGUAL expresion PUNTOCOMAif_instr           : IF PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDER PUNTOCOMAif_else_instr      : IF PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDER ELSE LLAVIZQ instrucciones LLAVDER PUNTOCOMAfuncion_instr      : FUNCTION ID PARIZQ ID COMA ID PARDER LLAVIZQ instrucciones LLAVDER PUNTOCOMAcall_funcion_instr      : ID PARIZQ expresion COMA expresion PARDER PUNTOCOMAinterface_instr : INTERFACE ID LLAVIZQ interface_params PUNTOCOMA LLAVDERinterface_params : interface_params PUNTOCOMA ID DOSPUNTOS expresion\n                        | ID DOSPUNTOS expresionexpresion : expresion MAS expresion\n                  | expresion MENOS expresion\n                  | expresion POR expresion\n                  | expresion DIVIDIDO expresionexpresion : expresion MAYOR expresion\n                  | expresion MENORQUE expresion\n                  | expresion IGUALQUE expresion\n                  | expresion DIFERENTE expresionexpresion : expresion AND expresion\n                  | expresion OR expresion\n                  | NOT expresionexpresion : MENOS expresion %prec MENOSUNARIOexpresion : PARIZQ expresion PARDERexpresion    : ENTERO\n                     expresion : CADENA\n    expresionCadena : CADENA COMA expresionCadena2\n    | CADENA\n    | TRUE\n    | FALSE\n    | NUMBER\n    | DECIMAL\n    expresionCadena2 : CADENA\n    | TRUE\n    | FALSE\n    | ENTERO\n    | DECIMAL\n    parseInt : PARSEINT PARIZQ expresionCadena PARDER PUNTOCOMAparseFloat : PARSEFLOAT PARIZQ expresionCadena PARDER PUNTOCOMAtoString : ID PUNTO TOSTRING PARIZQ PARDERtoLowerCase : ID PUNTO TOLOWERCASE PARIZQ PARDERtoUpperCase : ID PUNTO TOUPPERCASE PARIZQ PARDERtypeof : TYPEOF expresion\n                | TYPEOF IDexpresion    : ID\n                    | ID PUNTO ID'
    
_lr_action_items = {'CONSOLE':([0,2,3,9,10,11,],[6,6,-3,-2,-4,-5,]),'LET':([0,2,3,9,10,11,],[7,7,-3,-2,-4,-5,]),'VAR':([0,2,3,9,10,11,],[8,8,-3,-2,-4,-5,]),'$end':([1,2,3,9,10,11,],[0,-1,-3,-2,-4,-5,]),'PUNTOCOMA':([4,5,21,22,26,27,28,29,30,31,32,33,34,35,53,54,58,60,61,62,63,64,65,66,67,68,69,70,71,72,73,],[10,11,-59,-12,-39,-40,-14,-7,-8,-9,-10,-11,-13,-15,-37,-36,-6,-60,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-38,-16,-17,]),'PUNTO':([6,21,],[12,42,]),'ID':([7,8,16,18,23,24,25,42,43,44,45,46,47,48,49,50,51,52,56,57,],[13,14,21,21,21,21,21,60,21,21,21,21,21,21,21,21,21,21,21,21,]),'LOG':([12,],[15,]),'IGUAL':([13,14,28,29,30,31,32,33,35,],[16,18,56,-7,-8,-9,-10,-11,57,]),'DOSPUNTOS':([13,14,],[17,19,]),'PARIZQ':([15,16,18,23,24,25,43,44,45,46,47,48,49,50,51,52,56,57,],[20,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'NOT':([16,18,23,24,25,43,44,45,46,47,48,49,50,51,52,56,57,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'MENOS':([16,18,21,22,23,24,25,26,27,34,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,60,61,62,63,64,65,66,67,68,69,70,71,72,73,],[23,23,-59,44,23,23,23,-39,-40,44,23,23,23,23,23,23,23,23,23,23,-37,-36,44,23,23,-60,-26,-27,-28,-29,44,44,44,44,44,44,-38,44,44,]),'ENTERO':([16,18,23,24,25,43,44,45,46,47,48,49,50,51,52,56,57,59,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,78,]),'CADENA':([16,18,20,23,24,25,43,44,45,46,47,48,49,50,51,52,56,57,59,],[27,27,37,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,74,]),'STRING':([17,19,],[29,29,]),'NUMBER':([17,19,20,],[30,30,40,]),'FLOAT':([17,19,],[31,31,]),'BOOLEAN':([17,19,],[32,32,]),'CHAR':([17,19,],[33,33,]),'TRUE':([20,59,],[38,76,]),'FALSE':([20,59,],[39,77,]),'DECIMAL':([20,59,],[41,79,]),'MAS':([21,22,26,27,34,53,54,55,60,61,62,63,64,65,66,67,68,69,70,71,72,73,],[-59,43,-39,-40,43,-37,-36,43,-60,-26,-27,-28,-29,43,43,43,43,43,43,-38,43,43,]),'POR':([21,22,26,27,34,53,54,55,60,61,62,63,64,65,66,67,68,69,70,71,72,73,],[-59,45,-39,-40,45,-37,-36,45,-60,45,45,-28,-29,45,45,45,45,45,45,-38,45,45,]),'DIVIDIDO':([21,22,26,27,34,53,54,55,60,61,62,63,64,65,66,67,68,69,70,71,72,73,],[-59,46,-39,-40,46,-37,-36,46,-60,46,46,-28,-29,46,46,46,46,46,46,-38,46,46,]),'MAYOR':([21,22,26,27,34,53,54,55,60,61,62,63,64,65,66,67,68,69,70,71,72,73,],[-59,47,-39,-40,47,-37,-36,47,-60,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-38,47,47,]),'MENORQUE':([21,22,26,27,34,53,54,55,60,61,62,63,64,65,66,67,68,69,70,71,72,73,],[-59,48,-39,-40,48,-37,-36,48,-60,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-38,48,48,]),'IGUALQUE':([21,22,26,27,34,53,54,55,60,61,62,63,64,65,66,67,68,69,70,71,72,73,],[-59,49,-39,-40,49,-37,-36,49,-60,-26,-27,-28,-29,49,49,-32,-33,-34,-35,-38,49,49,]),'DIFERENTE':([21,22,26,27,34,53,54,55,60,61,62,63,64,65,66,67,68,69,70,71,72,73,],[-59,50,-39,-40,50,-37,-36,50,-60,-26,-27,-28,-29,50,50,-32,-33,-34,-35,-38,50,50,]),'AND':([21,22,26,27,34,53,54,55,60,61,62,63,64,65,66,67,68,69,70,71,72,73,],[-59,51,-39,-40,51,-37,-36,51,-60,-26,-27,-28,-29,51,51,51,51,-34,-35,-38,51,51,]),'OR':([21,22,26,27,34,53,54,55,60,61,62,63,64,65,66,67,68,69,70,71,72,73,],[-59,52,-39,-40,52,-37,-36,52,-60,-26,-27,-28,-29,52,52,52,52,52,-35,-38,52,52,]),'PARDER':([21,26,27,36,37,38,39,40,41,53,54,55,60,61,62,63,64,65,66,67,68,69,70,71,74,75,76,77,78,79,],[-59,-39,-40,58,-42,-43,-44,-45,-46,-37,-36,71,-60,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-38,-47,-41,-48,-49,-50,-51,]),'COMA':([37,],[59,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,],[2,]),'instruccion':([0,2,],[3,9,]),'imprimir_instr':([0,2,],[4,4,]),'declaracion_instr':([0,2,],[5,5,]),'expresion':([16,18,23,24,25,43,44,45,46,47,48,49,50,51,52,56,57,],[22,34,53,54,55,61,62,63,64,65,66,67,68,69,70,72,73,]),'tipo_dato':([17,19,],[28,35,]),'expresionCadena':([20,],[36,]),'expresionCadena2':([59,],[75,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','gramatica.py',252),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','gramatica.py',261),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','gramatica.py',271),
  ('instruccion -> imprimir_instr PUNTOCOMA','instruccion',2,'p_instruccion','gramatica.py',280),
  ('instruccion -> declaracion_instr PUNTOCOMA','instruccion',2,'p_instruccion','gramatica.py',281),
  ('imprimir_instr -> CONSOLE PUNTO LOG PARIZQ expresionCadena PARDER','imprimir_instr',6,'p_instruccion_console','gramatica.py',296),
  ('tipo_dato -> STRING','tipo_dato',1,'p_tipo_dato','gramatica.py',305),
  ('tipo_dato -> NUMBER','tipo_dato',1,'p_tipo_dato','gramatica.py',306),
  ('tipo_dato -> FLOAT','tipo_dato',1,'p_tipo_dato','gramatica.py',307),
  ('tipo_dato -> BOOLEAN','tipo_dato',1,'p_tipo_dato','gramatica.py',308),
  ('tipo_dato -> CHAR','tipo_dato',1,'p_tipo_dato','gramatica.py',309),
  ('declaracion_instr -> LET ID IGUAL expresion','declaracion_instr',4,'p_instruccion_declaracion','gramatica.py',321),
  ('declaracion_instr -> VAR ID IGUAL expresion','declaracion_instr',4,'p_instruccion_declaracion','gramatica.py',322),
  ('declaracion_instr -> LET ID DOSPUNTOS tipo_dato','declaracion_instr',4,'p_instruccion_declaracion','gramatica.py',323),
  ('declaracion_instr -> VAR ID DOSPUNTOS tipo_dato','declaracion_instr',4,'p_instruccion_declaracion','gramatica.py',324),
  ('declaracion_instr -> LET ID DOSPUNTOS tipo_dato IGUAL expresion','declaracion_instr',6,'p_instruccion_declaracion','gramatica.py',325),
  ('declaracion_instr -> VAR ID DOSPUNTOS tipo_dato IGUAL expresion','declaracion_instr',6,'p_instruccion_declaracion','gramatica.py',326),
  ('asignacion_instr -> ID IGUAL expresion PUNTOCOMA','asignacion_instr',4,'p_instruccion_asignacion','gramatica.py',343),
  ('if_instr -> IF PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDER PUNTOCOMA','if_instr',8,'p_if_instr','gramatica.py',353),
  ('if_else_instr -> IF PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDER ELSE LLAVIZQ instrucciones LLAVDER PUNTOCOMA','if_else_instr',12,'p_if_else_instr','gramatica.py',362),
  ('funcion_instr -> FUNCTION ID PARIZQ ID COMA ID PARDER LLAVIZQ instrucciones LLAVDER PUNTOCOMA','funcion_instr',11,'p_funcion_instr','gramatica.py',371),
  ('call_funcion_instr -> ID PARIZQ expresion COMA expresion PARDER PUNTOCOMA','call_funcion_instr',7,'p_call_funcion_instr','gramatica.py',381),
  ('interface_instr -> INTERFACE ID LLAVIZQ interface_params PUNTOCOMA LLAVDER','interface_instr',6,'p_instruccion_interface','gramatica.py',392),
  ('interface_params -> interface_params PUNTOCOMA ID DOSPUNTOS expresion','interface_params',5,'p_instruccion_interface_params','gramatica.py',401),
  ('interface_params -> ID DOSPUNTOS expresion','interface_params',3,'p_instruccion_interface_params','gramatica.py',402),
  ('expresion -> expresion MAS expresion','expresion',3,'p_expresion_binaria','gramatica.py',426),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_expresion_binaria','gramatica.py',427),
  ('expresion -> expresion POR expresion','expresion',3,'p_expresion_binaria','gramatica.py',428),
  ('expresion -> expresion DIVIDIDO expresion','expresion',3,'p_expresion_binaria','gramatica.py',429),
  ('expresion -> expresion MAYOR expresion','expresion',3,'p_expresion_logica','gramatica.py',445),
  ('expresion -> expresion MENORQUE expresion','expresion',3,'p_expresion_logica','gramatica.py',446),
  ('expresion -> expresion IGUALQUE expresion','expresion',3,'p_expresion_logica','gramatica.py',447),
  ('expresion -> expresion DIFERENTE expresion','expresion',3,'p_expresion_logica','gramatica.py',448),
  ('expresion -> expresion AND expresion','expresion',3,'p_operacion_logica','gramatica.py',464),
  ('expresion -> expresion OR expresion','expresion',3,'p_operacion_logica','gramatica.py',465),
  ('expresion -> NOT expresion','expresion',2,'p_operacion_logica','gramatica.py',466),
  ('expresion -> MENOS expresion','expresion',2,'p_expresion_unaria','gramatica.py',474),
  ('expresion -> PARIZQ expresion PARDER','expresion',3,'p_expresion_agrupacion','gramatica.py',483),
  ('expresion -> ENTERO','expresion',1,'p_expresion_number','gramatica.py',492),
  ('expresion -> CADENA','expresion',1,'p_expresion_cadenas','gramatica.py',502),
  ('expresionCadena -> CADENA COMA expresionCadena2','expresionCadena',3,'p_expresion_cadena','gramatica.py',508),
  ('expresionCadena -> CADENA','expresionCadena',1,'p_expresion_cadena','gramatica.py',509),
  ('expresionCadena -> TRUE','expresionCadena',1,'p_expresion_cadena','gramatica.py',510),
  ('expresionCadena -> FALSE','expresionCadena',1,'p_expresion_cadena','gramatica.py',511),
  ('expresionCadena -> NUMBER','expresionCadena',1,'p_expresion_cadena','gramatica.py',512),
  ('expresionCadena -> DECIMAL','expresionCadena',1,'p_expresion_cadena','gramatica.py',513),
  ('expresionCadena2 -> CADENA','expresionCadena2',1,'p_expresion_cadena2','gramatica.py',524),
  ('expresionCadena2 -> TRUE','expresionCadena2',1,'p_expresion_cadena2','gramatica.py',525),
  ('expresionCadena2 -> FALSE','expresionCadena2',1,'p_expresion_cadena2','gramatica.py',526),
  ('expresionCadena2 -> ENTERO','expresionCadena2',1,'p_expresion_cadena2','gramatica.py',527),
  ('expresionCadena2 -> DECIMAL','expresionCadena2',1,'p_expresion_cadena2','gramatica.py',528),
  ('parseInt -> PARSEINT PARIZQ expresionCadena PARDER PUNTOCOMA','parseInt',5,'p_parseInt','gramatica.py',539),
  ('parseFloat -> PARSEFLOAT PARIZQ expresionCadena PARDER PUNTOCOMA','parseFloat',5,'p_parseFloat','gramatica.py',548),
  ('toString -> ID PUNTO TOSTRING PARIZQ PARDER','toString',5,'p_toString','gramatica.py',557),
  ('toLowerCase -> ID PUNTO TOLOWERCASE PARIZQ PARDER','toLowerCase',5,'p_toLowerCase','gramatica.py',565),
  ('toUpperCase -> ID PUNTO TOUPPERCASE PARIZQ PARDER','toUpperCase',5,'p_toUpperCase','gramatica.py',572),
  ('typeof -> TYPEOF expresion','typeof',2,'p_typeof','gramatica.py',579),
  ('typeof -> TYPEOF ID','typeof',2,'p_typeof','gramatica.py',580),
  ('expresion -> ID','expresion',1,'p_expresion_id','gramatica.py',587),
  ('expresion -> ID PUNTO ID','expresion',3,'p_expresion_id','gramatica.py',588),
]

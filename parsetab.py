
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftMENORQUEMENORIGUALMAYORIGUALMAYORleftIGUALQUEDIFERENTEleftANDleftORleftMASMENOSleftPORDIVIDIDOMODULOrightMENOSUNARIONOTAND ARRAY BOOLEAN CADENA CHAR COMA COMMENTBLOCK CONSOLE CONST CORDER CORIZQ DIFERENTE DIVIDIDO DOSPUNTOS ELSE ENTERO FALSE FLOAT FUNCTION ID IF IGUAL IGUALQUE INTERFACE LET LLAVDER LLAVIZQ LOG MAS MAYOR MAYORIGUAL MENORIGUAL MENORQUE MENOS MENOSUNARIO MODULO NOT NULL NUMBER OR PARDER PARIZQ PARSEFLOAT PARSEINT POR PUNTO PUNTOCOMA QUESTION STRING TOLOWERCASE TOSTRING TOUPPERCASE TRUE TYPEOF VARinit            : instruccionesinstrucciones    : instrucciones instruccioninstrucciones    : instruccion instruccion  : imprimir_instr PUNTOCOMA\n                    | declaracion_instr PUNTOCOMA\n                    | asignacion_instr PUNTOCOMA\n                    | constante_instr PUNTOCOMA\n\n    imprimir_instr : CONSOLE PUNTO LOG PARIZQ expresionCadena PARDER tipo_dato : STRING\n                  | NUMBER\n                  | FLOAT\n                  | BOOLEAN\n                  | CHAR\n    declaracion_instr : LET ID IGUAL expresion\n                        | VAR ID IGUAL expresion\n                        | LET ID DOSPUNTOS tipo_dato\n                        | VAR ID DOSPUNTOS tipo_dato\n                        | LET ID DOSPUNTOS tipo_dato IGUAL expresion\n                        | VAR ID DOSPUNTOS tipo_dato IGUAL expresion\n                          asignacion_instr : ID IGUAL expresionconstante_instr : CONST ID IGUAL expresion\n                        | CONST ID DOSPUNTOS tipo_dato IGUAL expresion\n                          if_instr           : IF PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDERif_else_instr      : IF PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDER ELSE LLAVIZQ instrucciones LLAVDERfuncion_instr      : FUNCTION ID PARIZQ ID COMA ID PARDER LLAVIZQ instrucciones LLAVDER PUNTOCOMAcall_funcion_instr      : ID PARIZQ expresion COMA expresion PARDER PUNTOCOMAinterface_instr : INTERFACE ID LLAVIZQ interface_params PUNTOCOMA LLAVDERinterface_params : interface_params PUNTOCOMA ID DOSPUNTOS expresion\n                        | ID DOSPUNTOS expresionexpresion : expresion MAS expresion\n                  | expresion MENOS expresion\n                  | expresion POR expresion\n                  | expresion DIVIDIDO expresion\n                  | expresion MODULO expresion\n                  expresion : expresion MAYOR expresion\n                  | expresion MENORQUE expresion\n                  | expresion IGUALQUE expresion\n                  | expresion DIFERENTE expresionexpresion : expresion AND expresion\n                  | expresion OR expresion\n                  | NOT expresionexpresion : MENOS expresion %prec MENOSUNARIOexpresion : PARIZQ expresion PARDERexpresion    : ENTERO\n                     decimal : ENTERO PUNTO ENTEROexpresion    : decimal\n                     expresion : CADENA\n                | TRUE\n                | FALSE\n    expresionCadena : CADENA COMA expresionCadena2\n    | CADENA\n    | TRUE\n    | FALSE\n    | decimal\n    | ENTERO\n    expresionCadena2 : CADENA\n    | TRUE\n    | FALSE\n    | decimal\n    | ENTERO\n    parseInt : PARSEINT PARIZQ expresionCadena PARDER PUNTOCOMAparseFloat : PARSEFLOAT PARIZQ expresionCadena PARDER PUNTOCOMAtoString : ID PUNTO TOSTRING PARIZQ PARDERtoLowerCase : ID PUNTO TOLOWERCASE PARIZQ PARDERtoUpperCase : ID PUNTO TOUPPERCASE PARIZQ PARDERtypeof : TYPEOF expresion\n                | TYPEOF IDexpresion    : ID\n                    | ID PUNTO ID'
    
_lr_action_items = {'CONSOLE':([0,2,3,13,14,15,16,17,],[8,8,-3,-2,-4,-5,-6,-7,]),'LET':([0,2,3,13,14,15,16,17,],[9,9,-3,-2,-4,-5,-6,-7,]),'VAR':([0,2,3,13,14,15,16,17,],[11,11,-3,-2,-4,-5,-6,-7,]),'ID':([0,2,3,9,11,12,13,14,15,16,17,20,24,28,29,30,36,38,48,49,50,51,52,53,54,55,56,57,58,59,74,89,90,],[10,10,-3,19,21,22,-2,-4,-5,-6,-7,26,26,26,26,26,26,26,75,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'CONST':([0,2,3,13,14,15,16,17,],[12,12,-3,-2,-4,-5,-6,-7,]),'$end':([1,2,3,13,14,15,16,17,],[0,-1,-3,-2,-4,-5,-6,-7,]),'PUNTOCOMA':([4,5,6,7,26,27,31,32,33,34,35,41,42,43,44,45,46,47,60,61,64,65,66,75,76,77,78,79,80,81,82,83,84,85,86,87,88,91,93,94,95,],[14,15,16,17,-68,-20,-44,-46,-47,-48,-49,-14,-16,-9,-10,-11,-12,-13,-42,-41,-15,-17,-21,-69,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-43,-45,-8,-18,-19,-22,]),'PUNTO':([8,26,31,73,101,],[18,48,63,63,63,]),'IGUAL':([10,19,21,22,42,43,44,45,46,47,65,67,],[20,24,36,38,74,-9,-10,-11,-12,-13,89,90,]),'LOG':([18,],[23,]),'DOSPUNTOS':([19,21,22,],[25,37,39,]),'NOT':([20,24,28,29,30,36,38,49,50,51,52,53,54,55,56,57,58,59,74,89,90,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'MENOS':([20,24,26,27,28,29,30,31,32,33,34,35,36,38,41,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,93,94,95,],[28,28,-68,50,28,28,28,-44,-46,-47,-48,-49,28,28,50,28,28,28,28,28,28,28,28,28,28,28,-42,-41,50,50,50,28,-69,-30,-31,-32,-33,-34,50,50,50,50,50,50,-43,-45,28,28,50,50,50,]),'PARIZQ':([20,23,24,28,29,30,36,38,49,50,51,52,53,54,55,56,57,58,59,74,89,90,],[30,40,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'ENTERO':([20,24,28,29,30,36,38,40,49,50,51,52,53,54,55,56,57,58,59,63,74,89,90,92,],[31,31,31,31,31,31,31,73,31,31,31,31,31,31,31,31,31,31,31,88,31,31,31,101,]),'CADENA':([20,24,28,29,30,36,38,40,49,50,51,52,53,54,55,56,57,58,59,74,89,90,92,],[33,33,33,33,33,33,33,69,33,33,33,33,33,33,33,33,33,33,33,33,33,33,96,]),'TRUE':([20,24,28,29,30,36,38,40,49,50,51,52,53,54,55,56,57,58,59,74,89,90,92,],[34,34,34,34,34,34,34,70,34,34,34,34,34,34,34,34,34,34,34,34,34,34,98,]),'FALSE':([20,24,28,29,30,36,38,40,49,50,51,52,53,54,55,56,57,58,59,74,89,90,92,],[35,35,35,35,35,35,35,71,35,35,35,35,35,35,35,35,35,35,35,35,35,35,99,]),'STRING':([25,37,39,],[43,43,43,]),'NUMBER':([25,37,39,],[44,44,44,]),'FLOAT':([25,37,39,],[45,45,45,]),'BOOLEAN':([25,37,39,],[46,46,46,]),'CHAR':([25,37,39,],[47,47,47,]),'MAS':([26,27,31,32,33,34,35,41,60,61,62,64,66,75,76,77,78,79,80,81,82,83,84,85,86,87,88,93,94,95,],[-68,49,-44,-46,-47,-48,-49,49,-42,-41,49,49,49,-69,-30,-31,-32,-33,-34,49,49,49,49,49,49,-43,-45,49,49,49,]),'POR':([26,27,31,32,33,34,35,41,60,61,62,64,66,75,76,77,78,79,80,81,82,83,84,85,86,87,88,93,94,95,],[-68,51,-44,-46,-47,-48,-49,51,-42,-41,51,51,51,-69,51,51,-32,-33,-34,51,51,51,51,51,51,-43,-45,51,51,51,]),'DIVIDIDO':([26,27,31,32,33,34,35,41,60,61,62,64,66,75,76,77,78,79,80,81,82,83,84,85,86,87,88,93,94,95,],[-68,52,-44,-46,-47,-48,-49,52,-42,-41,52,52,52,-69,52,52,-32,-33,-34,52,52,52,52,52,52,-43,-45,52,52,52,]),'MODULO':([26,27,31,32,33,34,35,41,60,61,62,64,66,75,76,77,78,79,80,81,82,83,84,85,86,87,88,93,94,95,],[-68,53,-44,-46,-47,-48,-49,53,-42,-41,53,53,53,-69,53,53,-32,-33,-34,53,53,53,53,53,53,-43,-45,53,53,53,]),'MAYOR':([26,27,31,32,33,34,35,41,60,61,62,64,66,75,76,77,78,79,80,81,82,83,84,85,86,87,88,93,94,95,],[-68,54,-44,-46,-47,-48,-49,54,-42,-41,54,54,54,-69,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-43,-45,54,54,54,]),'MENORQUE':([26,27,31,32,33,34,35,41,60,61,62,64,66,75,76,77,78,79,80,81,82,83,84,85,86,87,88,93,94,95,],[-68,55,-44,-46,-47,-48,-49,55,-42,-41,55,55,55,-69,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-43,-45,55,55,55,]),'IGUALQUE':([26,27,31,32,33,34,35,41,60,61,62,64,66,75,76,77,78,79,80,81,82,83,84,85,86,87,88,93,94,95,],[-68,56,-44,-46,-47,-48,-49,56,-42,-41,56,56,56,-69,-30,-31,-32,-33,-34,56,56,-37,-38,-39,-40,-43,-45,56,56,56,]),'DIFERENTE':([26,27,31,32,33,34,35,41,60,61,62,64,66,75,76,77,78,79,80,81,82,83,84,85,86,87,88,93,94,95,],[-68,57,-44,-46,-47,-48,-49,57,-42,-41,57,57,57,-69,-30,-31,-32,-33,-34,57,57,-37,-38,-39,-40,-43,-45,57,57,57,]),'AND':([26,27,31,32,33,34,35,41,60,61,62,64,66,75,76,77,78,79,80,81,82,83,84,85,86,87,88,93,94,95,],[-68,58,-44,-46,-47,-48,-49,58,-42,-41,58,58,58,-69,-30,-31,-32,-33,-34,58,58,58,58,-39,-40,-43,-45,58,58,58,]),'OR':([26,27,31,32,33,34,35,41,60,61,62,64,66,75,76,77,78,79,80,81,82,83,84,85,86,87,88,93,94,95,],[-68,59,-44,-46,-47,-48,-49,59,-42,-41,59,59,59,-69,-30,-31,-32,-33,-34,59,59,59,59,59,-40,-43,-45,59,59,59,]),'PARDER':([26,31,32,33,34,35,60,61,62,68,69,70,71,72,73,75,76,77,78,79,80,81,82,83,84,85,86,87,88,96,97,98,99,100,101,],[-68,-44,-46,-47,-48,-49,-42,-41,87,91,-51,-52,-53,-54,-55,-69,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-43,-45,-56,-50,-57,-58,-59,-60,]),'COMA':([69,],[92,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,],[2,]),'instruccion':([0,2,],[3,13,]),'imprimir_instr':([0,2,],[4,4,]),'declaracion_instr':([0,2,],[5,5,]),'asignacion_instr':([0,2,],[6,6,]),'constante_instr':([0,2,],[7,7,]),'expresion':([20,24,28,29,30,36,38,49,50,51,52,53,54,55,56,57,58,59,74,89,90,],[27,41,60,61,62,64,66,76,77,78,79,80,81,82,83,84,85,86,93,94,95,]),'decimal':([20,24,28,29,30,36,38,40,49,50,51,52,53,54,55,56,57,58,59,74,89,90,92,],[32,32,32,32,32,32,32,72,32,32,32,32,32,32,32,32,32,32,32,32,32,32,100,]),'tipo_dato':([25,37,39,],[42,65,67,]),'expresionCadena':([40,],[68,]),'expresionCadena2':([92,],[97,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','gramatica.py',16),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','gramatica.py',25),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','gramatica.py',35),
  ('instruccion -> imprimir_instr PUNTOCOMA','instruccion',2,'p_instruccion','gramatica.py',44),
  ('instruccion -> declaracion_instr PUNTOCOMA','instruccion',2,'p_instruccion','gramatica.py',45),
  ('instruccion -> asignacion_instr PUNTOCOMA','instruccion',2,'p_instruccion','gramatica.py',46),
  ('instruccion -> constante_instr PUNTOCOMA','instruccion',2,'p_instruccion','gramatica.py',47),
  ('imprimir_instr -> CONSOLE PUNTO LOG PARIZQ expresionCadena PARDER','imprimir_instr',6,'p_instruccion_console','gramatica.py',63),
  ('tipo_dato -> STRING','tipo_dato',1,'p_tipo_dato','gramatica.py',72),
  ('tipo_dato -> NUMBER','tipo_dato',1,'p_tipo_dato','gramatica.py',73),
  ('tipo_dato -> FLOAT','tipo_dato',1,'p_tipo_dato','gramatica.py',74),
  ('tipo_dato -> BOOLEAN','tipo_dato',1,'p_tipo_dato','gramatica.py',75),
  ('tipo_dato -> CHAR','tipo_dato',1,'p_tipo_dato','gramatica.py',76),
  ('declaracion_instr -> LET ID IGUAL expresion','declaracion_instr',4,'p_instruccion_declaracion','gramatica.py',86),
  ('declaracion_instr -> VAR ID IGUAL expresion','declaracion_instr',4,'p_instruccion_declaracion','gramatica.py',87),
  ('declaracion_instr -> LET ID DOSPUNTOS tipo_dato','declaracion_instr',4,'p_instruccion_declaracion','gramatica.py',88),
  ('declaracion_instr -> VAR ID DOSPUNTOS tipo_dato','declaracion_instr',4,'p_instruccion_declaracion','gramatica.py',89),
  ('declaracion_instr -> LET ID DOSPUNTOS tipo_dato IGUAL expresion','declaracion_instr',6,'p_instruccion_declaracion','gramatica.py',90),
  ('declaracion_instr -> VAR ID DOSPUNTOS tipo_dato IGUAL expresion','declaracion_instr',6,'p_instruccion_declaracion','gramatica.py',91),
  ('asignacion_instr -> ID IGUAL expresion','asignacion_instr',3,'p_instruccion_asignacion','gramatica.py',107),
  ('constante_instr -> CONST ID IGUAL expresion','constante_instr',4,'p_instruccion_constantes','gramatica.py',116),
  ('constante_instr -> CONST ID DOSPUNTOS tipo_dato IGUAL expresion','constante_instr',6,'p_instruccion_constantes','gramatica.py',117),
  ('if_instr -> IF PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDER','if_instr',7,'p_if_instr','gramatica.py',140),
  ('if_else_instr -> IF PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDER ELSE LLAVIZQ instrucciones LLAVDER','if_else_instr',11,'p_if_else_instr','gramatica.py',149),
  ('funcion_instr -> FUNCTION ID PARIZQ ID COMA ID PARDER LLAVIZQ instrucciones LLAVDER PUNTOCOMA','funcion_instr',11,'p_funcion_instr','gramatica.py',158),
  ('call_funcion_instr -> ID PARIZQ expresion COMA expresion PARDER PUNTOCOMA','call_funcion_instr',7,'p_call_funcion_instr','gramatica.py',168),
  ('interface_instr -> INTERFACE ID LLAVIZQ interface_params PUNTOCOMA LLAVDER','interface_instr',6,'p_instruccion_interface','gramatica.py',179),
  ('interface_params -> interface_params PUNTOCOMA ID DOSPUNTOS expresion','interface_params',5,'p_instruccion_interface_params','gramatica.py',188),
  ('interface_params -> ID DOSPUNTOS expresion','interface_params',3,'p_instruccion_interface_params','gramatica.py',189),
  ('expresion -> expresion MAS expresion','expresion',3,'p_expresion_binaria','gramatica.py',203),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_expresion_binaria','gramatica.py',204),
  ('expresion -> expresion POR expresion','expresion',3,'p_expresion_binaria','gramatica.py',205),
  ('expresion -> expresion DIVIDIDO expresion','expresion',3,'p_expresion_binaria','gramatica.py',206),
  ('expresion -> expresion MODULO expresion','expresion',3,'p_expresion_binaria','gramatica.py',207),
  ('expresion -> expresion MAYOR expresion','expresion',3,'p_expresion_logica','gramatica.py',226),
  ('expresion -> expresion MENORQUE expresion','expresion',3,'p_expresion_logica','gramatica.py',227),
  ('expresion -> expresion IGUALQUE expresion','expresion',3,'p_expresion_logica','gramatica.py',228),
  ('expresion -> expresion DIFERENTE expresion','expresion',3,'p_expresion_logica','gramatica.py',229),
  ('expresion -> expresion AND expresion','expresion',3,'p_operacion_logica','gramatica.py',249),
  ('expresion -> expresion OR expresion','expresion',3,'p_operacion_logica','gramatica.py',250),
  ('expresion -> NOT expresion','expresion',2,'p_operacion_logica','gramatica.py',251),
  ('expresion -> MENOS expresion','expresion',2,'p_expresion_unaria','gramatica.py',265),
  ('expresion -> PARIZQ expresion PARDER','expresion',3,'p_expresion_agrupacion','gramatica.py',274),
  ('expresion -> ENTERO','expresion',1,'p_expresion_number','gramatica.py',283),
  ('decimal -> ENTERO PUNTO ENTERO','decimal',3,'p_decimal','gramatica.py',291),
  ('expresion -> decimal','expresion',1,'p_expresion_decimal','gramatica.py',296),
  ('expresion -> CADENA','expresion',1,'p_expresion_cadenas','gramatica.py',306),
  ('expresion -> TRUE','expresion',1,'p_expresion_cadenas','gramatica.py',307),
  ('expresion -> FALSE','expresion',1,'p_expresion_cadenas','gramatica.py',308),
  ('expresionCadena -> CADENA COMA expresionCadena2','expresionCadena',3,'p_expresion_cadena','gramatica.py',314),
  ('expresionCadena -> CADENA','expresionCadena',1,'p_expresion_cadena','gramatica.py',315),
  ('expresionCadena -> TRUE','expresionCadena',1,'p_expresion_cadena','gramatica.py',316),
  ('expresionCadena -> FALSE','expresionCadena',1,'p_expresion_cadena','gramatica.py',317),
  ('expresionCadena -> decimal','expresionCadena',1,'p_expresion_cadena','gramatica.py',318),
  ('expresionCadena -> ENTERO','expresionCadena',1,'p_expresion_cadena','gramatica.py',319),
  ('expresionCadena2 -> CADENA','expresionCadena2',1,'p_expresion_cadena2','gramatica.py',330),
  ('expresionCadena2 -> TRUE','expresionCadena2',1,'p_expresion_cadena2','gramatica.py',331),
  ('expresionCadena2 -> FALSE','expresionCadena2',1,'p_expresion_cadena2','gramatica.py',332),
  ('expresionCadena2 -> decimal','expresionCadena2',1,'p_expresion_cadena2','gramatica.py',333),
  ('expresionCadena2 -> ENTERO','expresionCadena2',1,'p_expresion_cadena2','gramatica.py',334),
  ('parseInt -> PARSEINT PARIZQ expresionCadena PARDER PUNTOCOMA','parseInt',5,'p_parseInt','gramatica.py',345),
  ('parseFloat -> PARSEFLOAT PARIZQ expresionCadena PARDER PUNTOCOMA','parseFloat',5,'p_parseFloat','gramatica.py',354),
  ('toString -> ID PUNTO TOSTRING PARIZQ PARDER','toString',5,'p_toString','gramatica.py',363),
  ('toLowerCase -> ID PUNTO TOLOWERCASE PARIZQ PARDER','toLowerCase',5,'p_toLowerCase','gramatica.py',371),
  ('toUpperCase -> ID PUNTO TOUPPERCASE PARIZQ PARDER','toUpperCase',5,'p_toUpperCase','gramatica.py',378),
  ('typeof -> TYPEOF expresion','typeof',2,'p_typeof','gramatica.py',385),
  ('typeof -> TYPEOF ID','typeof',2,'p_typeof','gramatica.py',386),
  ('expresion -> ID','expresion',1,'p_expresion_id','gramatica.py',393),
  ('expresion -> ID PUNTO ID','expresion',3,'p_expresion_id','gramatica.py',394),
]

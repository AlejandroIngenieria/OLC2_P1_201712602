
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftMENORQUEMENORIGUALMAYORIGUALMAYORleftIGUALQUEDIFERENTEleftANDleftORleftMASMENOSleftPORDIVIDIDOMODULOrightMENOSNOTAND ARRAY BOOLEAN CADENA CHAR COMA COMMENTBLOCK CONSOLE CONST CORDER CORIZQ DIFERENTE DIVIDIDO DOSPUNTOS ELSE ENTERO FALSE FLOAT FOR FUNCTION ID IF IGUAL IGUALQUE INTERFACE LET LLAVDER LLAVIZQ LOG MAS MAYOR MAYORIGUAL MENORIGUAL MENORQUE MENOS MODULO NOT NULL NUMBER OR PARDER PARIZQ PARSEFLOAT PARSEINT POR PUNTO PUNTOCOMA QUESTION STRING TOLOWERCASE TOSTRING TOUPPERCASE TRUE TYPEOF VAR WHILEinit            : instruccionesinstrucciones    : instrucciones instruccioninstrucciones    : instruccion instruccion  : imprimir_instr PUNTOCOMA\n                    | declaracion_instr PUNTOCOMA\n                    | asignacion_instr PUNTOCOMA\n                    | constante_instr PUNTOCOMA\n                    | if_instr\n                    | if_else_instr\n    imprimir_instr : CONSOLE PUNTO LOG PARIZQ expresionCadena PARDER tipo_dato : STRING\n                  | NUMBER\n                  | FLOAT\n                  | BOOLEAN\n                  | CHAR\n    declaracion_instr : LET ID IGUAL expresion\n                        | VAR ID IGUAL expresion\n                        | LET ID DOSPUNTOS tipo_dato\n                        | VAR ID DOSPUNTOS tipo_dato\n                        | LET ID DOSPUNTOS tipo_dato IGUAL expresion\n                        | VAR ID DOSPUNTOS tipo_dato IGUAL expresion\n                          asignacion_instr : ID IGUAL expresion\n                        | ID MAS IGUAL expresion\n                        | ID MENOS IGUAL expresion\n    constante_instr : CONST ID IGUAL expresion\n                        | CONST ID DOSPUNTOS tipo_dato IGUAL expresion\n                          expresion : expresion MAS expresion\n                  | MENOS expresion\n                  | expresion MENOS expresion\n                  | expresion POR expresion\n                  | expresion DIVIDIDO expresion\n                  | expresion MODULO expresion\n                  expresion :  expresion IGUALQUE expresion\n                  | expresion DIFERENTE expresion\n                  | expresion MAYOR expresion\n                  | expresion MAYORIGUAL expresion\n                  | expresion MENORQUE expresion\n                  | expresion MENORIGUAL expresion\n                  expresion : expresion AND expresion\n                  | expresion OR expresion\n                  | NOT expresionif_instr           : IF PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDERif_else_instr      : IF PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDER ELSE LLAVIZQ instrucciones LLAVDERfuncion_instr      : FUNCTION ID PARIZQ ID COMA ID PARDER LLAVIZQ instrucciones LLAVDER PUNTOCOMAcall_funcion_instr      : ID PARIZQ expresion COMA expresion PARDER PUNTOCOMAinterface_instr : INTERFACE ID LLAVIZQ interface_params PUNTOCOMA LLAVDERinterface_params : interface_params PUNTOCOMA ID DOSPUNTOS expresion\n                        | ID DOSPUNTOS expresionexpresion : PARIZQ expresion PARDERexpresion    : ENTERO\n                     decimal : ENTERO PUNTO ENTEROexpresion    : decimal\n                     expresion : TRUE\n                | FALSE\n                | CADENA\n    expresionCadena : CADENA COMA expresionCadena2\n    | CADENA\n    | TRUE\n    | FALSE\n    | decimal\n    | ENTERO\n    expresionCadena2 : CADENA\n    | TRUE\n    | FALSE\n    | decimal\n    | ENTERO\n    parseInt : PARSEINT PARIZQ expresionCadena PARDER PUNTOCOMAparseFloat : PARSEFLOAT PARIZQ expresionCadena PARDER PUNTOCOMAtoString : ID PUNTO TOSTRING PARIZQ PARDERtoLowerCase : ID PUNTO TOLOWERCASE PARIZQ PARDERtoUpperCase : ID PUNTO TOUPPERCASE PARIZQ PARDERtypeof : TYPEOF expresion\n                | TYPEOF IDexpresion    : ID\n                    | ID PUNTO ID'
    
_lr_action_items = {'CONSOLE':([0,2,3,8,9,16,17,18,19,20,107,113,120,122,123,124,],[10,10,-3,-8,-9,-2,-4,-5,-6,-7,10,10,-42,10,10,-43,]),'LET':([0,2,3,8,9,16,17,18,19,20,107,113,120,122,123,124,],[11,11,-3,-8,-9,-2,-4,-5,-6,-7,11,11,-42,11,11,-43,]),'VAR':([0,2,3,8,9,16,17,18,19,20,107,113,120,122,123,124,],[13,13,-3,-8,-9,-2,-4,-5,-6,-7,13,13,-42,13,13,-43,]),'ID':([0,2,3,8,9,11,13,14,16,17,18,19,20,23,28,30,34,35,36,42,43,44,46,57,58,59,60,61,62,63,64,65,66,67,68,69,70,88,105,106,107,113,120,122,123,124,],[12,12,-3,-8,-9,22,26,27,-2,-4,-5,-6,-7,32,32,32,32,32,32,32,32,32,32,89,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,12,12,-42,12,12,-43,]),'CONST':([0,2,3,8,9,16,17,18,19,20,107,113,120,122,123,124,],[14,14,-3,-8,-9,-2,-4,-5,-6,-7,14,14,-42,14,14,-43,]),'IF':([0,2,3,8,9,16,17,18,19,20,107,113,120,122,123,124,],[15,15,-3,-8,-9,-2,-4,-5,-6,-7,15,15,-42,15,15,-43,]),'$end':([1,2,3,8,9,16,17,18,19,20,120,124,],[0,-1,-3,-8,-9,-2,-4,-5,-6,-7,-42,-43,]),'LLAVDER':([3,8,9,16,17,18,19,20,113,120,123,124,],[-3,-8,-9,-2,-4,-5,-6,-7,120,-42,124,-43,]),'PUNTOCOMA':([4,5,6,7,32,33,37,38,39,40,41,50,51,52,53,54,55,56,71,72,75,76,77,78,79,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,108,110,111,112,],[17,18,19,20,-74,-22,-50,-52,-53,-54,-55,-16,-18,-11,-12,-13,-14,-15,-28,-41,-23,-24,-17,-19,-25,-75,-27,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-49,-51,-10,-20,-21,-26,]),'PUNTO':([10,32,37,87,119,],[21,57,74,74,74,]),'IGUAL':([12,22,24,25,26,27,51,52,53,54,55,56,78,80,],[23,30,42,43,44,46,88,-11,-12,-13,-14,-15,105,106,]),'MAS':([12,32,33,37,38,39,40,41,48,50,71,72,73,75,76,77,79,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,110,111,112,],[24,-74,58,-50,-52,-53,-54,-55,58,58,-28,-41,58,58,58,58,58,-75,-27,-29,-30,-31,-32,58,58,58,58,58,58,58,58,-49,-51,58,58,58,]),'MENOS':([12,23,28,30,32,33,34,35,36,37,38,39,40,41,42,43,44,46,48,50,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,77,79,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,110,111,112,],[25,34,34,34,-74,59,34,34,34,-50,-52,-53,-54,-55,34,34,34,34,59,59,34,34,34,34,34,34,34,34,34,34,34,34,34,-28,-41,59,59,59,59,59,34,-75,-27,-29,-30,-31,-32,59,59,59,59,59,59,59,59,-49,-51,34,34,59,59,59,]),'PARIZQ':([15,23,28,29,30,34,35,36,42,43,44,46,58,59,60,61,62,63,64,65,66,67,68,69,70,88,105,106,],[28,36,36,49,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'LOG':([21,],[29,]),'DOSPUNTOS':([22,26,27,],[31,45,47,]),'NOT':([23,28,30,34,35,36,42,43,44,46,58,59,60,61,62,63,64,65,66,67,68,69,70,88,105,106,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'ENTERO':([23,28,30,34,35,36,42,43,44,46,49,58,59,60,61,62,63,64,65,66,67,68,69,70,74,88,105,106,109,],[37,37,37,37,37,37,37,37,37,37,87,37,37,37,37,37,37,37,37,37,37,37,37,37,104,37,37,37,119,]),'TRUE':([23,28,30,34,35,36,42,43,44,46,49,58,59,60,61,62,63,64,65,66,67,68,69,70,88,105,106,109,],[39,39,39,39,39,39,39,39,39,39,84,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,116,]),'FALSE':([23,28,30,34,35,36,42,43,44,46,49,58,59,60,61,62,63,64,65,66,67,68,69,70,88,105,106,109,],[40,40,40,40,40,40,40,40,40,40,85,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,117,]),'CADENA':([23,28,30,34,35,36,42,43,44,46,49,58,59,60,61,62,63,64,65,66,67,68,69,70,88,105,106,109,],[41,41,41,41,41,41,41,41,41,41,83,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,114,]),'STRING':([31,45,47,],[52,52,52,]),'NUMBER':([31,45,47,],[53,53,53,]),'FLOAT':([31,45,47,],[54,54,54,]),'BOOLEAN':([31,45,47,],[55,55,55,]),'CHAR':([31,45,47,],[56,56,56,]),'POR':([32,33,37,38,39,40,41,48,50,71,72,73,75,76,77,79,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,110,111,112,],[-74,60,-50,-52,-53,-54,-55,60,60,60,-41,60,60,60,60,60,-75,60,60,-30,-31,-32,60,60,60,60,60,60,60,60,-49,-51,60,60,60,]),'DIVIDIDO':([32,33,37,38,39,40,41,48,50,71,72,73,75,76,77,79,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,110,111,112,],[-74,61,-50,-52,-53,-54,-55,61,61,61,-41,61,61,61,61,61,-75,61,61,-30,-31,-32,61,61,61,61,61,61,61,61,-49,-51,61,61,61,]),'MODULO':([32,33,37,38,39,40,41,48,50,71,72,73,75,76,77,79,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,110,111,112,],[-74,62,-50,-52,-53,-54,-55,62,62,62,-41,62,62,62,62,62,-75,62,62,-30,-31,-32,62,62,62,62,62,62,62,62,-49,-51,62,62,62,]),'IGUALQUE':([32,33,37,38,39,40,41,48,50,71,72,73,75,76,77,79,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,110,111,112,],[-74,63,-50,-52,-53,-54,-55,63,63,-28,-41,63,63,63,63,63,-75,-27,-29,-30,-31,-32,-33,-34,63,63,63,63,-39,-40,-49,-51,63,63,63,]),'DIFERENTE':([32,33,37,38,39,40,41,48,50,71,72,73,75,76,77,79,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,110,111,112,],[-74,64,-50,-52,-53,-54,-55,64,64,-28,-41,64,64,64,64,64,-75,-27,-29,-30,-31,-32,-33,-34,64,64,64,64,-39,-40,-49,-51,64,64,64,]),'MAYOR':([32,33,37,38,39,40,41,48,50,71,72,73,75,76,77,79,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,110,111,112,],[-74,65,-50,-52,-53,-54,-55,65,65,-28,-41,65,65,65,65,65,-75,-27,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-49,-51,65,65,65,]),'MAYORIGUAL':([32,33,37,38,39,40,41,48,50,71,72,73,75,76,77,79,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,110,111,112,],[-74,66,-50,-52,-53,-54,-55,66,66,-28,-41,66,66,66,66,66,-75,-27,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-49,-51,66,66,66,]),'MENORQUE':([32,33,37,38,39,40,41,48,50,71,72,73,75,76,77,79,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,110,111,112,],[-74,67,-50,-52,-53,-54,-55,67,67,-28,-41,67,67,67,67,67,-75,-27,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-49,-51,67,67,67,]),'MENORIGUAL':([32,33,37,38,39,40,41,48,50,71,72,73,75,76,77,79,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,110,111,112,],[-74,68,-50,-52,-53,-54,-55,68,68,-28,-41,68,68,68,68,68,-75,-27,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-49,-51,68,68,68,]),'AND':([32,33,37,38,39,40,41,48,50,71,72,73,75,76,77,79,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,110,111,112,],[-74,69,-50,-52,-53,-54,-55,69,69,-28,-41,69,69,69,69,69,-75,-27,-29,-30,-31,-32,69,69,69,69,69,69,-39,-40,-49,-51,69,69,69,]),'OR':([32,33,37,38,39,40,41,48,50,71,72,73,75,76,77,79,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,110,111,112,],[-74,70,-50,-52,-53,-54,-55,70,70,-28,-41,70,70,70,70,70,-75,-27,-29,-30,-31,-32,70,70,70,70,70,70,70,-40,-49,-51,70,70,70,]),'PARDER':([32,37,38,39,40,41,48,71,72,73,82,83,84,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,114,115,116,117,118,119,],[-74,-50,-52,-53,-54,-55,81,-28,-41,103,108,-57,-58,-59,-60,-61,-75,-27,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-49,-51,-62,-56,-63,-64,-65,-66,]),'LLAVIZQ':([81,121,],[107,122,]),'COMA':([83,],[109,]),'ELSE':([120,],[121,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,107,122,],[2,113,123,]),'instruccion':([0,2,107,113,122,123,],[3,16,3,16,3,16,]),'imprimir_instr':([0,2,107,113,122,123,],[4,4,4,4,4,4,]),'declaracion_instr':([0,2,107,113,122,123,],[5,5,5,5,5,5,]),'asignacion_instr':([0,2,107,113,122,123,],[6,6,6,6,6,6,]),'constante_instr':([0,2,107,113,122,123,],[7,7,7,7,7,7,]),'if_instr':([0,2,107,113,122,123,],[8,8,8,8,8,8,]),'if_else_instr':([0,2,107,113,122,123,],[9,9,9,9,9,9,]),'expresion':([23,28,30,34,35,36,42,43,44,46,58,59,60,61,62,63,64,65,66,67,68,69,70,88,105,106,],[33,48,50,71,72,73,75,76,77,79,90,91,92,93,94,95,96,97,98,99,100,101,102,110,111,112,]),'decimal':([23,28,30,34,35,36,42,43,44,46,49,58,59,60,61,62,63,64,65,66,67,68,69,70,88,105,106,109,],[38,38,38,38,38,38,38,38,38,38,86,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,118,]),'tipo_dato':([31,45,47,],[51,78,80,]),'expresionCadena':([49,],[82,]),'expresionCadena2':([109,],[115,]),}

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
  ('instruccion -> if_instr','instruccion',1,'p_instruccion','gramatica.py',48),
  ('instruccion -> if_else_instr','instruccion',1,'p_instruccion','gramatica.py',49),
  ('imprimir_instr -> CONSOLE PUNTO LOG PARIZQ expresionCadena PARDER','imprimir_instr',6,'p_instruccion_console','gramatica.py',61),
  ('tipo_dato -> STRING','tipo_dato',1,'p_tipo_dato','gramatica.py',70),
  ('tipo_dato -> NUMBER','tipo_dato',1,'p_tipo_dato','gramatica.py',71),
  ('tipo_dato -> FLOAT','tipo_dato',1,'p_tipo_dato','gramatica.py',72),
  ('tipo_dato -> BOOLEAN','tipo_dato',1,'p_tipo_dato','gramatica.py',73),
  ('tipo_dato -> CHAR','tipo_dato',1,'p_tipo_dato','gramatica.py',74),
  ('declaracion_instr -> LET ID IGUAL expresion','declaracion_instr',4,'p_instruccion_declaracion','gramatica.py',84),
  ('declaracion_instr -> VAR ID IGUAL expresion','declaracion_instr',4,'p_instruccion_declaracion','gramatica.py',85),
  ('declaracion_instr -> LET ID DOSPUNTOS tipo_dato','declaracion_instr',4,'p_instruccion_declaracion','gramatica.py',86),
  ('declaracion_instr -> VAR ID DOSPUNTOS tipo_dato','declaracion_instr',4,'p_instruccion_declaracion','gramatica.py',87),
  ('declaracion_instr -> LET ID DOSPUNTOS tipo_dato IGUAL expresion','declaracion_instr',6,'p_instruccion_declaracion','gramatica.py',88),
  ('declaracion_instr -> VAR ID DOSPUNTOS tipo_dato IGUAL expresion','declaracion_instr',6,'p_instruccion_declaracion','gramatica.py',89),
  ('asignacion_instr -> ID IGUAL expresion','asignacion_instr',3,'p_instruccion_asignacion','gramatica.py',105),
  ('asignacion_instr -> ID MAS IGUAL expresion','asignacion_instr',4,'p_instruccion_asignacion','gramatica.py',106),
  ('asignacion_instr -> ID MENOS IGUAL expresion','asignacion_instr',4,'p_instruccion_asignacion','gramatica.py',107),
  ('constante_instr -> CONST ID IGUAL expresion','constante_instr',4,'p_instruccion_constantes','gramatica.py',123),
  ('constante_instr -> CONST ID DOSPUNTOS tipo_dato IGUAL expresion','constante_instr',6,'p_instruccion_constantes','gramatica.py',124),
  ('expresion -> expresion MAS expresion','expresion',3,'p_expresion_binaria','gramatica.py',138),
  ('expresion -> MENOS expresion','expresion',2,'p_expresion_binaria','gramatica.py',139),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_expresion_binaria','gramatica.py',140),
  ('expresion -> expresion POR expresion','expresion',3,'p_expresion_binaria','gramatica.py',141),
  ('expresion -> expresion DIVIDIDO expresion','expresion',3,'p_expresion_binaria','gramatica.py',142),
  ('expresion -> expresion MODULO expresion','expresion',3,'p_expresion_binaria','gramatica.py',143),
  ('expresion -> expresion IGUALQUE expresion','expresion',3,'p_expresion_logica','gramatica.py',165),
  ('expresion -> expresion DIFERENTE expresion','expresion',3,'p_expresion_logica','gramatica.py',166),
  ('expresion -> expresion MAYOR expresion','expresion',3,'p_expresion_logica','gramatica.py',167),
  ('expresion -> expresion MAYORIGUAL expresion','expresion',3,'p_expresion_logica','gramatica.py',168),
  ('expresion -> expresion MENORQUE expresion','expresion',3,'p_expresion_logica','gramatica.py',169),
  ('expresion -> expresion MENORIGUAL expresion','expresion',3,'p_expresion_logica','gramatica.py',170),
  ('expresion -> expresion AND expresion','expresion',3,'p_operacion_logica','gramatica.py',191),
  ('expresion -> expresion OR expresion','expresion',3,'p_operacion_logica','gramatica.py',192),
  ('expresion -> NOT expresion','expresion',2,'p_operacion_logica','gramatica.py',193),
  ('if_instr -> IF PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDER','if_instr',7,'p_if_instr','gramatica.py',217),
  ('if_else_instr -> IF PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDER ELSE LLAVIZQ instrucciones LLAVDER','if_else_instr',11,'p_if_else_instr','gramatica.py',226),
  ('funcion_instr -> FUNCTION ID PARIZQ ID COMA ID PARDER LLAVIZQ instrucciones LLAVDER PUNTOCOMA','funcion_instr',11,'p_funcion_instr','gramatica.py',241),
  ('call_funcion_instr -> ID PARIZQ expresion COMA expresion PARDER PUNTOCOMA','call_funcion_instr',7,'p_call_funcion_instr','gramatica.py',251),
  ('interface_instr -> INTERFACE ID LLAVIZQ interface_params PUNTOCOMA LLAVDER','interface_instr',6,'p_instruccion_interface','gramatica.py',262),
  ('interface_params -> interface_params PUNTOCOMA ID DOSPUNTOS expresion','interface_params',5,'p_instruccion_interface_params','gramatica.py',271),
  ('interface_params -> ID DOSPUNTOS expresion','interface_params',3,'p_instruccion_interface_params','gramatica.py',272),
  ('expresion -> PARIZQ expresion PARDER','expresion',3,'p_expresion_agrupacion','gramatica.py',287),
  ('expresion -> ENTERO','expresion',1,'p_expresion_number','gramatica.py',296),
  ('decimal -> ENTERO PUNTO ENTERO','decimal',3,'p_decimal','gramatica.py',306),
  ('expresion -> decimal','expresion',1,'p_expresion_decimal','gramatica.py',312),
  ('expresion -> TRUE','expresion',1,'p_expresion_cadenas','gramatica.py',322),
  ('expresion -> FALSE','expresion',1,'p_expresion_cadenas','gramatica.py',323),
  ('expresion -> CADENA','expresion',1,'p_expresion_cadenas','gramatica.py',324),
  ('expresionCadena -> CADENA COMA expresionCadena2','expresionCadena',3,'p_expresion_cadena','gramatica.py',330),
  ('expresionCadena -> CADENA','expresionCadena',1,'p_expresion_cadena','gramatica.py',331),
  ('expresionCadena -> TRUE','expresionCadena',1,'p_expresion_cadena','gramatica.py',332),
  ('expresionCadena -> FALSE','expresionCadena',1,'p_expresion_cadena','gramatica.py',333),
  ('expresionCadena -> decimal','expresionCadena',1,'p_expresion_cadena','gramatica.py',334),
  ('expresionCadena -> ENTERO','expresionCadena',1,'p_expresion_cadena','gramatica.py',335),
  ('expresionCadena2 -> CADENA','expresionCadena2',1,'p_expresion_cadena2','gramatica.py',346),
  ('expresionCadena2 -> TRUE','expresionCadena2',1,'p_expresion_cadena2','gramatica.py',347),
  ('expresionCadena2 -> FALSE','expresionCadena2',1,'p_expresion_cadena2','gramatica.py',348),
  ('expresionCadena2 -> decimal','expresionCadena2',1,'p_expresion_cadena2','gramatica.py',349),
  ('expresionCadena2 -> ENTERO','expresionCadena2',1,'p_expresion_cadena2','gramatica.py',350),
  ('parseInt -> PARSEINT PARIZQ expresionCadena PARDER PUNTOCOMA','parseInt',5,'p_parseInt','gramatica.py',361),
  ('parseFloat -> PARSEFLOAT PARIZQ expresionCadena PARDER PUNTOCOMA','parseFloat',5,'p_parseFloat','gramatica.py',370),
  ('toString -> ID PUNTO TOSTRING PARIZQ PARDER','toString',5,'p_toString','gramatica.py',379),
  ('toLowerCase -> ID PUNTO TOLOWERCASE PARIZQ PARDER','toLowerCase',5,'p_toLowerCase','gramatica.py',387),
  ('toUpperCase -> ID PUNTO TOUPPERCASE PARIZQ PARDER','toUpperCase',5,'p_toUpperCase','gramatica.py',394),
  ('typeof -> TYPEOF expresion','typeof',2,'p_typeof','gramatica.py',401),
  ('typeof -> TYPEOF ID','typeof',2,'p_typeof','gramatica.py',402),
  ('expresion -> ID','expresion',1,'p_expresion_id','gramatica.py',409),
  ('expresion -> ID PUNTO ID','expresion',3,'p_expresion_id','gramatica.py',410),
]


# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'NUM PLUS MINUS TIMES DIVIDE LPAREN RPAREN\n    expr : expr PLUS term\n         | expr MINUS term\n    \n    expr : term\n    \n    term : term TIMES factor\n         | term DIVIDE factor\n    \n    term : factor\n    \n    factor : NUM\n    \n    factor : LPAREN expr RPAREN\n    '
    
_lr_action_items = {'DIVIDE':([3,4,5,11,12,13,14,15,],[-6,9,-7,-8,9,9,-5,-4,]),'LPAREN':([0,1,7,8,9,10,],[1,1,1,1,1,1,]),'PLUS':([2,3,4,5,6,11,12,13,14,15,],[8,-6,-3,-7,8,-8,-2,-1,-5,-4,]),'RPAREN':([3,4,5,6,11,12,13,14,15,],[-6,-3,-7,11,-8,-2,-1,-5,-4,]),'TIMES':([3,4,5,11,12,13,14,15,],[-6,10,-7,-8,10,10,-5,-4,]),'$end':([2,3,4,5,11,12,13,14,15,],[0,-6,-3,-7,-8,-2,-1,-5,-4,]),'MINUS':([2,3,4,5,6,11,12,13,14,15,],[7,-6,-3,-7,7,-8,-2,-1,-5,-4,]),'NUM':([0,1,7,8,9,10,],[5,5,5,5,5,5,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'factor':([0,1,7,8,9,10,],[3,3,3,3,14,15,]),'expr':([0,1,],[2,6,]),'term':([0,1,7,8,],[4,4,12,13,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expr","S'",1,None,None,None),
  ('expr -> expr PLUS term','expr',3,'p_expr','plyexample.py',44),
  ('expr -> expr MINUS term','expr',3,'p_expr','plyexample.py',45),
  ('expr -> term','expr',1,'p_expr_term','plyexample.py',55),
  ('term -> term TIMES factor','term',3,'p_term','plyexample.py',62),
  ('term -> term DIVIDE factor','term',3,'p_term','plyexample.py',63),
  ('term -> factor','term',1,'p_term_factor','plyexample.py',73),
  ('factor -> NUM','factor',1,'p_factor','plyexample.py',80),
  ('factor -> LPAREN expr RPAREN','factor',3,'p_factor_group','plyexample.py',87),
]


# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMMENT MOVE OPENING RESULT TITLE\n    game : tags moves\n    \n    tags : tag\n         | tag tags\n    \n    tag : TITLE\n        | RESULT\n        | OPENING\n    \n    moves : move\n          | move moves\n    \n    move : MOVE OPENING COMMENT\n         | MOVE OPENING\n    '
    
_lr_action_items = {'TITLE':([0,3,4,5,6,],[4,4,-4,-5,-6,]),'RESULT':([0,3,4,5,6,],[5,5,-4,-5,-6,]),'OPENING':([0,3,4,5,6,9,],[6,6,-4,-5,-6,12,]),'$end':([1,7,8,11,12,13,],[0,-1,-7,-8,-10,-9,]),'MOVE':([2,3,4,5,6,8,10,12,13,],[9,-2,-4,-5,-6,9,-3,-10,-9,]),'COMMENT':([12,],[13,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'game':([0,],[1,]),'tags':([0,3,],[2,10,]),'tag':([0,3,],[3,3,]),'moves':([2,8,],[7,11,]),'move':([2,8,],[8,8,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> game","S'",1,None,None,None),
  ('game -> tags moves','game',2,'p_game','testPgn.py',35),
  ('tags -> tag','tags',1,'p_tags','testPgn.py',40),
  ('tags -> tag tags','tags',2,'p_tags','testPgn.py',41),
  ('tag -> TITLE','tag',1,'p_tag','testPgn.py',46),
  ('tag -> RESULT','tag',1,'p_tag','testPgn.py',47),
  ('tag -> OPENING','tag',1,'p_tag','testPgn.py',48),
  ('moves -> move','moves',1,'p_moves','testPgn.py',53),
  ('moves -> move moves','moves',2,'p_moves','testPgn.py',54),
  ('move -> MOVE OPENING COMMENT','move',3,'p_move','testPgn.py',59),
  ('move -> MOVE OPENING','move',2,'p_move','testPgn.py',60),
]
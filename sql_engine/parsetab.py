
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BOOL COMMA DELETE EQ GE GT INSERT KEYWORD LE LIKE LT NE NUMBER OR SELECT SET STAR STR UPDATE VALUES WHEREsql_stam : select_stam\n                        | insert_stam\n                        | update_stam\n                        | delete_stamselect_stam : SELECT attr_list cond_staminsert_stam : INSERT attr_list VALUES values_listupdate_stam : UPDATE SET assg_stam cond_stamdelete_stam : DELETE cond_stamattr_list : attr COMMA attr_list\n                         | attr\n                         | STAR\n                         | emptyattr : STRcond_stam : WHERE or_cond\n                         | emptyor_cond : and_cond OR or_cond\n                       | and_condand_cond : cond AND and_cond\n                        | condcond : STR pred valuepred : EQ\n \t                | NE\n \t                | LT\n \t                | LE\n \t                | GT\n \t                | GE\n \t                | LIKEvalues_list : value COMMA values_list\n \t                       | valuevalue : STR\n \t                 | NUMBER\n \t                 | BOOLassg_stam : assg COMMA assg_stam\n \t                     | assgassg : STR EQ valueempty :'
    
_lr_action_items = {'SELECT':([0,],[6,]),'INSERT':([0,],[7,]),'UPDATE':([0,],[8,]),'DELETE':([0,],[9,]),'$end':([1,2,3,4,5,6,9,10,11,12,13,14,17,19,20,21,23,24,26,27,28,30,31,32,33,34,35,36,50,51,52,53,54,55,],[0,-1,-2,-3,-4,-36,-36,-36,-10,-11,-12,-13,-8,-15,-5,-36,-36,-34,-14,-17,-19,-9,-6,-29,-30,-31,-32,-7,-33,-35,-16,-18,-20,-28,]),'STAR':([6,7,21,],[12,12,12,]),'STR':([6,7,16,18,21,22,37,38,39,40,41,42,43,44,45,46,47,48,49,],[14,14,25,29,14,33,25,33,29,29,33,-21,-22,-23,-24,-25,-26,-27,33,]),'WHERE':([6,9,10,11,12,13,14,21,23,24,30,33,34,35,50,51,],[-36,18,18,-10,-11,-12,-13,-36,18,-34,-9,-30,-31,-32,-33,-35,]),'VALUES':([7,11,12,13,14,15,21,30,],[-36,-10,-11,-12,-13,22,-36,-9,]),'SET':([8,],[16,]),'COMMA':([11,14,24,32,33,34,35,51,],[21,-13,37,49,-30,-31,-32,-35,]),'NUMBER':([22,38,41,42,43,44,45,46,47,48,49,],[34,34,34,-21,-22,-23,-24,-25,-26,-27,34,]),'BOOL':([22,38,41,42,43,44,45,46,47,48,49,],[35,35,35,-21,-22,-23,-24,-25,-26,-27,35,]),'EQ':([25,29,],[38,42,]),'OR':([27,28,33,34,35,53,54,],[39,-19,-30,-31,-32,-18,-20,]),'AND':([28,33,34,35,54,],[40,-30,-31,-32,-20,]),'NE':([29,],[43,]),'LT':([29,],[44,]),'LE':([29,],[45,]),'GT':([29,],[46,]),'GE':([29,],[47,]),'LIKE':([29,],[48,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sql_stam':([0,],[1,]),'select_stam':([0,],[2,]),'insert_stam':([0,],[3,]),'update_stam':([0,],[4,]),'delete_stam':([0,],[5,]),'attr_list':([6,7,21,],[10,15,30,]),'attr':([6,7,21,],[11,11,11,]),'empty':([6,7,9,10,21,23,],[13,13,19,19,13,19,]),'cond_stam':([9,10,23,],[17,20,36,]),'assg_stam':([16,37,],[23,50,]),'assg':([16,37,],[24,24,]),'or_cond':([18,39,],[26,52,]),'and_cond':([18,39,40,],[27,27,53,]),'cond':([18,39,40,],[28,28,28,]),'values_list':([22,49,],[31,55,]),'value':([22,38,41,49,],[32,51,54,32,]),'pred':([29,],[41,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sql_stam","S'",1,None,None,None),
  ('sql_stam -> select_stam','sql_stam',1,'p_sql_stam','sql_engine.py',94),
  ('sql_stam -> insert_stam','sql_stam',1,'p_sql_stam','sql_engine.py',95),
  ('sql_stam -> update_stam','sql_stam',1,'p_sql_stam','sql_engine.py',96),
  ('sql_stam -> delete_stam','sql_stam',1,'p_sql_stam','sql_engine.py',97),
  ('select_stam -> SELECT attr_list cond_stam','select_stam',3,'p_select_stam','sql_engine.py',102),
  ('insert_stam -> INSERT attr_list VALUES values_list','insert_stam',4,'p_insert_stam','sql_engine.py',107),
  ('update_stam -> UPDATE SET assg_stam cond_stam','update_stam',4,'p_update_stam','sql_engine.py',112),
  ('delete_stam -> DELETE cond_stam','delete_stam',2,'p_delete_stam','sql_engine.py',117),
  ('attr_list -> attr COMMA attr_list','attr_list',3,'p_attr_list','sql_engine.py',122),
  ('attr_list -> attr','attr_list',1,'p_attr_list','sql_engine.py',123),
  ('attr_list -> STAR','attr_list',1,'p_attr_list','sql_engine.py',124),
  ('attr_list -> empty','attr_list',1,'p_attr_list','sql_engine.py',125),
  ('attr -> STR','attr',1,'p_attr','sql_engine.py',130),
  ('cond_stam -> WHERE or_cond','cond_stam',2,'p_cond_stam','sql_engine.py',135),
  ('cond_stam -> empty','cond_stam',1,'p_cond_stam','sql_engine.py',136),
  ('or_cond -> and_cond OR or_cond','or_cond',3,'p_or_cond','sql_engine.py',141),
  ('or_cond -> and_cond','or_cond',1,'p_or_cond','sql_engine.py',142),
  ('and_cond -> cond AND and_cond','and_cond',3,'p_and_cond','sql_engine.py',147),
  ('and_cond -> cond','and_cond',1,'p_and_cond','sql_engine.py',148),
  ('cond -> STR pred value','cond',3,'p_cond','sql_engine.py',153),
  ('pred -> EQ','pred',1,'p_pred','sql_engine.py',159),
  ('pred -> NE','pred',1,'p_pred','sql_engine.py',160),
  ('pred -> LT','pred',1,'p_pred','sql_engine.py',161),
  ('pred -> LE','pred',1,'p_pred','sql_engine.py',162),
  ('pred -> GT','pred',1,'p_pred','sql_engine.py',163),
  ('pred -> GE','pred',1,'p_pred','sql_engine.py',164),
  ('pred -> LIKE','pred',1,'p_pred','sql_engine.py',165),
  ('values_list -> value COMMA values_list','values_list',3,'p_values_list','sql_engine.py',170),
  ('values_list -> value','values_list',1,'p_values_list','sql_engine.py',171),
  ('value -> STR','value',1,'p_value','sql_engine.py',176),
  ('value -> NUMBER','value',1,'p_value','sql_engine.py',177),
  ('value -> BOOL','value',1,'p_value','sql_engine.py',178),
  ('assg_stam -> assg COMMA assg_stam','assg_stam',3,'p_assg_stam','sql_engine.py',183),
  ('assg_stam -> assg','assg_stam',1,'p_assg_stam','sql_engine.py',184),
  ('assg -> STR EQ value','assg',3,'p_assg','sql_engine.py',189),
  ('empty -> <empty>','empty',0,'p_empty','sql_engine.py',194),
]

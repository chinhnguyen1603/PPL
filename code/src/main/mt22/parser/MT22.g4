/*-------------- Student id: 1811622 Nguyen Ngoc Chinh---------------------*/

grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

/*-------------- Parse ---------------------*/
/*-------------- Parse ---------------------*/
/*-------------- Parse ---------------------*/
program:  (var_decl|func_decl)+ EOF ;

//variable declarations
var_decl: global_var_decl | local_var_decl | parameter_of_func;
global_var_decl: id_list COLON typ (ASSIGN list_expr)? SEMICOLON 
{
if ($list_expr.text != None):   
   if (len($id_list.text.split(',')) != len($list_expr.text.split(','))):
      offendingSymbol = self._ctx.start
      line = offendingSymbol.line
      column = self.getCurrentToken().stop
      offendingSymbol.text = ";"
      listener = self._listeners[-1]
      listener.syntaxError(self, offendingSymbol, line, column, "", None)
};
local_var_decl: id_list COLON typ (ASSIGN list_expr)? SEMICOLON
{
if ($list_expr.text != None):   
   if (len($id_list.text.split(',')) != len($list_expr.text.split(','))):
      offendingSymbol = self._ctx.start
      line = offendingSymbol.line
      column = self.getCurrentToken().stop
      offendingSymbol.text = ";"
      listener = self._listeners[-1]
      listener.syntaxError(self, offendingSymbol, line, column, "", None)
};
parameter_of_func: INHERIT? OUT? ID COLON typ;
list_parameter: parameter_of_func (COMMA parameter_of_func)* ;
id_list: ID (COMMA ID)*;

//function declarations
func_decl: func_prototype func_body;
func_prototype: ID COLON FUNCTION typ LB list_parameter* RB (INHERIT ID)*;
func_body: block_stmt;


boolean_literal: TRUE | FALSE ;
literal: INT_LIT | FLOAT_LIT | STRING_LIT | boolean_literal | index_array;

//type_declaration
atomic_typ: BOOLEAN | INTERGER | FLOAT | STRING;
index_array: LP literal (',' literal)* RP; //{1, 5, 7, 12} or  {"Kangxi", "Yongzheng", "Qianlong"}
array_literal_type: ARRAY LSB literal (',' literal)* RSB OF atomic_typ; //array [2, 3] of integer
//all type of system
typ: atomic_typ 
   | array_literal_type
   | VOID
   | AUTO
   ; 

//expression
list_expr: expression (COMMA expression)*;
expression: string_expr;
string_expr: relation_expr string_operator relation_expr //lowest - infix -none
           | relation_expr
		   ;
relation_expr: logical_first_expr relational_operator logical_first_expr  // infix -none
           |logical_first_expr 
		   ;
logical_first_expr: logical_first_expr logical_first_operator adding_expr  // infix - left
           | adding_expr 
		   ;
adding_expr: adding_expr adding_operator multiplying_expr  // infix - left
           | multiplying_expr
		   ;
multiplying_expr: multiplying_expr multiplying_operator logical_second_expr  // infix - left
           | logical_second_expr 
		   ;
logical_second_expr: logical_second_operator sign_expr  // prefix - right
           | sign_expr
		   ;
sign_expr: sign_operator index_expr  // prefix - right
           | index_expr
		   ;
index_expr: index_expr index_operator
           | operand
		   ;
operand
    : ID
    | literal
    | func_call_exp
    | '(' expression ')' //sub_exp; phải đc ưu tiên tính trước nên có () (biểu thức trong biểu thức: a=exp=>2-exp=>2-(3+4))
    ;

func_call_exp: ID LB (expression (COMMA expression)*)? RB ;

//operator
string_operator: DOUBLE_COLON;
relational_operator: EQUAL 
                   | NOT_EQUAL
				   | LESS
				   | GREATER
				   | LESS_OR_EQUAL
				   | GREATER_OR_EQUAL
				   ;
logical_first_operator: AND
                      | OR
					  ;
adding_operator: ADDOP
               | SUBOP
			   ;
multiplying_operator: MULOP
                    | DIV
					| MOD
					;			   					  				    
logical_second_operator: NOT;
sign_operator: SUBOP;
index_operator: LSB expression RSB;


//statement
stmt_decl: assign_stmt 
    | if_stmt
    | for_stmt
    | while_stmt 
    | do_while_stmt
    | break_stmt
    | continue_stmt
    | call_stmt
    | return_stmt
    ;
assign_stmt: (scalar_var index_operator?) ASSIGN expression SEMICOLON;
if_stmt:IF expression list_stmt SEMICOLON? (ELSE list_stmt SEMICOLON?)?;
break_stmt: BREAK SEMICOLON;
for_stmt
    :
        FOR LB scalar_var ASSIGN expression COMMA expression COMMA expression RB LP
            list_stmt
        RP
    ;
while_stmt: WHILE LB expression RB LP list_stmt RP ;
do_while_stmt: DO block_stmt WHILE LB expression RB SEMICOLON;
call_stmt: func_call_exp SEMICOLON;
return_stmt: RETURN expression? SEMICOLON;
continue_stmt: CONTINUE_MT SEMICOLON;
list_stmt: stmt_decl*;

block_stmt: LP var_decl* list_stmt RP;
scalar_var: ID;








/*-------------- Lexer ---------------------*/
/*-------------- Lexer ---------------------*/
/*-------------- Lexer ---------------------*/

//comment
COMMENT_C  : '/*' .*? '*/' -> skip;
COMMENT_CPLUS   : '//' ~ [\r\n]* -> skip ;

//Literal
fragment INT: [1-9]([0-9]*'_'[0-9]+)*| '0' | [1-9][0-9]*;
fragment EXPONENT: [eE] SIGN? DIGIT+ ;
fragment SIGN: [+-] ;

//Integer_Literal
INT_LIT: INT {
	self.text = (self.text).replace("_", "") 
};

//Float_Literal
fragment FLOATFRAG: INT '.' DIGIT* EXPONENT* //Decimal part absent 
        | INT? '.' DIGIT+ //Integer part absent or not 
		| INT EXPONENT //7E-10
		| INT '.' DIGIT+ EXPONENT //no part absent
        ;
FLOAT_LIT: FLOATFRAG{
    self.text = (self.text).replace("_", "") 
};

//Boolean_Literal -> of Parse
//BOOLLIT: TRUE | FALSE ;

//String_Literal
STRING_LIT: '"' STRING_CHAR* '"'{
	self.text = (self.text)[1:-1]
};
fragment STRING_CHAR: ~["\\] | ESC_SEQ |  '\\"';
fragment ESC_SEQ: '\\' [btnfr'\\] ; // tức là \b nhưng phải gõ \\b để loại trừ \đầu
fragment ESC_ILLEGAL: '\\' ~[btnfr"'\\] | ~'\\' ;

//Array_Literal -> of Parse

//keyword
AUTO: 'auto';
FALSE: 'false';
INTERGER: 'integer';
VOID: 'void';
ARRAY: 'array';
BREAK: 'break';
FLOAT: 'float';
RETURN: 'return';
OUT: 'out';
BOOLEAN: 'boolean';
FOR: 'for';
STRING: 'string';
CONTINUE_MT: 'continue';
DO: 'do';
FUNCTION: 'function';
TRUE: 'true';
OF: 'of';
ELSE: 'else';
IF: 'if';
WHILE: 'while';
INHERIT: 'inherit';

//operator
ADDOP: '+';
SUBOP: '-';
MULOP: '*';
DIV: '/';
MOD: '%';
NOT: '!';
AND: '&&';
OR: '||';
EQUAL: '==';
NOT_EQUAL: '!=';
LESS: '<'	;
LESS_OR_EQUAL: '<=';
GREATER: '>';
GREATER_OR_EQUAL: '>=';	
DOUBLE_COLON: '::';


//separator
LB: '(';
RB: ')';
LSB: '[';
RSB: ']';
DOT: '.';
COMMA: ',';
SEMICOLON: ';';
COLON: ':';
LP: '{';
RP: '}';
ASSIGN: '=';

//Identifier
fragment LETTER: [a-zA-Z];
fragment UNDERSCORE: '_';
fragment DIGIT: [0-9];
ID: (UNDERSCORE | LETTER) (UNDERSCORE | LETTER | DIGIT)*;

// skip spaces, tabs, newlines
WS : [ \b\f\t\r\n]+ -> skip ; 

//Lexical Error
ERROR_CHAR: . {raise ErrorToken(self.text) };
UNCLOSE_STRING: '"' STRING_CHAR* ( [\b\t\n\f\r"'\\] | EOF )
	{
		possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
		if self.text[-1] in possible:
			raise UncloseString(self.text[1:-1])
		else:
			raise UncloseString(self.text[1:])
	}
	;


ILLEGAL_ESCAPE: '"' STRING_CHAR* ESC_ILLEGAL
	{
		raise IllegalEscape(self.text[1:])
	}
	;

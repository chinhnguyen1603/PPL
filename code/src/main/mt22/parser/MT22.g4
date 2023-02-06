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
program:  var_decl* func_decl* EOF ;
var_decl: id_list COLON INTERGER (ASSIGN INTLIT (COMMA INTLIT)*)* SEMICOLON;
id_list: ID (COMMA ID)*;

//Function declaration
func_decl: FUNCTION;





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
INTLIT: INT {
	self.text = (self.text).replace("_", "") 
};

//Float_Literal
fragment FLOATFRAG: INT '.' DIGIT* EXPONENT* //Decimal part absent 
        | INT? '.' DIGIT+ //Integer part absent or not 
		| INT EXPONENT //7E-10
		| INT '.' DIGIT+ EXPONENT //no part absent
        ;
FLOATLIT: FLOATFRAG{
    self.text = (self.text).replace("_", "") 
};

//Boolean_Literal -> of Parse
BOOLLIT: TRUE | FALSE ;

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
CONTINUE: 'continue';
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
	
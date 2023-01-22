grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program:  EOF ;
/*-------------- Parse ---------------------*/

/*-------------- Lexer ---------------------*/

//comment
COMMENT_C  : '/*' .*? '*/' -> skip;
COMMENT_CPLUS   : '//' ~ [\r\n]* -> skip ;

//Identifier
fragment LETTER: [a-zA-Z];
fragment UNDERSCORE: '_';
fragment DIGIT: [0-9];
ID: (UNDERSCORE | LETTER) (UNDERSCORE | LETTER | DIGIT)*;

//keyword
AUTO: 'auto';
FALSE: 'false';
INT: 'integer';
WHILE: 'while';
OF: 'of';
BREAK: 'break';
FLOAT: 'float';
RETURN: 'return';
VOID: 'void';
INHERIT: 'inherit';
BOOLEAN: 'boolean';
FOR: 'for';
STRING: 'string';
FUNCTION: 'function';
DO: 'do';
TRUE: 'true';
OUT: 'out';
ELSE: 'else';
IF: 'if';
CONTINUE: 'continue';


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
//ASSIGN: '=';
//INDEXOP: ':=';

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


// skip spaces, tabs, newlines
WS : [ \b\f\t\r\n]+ -> skip ; 

ERROR_CHAR: . {raise ErrorToken(self.text) };
UNCLOSE_STRING: . {raise UncloseString(self.text) };
ILLEGAL_ESCAPE: . {raise IllegalEscape(self.text) };
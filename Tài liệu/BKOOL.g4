grammar BKOOL;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    else:
        return result;
}

options{
	language=Python3;
}

//-------------------------------------------------------------------------------------------------
// -----------------------Parser-------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------
program  : classDecl+ EOF ;

classDecl: CLASS ID (EXTENDS ID)? LP member* RP;

member:  attribute SEMI
		| (STATIC)? method
		;

attribute: STATIC? mutable 
		| (FINAL | STATIC FINAL |FINAL STATIC)?  immutable
		;

immutable: mType tailImmutable;

mutable: mType tailMutable;

tailMutable: initialMutable (COMMA initialMutable)*;

initialMutable: ID (EQUAL exp)?;

tailImmutable: initialImmutable (COMMA initialImmutable)*;

initialImmutable: ID (EQUAL exp)?;

classType: ID;

arrayType: elementType LSB INTEGER_LITERAL RSB;

elementType: INT | FLOAT | STRING | BOOLEAN | classType | VOID;

method: mType ID LB listParameter? RB blockStmt
    | 	contructorMethod	//contructorMethod
    ;

contructorMethod: ID  LB listParameter? RB blockStmt;

mType: INT | FLOAT | STRING | BOOLEAN | VOID | classType | arrayType;

listParameter: parameter (SEMI parameter)*;

parameter: mType ID (COMMA ID)*;

//-------------------------------------------------------------------------------
//---------------------Statement-------------------------------------------------
//-------------------------------------------------------------------------------

//---Block Statement---
blockStmt: LP contentBlock RP;

contentBlock: (listValDecl SEMI)* (listStmt)*
			;

listValDecl: mutable| FINAL immutable;

listStmt:  blockStmt 
		| assignmentStmt 
		| ifStmt 
		| forStmt 
		| breakStmt 
		| continueStmt 
		| returnStmt 
		| methodInvocationStmt SEMI
		;

//---Assignment Statement---
assignmentStmt: exp ASSIGN exp SEMI;

//---If statement---
ifStmt: IF exp THEN listStmt (ELSE listStmt)?;

//---For statement---
forStmt: FOR ID ASSIGN exp (TO | DOWNTO) exp DO listStmt;

//---Break statement---
breakStmt: BREAK SEMI;

//---Continue statement---
continueStmt: CONTINUE SEMI;

//---Return statement---
returnStmt: RETURN exp SEMI;

//---Method Invocation Statement---
methodInvocationStmt: exp DOT methodCall;

methodCall: ID LB listExp? RB;


//---------------------------------------------------------------------------------------------------
//---------------------------------------Expresion---------------------------------------------------
//---------------------------------------------------------------------------------------------------
exp:  exp1 (LESSTHAN | GREATERTHAN | LESSTHANOREQUAL | GREATERTHANOREQUAL) exp1
	| exp1
	;

exp1: exp2 ( EQ | NOT_EQ) exp2
	| exp2
	;

exp2: exp2 (OR | AND) exp3
	| exp3
	;

exp3: exp3 (SUB | ADD) exp4
	| exp4
	;

exp4: exp4 (MUL | DIVINT | DIVFLOAT | MOD) exp5
	| exp5
	;

exp5: exp5 CONCATENATION exp6
	| exp6
	;

exp6: NOT exp6	
	| exp7
	;

exp7: (ADD | SUB) exp7
	| exp8
	;

exp8:  exp9 indexExp
	| exp9
	;

exp9: exp9 DOT (ID | methodCall)
	| exp10
	;

exp10: NEW ID LB listExp? RB
	| exp11
	;

exp11: LB exp RB
	| literal
	| ID
	;

literal: INTEGER_LITERAL
	| FLOAT_LITERAL
	| booleanLiteral
	| STRING_LITERAL
	| arrayLiteral
	| THIS
	| NIL
	;

booleanLiteral: TRUE | FALSE;

arrayLiteral: LP listElement  RP;

listElement: element (COMMA element)*;

element: INTEGER_LITERAL
	| FLOAT_LITERAL
	| booleanLiteral
	| STRING_LITERAL
	| THIS
	| NIL
	;

listExp: exp (COMMA exp)*;

indexExp: LSB exp RSB;


//---------------------------------------------------------------------------------------------------
//----------------------------------------Lexer------------------------------------------------------
//---------------------------------------------------------------------------------------------------


//--KEYWORD--
BOOLEAN: 'boolean';
BREAK: 'break';
CLASS: 'class';
CONTINUE: 'continue';
DO: 'do';
ELSE: 'else';
EXTENDS: 'extends';
FLOAT: 'float';
IF: 'if';
INT: 'int';
NEW: 'new';
STRING: 'string';
THEN: 'then';
FOR: 'for';
RETURN: 'return';
TRUE: 'true';
FALSE: 'false';
VOID: 'void';
NIL: 'nil';
THIS: 'this';
FINAL: 'final';
STATIC: 'static';
TO: 'to';
DOWNTO: 'downto';

//--Operator--
ASSIGN: ':=';
ADD: '+';
SUB: '-';
MUL: '*';
DIVINT: '\\';
DIVFLOAT: '/';
MOD: '%';
NOT_EQ: '!=';
EQ: '==';
EQUAL: '=';
LESSTHAN: '<';
GREATERTHAN: '>';
LESSTHANOREQUAL: '<=';
GREATERTHANOREQUAL: '>=';
OR: '||';
AND: '&&';
NOT: '!';
CONCATENATION: '^';
OBJECTCREATE: NEW;

//--Sepatator--
LSB: '[';
RSB: ']';
LP: '{';
RP: '}';
LB: '(';
RB: ')';
SEMI: ';';
COLON: ':';
DOT: '.';
COMMA: ',';

// --COMMENT--
WS  :  [ \t\r\n]+ -> skip 
    ;

COMMENT
    :   '/*' .*? '*/' -> skip
    ;

LINE_COMMENT
    :   '#' ~[\r\n]* -> skip
    ;

//--IDENTIFIER--
ID: (LETTER | UNDERSCORE) (LETTER | UNDERSCORE | DIGIT)*;
fragment LETTER: [a-zA-Z];
fragment UNDERSCORE: [_];
fragment DIGIT: [0-9];


//--LITERAL--
INTEGER_LITERAL: DIGIT+;
FLOAT_LITERAL: DIGIT+ '.' DIGIT*
            | DIGIT+ [eE] [+-]? DIGIT+
            | DIGIT+ '.' DIGIT* [eE] [+-]? DIGIT+
            ;
STRING_LITERAL: '"' STR_CHAR* '"';

ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL;

UNCLOSE_STRING: '"' STR_CHAR* ([\r\n] | EOF)
                    {
                        y = str(self.text)
                        if y[-1] in ['\r', '\n']:
                            self.text = y[:-1]
                        else:
                            self.text = y
                    }
                    ;

// --Character Set--
fragment STR_CHAR: ~["\\\r\n] | ESC_SEQ;
// Note: ~["\\\r\n]: là xuống hàng
fragment ESC_SEQ: '\\' [btnfr"\\];
// Note: '\\' [btnfr"\\] : là các kí tự viết ra
fragment ESC_ILLEGAL: '\\' ~[btnfr"\\];


ERROR_CHAR: .;

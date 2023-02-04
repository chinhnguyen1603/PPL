# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3;")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\7\2\2\3\5\3\3\2\2\2\2")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'auto'", "'false'", "'integer'", 
                     "'void'", "'array'", "'break'", "'float'", "'return'", 
                     "'out'", "'boolean'", "'for'", "'string'", "'continue'", 
                     "'do'", "'function'", "'true'", "'of'", "'else'", "'if'", 
                     "'while'", "'inherit'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", 
                     "'<='", "'>'", "'>='", "'::'", "'('", "')'", "'['", 
                     "']'", "'.'", "','", "';'", "':'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>", "COMMENT_C", "COMMENT_CPLUS", "INTLIT", 
                      "FLOATLIT", "BOOLLIT", "AUTO", "FALSE", "INTERGER", 
                      "VOID", "ARRAY", "BREAK", "FLOAT", "RETURN", "OUT", 
                      "BOOLEAN", "FOR", "STRING", "CONTINUE", "DO", "FUNCTION", 
                      "TRUE", "OF", "ELSE", "IF", "WHILE", "INHERIT", "ADDOP", 
                      "SUBOP", "MULOP", "DIV", "MOD", "NOT", "AND", "OR", 
                      "EQUAL", "NOT_EQUAL", "LESS", "LESS_OR_EQUAL", "GREATER", 
                      "GREATER_OR_EQUAL", "DOUBLE_COLON", "LB", "RB", "LSB", 
                      "RSB", "DOT", "COMMA", "SEMICOLON", "COLON", "LP", 
                      "RP", "ASSIGN", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    COMMENT_C=1
    COMMENT_CPLUS=2
    INTLIT=3
    FLOATLIT=4
    BOOLLIT=5
    AUTO=6
    FALSE=7
    INTERGER=8
    VOID=9
    ARRAY=10
    BREAK=11
    FLOAT=12
    RETURN=13
    OUT=14
    BOOLEAN=15
    FOR=16
    STRING=17
    CONTINUE=18
    DO=19
    FUNCTION=20
    TRUE=21
    OF=22
    ELSE=23
    IF=24
    WHILE=25
    INHERIT=26
    ADDOP=27
    SUBOP=28
    MULOP=29
    DIV=30
    MOD=31
    NOT=32
    AND=33
    OR=34
    EQUAL=35
    NOT_EQUAL=36
    LESS=37
    LESS_OR_EQUAL=38
    GREATER=39
    GREATER_OR_EQUAL=40
    DOUBLE_COLON=41
    LB=42
    RB=43
    LSB=44
    RSB=45
    DOT=46
    COMMA=47
    SEMICOLON=48
    COLON=49
    LP=50
    RP=51
    ASSIGN=52
    ID=53
    WS=54
    ERROR_CHAR=55
    UNCLOSE_STRING=56
    ILLEGAL_ESCAPE=57

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






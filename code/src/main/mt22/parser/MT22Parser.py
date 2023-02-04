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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3<")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\7\2\2\3\5\3\3\2\2\2\2")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'auto'", "'false'", 
                     "'integer'", "'void'", "'array'", "'break'", "'float'", 
                     "'return'", "'out'", "'boolean'", "'for'", "'string'", 
                     "'continue'", "'do'", "'function'", "'true'", "'of'", 
                     "'else'", "'if'", "'while'", "'inherit'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", "'('", 
                     "')'", "'['", "']'", "'.'", "','", "';'", "':'", "'{'", 
                     "'}'", "'='" ]

    symbolicNames = [ "<INVALID>", "COMMENT_C", "COMMENT_CPLUS", "INTLIT", 
                      "FLOATLIT", "BOOLLIT", "STRING_LIT", "AUTO", "FALSE", 
                      "INTERGER", "VOID", "ARRAY", "BREAK", "FLOAT", "RETURN", 
                      "OUT", "BOOLEAN", "FOR", "STRING", "CONTINUE", "DO", 
                      "FUNCTION", "TRUE", "OF", "ELSE", "IF", "WHILE", "INHERIT", 
                      "ADDOP", "SUBOP", "MULOP", "DIV", "MOD", "NOT", "AND", 
                      "OR", "EQUAL", "NOT_EQUAL", "LESS", "LESS_OR_EQUAL", 
                      "GREATER", "GREATER_OR_EQUAL", "DOUBLE_COLON", "LB", 
                      "RB", "LSB", "RSB", "DOT", "COMMA", "SEMICOLON", "COLON", 
                      "LP", "RP", "ASSIGN", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    COMMENT_C=1
    COMMENT_CPLUS=2
    INTLIT=3
    FLOATLIT=4
    BOOLLIT=5
    STRING_LIT=6
    AUTO=7
    FALSE=8
    INTERGER=9
    VOID=10
    ARRAY=11
    BREAK=12
    FLOAT=13
    RETURN=14
    OUT=15
    BOOLEAN=16
    FOR=17
    STRING=18
    CONTINUE=19
    DO=20
    FUNCTION=21
    TRUE=22
    OF=23
    ELSE=24
    IF=25
    WHILE=26
    INHERIT=27
    ADDOP=28
    SUBOP=29
    MULOP=30
    DIV=31
    MOD=32
    NOT=33
    AND=34
    OR=35
    EQUAL=36
    NOT_EQUAL=37
    LESS=38
    LESS_OR_EQUAL=39
    GREATER=40
    GREATER_OR_EQUAL=41
    DOUBLE_COLON=42
    LB=43
    RB=44
    LSB=45
    RSB=46
    DOT=47
    COMMA=48
    SEMICOLON=49
    COLON=50
    LP=51
    RP=52
    ASSIGN=53
    ID=54
    WS=55
    ERROR_CHAR=56
    UNCLOSE_STRING=57
    ILLEGAL_ESCAPE=58

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






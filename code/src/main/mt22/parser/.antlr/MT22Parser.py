# Generated from e:\PPL\PPL\code\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3:")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\7\2\2\3\5\3\3\2\2\2\2")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'auto'", "'false'", "'integer'", "'void'", 
                     "'array'", "'break'", "'float'", "'return'", "'out'", 
                     "'boolean'", "'for'", "'string'", "'continue'", "'do'", 
                     "'function'", "'true'", "'of'", "'else'", "'if'", "'while'", 
                     "'inherit'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", 
                     "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", 
                     "'>='", "'::'", "'('", "')'", "'['", "']'", "'.'", 
                     "','", "';'", "':'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>", "COMMENT_C", "COMMENT_CPLUS", "INTLIT", 
                      "BOOLLIT", "AUTO", "FALSE", "INTERGER", "VOID", "ARRAY", 
                      "BREAK", "FLOAT", "RETURN", "OUT", "BOOLEAN", "FOR", 
                      "STRING", "CONTINUE", "DO", "FUNCTION", "TRUE", "OF", 
                      "ELSE", "IF", "WHILE", "INHERIT", "ADDOP", "SUBOP", 
                      "MULOP", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", 
                      "NOT_EQUAL", "LESS", "LESS_OR_EQUAL", "GREATER", "GREATER_OR_EQUAL", 
                      "DOUBLE_COLON", "LB", "RB", "LSB", "RSB", "DOT", "COMMA", 
                      "SEMICOLON", "COLON", "LP", "RP", "ASSIGN", "ID", 
                      "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    COMMENT_C=1
    COMMENT_CPLUS=2
    INTLIT=3
    BOOLLIT=4
    AUTO=5
    FALSE=6
    INTERGER=7
    VOID=8
    ARRAY=9
    BREAK=10
    FLOAT=11
    RETURN=12
    OUT=13
    BOOLEAN=14
    FOR=15
    STRING=16
    CONTINUE=17
    DO=18
    FUNCTION=19
    TRUE=20
    OF=21
    ELSE=22
    IF=23
    WHILE=24
    INHERIT=25
    ADDOP=26
    SUBOP=27
    MULOP=28
    DIV=29
    MOD=30
    NOT=31
    AND=32
    OR=33
    EQUAL=34
    NOT_EQUAL=35
    LESS=36
    LESS_OR_EQUAL=37
    GREATER=38
    GREATER_OR_EQUAL=39
    DOUBLE_COLON=40
    LB=41
    RB=42
    LSB=43
    RSB=44
    DOT=45
    COMMA=46
    SEMICOLON=47
    COLON=48
    LP=49
    RP=50
    ASSIGN=51
    ID=52
    WS=53
    ERROR_CHAR=54
    UNCLOSE_STRING=55
    ILLEGAL_ESCAPE=56

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






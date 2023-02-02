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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\38")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\7\2\2\3\5\3\3\2\2\2\2")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'auto'", "'false'", "'integer'", "'void'", "'array'", 
                     "'break'", "'float'", "'return'", "'out'", "'boolean'", 
                     "'for'", "'string'", "'continue'", "'do'", "'function'", 
                     "'true'", "'of'", "'else'", "'if'", "'while'", "'inherit'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
                     "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", 
                     "'('", "')'", "'['", "']'", "'.'", "','", "';'", "':'", 
                     "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>", "COMMENT_C", "COMMENT_CPLUS", "ID", "AUTO", 
                      "FALSE", "INTERGER", "VOID", "ARRAY", "BREAK", "FLOAT", 
                      "RETURN", "OUT", "BOOLEAN", "FOR", "STRING", "CONTINUE", 
                      "DO", "FUNCTION", "TRUE", "OF", "ELSE", "IF", "WHILE", 
                      "INHERIT", "ADDOP", "SUBOP", "MULOP", "DIV", "MOD", 
                      "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", "LESS", 
                      "LESS_OR_EQUAL", "GREATER", "GREATER_OR_EQUAL", "DOUBLE_COLON", 
                      "LB", "RB", "LSB", "RSB", "DOT", "COMMA", "SEMICOLON", 
                      "COLON", "LP", "RP", "ASSIGN", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    COMMENT_C=1
    COMMENT_CPLUS=2
    ID=3
    AUTO=4
    FALSE=5
    INTERGER=6
    VOID=7
    ARRAY=8
    BREAK=9
    FLOAT=10
    RETURN=11
    OUT=12
    BOOLEAN=13
    FOR=14
    STRING=15
    CONTINUE=16
    DO=17
    FUNCTION=18
    TRUE=19
    OF=20
    ELSE=21
    IF=22
    WHILE=23
    INHERIT=24
    ADDOP=25
    SUBOP=26
    MULOP=27
    DIV=28
    MOD=29
    NOT=30
    AND=31
    OR=32
    EQUAL=33
    NOT_EQUAL=34
    LESS=35
    LESS_OR_EQUAL=36
    GREATER=37
    GREATER_OR_EQUAL=38
    DOUBLE_COLON=39
    LB=40
    RB=41
    LSB=42
    RSB=43
    DOT=44
    COMMA=45
    SEMICOLON=46
    COLON=47
    LP=48
    RP=49
    ASSIGN=50
    WS=51
    ERROR_CHAR=52
    UNCLOSE_STRING=53
    ILLEGAL_ESCAPE=54

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






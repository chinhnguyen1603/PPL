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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\66")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\7\2\2\3\5\3\3\2\2\2\2")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'auto'", "'false'", "'integer'", "'while'", "'of'", 
                     "'break'", "'float'", "'return'", "'void'", "'inherit'", 
                     "'boolean'", "'for'", "'string'", "'function'", "'do'", 
                     "'true'", "'out'", "'else'", "'if'", "'continue'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
                     "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", 
                     "'('", "')'", "'['", "']'", "'.'", "','", "';'", "':'", 
                     "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "COMMENT_C", "COMMENT_CPLUS", "ID", "AUTO", 
                      "FALSE", "INT", "WHILE", "OF", "BREAK", "FLOAT", "RETURN", 
                      "VOID", "INHERIT", "BOOLEAN", "FOR", "STRING", "FUNCTION", 
                      "DO", "TRUE", "OUT", "ELSE", "IF", "CONTINUE", "ADDOP", 
                      "SUBOP", "MULOP", "DIV", "MOD", "NOT", "AND", "OR", 
                      "EQUAL", "NOT_EQUAL", "LESS", "LESS_OR_EQUAL", "GREATER", 
                      "GREATER_OR_EQUAL", "DOUBLE_COLON", "LB", "RB", "LSB", 
                      "RSB", "DOT", "COMMA", "SEMICOLON", "COLON", "LP", 
                      "RP", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    COMMENT_C=1
    COMMENT_CPLUS=2
    ID=3
    AUTO=4
    FALSE=5
    INT=6
    WHILE=7
    OF=8
    BREAK=9
    FLOAT=10
    RETURN=11
    VOID=12
    INHERIT=13
    BOOLEAN=14
    FOR=15
    STRING=16
    FUNCTION=17
    DO=18
    TRUE=19
    OUT=20
    ELSE=21
    IF=22
    CONTINUE=23
    ADDOP=24
    SUBOP=25
    MULOP=26
    DIV=27
    MOD=28
    NOT=29
    AND=30
    OR=31
    EQUAL=32
    NOT_EQUAL=33
    LESS=34
    LESS_OR_EQUAL=35
    GREATER=36
    GREATER_OR_EQUAL=37
    DOUBLE_COLON=38
    LB=39
    RB=40
    LSB=41
    RSB=42
    DOT=43
    COMMA=44
    SEMICOLON=45
    COLON=46
    LP=47
    RP=48
    WS=49
    ERROR_CHAR=50
    UNCLOSE_STRING=51
    ILLEGAL_ESCAPE=52

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






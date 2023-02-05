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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3=")
        buf.write("\66\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\7\2\f\n\2\f\2")
        buf.write("\16\2\17\13\2\3\2\7\2\22\n\2\f\2\16\2\25\13\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3 \n\3\f\3\16\3#\13\3\7")
        buf.write("\3%\n\3\f\3\16\3(\13\3\3\3\3\3\3\4\3\4\3\4\7\4/\n\4\f")
        buf.write("\4\16\4\62\13\4\3\5\3\5\3\5\2\2\6\2\4\6\b\2\2\2\66\2\r")
        buf.write("\3\2\2\2\4\30\3\2\2\2\6+\3\2\2\2\b\63\3\2\2\2\n\f\5\4")
        buf.write("\3\2\13\n\3\2\2\2\f\17\3\2\2\2\r\13\3\2\2\2\r\16\3\2\2")
        buf.write("\2\16\23\3\2\2\2\17\r\3\2\2\2\20\22\5\b\5\2\21\20\3\2")
        buf.write("\2\2\22\25\3\2\2\2\23\21\3\2\2\2\23\24\3\2\2\2\24\26\3")
        buf.write("\2\2\2\25\23\3\2\2\2\26\27\7\2\2\3\27\3\3\2\2\2\30\31")
        buf.write("\5\6\4\2\31\32\7\65\2\2\32&\7\f\2\2\33\34\78\2\2\34!\7")
        buf.write("\6\2\2\35\36\7\63\2\2\36 \7\6\2\2\37\35\3\2\2\2 #\3\2")
        buf.write("\2\2!\37\3\2\2\2!\"\3\2\2\2\"%\3\2\2\2#!\3\2\2\2$\33\3")
        buf.write("\2\2\2%(\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\')\3\2\2\2(&\3\2")
        buf.write("\2\2)*\7\64\2\2*\5\3\2\2\2+\60\79\2\2,-\7\63\2\2-/\79")
        buf.write("\2\2.,\3\2\2\2/\62\3\2\2\2\60.\3\2\2\2\60\61\3\2\2\2\61")
        buf.write("\7\3\2\2\2\62\60\3\2\2\2\63\64\7\3\2\2\64\t\3\2\2\2\7")
        buf.write("\r\23!&\60")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'func_decl'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'auto'", "'false'", "'integer'", "'void'", "'array'", 
                     "'break'", "'float'", "'return'", "'out'", "'boolean'", 
                     "'for'", "'string'", "'continue'", "'do'", "'function'", 
                     "'true'", "'of'", "'else'", "'if'", "'while'", "'inherit'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
                     "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", 
                     "'('", "')'", "'['", "']'", "'.'", "','", "';'", "':'", 
                     "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "COMMENT_C", "COMMENT_CPLUS", 
                      "INTLIT", "FLOATLIT", "BOOLLIT", "STRING_LIT", "AUTO", 
                      "FALSE", "INTERGER", "VOID", "ARRAY", "BREAK", "FLOAT", 
                      "RETURN", "OUT", "BOOLEAN", "FOR", "STRING", "CONTINUE", 
                      "DO", "FUNCTION", "TRUE", "OF", "ELSE", "IF", "WHILE", 
                      "INHERIT", "ADDOP", "SUBOP", "MULOP", "DIV", "MOD", 
                      "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", "LESS", 
                      "LESS_OR_EQUAL", "GREATER", "GREATER_OR_EQUAL", "DOUBLE_COLON", 
                      "LB", "RB", "LSB", "RSB", "DOT", "COMMA", "SEMICOLON", 
                      "COLON", "LP", "RP", "ASSIGN", "ID", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_var_decl = 1
    RULE_id_list = 2
    RULE_func_decl = 3

    ruleNames =  [ "program", "var_decl", "id_list", "func_decl" ]

    EOF = Token.EOF
    T__0=1
    COMMENT_C=2
    COMMENT_CPLUS=3
    INTLIT=4
    FLOATLIT=5
    BOOLLIT=6
    STRING_LIT=7
    AUTO=8
    FALSE=9
    INTERGER=10
    VOID=11
    ARRAY=12
    BREAK=13
    FLOAT=14
    RETURN=15
    OUT=16
    BOOLEAN=17
    FOR=18
    STRING=19
    CONTINUE=20
    DO=21
    FUNCTION=22
    TRUE=23
    OF=24
    ELSE=25
    IF=26
    WHILE=27
    INHERIT=28
    ADDOP=29
    SUBOP=30
    MULOP=31
    DIV=32
    MOD=33
    NOT=34
    AND=35
    OR=36
    EQUAL=37
    NOT_EQUAL=38
    LESS=39
    LESS_OR_EQUAL=40
    GREATER=41
    GREATER_OR_EQUAL=42
    DOUBLE_COLON=43
    LB=44
    RB=45
    LSB=46
    RSB=47
    DOT=48
    COMMA=49
    SEMICOLON=50
    COLON=51
    LP=52
    RP=53
    ASSIGN=54
    ID=55
    WS=56
    ERROR_CHAR=57
    UNCLOSE_STRING=58
    ILLEGAL_ESCAPE=59

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

        def var_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Var_declContext)
            else:
                return self.getTypedRuleContext(MT22Parser.Var_declContext,i)


        def func_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Func_declContext)
            else:
                return self.getTypedRuleContext(MT22Parser.Func_declContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.ID:
                self.state = 8
                self.var_decl()
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.T__0:
                self.state = 14
                self.func_decl()
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 20
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_list(self):
            return self.getTypedRuleContext(MT22Parser.Id_listContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def INTERGER(self):
            return self.getToken(MT22Parser.INTERGER, 0)

        def SEMICOLON(self):
            return self.getToken(MT22Parser.SEMICOLON, 0)

        def ASSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.ASSIGN)
            else:
                return self.getToken(MT22Parser.ASSIGN, i)

        def INTLIT(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.INTLIT)
            else:
                return self.getToken(MT22Parser.INTLIT, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = MT22Parser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.id_list()
            self.state = 23
            self.match(MT22Parser.COLON)
            self.state = 24
            self.match(MT22Parser.INTERGER)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.ASSIGN:
                self.state = 25
                self.match(MT22Parser.ASSIGN)
                self.state = 26
                self.match(MT22Parser.INTLIT)
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MT22Parser.COMMA:
                    self.state = 27
                    self.match(MT22Parser.COMMA)
                    self.state = 28
                    self.match(MT22Parser.INTLIT)
                    self.state = 33
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 39
            self.match(MT22Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.ID)
            else:
                return self.getToken(MT22Parser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_id_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_list" ):
                return visitor.visitId_list(self)
            else:
                return visitor.visitChildren(self)




    def id_list(self):

        localctx = MT22Parser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_id_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(MT22Parser.ID)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.COMMA:
                self.state = 42
                self.match(MT22Parser.COMMA)
                self.state = 43
                self.match(MT22Parser.ID)
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MT22Parser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = MT22Parser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(MT22Parser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






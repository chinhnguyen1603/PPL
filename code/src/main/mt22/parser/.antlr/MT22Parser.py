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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3<")
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
        buf.write("\5\6\4\2\31\32\7\64\2\2\32&\7\13\2\2\33\34\7\67\2\2\34")
        buf.write("!\7\5\2\2\35\36\7\62\2\2\36 \7\5\2\2\37\35\3\2\2\2 #\3")
        buf.write("\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"%\3\2\2\2#!\3\2\2\2$\33")
        buf.write("\3\2\2\2%(\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\')\3\2\2\2(&\3")
        buf.write("\2\2\2)*\7\63\2\2*\5\3\2\2\2+\60\78\2\2,-\7\62\2\2-/\7")
        buf.write("8\2\2.,\3\2\2\2/\62\3\2\2\2\60.\3\2\2\2\60\61\3\2\2\2")
        buf.write("\61\7\3\2\2\2\62\60\3\2\2\2\63\64\7\27\2\2\64\t\3\2\2")
        buf.write("\2\7\r\23!&\60")
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
    RULE_var_decl = 1
    RULE_id_list = 2
    RULE_func_decl = 3

    ruleNames =  [ "program", "var_decl", "id_list", "func_decl" ]

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
            while _la==MT22Parser.FUNCTION:
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

        def FUNCTION(self):
            return self.getToken(MT22Parser.FUNCTION, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_func_decl




    def func_decl(self):

        localctx = MT22Parser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(MT22Parser.FUNCTION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\66")
        buf.write("\u015a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\3\2\3\2")
        buf.write("\3\2\7\2v\n\2\f\2\16\2y\13\2\3\2\3\2\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\7\3\u0084\n\3\f\3\16\3\u0087\13\3\3\3\3\3\3")
        buf.write("\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\5\7\u0093\n\7\3\7\3\7\3")
        buf.write("\7\7\7\u0098\n\7\f\7\16\7\u009b\13\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3")
        buf.write("\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3\'\3")
        buf.write("(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65")
        buf.write("\6\65\u014c\n\65\r\65\16\65\u014d\3\65\3\65\3\66\3\66")
        buf.write("\3\66\3\67\3\67\3\67\38\38\38\3w\29\3\3\5\4\7\2\t\2\13")
        buf.write("\2\r\5\17\6\21\7\23\b\25\t\27\n\31\13\33\f\35\r\37\16")
        buf.write("!\17#\20%\21\'\22)\23+\24-\25/\26\61\27\63\30\65\31\67")
        buf.write("\329\33;\34=\35?\36A\37C E!G\"I#K$M%O&Q\'S(U)W*Y+[,]-")
        buf.write("_.a/c\60e\61g\62i\63k\64m\65o\66\3\2\6\4\2\f\f\17\17\4")
        buf.write("\2C\\c|\3\2\62;\5\2\n\f\16\17\"\"\2\u015d\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23")
        buf.write("\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3")
        buf.write("\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2")
        buf.write("\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2")
        buf.write("\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2")
        buf.write("\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2")
        buf.write("\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2")
        buf.write("\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3")
        buf.write("\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]")
        buf.write("\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2")
        buf.write("g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2")
        buf.write("\3q\3\2\2\2\5\177\3\2\2\2\7\u008a\3\2\2\2\t\u008c\3\2")
        buf.write("\2\2\13\u008e\3\2\2\2\r\u0092\3\2\2\2\17\u009c\3\2\2\2")
        buf.write("\21\u00a1\3\2\2\2\23\u00a7\3\2\2\2\25\u00af\3\2\2\2\27")
        buf.write("\u00b5\3\2\2\2\31\u00b8\3\2\2\2\33\u00be\3\2\2\2\35\u00c4")
        buf.write("\3\2\2\2\37\u00cb\3\2\2\2!\u00d0\3\2\2\2#\u00d8\3\2\2")
        buf.write("\2%\u00e0\3\2\2\2\'\u00e4\3\2\2\2)\u00eb\3\2\2\2+\u00f4")
        buf.write("\3\2\2\2-\u00f7\3\2\2\2/\u00fc\3\2\2\2\61\u0100\3\2\2")
        buf.write("\2\63\u0105\3\2\2\2\65\u0108\3\2\2\2\67\u0111\3\2\2\2")
        buf.write("9\u0113\3\2\2\2;\u0115\3\2\2\2=\u0117\3\2\2\2?\u0119\3")
        buf.write("\2\2\2A\u011b\3\2\2\2C\u011d\3\2\2\2E\u0120\3\2\2\2G\u0123")
        buf.write("\3\2\2\2I\u0126\3\2\2\2K\u0129\3\2\2\2M\u012b\3\2\2\2")
        buf.write("O\u012e\3\2\2\2Q\u0130\3\2\2\2S\u0133\3\2\2\2U\u0136\3")
        buf.write("\2\2\2W\u0138\3\2\2\2Y\u013a\3\2\2\2[\u013c\3\2\2\2]\u013e")
        buf.write("\3\2\2\2_\u0140\3\2\2\2a\u0142\3\2\2\2c\u0144\3\2\2\2")
        buf.write("e\u0146\3\2\2\2g\u0148\3\2\2\2i\u014b\3\2\2\2k\u0151\3")
        buf.write("\2\2\2m\u0154\3\2\2\2o\u0157\3\2\2\2qr\7\61\2\2rs\7,\2")
        buf.write("\2sw\3\2\2\2tv\13\2\2\2ut\3\2\2\2vy\3\2\2\2wx\3\2\2\2")
        buf.write("wu\3\2\2\2xz\3\2\2\2yw\3\2\2\2z{\7,\2\2{|\7\61\2\2|}\3")
        buf.write("\2\2\2}~\b\2\2\2~\4\3\2\2\2\177\u0080\7\61\2\2\u0080\u0081")
        buf.write("\7\61\2\2\u0081\u0085\3\2\2\2\u0082\u0084\n\2\2\2\u0083")
        buf.write("\u0082\3\2\2\2\u0084\u0087\3\2\2\2\u0085\u0083\3\2\2\2")
        buf.write("\u0085\u0086\3\2\2\2\u0086\u0088\3\2\2\2\u0087\u0085\3")
        buf.write("\2\2\2\u0088\u0089\b\3\2\2\u0089\6\3\2\2\2\u008a\u008b")
        buf.write("\t\3\2\2\u008b\b\3\2\2\2\u008c\u008d\7a\2\2\u008d\n\3")
        buf.write("\2\2\2\u008e\u008f\t\4\2\2\u008f\f\3\2\2\2\u0090\u0093")
        buf.write("\5\t\5\2\u0091\u0093\5\7\4\2\u0092\u0090\3\2\2\2\u0092")
        buf.write("\u0091\3\2\2\2\u0093\u0099\3\2\2\2\u0094\u0098\5\t\5\2")
        buf.write("\u0095\u0098\5\7\4\2\u0096\u0098\5\13\6\2\u0097\u0094")
        buf.write("\3\2\2\2\u0097\u0095\3\2\2\2\u0097\u0096\3\2\2\2\u0098")
        buf.write("\u009b\3\2\2\2\u0099\u0097\3\2\2\2\u0099\u009a\3\2\2\2")
        buf.write("\u009a\16\3\2\2\2\u009b\u0099\3\2\2\2\u009c\u009d\7c\2")
        buf.write("\2\u009d\u009e\7w\2\2\u009e\u009f\7v\2\2\u009f\u00a0\7")
        buf.write("q\2\2\u00a0\20\3\2\2\2\u00a1\u00a2\7h\2\2\u00a2\u00a3")
        buf.write("\7c\2\2\u00a3\u00a4\7n\2\2\u00a4\u00a5\7u\2\2\u00a5\u00a6")
        buf.write("\7g\2\2\u00a6\22\3\2\2\2\u00a7\u00a8\7k\2\2\u00a8\u00a9")
        buf.write("\7p\2\2\u00a9\u00aa\7v\2\2\u00aa\u00ab\7g\2\2\u00ab\u00ac")
        buf.write("\7i\2\2\u00ac\u00ad\7g\2\2\u00ad\u00ae\7t\2\2\u00ae\24")
        buf.write("\3\2\2\2\u00af\u00b0\7y\2\2\u00b0\u00b1\7j\2\2\u00b1\u00b2")
        buf.write("\7k\2\2\u00b2\u00b3\7n\2\2\u00b3\u00b4\7g\2\2\u00b4\26")
        buf.write("\3\2\2\2\u00b5\u00b6\7q\2\2\u00b6\u00b7\7h\2\2\u00b7\30")
        buf.write("\3\2\2\2\u00b8\u00b9\7d\2\2\u00b9\u00ba\7t\2\2\u00ba\u00bb")
        buf.write("\7g\2\2\u00bb\u00bc\7c\2\2\u00bc\u00bd\7m\2\2\u00bd\32")
        buf.write("\3\2\2\2\u00be\u00bf\7h\2\2\u00bf\u00c0\7n\2\2\u00c0\u00c1")
        buf.write("\7q\2\2\u00c1\u00c2\7c\2\2\u00c2\u00c3\7v\2\2\u00c3\34")
        buf.write("\3\2\2\2\u00c4\u00c5\7t\2\2\u00c5\u00c6\7g\2\2\u00c6\u00c7")
        buf.write("\7v\2\2\u00c7\u00c8\7w\2\2\u00c8\u00c9\7t\2\2\u00c9\u00ca")
        buf.write("\7p\2\2\u00ca\36\3\2\2\2\u00cb\u00cc\7x\2\2\u00cc\u00cd")
        buf.write("\7q\2\2\u00cd\u00ce\7k\2\2\u00ce\u00cf\7f\2\2\u00cf \3")
        buf.write("\2\2\2\u00d0\u00d1\7k\2\2\u00d1\u00d2\7p\2\2\u00d2\u00d3")
        buf.write("\7j\2\2\u00d3\u00d4\7g\2\2\u00d4\u00d5\7t\2\2\u00d5\u00d6")
        buf.write("\7k\2\2\u00d6\u00d7\7v\2\2\u00d7\"\3\2\2\2\u00d8\u00d9")
        buf.write("\7d\2\2\u00d9\u00da\7q\2\2\u00da\u00db\7q\2\2\u00db\u00dc")
        buf.write("\7n\2\2\u00dc\u00dd\7g\2\2\u00dd\u00de\7c\2\2\u00de\u00df")
        buf.write("\7p\2\2\u00df$\3\2\2\2\u00e0\u00e1\7h\2\2\u00e1\u00e2")
        buf.write("\7q\2\2\u00e2\u00e3\7t\2\2\u00e3&\3\2\2\2\u00e4\u00e5")
        buf.write("\7u\2\2\u00e5\u00e6\7v\2\2\u00e6\u00e7\7t\2\2\u00e7\u00e8")
        buf.write("\7k\2\2\u00e8\u00e9\7p\2\2\u00e9\u00ea\7i\2\2\u00ea(\3")
        buf.write("\2\2\2\u00eb\u00ec\7h\2\2\u00ec\u00ed\7w\2\2\u00ed\u00ee")
        buf.write("\7p\2\2\u00ee\u00ef\7e\2\2\u00ef\u00f0\7v\2\2\u00f0\u00f1")
        buf.write("\7k\2\2\u00f1\u00f2\7q\2\2\u00f2\u00f3\7p\2\2\u00f3*\3")
        buf.write("\2\2\2\u00f4\u00f5\7f\2\2\u00f5\u00f6\7q\2\2\u00f6,\3")
        buf.write("\2\2\2\u00f7\u00f8\7v\2\2\u00f8\u00f9\7t\2\2\u00f9\u00fa")
        buf.write("\7w\2\2\u00fa\u00fb\7g\2\2\u00fb.\3\2\2\2\u00fc\u00fd")
        buf.write("\7q\2\2\u00fd\u00fe\7w\2\2\u00fe\u00ff\7v\2\2\u00ff\60")
        buf.write("\3\2\2\2\u0100\u0101\7g\2\2\u0101\u0102\7n\2\2\u0102\u0103")
        buf.write("\7u\2\2\u0103\u0104\7g\2\2\u0104\62\3\2\2\2\u0105\u0106")
        buf.write("\7k\2\2\u0106\u0107\7h\2\2\u0107\64\3\2\2\2\u0108\u0109")
        buf.write("\7e\2\2\u0109\u010a\7q\2\2\u010a\u010b\7p\2\2\u010b\u010c")
        buf.write("\7v\2\2\u010c\u010d\7k\2\2\u010d\u010e\7p\2\2\u010e\u010f")
        buf.write("\7w\2\2\u010f\u0110\7g\2\2\u0110\66\3\2\2\2\u0111\u0112")
        buf.write("\7-\2\2\u01128\3\2\2\2\u0113\u0114\7/\2\2\u0114:\3\2\2")
        buf.write("\2\u0115\u0116\7,\2\2\u0116<\3\2\2\2\u0117\u0118\7\61")
        buf.write("\2\2\u0118>\3\2\2\2\u0119\u011a\7\'\2\2\u011a@\3\2\2\2")
        buf.write("\u011b\u011c\7#\2\2\u011cB\3\2\2\2\u011d\u011e\7(\2\2")
        buf.write("\u011e\u011f\7(\2\2\u011fD\3\2\2\2\u0120\u0121\7~\2\2")
        buf.write("\u0121\u0122\7~\2\2\u0122F\3\2\2\2\u0123\u0124\7?\2\2")
        buf.write("\u0124\u0125\7?\2\2\u0125H\3\2\2\2\u0126\u0127\7#\2\2")
        buf.write("\u0127\u0128\7?\2\2\u0128J\3\2\2\2\u0129\u012a\7>\2\2")
        buf.write("\u012aL\3\2\2\2\u012b\u012c\7>\2\2\u012c\u012d\7?\2\2")
        buf.write("\u012dN\3\2\2\2\u012e\u012f\7@\2\2\u012fP\3\2\2\2\u0130")
        buf.write("\u0131\7@\2\2\u0131\u0132\7?\2\2\u0132R\3\2\2\2\u0133")
        buf.write("\u0134\7<\2\2\u0134\u0135\7<\2\2\u0135T\3\2\2\2\u0136")
        buf.write("\u0137\7*\2\2\u0137V\3\2\2\2\u0138\u0139\7+\2\2\u0139")
        buf.write("X\3\2\2\2\u013a\u013b\7]\2\2\u013bZ\3\2\2\2\u013c\u013d")
        buf.write("\7_\2\2\u013d\\\3\2\2\2\u013e\u013f\7\60\2\2\u013f^\3")
        buf.write("\2\2\2\u0140\u0141\7.\2\2\u0141`\3\2\2\2\u0142\u0143\7")
        buf.write("=\2\2\u0143b\3\2\2\2\u0144\u0145\7<\2\2\u0145d\3\2\2\2")
        buf.write("\u0146\u0147\7}\2\2\u0147f\3\2\2\2\u0148\u0149\7\177\2")
        buf.write("\2\u0149h\3\2\2\2\u014a\u014c\t\5\2\2\u014b\u014a\3\2")
        buf.write("\2\2\u014c\u014d\3\2\2\2\u014d\u014b\3\2\2\2\u014d\u014e")
        buf.write("\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u0150\b\65\2\2\u0150")
        buf.write("j\3\2\2\2\u0151\u0152\13\2\2\2\u0152\u0153\b\66\3\2\u0153")
        buf.write("l\3\2\2\2\u0154\u0155\13\2\2\2\u0155\u0156\b\67\4\2\u0156")
        buf.write("n\3\2\2\2\u0157\u0158\13\2\2\2\u0158\u0159\b8\5\2\u0159")
        buf.write("p\3\2\2\2\t\2w\u0085\u0092\u0097\u0099\u014d\6\b\2\2\3")
        buf.write("\66\2\3\67\3\38\4")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT_C = 1
    COMMENT_CPLUS = 2
    ID = 3
    AUTO = 4
    FALSE = 5
    INT = 6
    WHILE = 7
    OF = 8
    BREAK = 9
    FLOAT = 10
    RETURN = 11
    VOID = 12
    INHERIT = 13
    BOOLEAN = 14
    FOR = 15
    STRING = 16
    FUNCTION = 17
    DO = 18
    TRUE = 19
    OUT = 20
    ELSE = 21
    IF = 22
    CONTINUE = 23
    ADDOP = 24
    SUBOP = 25
    MULOP = 26
    DIV = 27
    MOD = 28
    NOT = 29
    AND = 30
    OR = 31
    EQUAL = 32
    NOT_EQUAL = 33
    LESS = 34
    LESS_OR_EQUAL = 35
    GREATER = 36
    GREATER_OR_EQUAL = 37
    DOUBLE_COLON = 38
    LB = 39
    RB = 40
    LSB = 41
    RSB = 42
    DOT = 43
    COMMA = 44
    SEMICOLON = 45
    COLON = 46
    LP = 47
    RP = 48
    WS = 49
    ERROR_CHAR = 50
    UNCLOSE_STRING = 51
    ILLEGAL_ESCAPE = 52

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'false'", "'integer'", "'while'", "'of'", "'break'", 
            "'float'", "'return'", "'void'", "'inherit'", "'boolean'", "'for'", 
            "'string'", "'function'", "'do'", "'true'", "'out'", "'else'", 
            "'if'", "'continue'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", 
            "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'::'", "'('", "')'", "'['", "']'", "'.'", "','", "';'", "':'", 
            "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT_C", "COMMENT_CPLUS", "ID", "AUTO", "FALSE", "INT", 
            "WHILE", "OF", "BREAK", "FLOAT", "RETURN", "VOID", "INHERIT", 
            "BOOLEAN", "FOR", "STRING", "FUNCTION", "DO", "TRUE", "OUT", 
            "ELSE", "IF", "CONTINUE", "ADDOP", "SUBOP", "MULOP", "DIV", 
            "MOD", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", "LESS", "LESS_OR_EQUAL", 
            "GREATER", "GREATER_OR_EQUAL", "DOUBLE_COLON", "LB", "RB", "LSB", 
            "RSB", "DOT", "COMMA", "SEMICOLON", "COLON", "LP", "RP", "WS", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "COMMENT_C", "COMMENT_CPLUS", "LETTER", "UNDERSCORE", 
                  "DIGIT", "ID", "AUTO", "FALSE", "INT", "WHILE", "OF", 
                  "BREAK", "FLOAT", "RETURN", "VOID", "INHERIT", "BOOLEAN", 
                  "FOR", "STRING", "FUNCTION", "DO", "TRUE", "OUT", "ELSE", 
                  "IF", "CONTINUE", "ADDOP", "SUBOP", "MULOP", "DIV", "MOD", 
                  "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", "LESS", "LESS_OR_EQUAL", 
                  "GREATER", "GREATER_OR_EQUAL", "DOUBLE_COLON", "LB", "RB", 
                  "LSB", "RSB", "DOT", "COMMA", "SEMICOLON", "COLON", "LP", 
                  "RP", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[52] = self.ERROR_CHAR_action 
            actions[53] = self.UNCLOSE_STRING_action 
            actions[54] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text) 
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise UncloseString(self.text) 
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise IllegalEscape(self.text) 
     



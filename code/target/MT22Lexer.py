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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\28")
        buf.write("\u0166\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\3\2\3\2\3\2\3\2\7\2z\n\2\f\2\16\2}\13\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\7\3\u0088\n\3\f\3\16\3\u008b\13")
        buf.write("\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\5\7\u0097\n")
        buf.write("\7\3\7\3\7\3\7\7\7\u009c\n\7\f\7\16\7\u009f\13\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write("\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3")
        buf.write("%\3%\3&\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3*\3+\3+\3")
        buf.write("+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62")
        buf.write("\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\6\67\u0158")
        buf.write("\n\67\r\67\16\67\u0159\3\67\3\67\38\38\38\39\39\39\3:")
        buf.write("\3:\3:\3{\2;\3\3\5\4\7\2\t\2\13\2\r\5\17\6\21\7\23\b\25")
        buf.write("\t\27\n\31\13\33\f\35\r\37\16!\17#\20%\21\'\22)\23+\24")
        buf.write("-\25/\26\61\27\63\30\65\31\67\329\33;\34=\35?\36A\37C")
        buf.write(" E!G\"I#K$M%O&Q\'S(U)W*Y+[,]-_.a/c\60e\61g\62i\63k\64")
        buf.write("m\65o\66q\67s8\3\2\6\4\2\f\f\17\17\4\2C\\c|\3\2\62;\5")
        buf.write("\2\n\f\16\17\"\"\2\u0169\2\3\3\2\2\2\2\5\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2")
        buf.write("\2\2\3u\3\2\2\2\5\u0083\3\2\2\2\7\u008e\3\2\2\2\t\u0090")
        buf.write("\3\2\2\2\13\u0092\3\2\2\2\r\u0096\3\2\2\2\17\u00a0\3\2")
        buf.write("\2\2\21\u00a5\3\2\2\2\23\u00ab\3\2\2\2\25\u00b3\3\2\2")
        buf.write("\2\27\u00b8\3\2\2\2\31\u00be\3\2\2\2\33\u00c4\3\2\2\2")
        buf.write("\35\u00ca\3\2\2\2\37\u00d1\3\2\2\2!\u00d5\3\2\2\2#\u00dd")
        buf.write("\3\2\2\2%\u00e1\3\2\2\2\'\u00e8\3\2\2\2)\u00f1\3\2\2\2")
        buf.write("+\u00f4\3\2\2\2-\u00fd\3\2\2\2/\u0102\3\2\2\2\61\u0105")
        buf.write("\3\2\2\2\63\u010a\3\2\2\2\65\u010d\3\2\2\2\67\u0113\3")
        buf.write("\2\2\29\u011b\3\2\2\2;\u011d\3\2\2\2=\u011f\3\2\2\2?\u0121")
        buf.write("\3\2\2\2A\u0123\3\2\2\2C\u0125\3\2\2\2E\u0127\3\2\2\2")
        buf.write("G\u012a\3\2\2\2I\u012d\3\2\2\2K\u0130\3\2\2\2M\u0133\3")
        buf.write("\2\2\2O\u0135\3\2\2\2Q\u0138\3\2\2\2S\u013a\3\2\2\2U\u013d")
        buf.write("\3\2\2\2W\u0140\3\2\2\2Y\u0142\3\2\2\2[\u0144\3\2\2\2")
        buf.write("]\u0146\3\2\2\2_\u0148\3\2\2\2a\u014a\3\2\2\2c\u014c\3")
        buf.write("\2\2\2e\u014e\3\2\2\2g\u0150\3\2\2\2i\u0152\3\2\2\2k\u0154")
        buf.write("\3\2\2\2m\u0157\3\2\2\2o\u015d\3\2\2\2q\u0160\3\2\2\2")
        buf.write("s\u0163\3\2\2\2uv\7\61\2\2vw\7,\2\2w{\3\2\2\2xz\13\2\2")
        buf.write("\2yx\3\2\2\2z}\3\2\2\2{|\3\2\2\2{y\3\2\2\2|~\3\2\2\2}")
        buf.write("{\3\2\2\2~\177\7,\2\2\177\u0080\7\61\2\2\u0080\u0081\3")
        buf.write("\2\2\2\u0081\u0082\b\2\2\2\u0082\4\3\2\2\2\u0083\u0084")
        buf.write("\7\61\2\2\u0084\u0085\7\61\2\2\u0085\u0089\3\2\2\2\u0086")
        buf.write("\u0088\n\2\2\2\u0087\u0086\3\2\2\2\u0088\u008b\3\2\2\2")
        buf.write("\u0089\u0087\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u008c\3")
        buf.write("\2\2\2\u008b\u0089\3\2\2\2\u008c\u008d\b\3\2\2\u008d\6")
        buf.write("\3\2\2\2\u008e\u008f\t\3\2\2\u008f\b\3\2\2\2\u0090\u0091")
        buf.write("\7a\2\2\u0091\n\3\2\2\2\u0092\u0093\t\4\2\2\u0093\f\3")
        buf.write("\2\2\2\u0094\u0097\5\t\5\2\u0095\u0097\5\7\4\2\u0096\u0094")
        buf.write("\3\2\2\2\u0096\u0095\3\2\2\2\u0097\u009d\3\2\2\2\u0098")
        buf.write("\u009c\5\t\5\2\u0099\u009c\5\7\4\2\u009a\u009c\5\13\6")
        buf.write("\2\u009b\u0098\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009a")
        buf.write("\3\2\2\2\u009c\u009f\3\2\2\2\u009d\u009b\3\2\2\2\u009d")
        buf.write("\u009e\3\2\2\2\u009e\16\3\2\2\2\u009f\u009d\3\2\2\2\u00a0")
        buf.write("\u00a1\7c\2\2\u00a1\u00a2\7w\2\2\u00a2\u00a3\7v\2\2\u00a3")
        buf.write("\u00a4\7q\2\2\u00a4\20\3\2\2\2\u00a5\u00a6\7h\2\2\u00a6")
        buf.write("\u00a7\7c\2\2\u00a7\u00a8\7n\2\2\u00a8\u00a9\7u\2\2\u00a9")
        buf.write("\u00aa\7g\2\2\u00aa\22\3\2\2\2\u00ab\u00ac\7k\2\2\u00ac")
        buf.write("\u00ad\7p\2\2\u00ad\u00ae\7v\2\2\u00ae\u00af\7g\2\2\u00af")
        buf.write("\u00b0\7i\2\2\u00b0\u00b1\7g\2\2\u00b1\u00b2\7t\2\2\u00b2")
        buf.write("\24\3\2\2\2\u00b3\u00b4\7x\2\2\u00b4\u00b5\7q\2\2\u00b5")
        buf.write("\u00b6\7k\2\2\u00b6\u00b7\7f\2\2\u00b7\26\3\2\2\2\u00b8")
        buf.write("\u00b9\7c\2\2\u00b9\u00ba\7t\2\2\u00ba\u00bb\7t\2\2\u00bb")
        buf.write("\u00bc\7c\2\2\u00bc\u00bd\7{\2\2\u00bd\30\3\2\2\2\u00be")
        buf.write("\u00bf\7d\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1\7g\2\2\u00c1")
        buf.write("\u00c2\7c\2\2\u00c2\u00c3\7m\2\2\u00c3\32\3\2\2\2\u00c4")
        buf.write("\u00c5\7h\2\2\u00c5\u00c6\7n\2\2\u00c6\u00c7\7q\2\2\u00c7")
        buf.write("\u00c8\7c\2\2\u00c8\u00c9\7v\2\2\u00c9\34\3\2\2\2\u00ca")
        buf.write("\u00cb\7t\2\2\u00cb\u00cc\7g\2\2\u00cc\u00cd\7v\2\2\u00cd")
        buf.write("\u00ce\7w\2\2\u00ce\u00cf\7t\2\2\u00cf\u00d0\7p\2\2\u00d0")
        buf.write("\36\3\2\2\2\u00d1\u00d2\7q\2\2\u00d2\u00d3\7w\2\2\u00d3")
        buf.write("\u00d4\7v\2\2\u00d4 \3\2\2\2\u00d5\u00d6\7d\2\2\u00d6")
        buf.write("\u00d7\7q\2\2\u00d7\u00d8\7q\2\2\u00d8\u00d9\7n\2\2\u00d9")
        buf.write("\u00da\7g\2\2\u00da\u00db\7c\2\2\u00db\u00dc\7p\2\2\u00dc")
        buf.write("\"\3\2\2\2\u00dd\u00de\7h\2\2\u00de\u00df\7q\2\2\u00df")
        buf.write("\u00e0\7t\2\2\u00e0$\3\2\2\2\u00e1\u00e2\7u\2\2\u00e2")
        buf.write("\u00e3\7v\2\2\u00e3\u00e4\7t\2\2\u00e4\u00e5\7k\2\2\u00e5")
        buf.write("\u00e6\7p\2\2\u00e6\u00e7\7i\2\2\u00e7&\3\2\2\2\u00e8")
        buf.write("\u00e9\7e\2\2\u00e9\u00ea\7q\2\2\u00ea\u00eb\7p\2\2\u00eb")
        buf.write("\u00ec\7v\2\2\u00ec\u00ed\7k\2\2\u00ed\u00ee\7p\2\2\u00ee")
        buf.write("\u00ef\7w\2\2\u00ef\u00f0\7g\2\2\u00f0(\3\2\2\2\u00f1")
        buf.write("\u00f2\7f\2\2\u00f2\u00f3\7q\2\2\u00f3*\3\2\2\2\u00f4")
        buf.write("\u00f5\7h\2\2\u00f5\u00f6\7w\2\2\u00f6\u00f7\7p\2\2\u00f7")
        buf.write("\u00f8\7e\2\2\u00f8\u00f9\7v\2\2\u00f9\u00fa\7k\2\2\u00fa")
        buf.write("\u00fb\7q\2\2\u00fb\u00fc\7p\2\2\u00fc,\3\2\2\2\u00fd")
        buf.write("\u00fe\7v\2\2\u00fe\u00ff\7t\2\2\u00ff\u0100\7w\2\2\u0100")
        buf.write("\u0101\7g\2\2\u0101.\3\2\2\2\u0102\u0103\7q\2\2\u0103")
        buf.write("\u0104\7h\2\2\u0104\60\3\2\2\2\u0105\u0106\7g\2\2\u0106")
        buf.write("\u0107\7n\2\2\u0107\u0108\7u\2\2\u0108\u0109\7g\2\2\u0109")
        buf.write("\62\3\2\2\2\u010a\u010b\7k\2\2\u010b\u010c\7h\2\2\u010c")
        buf.write("\64\3\2\2\2\u010d\u010e\7y\2\2\u010e\u010f\7j\2\2\u010f")
        buf.write("\u0110\7k\2\2\u0110\u0111\7n\2\2\u0111\u0112\7g\2\2\u0112")
        buf.write("\66\3\2\2\2\u0113\u0114\7k\2\2\u0114\u0115\7p\2\2\u0115")
        buf.write("\u0116\7j\2\2\u0116\u0117\7g\2\2\u0117\u0118\7t\2\2\u0118")
        buf.write("\u0119\7k\2\2\u0119\u011a\7v\2\2\u011a8\3\2\2\2\u011b")
        buf.write("\u011c\7-\2\2\u011c:\3\2\2\2\u011d\u011e\7/\2\2\u011e")
        buf.write("<\3\2\2\2\u011f\u0120\7,\2\2\u0120>\3\2\2\2\u0121\u0122")
        buf.write("\7\61\2\2\u0122@\3\2\2\2\u0123\u0124\7\'\2\2\u0124B\3")
        buf.write("\2\2\2\u0125\u0126\7#\2\2\u0126D\3\2\2\2\u0127\u0128\7")
        buf.write("(\2\2\u0128\u0129\7(\2\2\u0129F\3\2\2\2\u012a\u012b\7")
        buf.write("~\2\2\u012b\u012c\7~\2\2\u012cH\3\2\2\2\u012d\u012e\7")
        buf.write("?\2\2\u012e\u012f\7?\2\2\u012fJ\3\2\2\2\u0130\u0131\7")
        buf.write("#\2\2\u0131\u0132\7?\2\2\u0132L\3\2\2\2\u0133\u0134\7")
        buf.write(">\2\2\u0134N\3\2\2\2\u0135\u0136\7>\2\2\u0136\u0137\7")
        buf.write("?\2\2\u0137P\3\2\2\2\u0138\u0139\7@\2\2\u0139R\3\2\2\2")
        buf.write("\u013a\u013b\7@\2\2\u013b\u013c\7?\2\2\u013cT\3\2\2\2")
        buf.write("\u013d\u013e\7<\2\2\u013e\u013f\7<\2\2\u013fV\3\2\2\2")
        buf.write("\u0140\u0141\7*\2\2\u0141X\3\2\2\2\u0142\u0143\7+\2\2")
        buf.write("\u0143Z\3\2\2\2\u0144\u0145\7]\2\2\u0145\\\3\2\2\2\u0146")
        buf.write("\u0147\7_\2\2\u0147^\3\2\2\2\u0148\u0149\7\60\2\2\u0149")
        buf.write("`\3\2\2\2\u014a\u014b\7.\2\2\u014bb\3\2\2\2\u014c\u014d")
        buf.write("\7=\2\2\u014dd\3\2\2\2\u014e\u014f\7<\2\2\u014ff\3\2\2")
        buf.write("\2\u0150\u0151\7}\2\2\u0151h\3\2\2\2\u0152\u0153\7\177")
        buf.write("\2\2\u0153j\3\2\2\2\u0154\u0155\7?\2\2\u0155l\3\2\2\2")
        buf.write("\u0156\u0158\t\5\2\2\u0157\u0156\3\2\2\2\u0158\u0159\3")
        buf.write("\2\2\2\u0159\u0157\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u015b")
        buf.write("\3\2\2\2\u015b\u015c\b\67\2\2\u015cn\3\2\2\2\u015d\u015e")
        buf.write("\13\2\2\2\u015e\u015f\b8\3\2\u015fp\3\2\2\2\u0160\u0161")
        buf.write("\13\2\2\2\u0161\u0162\b9\4\2\u0162r\3\2\2\2\u0163\u0164")
        buf.write("\13\2\2\2\u0164\u0165\b:\5\2\u0165t\3\2\2\2\t\2{\u0089")
        buf.write("\u0096\u009b\u009d\u0159\6\b\2\2\38\2\39\3\3:\4")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT_C = 1
    COMMENT_CPLUS = 2
    ID = 3
    AUTO = 4
    FALSE = 5
    INTERGER = 6
    VOID = 7
    ARRAY = 8
    BREAK = 9
    FLOAT = 10
    RETURN = 11
    OUT = 12
    BOOLEAN = 13
    FOR = 14
    STRING = 15
    CONTINUE = 16
    DO = 17
    FUNCTION = 18
    TRUE = 19
    OF = 20
    ELSE = 21
    IF = 22
    WHILE = 23
    INHERIT = 24
    ADDOP = 25
    SUBOP = 26
    MULOP = 27
    DIV = 28
    MOD = 29
    NOT = 30
    AND = 31
    OR = 32
    EQUAL = 33
    NOT_EQUAL = 34
    LESS = 35
    LESS_OR_EQUAL = 36
    GREATER = 37
    GREATER_OR_EQUAL = 38
    DOUBLE_COLON = 39
    LB = 40
    RB = 41
    LSB = 42
    RSB = 43
    DOT = 44
    COMMA = 45
    SEMICOLON = 46
    COLON = 47
    LP = 48
    RP = 49
    ASSIGN = 50
    WS = 51
    ERROR_CHAR = 52
    UNCLOSE_STRING = 53
    ILLEGAL_ESCAPE = 54

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'false'", "'integer'", "'void'", "'array'", "'break'", 
            "'float'", "'return'", "'out'", "'boolean'", "'for'", "'string'", 
            "'continue'", "'do'", "'function'", "'true'", "'of'", "'else'", 
            "'if'", "'while'", "'inherit'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", 
            "'>'", "'>='", "'::'", "'('", "')'", "'['", "']'", "'.'", "','", 
            "';'", "':'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT_C", "COMMENT_CPLUS", "ID", "AUTO", "FALSE", "INTERGER", 
            "VOID", "ARRAY", "BREAK", "FLOAT", "RETURN", "OUT", "BOOLEAN", 
            "FOR", "STRING", "CONTINUE", "DO", "FUNCTION", "TRUE", "OF", 
            "ELSE", "IF", "WHILE", "INHERIT", "ADDOP", "SUBOP", "MULOP", 
            "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", "LESS", 
            "LESS_OR_EQUAL", "GREATER", "GREATER_OR_EQUAL", "DOUBLE_COLON", 
            "LB", "RB", "LSB", "RSB", "DOT", "COMMA", "SEMICOLON", "COLON", 
            "LP", "RP", "ASSIGN", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "COMMENT_C", "COMMENT_CPLUS", "LETTER", "UNDERSCORE", 
                  "DIGIT", "ID", "AUTO", "FALSE", "INTERGER", "VOID", "ARRAY", 
                  "BREAK", "FLOAT", "RETURN", "OUT", "BOOLEAN", "FOR", "STRING", 
                  "CONTINUE", "DO", "FUNCTION", "TRUE", "OF", "ELSE", "IF", 
                  "WHILE", "INHERIT", "ADDOP", "SUBOP", "MULOP", "DIV", 
                  "MOD", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", "LESS", 
                  "LESS_OR_EQUAL", "GREATER", "GREATER_OR_EQUAL", "DOUBLE_COLON", 
                  "LB", "RB", "LSB", "RSB", "DOT", "COMMA", "SEMICOLON", 
                  "COLON", "LP", "RP", "ASSIGN", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

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
            actions[54] = self.ERROR_CHAR_action 
            actions[55] = self.UNCLOSE_STRING_action 
            actions[56] = self.ILLEGAL_ESCAPE_action 
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
     



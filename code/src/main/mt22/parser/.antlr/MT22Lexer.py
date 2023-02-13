# Generated from e:\PPL\PPL\code\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2;")
        buf.write("\u01f4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\3\2\3\2\3\2\3\2\7\2\u008e\n\2\f\2\16\2\u0091\13")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u009c\n\3\f")
        buf.write("\3\16\3\u009f\13\3\3\3\3\3\3\4\3\4\7\4\u00a5\n\4\f\4\16")
        buf.write("\4\u00a8\13\4\3\4\3\4\6\4\u00ac\n\4\r\4\16\4\u00ad\7\4")
        buf.write("\u00b0\n\4\f\4\16\4\u00b3\13\4\3\4\3\4\3\4\7\4\u00b8\n")
        buf.write("\4\f\4\16\4\u00bb\13\4\5\4\u00bd\n\4\3\5\3\5\5\5\u00c1")
        buf.write("\n\5\3\5\6\5\u00c4\n\5\r\5\16\5\u00c5\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\7\b\u00d0\n\b\f\b\16\b\u00d3\13\b\3\b")
        buf.write("\7\b\u00d6\n\b\f\b\16\b\u00d9\13\b\3\b\5\b\u00dc\n\b\3")
        buf.write("\b\3\b\6\b\u00e0\n\b\r\b\16\b\u00e1\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\6\b\u00ea\n\b\r\b\16\b\u00eb\3\b\3\b\5\b\u00f0")
        buf.write("\n\b\3\t\3\t\3\t\3\n\3\n\7\n\u00f7\n\n\f\n\16\n\u00fa")
        buf.write("\13\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\5\13\u0103\n\13")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\r\5\r\u010b\n\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'")
        buf.write("\3\'\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3")
        buf.write(".\3.\3.\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\62\3\62")
        buf.write("\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38")
        buf.write("\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\5")
        buf.write("@\u01cb\n@\3@\3@\3@\7@\u01d0\n@\f@\16@\u01d3\13@\3A\6")
        buf.write("A\u01d6\nA\rA\16A\u01d7\3A\3A\3B\3B\3B\3C\3C\7C\u01e1")
        buf.write("\nC\fC\16C\u01e4\13C\3C\5C\u01e7\nC\3C\3C\3D\3D\7D\u01ed")
        buf.write("\nD\fD\16D\u01f0\13D\3D\3D\3D\3\u008f\2E\3\3\5\4\7\2\t")
        buf.write("\2\13\2\r\5\17\2\21\6\23\7\25\2\27\2\31\2\33\b\35\t\37")
        buf.write("\n!\13#\f%\r\'\16)\17+\20-\21/\22\61\23\63\24\65\25\67")
        buf.write("\269\27;\30=\31?\32A\33C\34E\35G\36I\37K M!O\"Q#S$U%W")
        buf.write("&Y\'[(])_*a+c,e-g.i/k\60m\61o\62q\63s\64u\65w\66y\2{\2")
        buf.write("}\2\177\67\u00818\u00839\u0085:\u0087;\3\2\16\4\2\f\f")
        buf.write("\17\17\3\2\63;\3\2\62;\4\2GGgg\4\2--//\4\2$$^^\t\2))^")
        buf.write("^ddhhppttvv\n\2$$))^^ddhhppttvv\3\2^^\4\2C\\c|\5\2\n\f")
        buf.write("\16\17\"\"\7\3\n\f\16\17$$))^^\2\u0206\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\33\3")
        buf.write("\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2")
        buf.write("\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2")
        buf.write("\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2")
        buf.write("\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2")
        buf.write("\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2")
        buf.write("\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3")
        buf.write("\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]")
        buf.write("\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2")
        buf.write("g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2")
        buf.write("\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2\177\3\2")
        buf.write("\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2")
        buf.write("\u0087\3\2\2\2\3\u0089\3\2\2\2\5\u0097\3\2\2\2\7\u00bc")
        buf.write("\3\2\2\2\t\u00be\3\2\2\2\13\u00c7\3\2\2\2\r\u00c9\3\2")
        buf.write("\2\2\17\u00ef\3\2\2\2\21\u00f1\3\2\2\2\23\u00f4\3\2\2")
        buf.write("\2\25\u0102\3\2\2\2\27\u0104\3\2\2\2\31\u010a\3\2\2\2")
        buf.write("\33\u010c\3\2\2\2\35\u0111\3\2\2\2\37\u0117\3\2\2\2!\u011f")
        buf.write("\3\2\2\2#\u0124\3\2\2\2%\u012a\3\2\2\2\'\u0130\3\2\2\2")
        buf.write(")\u0136\3\2\2\2+\u013d\3\2\2\2-\u0141\3\2\2\2/\u0149\3")
        buf.write("\2\2\2\61\u014d\3\2\2\2\63\u0154\3\2\2\2\65\u015d\3\2")
        buf.write("\2\2\67\u0160\3\2\2\29\u0169\3\2\2\2;\u016e\3\2\2\2=\u0171")
        buf.write("\3\2\2\2?\u0176\3\2\2\2A\u0179\3\2\2\2C\u017f\3\2\2\2")
        buf.write("E\u0187\3\2\2\2G\u0189\3\2\2\2I\u018b\3\2\2\2K\u018d\3")
        buf.write("\2\2\2M\u018f\3\2\2\2O\u0191\3\2\2\2Q\u0193\3\2\2\2S\u0196")
        buf.write("\3\2\2\2U\u0199\3\2\2\2W\u019c\3\2\2\2Y\u019f\3\2\2\2")
        buf.write("[\u01a1\3\2\2\2]\u01a4\3\2\2\2_\u01a6\3\2\2\2a\u01a9\3")
        buf.write("\2\2\2c\u01ac\3\2\2\2e\u01ae\3\2\2\2g\u01b0\3\2\2\2i\u01b2")
        buf.write("\3\2\2\2k\u01b4\3\2\2\2m\u01b6\3\2\2\2o\u01b8\3\2\2\2")
        buf.write("q\u01ba\3\2\2\2s\u01bc\3\2\2\2u\u01be\3\2\2\2w\u01c0\3")
        buf.write("\2\2\2y\u01c2\3\2\2\2{\u01c4\3\2\2\2}\u01c6\3\2\2\2\177")
        buf.write("\u01ca\3\2\2\2\u0081\u01d5\3\2\2\2\u0083\u01db\3\2\2\2")
        buf.write("\u0085\u01de\3\2\2\2\u0087\u01ea\3\2\2\2\u0089\u008a\7")
        buf.write("\61\2\2\u008a\u008b\7,\2\2\u008b\u008f\3\2\2\2\u008c\u008e")
        buf.write("\13\2\2\2\u008d\u008c\3\2\2\2\u008e\u0091\3\2\2\2\u008f")
        buf.write("\u0090\3\2\2\2\u008f\u008d\3\2\2\2\u0090\u0092\3\2\2\2")
        buf.write("\u0091\u008f\3\2\2\2\u0092\u0093\7,\2\2\u0093\u0094\7")
        buf.write("\61\2\2\u0094\u0095\3\2\2\2\u0095\u0096\b\2\2\2\u0096")
        buf.write("\4\3\2\2\2\u0097\u0098\7\61\2\2\u0098\u0099\7\61\2\2\u0099")
        buf.write("\u009d\3\2\2\2\u009a\u009c\n\2\2\2\u009b\u009a\3\2\2\2")
        buf.write("\u009c\u009f\3\2\2\2\u009d\u009b\3\2\2\2\u009d\u009e\3")
        buf.write("\2\2\2\u009e\u00a0\3\2\2\2\u009f\u009d\3\2\2\2\u00a0\u00a1")
        buf.write("\b\3\2\2\u00a1\6\3\2\2\2\u00a2\u00b1\t\3\2\2\u00a3\u00a5")
        buf.write("\t\4\2\2\u00a4\u00a3\3\2\2\2\u00a5\u00a8\3\2\2\2\u00a6")
        buf.write("\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a9\3\2\2\2")
        buf.write("\u00a8\u00a6\3\2\2\2\u00a9\u00ab\7a\2\2\u00aa\u00ac\t")
        buf.write("\4\2\2\u00ab\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00ab")
        buf.write("\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00b0\3\2\2\2\u00af")
        buf.write("\u00a6\3\2\2\2\u00b0\u00b3\3\2\2\2\u00b1\u00af\3\2\2\2")
        buf.write("\u00b1\u00b2\3\2\2\2\u00b2\u00bd\3\2\2\2\u00b3\u00b1\3")
        buf.write("\2\2\2\u00b4\u00bd\7\62\2\2\u00b5\u00b9\t\3\2\2\u00b6")
        buf.write("\u00b8\t\4\2\2\u00b7\u00b6\3\2\2\2\u00b8\u00bb\3\2\2\2")
        buf.write("\u00b9\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bd\3")
        buf.write("\2\2\2\u00bb\u00b9\3\2\2\2\u00bc\u00a2\3\2\2\2\u00bc\u00b4")
        buf.write("\3\2\2\2\u00bc\u00b5\3\2\2\2\u00bd\b\3\2\2\2\u00be\u00c0")
        buf.write("\t\5\2\2\u00bf\u00c1\5\13\6\2\u00c0\u00bf\3\2\2\2\u00c0")
        buf.write("\u00c1\3\2\2\2\u00c1\u00c3\3\2\2\2\u00c2\u00c4\5}?\2\u00c3")
        buf.write("\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c3\3\2\2\2")
        buf.write("\u00c5\u00c6\3\2\2\2\u00c6\n\3\2\2\2\u00c7\u00c8\t\6\2")
        buf.write("\2\u00c8\f\3\2\2\2\u00c9\u00ca\5\7\4\2\u00ca\u00cb\b\7")
        buf.write("\3\2\u00cb\16\3\2\2\2\u00cc\u00cd\5\7\4\2\u00cd\u00d1")
        buf.write("\7\60\2\2\u00ce\u00d0\5}?\2\u00cf\u00ce\3\2\2\2\u00d0")
        buf.write("\u00d3\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2")
        buf.write("\u00d2\u00d7\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d4\u00d6\5")
        buf.write("\t\5\2\u00d5\u00d4\3\2\2\2\u00d6\u00d9\3\2\2\2\u00d7\u00d5")
        buf.write("\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00f0\3\2\2\2\u00d9")
        buf.write("\u00d7\3\2\2\2\u00da\u00dc\5\7\4\2\u00db\u00da\3\2\2\2")
        buf.write("\u00db\u00dc\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00df\7")
        buf.write("\60\2\2\u00de\u00e0\5}?\2\u00df\u00de\3\2\2\2\u00e0\u00e1")
        buf.write("\3\2\2\2\u00e1\u00df\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2")
        buf.write("\u00f0\3\2\2\2\u00e3\u00e4\5\7\4\2\u00e4\u00e5\5\t\5\2")
        buf.write("\u00e5\u00f0\3\2\2\2\u00e6\u00e7\5\7\4\2\u00e7\u00e9\7")
        buf.write("\60\2\2\u00e8\u00ea\5}?\2\u00e9\u00e8\3\2\2\2\u00ea\u00eb")
        buf.write("\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec")
        buf.write("\u00ed\3\2\2\2\u00ed\u00ee\5\t\5\2\u00ee\u00f0\3\2\2\2")
        buf.write("\u00ef\u00cc\3\2\2\2\u00ef\u00db\3\2\2\2\u00ef\u00e3\3")
        buf.write("\2\2\2\u00ef\u00e6\3\2\2\2\u00f0\20\3\2\2\2\u00f1\u00f2")
        buf.write("\5\17\b\2\u00f2\u00f3\b\t\4\2\u00f3\22\3\2\2\2\u00f4\u00f8")
        buf.write("\7$\2\2\u00f5\u00f7\5\25\13\2\u00f6\u00f5\3\2\2\2\u00f7")
        buf.write("\u00fa\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f8\u00f9\3\2\2\2")
        buf.write("\u00f9\u00fb\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fb\u00fc\7")
        buf.write("$\2\2\u00fc\u00fd\b\n\5\2\u00fd\24\3\2\2\2\u00fe\u0103")
        buf.write("\n\7\2\2\u00ff\u0103\5\27\f\2\u0100\u0101\7^\2\2\u0101")
        buf.write("\u0103\7$\2\2\u0102\u00fe\3\2\2\2\u0102\u00ff\3\2\2\2")
        buf.write("\u0102\u0100\3\2\2\2\u0103\26\3\2\2\2\u0104\u0105\7^\2")
        buf.write("\2\u0105\u0106\t\b\2\2\u0106\30\3\2\2\2\u0107\u0108\7")
        buf.write("^\2\2\u0108\u010b\n\t\2\2\u0109\u010b\n\n\2\2\u010a\u0107")
        buf.write("\3\2\2\2\u010a\u0109\3\2\2\2\u010b\32\3\2\2\2\u010c\u010d")
        buf.write("\7c\2\2\u010d\u010e\7w\2\2\u010e\u010f\7v\2\2\u010f\u0110")
        buf.write("\7q\2\2\u0110\34\3\2\2\2\u0111\u0112\7h\2\2\u0112\u0113")
        buf.write("\7c\2\2\u0113\u0114\7n\2\2\u0114\u0115\7u\2\2\u0115\u0116")
        buf.write("\7g\2\2\u0116\36\3\2\2\2\u0117\u0118\7k\2\2\u0118\u0119")
        buf.write("\7p\2\2\u0119\u011a\7v\2\2\u011a\u011b\7g\2\2\u011b\u011c")
        buf.write("\7i\2\2\u011c\u011d\7g\2\2\u011d\u011e\7t\2\2\u011e \3")
        buf.write("\2\2\2\u011f\u0120\7x\2\2\u0120\u0121\7q\2\2\u0121\u0122")
        buf.write("\7k\2\2\u0122\u0123\7f\2\2\u0123\"\3\2\2\2\u0124\u0125")
        buf.write("\7c\2\2\u0125\u0126\7t\2\2\u0126\u0127\7t\2\2\u0127\u0128")
        buf.write("\7c\2\2\u0128\u0129\7{\2\2\u0129$\3\2\2\2\u012a\u012b")
        buf.write("\7d\2\2\u012b\u012c\7t\2\2\u012c\u012d\7g\2\2\u012d\u012e")
        buf.write("\7c\2\2\u012e\u012f\7m\2\2\u012f&\3\2\2\2\u0130\u0131")
        buf.write("\7h\2\2\u0131\u0132\7n\2\2\u0132\u0133\7q\2\2\u0133\u0134")
        buf.write("\7c\2\2\u0134\u0135\7v\2\2\u0135(\3\2\2\2\u0136\u0137")
        buf.write("\7t\2\2\u0137\u0138\7g\2\2\u0138\u0139\7v\2\2\u0139\u013a")
        buf.write("\7w\2\2\u013a\u013b\7t\2\2\u013b\u013c\7p\2\2\u013c*\3")
        buf.write("\2\2\2\u013d\u013e\7q\2\2\u013e\u013f\7w\2\2\u013f\u0140")
        buf.write("\7v\2\2\u0140,\3\2\2\2\u0141\u0142\7d\2\2\u0142\u0143")
        buf.write("\7q\2\2\u0143\u0144\7q\2\2\u0144\u0145\7n\2\2\u0145\u0146")
        buf.write("\7g\2\2\u0146\u0147\7c\2\2\u0147\u0148\7p\2\2\u0148.\3")
        buf.write("\2\2\2\u0149\u014a\7h\2\2\u014a\u014b\7q\2\2\u014b\u014c")
        buf.write("\7t\2\2\u014c\60\3\2\2\2\u014d\u014e\7u\2\2\u014e\u014f")
        buf.write("\7v\2\2\u014f\u0150\7t\2\2\u0150\u0151\7k\2\2\u0151\u0152")
        buf.write("\7p\2\2\u0152\u0153\7i\2\2\u0153\62\3\2\2\2\u0154\u0155")
        buf.write("\7e\2\2\u0155\u0156\7q\2\2\u0156\u0157\7p\2\2\u0157\u0158")
        buf.write("\7v\2\2\u0158\u0159\7k\2\2\u0159\u015a\7p\2\2\u015a\u015b")
        buf.write("\7w\2\2\u015b\u015c\7g\2\2\u015c\64\3\2\2\2\u015d\u015e")
        buf.write("\7f\2\2\u015e\u015f\7q\2\2\u015f\66\3\2\2\2\u0160\u0161")
        buf.write("\7h\2\2\u0161\u0162\7w\2\2\u0162\u0163\7p\2\2\u0163\u0164")
        buf.write("\7e\2\2\u0164\u0165\7v\2\2\u0165\u0166\7k\2\2\u0166\u0167")
        buf.write("\7q\2\2\u0167\u0168\7p\2\2\u01688\3\2\2\2\u0169\u016a")
        buf.write("\7v\2\2\u016a\u016b\7t\2\2\u016b\u016c\7w\2\2\u016c\u016d")
        buf.write("\7g\2\2\u016d:\3\2\2\2\u016e\u016f\7q\2\2\u016f\u0170")
        buf.write("\7h\2\2\u0170<\3\2\2\2\u0171\u0172\7g\2\2\u0172\u0173")
        buf.write("\7n\2\2\u0173\u0174\7u\2\2\u0174\u0175\7g\2\2\u0175>\3")
        buf.write("\2\2\2\u0176\u0177\7k\2\2\u0177\u0178\7h\2\2\u0178@\3")
        buf.write("\2\2\2\u0179\u017a\7y\2\2\u017a\u017b\7j\2\2\u017b\u017c")
        buf.write("\7k\2\2\u017c\u017d\7n\2\2\u017d\u017e\7g\2\2\u017eB\3")
        buf.write("\2\2\2\u017f\u0180\7k\2\2\u0180\u0181\7p\2\2\u0181\u0182")
        buf.write("\7j\2\2\u0182\u0183\7g\2\2\u0183\u0184\7t\2\2\u0184\u0185")
        buf.write("\7k\2\2\u0185\u0186\7v\2\2\u0186D\3\2\2\2\u0187\u0188")
        buf.write("\7-\2\2\u0188F\3\2\2\2\u0189\u018a\7/\2\2\u018aH\3\2\2")
        buf.write("\2\u018b\u018c\7,\2\2\u018cJ\3\2\2\2\u018d\u018e\7\61")
        buf.write("\2\2\u018eL\3\2\2\2\u018f\u0190\7\'\2\2\u0190N\3\2\2\2")
        buf.write("\u0191\u0192\7#\2\2\u0192P\3\2\2\2\u0193\u0194\7(\2\2")
        buf.write("\u0194\u0195\7(\2\2\u0195R\3\2\2\2\u0196\u0197\7~\2\2")
        buf.write("\u0197\u0198\7~\2\2\u0198T\3\2\2\2\u0199\u019a\7?\2\2")
        buf.write("\u019a\u019b\7?\2\2\u019bV\3\2\2\2\u019c\u019d\7#\2\2")
        buf.write("\u019d\u019e\7?\2\2\u019eX\3\2\2\2\u019f\u01a0\7>\2\2")
        buf.write("\u01a0Z\3\2\2\2\u01a1\u01a2\7>\2\2\u01a2\u01a3\7?\2\2")
        buf.write("\u01a3\\\3\2\2\2\u01a4\u01a5\7@\2\2\u01a5^\3\2\2\2\u01a6")
        buf.write("\u01a7\7@\2\2\u01a7\u01a8\7?\2\2\u01a8`\3\2\2\2\u01a9")
        buf.write("\u01aa\7<\2\2\u01aa\u01ab\7<\2\2\u01abb\3\2\2\2\u01ac")
        buf.write("\u01ad\7*\2\2\u01add\3\2\2\2\u01ae\u01af\7+\2\2\u01af")
        buf.write("f\3\2\2\2\u01b0\u01b1\7]\2\2\u01b1h\3\2\2\2\u01b2\u01b3")
        buf.write("\7_\2\2\u01b3j\3\2\2\2\u01b4\u01b5\7\60\2\2\u01b5l\3\2")
        buf.write("\2\2\u01b6\u01b7\7.\2\2\u01b7n\3\2\2\2\u01b8\u01b9\7=")
        buf.write("\2\2\u01b9p\3\2\2\2\u01ba\u01bb\7<\2\2\u01bbr\3\2\2\2")
        buf.write("\u01bc\u01bd\7}\2\2\u01bdt\3\2\2\2\u01be\u01bf\7\177\2")
        buf.write("\2\u01bfv\3\2\2\2\u01c0\u01c1\7?\2\2\u01c1x\3\2\2\2\u01c2")
        buf.write("\u01c3\t\13\2\2\u01c3z\3\2\2\2\u01c4\u01c5\7a\2\2\u01c5")
        buf.write("|\3\2\2\2\u01c6\u01c7\t\4\2\2\u01c7~\3\2\2\2\u01c8\u01cb")
        buf.write("\5{>\2\u01c9\u01cb\5y=\2\u01ca\u01c8\3\2\2\2\u01ca\u01c9")
        buf.write("\3\2\2\2\u01cb\u01d1\3\2\2\2\u01cc\u01d0\5{>\2\u01cd\u01d0")
        buf.write("\5y=\2\u01ce\u01d0\5}?\2\u01cf\u01cc\3\2\2\2\u01cf\u01cd")
        buf.write("\3\2\2\2\u01cf\u01ce\3\2\2\2\u01d0\u01d3\3\2\2\2\u01d1")
        buf.write("\u01cf\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u0080\3\2\2\2")
        buf.write("\u01d3\u01d1\3\2\2\2\u01d4\u01d6\t\f\2\2\u01d5\u01d4\3")
        buf.write("\2\2\2\u01d6\u01d7\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d7\u01d8")
        buf.write("\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01da\bA\2\2\u01da")
        buf.write("\u0082\3\2\2\2\u01db\u01dc\13\2\2\2\u01dc\u01dd\bB\6\2")
        buf.write("\u01dd\u0084\3\2\2\2\u01de\u01e2\7$\2\2\u01df\u01e1\5")
        buf.write("\25\13\2\u01e0\u01df\3\2\2\2\u01e1\u01e4\3\2\2\2\u01e2")
        buf.write("\u01e0\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3\u01e6\3\2\2\2")
        buf.write("\u01e4\u01e2\3\2\2\2\u01e5\u01e7\t\r\2\2\u01e6\u01e5\3")
        buf.write("\2\2\2\u01e7\u01e8\3\2\2\2\u01e8\u01e9\bC\7\2\u01e9\u0086")
        buf.write("\3\2\2\2\u01ea\u01ee\7$\2\2\u01eb\u01ed\5\25\13\2\u01ec")
        buf.write("\u01eb\3\2\2\2\u01ed\u01f0\3\2\2\2\u01ee\u01ec\3\2\2\2")
        buf.write("\u01ee\u01ef\3\2\2\2\u01ef\u01f1\3\2\2\2\u01f0\u01ee\3")
        buf.write("\2\2\2\u01f1\u01f2\5\31\r\2\u01f2\u01f3\bD\b\2\u01f3\u0088")
        buf.write("\3\2\2\2\34\2\u008f\u009d\u00a6\u00ad\u00b1\u00b9\u00bc")
        buf.write("\u00c0\u00c5\u00d1\u00d7\u00db\u00e1\u00eb\u00ef\u00f8")
        buf.write("\u0102\u010a\u01ca\u01cf\u01d1\u01d7\u01e2\u01e6\u01ee")
        buf.write("\t\b\2\2\3\7\2\3\t\3\3\n\4\3B\5\3C\6\3D\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT_C = 1
    COMMENT_CPLUS = 2
    INT_LIT = 3
    FLOAT_LIT = 4
    STRING_LIT = 5
    AUTO = 6
    FALSE = 7
    INTERGER = 8
    VOID = 9
    ARRAY = 10
    BREAK = 11
    FLOAT = 12
    RETURN = 13
    OUT = 14
    BOOLEAN = 15
    FOR = 16
    STRING = 17
    CONTINUE = 18
    DO = 19
    FUNCTION = 20
    TRUE = 21
    OF = 22
    ELSE = 23
    IF = 24
    WHILE = 25
    INHERIT = 26
    ADDOP = 27
    SUBOP = 28
    MULOP = 29
    DIV = 30
    MOD = 31
    NOT = 32
    AND = 33
    OR = 34
    EQUAL = 35
    NOT_EQUAL = 36
    LESS = 37
    LESS_OR_EQUAL = 38
    GREATER = 39
    GREATER_OR_EQUAL = 40
    DOUBLE_COLON = 41
    LB = 42
    RB = 43
    LSB = 44
    RSB = 45
    DOT = 46
    COMMA = 47
    SEMICOLON = 48
    COLON = 49
    LP = 50
    RP = 51
    ASSIGN = 52
    ID = 53
    WS = 54
    ERROR_CHAR = 55
    UNCLOSE_STRING = 56
    ILLEGAL_ESCAPE = 57

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
            "COMMENT_C", "COMMENT_CPLUS", "INT_LIT", "FLOAT_LIT", "STRING_LIT", 
            "AUTO", "FALSE", "INTERGER", "VOID", "ARRAY", "BREAK", "FLOAT", 
            "RETURN", "OUT", "BOOLEAN", "FOR", "STRING", "CONTINUE", "DO", 
            "FUNCTION", "TRUE", "OF", "ELSE", "IF", "WHILE", "INHERIT", 
            "ADDOP", "SUBOP", "MULOP", "DIV", "MOD", "NOT", "AND", "OR", 
            "EQUAL", "NOT_EQUAL", "LESS", "LESS_OR_EQUAL", "GREATER", "GREATER_OR_EQUAL", 
            "DOUBLE_COLON", "LB", "RB", "LSB", "RSB", "DOT", "COMMA", "SEMICOLON", 
            "COLON", "LP", "RP", "ASSIGN", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "COMMENT_C", "COMMENT_CPLUS", "INT", "EXPONENT", "SIGN", 
                  "INT_LIT", "FLOATFRAG", "FLOAT_LIT", "STRING_LIT", "STRING_CHAR", 
                  "ESC_SEQ", "ESC_ILLEGAL", "AUTO", "FALSE", "INTERGER", 
                  "VOID", "ARRAY", "BREAK", "FLOAT", "RETURN", "OUT", "BOOLEAN", 
                  "FOR", "STRING", "CONTINUE", "DO", "FUNCTION", "TRUE", 
                  "OF", "ELSE", "IF", "WHILE", "INHERIT", "ADDOP", "SUBOP", 
                  "MULOP", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", 
                  "LESS", "LESS_OR_EQUAL", "GREATER", "GREATER_OR_EQUAL", 
                  "DOUBLE_COLON", "LB", "RB", "LSB", "RSB", "DOT", "COMMA", 
                  "SEMICOLON", "COLON", "LP", "RP", "ASSIGN", "LETTER", 
                  "UNDERSCORE", "DIGIT", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
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
            actions[5] = self.INT_LIT_action 
            actions[7] = self.FLOAT_LIT_action 
            actions[8] = self.STRING_LIT_action 
            actions[64] = self.ERROR_CHAR_action 
            actions[65] = self.UNCLOSE_STRING_action 
            actions[66] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	self.text = (self.text).replace("_", "") 

     

    def FLOAT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                self.text = (self.text).replace("_", "") 

     

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	self.text = (self.text)[1:-1]

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text) 
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            		possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
            		if self.text[-1] in possible:
            			raise UncloseString(self.text[1:-1])
            		else:
            			raise UncloseString(self.text[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            		raise IllegalEscape(self.text[1:])
            	
     



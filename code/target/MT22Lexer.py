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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2:")
        buf.write("\u018a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\3\2\3\2\3\2\3\2\7\2~\n\2\f\2\16\2\u0081\13")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u008c\n\3\f")
        buf.write("\3\16\3\u008f\13\3\3\3\3\3\3\4\3\4\7\4\u0095\n\4\f\4\16")
        buf.write("\4\u0098\13\4\3\4\3\4\6\4\u009c\n\4\r\4\16\4\u009d\7\4")
        buf.write("\u00a0\n\4\f\4\16\4\u00a3\13\4\3\4\3\4\3\4\7\4\u00a8\n")
        buf.write("\4\f\4\16\4\u00ab\13\4\5\4\u00ad\n\4\3\5\3\5\5\5\u00b1")
        buf.write("\n\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3\"\3")
        buf.write("#\3#\3#\3$\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3(\3)\3")
        buf.write(")\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61")
        buf.write("\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\3\67\3\67\38\38\58\u0171\n8\38\38\38\78\u0176\n8\f8\16")
        buf.write("8\u0179\138\39\69\u017c\n9\r9\169\u017d\39\39\3:\3:\3")
        buf.write(":\3;\3;\3;\3<\3<\3<\3\177\2=\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22")
        buf.write("#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\35")
        buf.write("9\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62")
        buf.write("c\63e\64g\65i\2k\2m\2o\66q\67s8u9w:\3\2\7\4\2\f\f\17\17")
        buf.write("\3\2\63;\3\2\62;\4\2C\\c|\5\2\n\f\16\17\"\"\2\u0194\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w")
        buf.write("\3\2\2\2\3y\3\2\2\2\5\u0087\3\2\2\2\7\u00ac\3\2\2\2\t")
        buf.write("\u00b0\3\2\2\2\13\u00b2\3\2\2\2\r\u00b7\3\2\2\2\17\u00bd")
        buf.write("\3\2\2\2\21\u00c5\3\2\2\2\23\u00ca\3\2\2\2\25\u00d0\3")
        buf.write("\2\2\2\27\u00d6\3\2\2\2\31\u00dc\3\2\2\2\33\u00e3\3\2")
        buf.write("\2\2\35\u00e7\3\2\2\2\37\u00ef\3\2\2\2!\u00f3\3\2\2\2")
        buf.write("#\u00fa\3\2\2\2%\u0103\3\2\2\2\'\u0106\3\2\2\2)\u010f")
        buf.write("\3\2\2\2+\u0114\3\2\2\2-\u0117\3\2\2\2/\u011c\3\2\2\2")
        buf.write("\61\u011f\3\2\2\2\63\u0125\3\2\2\2\65\u012d\3\2\2\2\67")
        buf.write("\u012f\3\2\2\29\u0131\3\2\2\2;\u0133\3\2\2\2=\u0135\3")
        buf.write("\2\2\2?\u0137\3\2\2\2A\u0139\3\2\2\2C\u013c\3\2\2\2E\u013f")
        buf.write("\3\2\2\2G\u0142\3\2\2\2I\u0145\3\2\2\2K\u0147\3\2\2\2")
        buf.write("M\u014a\3\2\2\2O\u014c\3\2\2\2Q\u014f\3\2\2\2S\u0152\3")
        buf.write("\2\2\2U\u0154\3\2\2\2W\u0156\3\2\2\2Y\u0158\3\2\2\2[\u015a")
        buf.write("\3\2\2\2]\u015c\3\2\2\2_\u015e\3\2\2\2a\u0160\3\2\2\2")
        buf.write("c\u0162\3\2\2\2e\u0164\3\2\2\2g\u0166\3\2\2\2i\u0168\3")
        buf.write("\2\2\2k\u016a\3\2\2\2m\u016c\3\2\2\2o\u0170\3\2\2\2q\u017b")
        buf.write("\3\2\2\2s\u0181\3\2\2\2u\u0184\3\2\2\2w\u0187\3\2\2\2")
        buf.write("yz\7\61\2\2z{\7,\2\2{\177\3\2\2\2|~\13\2\2\2}|\3\2\2\2")
        buf.write("~\u0081\3\2\2\2\177\u0080\3\2\2\2\177}\3\2\2\2\u0080\u0082")
        buf.write("\3\2\2\2\u0081\177\3\2\2\2\u0082\u0083\7,\2\2\u0083\u0084")
        buf.write("\7\61\2\2\u0084\u0085\3\2\2\2\u0085\u0086\b\2\2\2\u0086")
        buf.write("\4\3\2\2\2\u0087\u0088\7\61\2\2\u0088\u0089\7\61\2\2\u0089")
        buf.write("\u008d\3\2\2\2\u008a\u008c\n\2\2\2\u008b\u008a\3\2\2\2")
        buf.write("\u008c\u008f\3\2\2\2\u008d\u008b\3\2\2\2\u008d\u008e\3")
        buf.write("\2\2\2\u008e\u0090\3\2\2\2\u008f\u008d\3\2\2\2\u0090\u0091")
        buf.write("\b\3\2\2\u0091\6\3\2\2\2\u0092\u00a1\t\3\2\2\u0093\u0095")
        buf.write("\t\4\2\2\u0094\u0093\3\2\2\2\u0095\u0098\3\2\2\2\u0096")
        buf.write("\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0099\3\2\2\2")
        buf.write("\u0098\u0096\3\2\2\2\u0099\u009b\7a\2\2\u009a\u009c\t")
        buf.write("\4\2\2\u009b\u009a\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u009b")
        buf.write("\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u00a0\3\2\2\2\u009f")
        buf.write("\u0096\3\2\2\2\u00a0\u00a3\3\2\2\2\u00a1\u009f\3\2\2\2")
        buf.write("\u00a1\u00a2\3\2\2\2\u00a2\u00ad\3\2\2\2\u00a3\u00a1\3")
        buf.write("\2\2\2\u00a4\u00ad\7\62\2\2\u00a5\u00a9\t\3\2\2\u00a6")
        buf.write("\u00a8\t\4\2\2\u00a7\u00a6\3\2\2\2\u00a8\u00ab\3\2\2\2")
        buf.write("\u00a9\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ad\3")
        buf.write("\2\2\2\u00ab\u00a9\3\2\2\2\u00ac\u0092\3\2\2\2\u00ac\u00a4")
        buf.write("\3\2\2\2\u00ac\u00a5\3\2\2\2\u00ad\b\3\2\2\2\u00ae\u00b1")
        buf.write("\5)\25\2\u00af\u00b1\5\r\7\2\u00b0\u00ae\3\2\2\2\u00b0")
        buf.write("\u00af\3\2\2\2\u00b1\n\3\2\2\2\u00b2\u00b3\7c\2\2\u00b3")
        buf.write("\u00b4\7w\2\2\u00b4\u00b5\7v\2\2\u00b5\u00b6\7q\2\2\u00b6")
        buf.write("\f\3\2\2\2\u00b7\u00b8\7h\2\2\u00b8\u00b9\7c\2\2\u00b9")
        buf.write("\u00ba\7n\2\2\u00ba\u00bb\7u\2\2\u00bb\u00bc\7g\2\2\u00bc")
        buf.write("\16\3\2\2\2\u00bd\u00be\7k\2\2\u00be\u00bf\7p\2\2\u00bf")
        buf.write("\u00c0\7v\2\2\u00c0\u00c1\7g\2\2\u00c1\u00c2\7i\2\2\u00c2")
        buf.write("\u00c3\7g\2\2\u00c3\u00c4\7t\2\2\u00c4\20\3\2\2\2\u00c5")
        buf.write("\u00c6\7x\2\2\u00c6\u00c7\7q\2\2\u00c7\u00c8\7k\2\2\u00c8")
        buf.write("\u00c9\7f\2\2\u00c9\22\3\2\2\2\u00ca\u00cb\7c\2\2\u00cb")
        buf.write("\u00cc\7t\2\2\u00cc\u00cd\7t\2\2\u00cd\u00ce\7c\2\2\u00ce")
        buf.write("\u00cf\7{\2\2\u00cf\24\3\2\2\2\u00d0\u00d1\7d\2\2\u00d1")
        buf.write("\u00d2\7t\2\2\u00d2\u00d3\7g\2\2\u00d3\u00d4\7c\2\2\u00d4")
        buf.write("\u00d5\7m\2\2\u00d5\26\3\2\2\2\u00d6\u00d7\7h\2\2\u00d7")
        buf.write("\u00d8\7n\2\2\u00d8\u00d9\7q\2\2\u00d9\u00da\7c\2\2\u00da")
        buf.write("\u00db\7v\2\2\u00db\30\3\2\2\2\u00dc\u00dd\7t\2\2\u00dd")
        buf.write("\u00de\7g\2\2\u00de\u00df\7v\2\2\u00df\u00e0\7w\2\2\u00e0")
        buf.write("\u00e1\7t\2\2\u00e1\u00e2\7p\2\2\u00e2\32\3\2\2\2\u00e3")
        buf.write("\u00e4\7q\2\2\u00e4\u00e5\7w\2\2\u00e5\u00e6\7v\2\2\u00e6")
        buf.write("\34\3\2\2\2\u00e7\u00e8\7d\2\2\u00e8\u00e9\7q\2\2\u00e9")
        buf.write("\u00ea\7q\2\2\u00ea\u00eb\7n\2\2\u00eb\u00ec\7g\2\2\u00ec")
        buf.write("\u00ed\7c\2\2\u00ed\u00ee\7p\2\2\u00ee\36\3\2\2\2\u00ef")
        buf.write("\u00f0\7h\2\2\u00f0\u00f1\7q\2\2\u00f1\u00f2\7t\2\2\u00f2")
        buf.write(" \3\2\2\2\u00f3\u00f4\7u\2\2\u00f4\u00f5\7v\2\2\u00f5")
        buf.write("\u00f6\7t\2\2\u00f6\u00f7\7k\2\2\u00f7\u00f8\7p\2\2\u00f8")
        buf.write("\u00f9\7i\2\2\u00f9\"\3\2\2\2\u00fa\u00fb\7e\2\2\u00fb")
        buf.write("\u00fc\7q\2\2\u00fc\u00fd\7p\2\2\u00fd\u00fe\7v\2\2\u00fe")
        buf.write("\u00ff\7k\2\2\u00ff\u0100\7p\2\2\u0100\u0101\7w\2\2\u0101")
        buf.write("\u0102\7g\2\2\u0102$\3\2\2\2\u0103\u0104\7f\2\2\u0104")
        buf.write("\u0105\7q\2\2\u0105&\3\2\2\2\u0106\u0107\7h\2\2\u0107")
        buf.write("\u0108\7w\2\2\u0108\u0109\7p\2\2\u0109\u010a\7e\2\2\u010a")
        buf.write("\u010b\7v\2\2\u010b\u010c\7k\2\2\u010c\u010d\7q\2\2\u010d")
        buf.write("\u010e\7p\2\2\u010e(\3\2\2\2\u010f\u0110\7v\2\2\u0110")
        buf.write("\u0111\7t\2\2\u0111\u0112\7w\2\2\u0112\u0113\7g\2\2\u0113")
        buf.write("*\3\2\2\2\u0114\u0115\7q\2\2\u0115\u0116\7h\2\2\u0116")
        buf.write(",\3\2\2\2\u0117\u0118\7g\2\2\u0118\u0119\7n\2\2\u0119")
        buf.write("\u011a\7u\2\2\u011a\u011b\7g\2\2\u011b.\3\2\2\2\u011c")
        buf.write("\u011d\7k\2\2\u011d\u011e\7h\2\2\u011e\60\3\2\2\2\u011f")
        buf.write("\u0120\7y\2\2\u0120\u0121\7j\2\2\u0121\u0122\7k\2\2\u0122")
        buf.write("\u0123\7n\2\2\u0123\u0124\7g\2\2\u0124\62\3\2\2\2\u0125")
        buf.write("\u0126\7k\2\2\u0126\u0127\7p\2\2\u0127\u0128\7j\2\2\u0128")
        buf.write("\u0129\7g\2\2\u0129\u012a\7t\2\2\u012a\u012b\7k\2\2\u012b")
        buf.write("\u012c\7v\2\2\u012c\64\3\2\2\2\u012d\u012e\7-\2\2\u012e")
        buf.write("\66\3\2\2\2\u012f\u0130\7/\2\2\u01308\3\2\2\2\u0131\u0132")
        buf.write("\7,\2\2\u0132:\3\2\2\2\u0133\u0134\7\61\2\2\u0134<\3\2")
        buf.write("\2\2\u0135\u0136\7\'\2\2\u0136>\3\2\2\2\u0137\u0138\7")
        buf.write("#\2\2\u0138@\3\2\2\2\u0139\u013a\7(\2\2\u013a\u013b\7")
        buf.write("(\2\2\u013bB\3\2\2\2\u013c\u013d\7~\2\2\u013d\u013e\7")
        buf.write("~\2\2\u013eD\3\2\2\2\u013f\u0140\7?\2\2\u0140\u0141\7")
        buf.write("?\2\2\u0141F\3\2\2\2\u0142\u0143\7#\2\2\u0143\u0144\7")
        buf.write("?\2\2\u0144H\3\2\2\2\u0145\u0146\7>\2\2\u0146J\3\2\2\2")
        buf.write("\u0147\u0148\7>\2\2\u0148\u0149\7?\2\2\u0149L\3\2\2\2")
        buf.write("\u014a\u014b\7@\2\2\u014bN\3\2\2\2\u014c\u014d\7@\2\2")
        buf.write("\u014d\u014e\7?\2\2\u014eP\3\2\2\2\u014f\u0150\7<\2\2")
        buf.write("\u0150\u0151\7<\2\2\u0151R\3\2\2\2\u0152\u0153\7*\2\2")
        buf.write("\u0153T\3\2\2\2\u0154\u0155\7+\2\2\u0155V\3\2\2\2\u0156")
        buf.write("\u0157\7]\2\2\u0157X\3\2\2\2\u0158\u0159\7_\2\2\u0159")
        buf.write("Z\3\2\2\2\u015a\u015b\7\60\2\2\u015b\\\3\2\2\2\u015c\u015d")
        buf.write("\7.\2\2\u015d^\3\2\2\2\u015e\u015f\7=\2\2\u015f`\3\2\2")
        buf.write("\2\u0160\u0161\7<\2\2\u0161b\3\2\2\2\u0162\u0163\7}\2")
        buf.write("\2\u0163d\3\2\2\2\u0164\u0165\7\177\2\2\u0165f\3\2\2\2")
        buf.write("\u0166\u0167\7?\2\2\u0167h\3\2\2\2\u0168\u0169\t\5\2\2")
        buf.write("\u0169j\3\2\2\2\u016a\u016b\7a\2\2\u016bl\3\2\2\2\u016c")
        buf.write("\u016d\t\4\2\2\u016dn\3\2\2\2\u016e\u0171\5k\66\2\u016f")
        buf.write("\u0171\5i\65\2\u0170\u016e\3\2\2\2\u0170\u016f\3\2\2\2")
        buf.write("\u0171\u0177\3\2\2\2\u0172\u0176\5k\66\2\u0173\u0176\5")
        buf.write("i\65\2\u0174\u0176\5m\67\2\u0175\u0172\3\2\2\2\u0175\u0173")
        buf.write("\3\2\2\2\u0175\u0174\3\2\2\2\u0176\u0179\3\2\2\2\u0177")
        buf.write("\u0175\3\2\2\2\u0177\u0178\3\2\2\2\u0178p\3\2\2\2\u0179")
        buf.write("\u0177\3\2\2\2\u017a\u017c\t\6\2\2\u017b\u017a\3\2\2\2")
        buf.write("\u017c\u017d\3\2\2\2\u017d\u017b\3\2\2\2\u017d\u017e\3")
        buf.write("\2\2\2\u017e\u017f\3\2\2\2\u017f\u0180\b9\2\2\u0180r\3")
        buf.write("\2\2\2\u0181\u0182\13\2\2\2\u0182\u0183\b:\3\2\u0183t")
        buf.write("\3\2\2\2\u0184\u0185\13\2\2\2\u0185\u0186\b;\4\2\u0186")
        buf.write("v\3\2\2\2\u0187\u0188\13\2\2\2\u0188\u0189\b<\5\2\u0189")
        buf.write("x\3\2\2\2\17\2\177\u008d\u0096\u009d\u00a1\u00a9\u00ac")
        buf.write("\u00b0\u0170\u0175\u0177\u017d\6\b\2\2\3:\2\3;\3\3<\4")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT_C = 1
    COMMENT_CPLUS = 2
    INTLIT = 3
    BOOLLIT = 4
    AUTO = 5
    FALSE = 6
    INTERGER = 7
    VOID = 8
    ARRAY = 9
    BREAK = 10
    FLOAT = 11
    RETURN = 12
    OUT = 13
    BOOLEAN = 14
    FOR = 15
    STRING = 16
    CONTINUE = 17
    DO = 18
    FUNCTION = 19
    TRUE = 20
    OF = 21
    ELSE = 22
    IF = 23
    WHILE = 24
    INHERIT = 25
    ADDOP = 26
    SUBOP = 27
    MULOP = 28
    DIV = 29
    MOD = 30
    NOT = 31
    AND = 32
    OR = 33
    EQUAL = 34
    NOT_EQUAL = 35
    LESS = 36
    LESS_OR_EQUAL = 37
    GREATER = 38
    GREATER_OR_EQUAL = 39
    DOUBLE_COLON = 40
    LB = 41
    RB = 42
    LSB = 43
    RSB = 44
    DOT = 45
    COMMA = 46
    SEMICOLON = 47
    COLON = 48
    LP = 49
    RP = 50
    ASSIGN = 51
    ID = 52
    WS = 53
    ERROR_CHAR = 54
    UNCLOSE_STRING = 55
    ILLEGAL_ESCAPE = 56

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
            "COMMENT_C", "COMMENT_CPLUS", "INTLIT", "BOOLLIT", "AUTO", "FALSE", 
            "INTERGER", "VOID", "ARRAY", "BREAK", "FLOAT", "RETURN", "OUT", 
            "BOOLEAN", "FOR", "STRING", "CONTINUE", "DO", "FUNCTION", "TRUE", 
            "OF", "ELSE", "IF", "WHILE", "INHERIT", "ADDOP", "SUBOP", "MULOP", 
            "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", "LESS", 
            "LESS_OR_EQUAL", "GREATER", "GREATER_OR_EQUAL", "DOUBLE_COLON", 
            "LB", "RB", "LSB", "RSB", "DOT", "COMMA", "SEMICOLON", "COLON", 
            "LP", "RP", "ASSIGN", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "COMMENT_C", "COMMENT_CPLUS", "INTLIT", "BOOLLIT", "AUTO", 
                  "FALSE", "INTERGER", "VOID", "ARRAY", "BREAK", "FLOAT", 
                  "RETURN", "OUT", "BOOLEAN", "FOR", "STRING", "CONTINUE", 
                  "DO", "FUNCTION", "TRUE", "OF", "ELSE", "IF", "WHILE", 
                  "INHERIT", "ADDOP", "SUBOP", "MULOP", "DIV", "MOD", "NOT", 
                  "AND", "OR", "EQUAL", "NOT_EQUAL", "LESS", "LESS_OR_EQUAL", 
                  "GREATER", "GREATER_OR_EQUAL", "DOUBLE_COLON", "LB", "RB", 
                  "LSB", "RSB", "DOT", "COMMA", "SEMICOLON", "COLON", "LP", 
                  "RP", "ASSIGN", "LETTER", "UNDERSCORE", "DIGIT", "ID", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[56] = self.ERROR_CHAR_action 
            actions[57] = self.UNCLOSE_STRING_action 
            actions[58] = self.ILLEGAL_ESCAPE_action 
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
     



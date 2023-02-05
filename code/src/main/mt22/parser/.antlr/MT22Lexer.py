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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2=")
        buf.write("\u01fe\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\7\3\u009c\n\3\f\3\16\3\u009f\13")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4\u00aa\n\4\f")
        buf.write("\4\16\4\u00ad\13\4\3\4\3\4\3\5\3\5\7\5\u00b3\n\5\f\5\16")
        buf.write("\5\u00b6\13\5\3\5\3\5\6\5\u00ba\n\5\r\5\16\5\u00bb\7\5")
        buf.write("\u00be\n\5\f\5\16\5\u00c1\13\5\3\5\3\5\3\5\7\5\u00c6\n")
        buf.write("\5\f\5\16\5\u00c9\13\5\5\5\u00cb\n\5\3\6\3\6\5\6\u00cf")
        buf.write("\n\6\3\6\6\6\u00d2\n\6\r\6\16\6\u00d3\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\t\3\t\3\t\7\t\u00de\n\t\f\t\16\t\u00e1\13\t\3\t")
        buf.write("\5\t\u00e4\n\t\3\t\3\t\6\t\u00e8\n\t\r\t\16\t\u00e9\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\6\t\u00f2\n\t\r\t\16\t\u00f3\3")
        buf.write("\t\3\t\5\t\u00f8\n\t\3\n\3\n\3\n\3\13\3\13\5\13\u00ff")
        buf.write("\n\13\3\f\3\f\7\f\u0103\n\f\f\f\16\f\u0106\13\f\3\f\3")
        buf.write("\f\3\f\3\r\3\r\5\r\u010d\n\r\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\5\17\u0115\n\17\3\20\3\20\3\20\3\20\3\20\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3!\3!\3\"\3\"\3")
        buf.write("\"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3&")
        buf.write("\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-")
        buf.write("\3-\3.\3.\3.\3/\3/\3\60\3\60\3\60\3\61\3\61\3\62\3\62")
        buf.write("\3\62\3\63\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67")
        buf.write("\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?")
        buf.write("\3@\3@\3A\3A\3B\3B\5B\u01d5\nB\3B\3B\3B\7B\u01da\nB\f")
        buf.write("B\16B\u01dd\13B\3C\6C\u01e0\nC\rC\16C\u01e1\3C\3C\3D\3")
        buf.write("D\3D\3E\3E\7E\u01eb\nE\fE\16E\u01ee\13E\3E\5E\u01f1\n")
        buf.write("E\3E\3E\3F\3F\7F\u01f7\nF\fF\16F\u01fa\13F\3F\3F\3F\3")
        buf.write("\u009d\2G\3\3\5\4\7\5\t\2\13\2\r\2\17\6\21\2\23\7\25\b")
        buf.write("\27\t\31\2\33\2\35\2\37\n!\13#\f%\r\'\16)\17+\20-\21/")
        buf.write("\22\61\23\63\24\65\25\67\269\27;\30=\31?\32A\33C\34E\35")
        buf.write("G\36I\37K M!O\"Q#S$U%W&Y\'[(])_*a+c,e-g.i/k\60m\61o\62")
        buf.write("q\63s\64u\65w\66y\67{8}\2\177\2\u0081\2\u00839\u0085:")
        buf.write("\u0087;\u0089<\u008b=\3\2\r\4\2\f\f\17\17\3\2\63;\3\2")
        buf.write("\62;\4\2GGgg\4\2--//\7\2\n\f\16\17$$))^^\n\2$$))^^ddh")
        buf.write("hppttvv\3\2^^\4\2C\\c|\5\2\n\f\16\17\"\"\7\3\n\f\16\17")
        buf.write("$$))^^\2\u020f\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3")
        buf.write("\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k")
        buf.write("\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2")
        buf.write("u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2\u0083\3\2")
        buf.write("\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2")
        buf.write("\u008b\3\2\2\2\3\u008d\3\2\2\2\5\u0097\3\2\2\2\7\u00a5")
        buf.write("\3\2\2\2\t\u00ca\3\2\2\2\13\u00cc\3\2\2\2\r\u00d5\3\2")
        buf.write("\2\2\17\u00d7\3\2\2\2\21\u00f7\3\2\2\2\23\u00f9\3\2\2")
        buf.write("\2\25\u00fe\3\2\2\2\27\u0100\3\2\2\2\31\u010c\3\2\2\2")
        buf.write("\33\u010e\3\2\2\2\35\u0114\3\2\2\2\37\u0116\3\2\2\2!\u011b")
        buf.write("\3\2\2\2#\u0121\3\2\2\2%\u0129\3\2\2\2\'\u012e\3\2\2\2")
        buf.write(")\u0134\3\2\2\2+\u013a\3\2\2\2-\u0140\3\2\2\2/\u0147\3")
        buf.write("\2\2\2\61\u014b\3\2\2\2\63\u0153\3\2\2\2\65\u0157\3\2")
        buf.write("\2\2\67\u015e\3\2\2\29\u0167\3\2\2\2;\u016a\3\2\2\2=\u0173")
        buf.write("\3\2\2\2?\u0178\3\2\2\2A\u017b\3\2\2\2C\u0180\3\2\2\2")
        buf.write("E\u0183\3\2\2\2G\u0189\3\2\2\2I\u0191\3\2\2\2K\u0193\3")
        buf.write("\2\2\2M\u0195\3\2\2\2O\u0197\3\2\2\2Q\u0199\3\2\2\2S\u019b")
        buf.write("\3\2\2\2U\u019d\3\2\2\2W\u01a0\3\2\2\2Y\u01a3\3\2\2\2")
        buf.write("[\u01a6\3\2\2\2]\u01a9\3\2\2\2_\u01ab\3\2\2\2a\u01ae\3")
        buf.write("\2\2\2c\u01b0\3\2\2\2e\u01b3\3\2\2\2g\u01b6\3\2\2\2i\u01b8")
        buf.write("\3\2\2\2k\u01ba\3\2\2\2m\u01bc\3\2\2\2o\u01be\3\2\2\2")
        buf.write("q\u01c0\3\2\2\2s\u01c2\3\2\2\2u\u01c4\3\2\2\2w\u01c6\3")
        buf.write("\2\2\2y\u01c8\3\2\2\2{\u01ca\3\2\2\2}\u01cc\3\2\2\2\177")
        buf.write("\u01ce\3\2\2\2\u0081\u01d0\3\2\2\2\u0083\u01d4\3\2\2\2")
        buf.write("\u0085\u01df\3\2\2\2\u0087\u01e5\3\2\2\2\u0089\u01e8\3")
        buf.write("\2\2\2\u008b\u01f4\3\2\2\2\u008d\u008e\7h\2\2\u008e\u008f")
        buf.write("\7w\2\2\u008f\u0090\7p\2\2\u0090\u0091\7e\2\2\u0091\u0092")
        buf.write("\7a\2\2\u0092\u0093\7f\2\2\u0093\u0094\7g\2\2\u0094\u0095")
        buf.write("\7e\2\2\u0095\u0096\7n\2\2\u0096\4\3\2\2\2\u0097\u0098")
        buf.write("\7\61\2\2\u0098\u0099\7,\2\2\u0099\u009d\3\2\2\2\u009a")
        buf.write("\u009c\13\2\2\2\u009b\u009a\3\2\2\2\u009c\u009f\3\2\2")
        buf.write("\2\u009d\u009e\3\2\2\2\u009d\u009b\3\2\2\2\u009e\u00a0")
        buf.write("\3\2\2\2\u009f\u009d\3\2\2\2\u00a0\u00a1\7,\2\2\u00a1")
        buf.write("\u00a2\7\61\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a4\b\3\2")
        buf.write("\2\u00a4\6\3\2\2\2\u00a5\u00a6\7\61\2\2\u00a6\u00a7\7")
        buf.write("\61\2\2\u00a7\u00ab\3\2\2\2\u00a8\u00aa\n\2\2\2\u00a9")
        buf.write("\u00a8\3\2\2\2\u00aa\u00ad\3\2\2\2\u00ab\u00a9\3\2\2\2")
        buf.write("\u00ab\u00ac\3\2\2\2\u00ac\u00ae\3\2\2\2\u00ad\u00ab\3")
        buf.write("\2\2\2\u00ae\u00af\b\4\2\2\u00af\b\3\2\2\2\u00b0\u00bf")
        buf.write("\t\3\2\2\u00b1\u00b3\t\4\2\2\u00b2\u00b1\3\2\2\2\u00b3")
        buf.write("\u00b6\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2")
        buf.write("\u00b5\u00b7\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b7\u00b9\7")
        buf.write("a\2\2\u00b8\u00ba\t\4\2\2\u00b9\u00b8\3\2\2\2\u00ba\u00bb")
        buf.write("\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc")
        buf.write("\u00be\3\2\2\2\u00bd\u00b4\3\2\2\2\u00be\u00c1\3\2\2\2")
        buf.write("\u00bf\u00bd\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00cb\3")
        buf.write("\2\2\2\u00c1\u00bf\3\2\2\2\u00c2\u00cb\7\62\2\2\u00c3")
        buf.write("\u00c7\t\3\2\2\u00c4\u00c6\t\4\2\2\u00c5\u00c4\3\2\2\2")
        buf.write("\u00c6\u00c9\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c8\3")
        buf.write("\2\2\2\u00c8\u00cb\3\2\2\2\u00c9\u00c7\3\2\2\2\u00ca\u00b0")
        buf.write("\3\2\2\2\u00ca\u00c2\3\2\2\2\u00ca\u00c3\3\2\2\2\u00cb")
        buf.write("\n\3\2\2\2\u00cc\u00ce\t\5\2\2\u00cd\u00cf\5\r\7\2\u00ce")
        buf.write("\u00cd\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d1\3\2\2\2")
        buf.write("\u00d0\u00d2\5\u0081A\2\u00d1\u00d0\3\2\2\2\u00d2\u00d3")
        buf.write("\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4")
        buf.write("\f\3\2\2\2\u00d5\u00d6\t\6\2\2\u00d6\16\3\2\2\2\u00d7")
        buf.write("\u00d8\5\t\5\2\u00d8\u00d9\b\b\3\2\u00d9\20\3\2\2\2\u00da")
        buf.write("\u00db\5\t\5\2\u00db\u00df\7\60\2\2\u00dc\u00de\5\u0081")
        buf.write("A\2\u00dd\u00dc\3\2\2\2\u00de\u00e1\3\2\2\2\u00df\u00dd")
        buf.write("\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00f8\3\2\2\2\u00e1")
        buf.write("\u00df\3\2\2\2\u00e2\u00e4\5\t\5\2\u00e3\u00e2\3\2\2\2")
        buf.write("\u00e3\u00e4\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e7\7")
        buf.write("\60\2\2\u00e6\u00e8\5\u0081A\2\u00e7\u00e6\3\2\2\2\u00e8")
        buf.write("\u00e9\3\2\2\2\u00e9\u00e7\3\2\2\2\u00e9\u00ea\3\2\2\2")
        buf.write("\u00ea\u00f8\3\2\2\2\u00eb\u00ec\5\t\5\2\u00ec\u00ed\5")
        buf.write("\13\6\2\u00ed\u00f8\3\2\2\2\u00ee\u00ef\5\t\5\2\u00ef")
        buf.write("\u00f1\7\60\2\2\u00f0\u00f2\5\u0081A\2\u00f1\u00f0\3\2")
        buf.write("\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f3\u00f4")
        buf.write("\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f6\5\13\6\2\u00f6")
        buf.write("\u00f8\3\2\2\2\u00f7\u00da\3\2\2\2\u00f7\u00e3\3\2\2\2")
        buf.write("\u00f7\u00eb\3\2\2\2\u00f7\u00ee\3\2\2\2\u00f8\22\3\2")
        buf.write("\2\2\u00f9\u00fa\5\21\t\2\u00fa\u00fb\b\n\4\2\u00fb\24")
        buf.write("\3\2\2\2\u00fc\u00ff\5=\37\2\u00fd\u00ff\5!\21\2\u00fe")
        buf.write("\u00fc\3\2\2\2\u00fe\u00fd\3\2\2\2\u00ff\26\3\2\2\2\u0100")
        buf.write("\u0104\7$\2\2\u0101\u0103\5\31\r\2\u0102\u0101\3\2\2\2")
        buf.write("\u0103\u0106\3\2\2\2\u0104\u0102\3\2\2\2\u0104\u0105\3")
        buf.write("\2\2\2\u0105\u0107\3\2\2\2\u0106\u0104\3\2\2\2\u0107\u0108")
        buf.write("\7$\2\2\u0108\u0109\b\f\5\2\u0109\30\3\2\2\2\u010a\u010d")
        buf.write("\n\7\2\2\u010b\u010d\5\33\16\2\u010c\u010a\3\2\2\2\u010c")
        buf.write("\u010b\3\2\2\2\u010d\32\3\2\2\2\u010e\u010f\7^\2\2\u010f")
        buf.write("\u0110\t\b\2\2\u0110\34\3\2\2\2\u0111\u0112\7^\2\2\u0112")
        buf.write("\u0115\n\b\2\2\u0113\u0115\n\t\2\2\u0114\u0111\3\2\2\2")
        buf.write("\u0114\u0113\3\2\2\2\u0115\36\3\2\2\2\u0116\u0117\7c\2")
        buf.write("\2\u0117\u0118\7w\2\2\u0118\u0119\7v\2\2\u0119\u011a\7")
        buf.write("q\2\2\u011a \3\2\2\2\u011b\u011c\7h\2\2\u011c\u011d\7")
        buf.write("c\2\2\u011d\u011e\7n\2\2\u011e\u011f\7u\2\2\u011f\u0120")
        buf.write("\7g\2\2\u0120\"\3\2\2\2\u0121\u0122\7k\2\2\u0122\u0123")
        buf.write("\7p\2\2\u0123\u0124\7v\2\2\u0124\u0125\7g\2\2\u0125\u0126")
        buf.write("\7i\2\2\u0126\u0127\7g\2\2\u0127\u0128\7t\2\2\u0128$\3")
        buf.write("\2\2\2\u0129\u012a\7x\2\2\u012a\u012b\7q\2\2\u012b\u012c")
        buf.write("\7k\2\2\u012c\u012d\7f\2\2\u012d&\3\2\2\2\u012e\u012f")
        buf.write("\7c\2\2\u012f\u0130\7t\2\2\u0130\u0131\7t\2\2\u0131\u0132")
        buf.write("\7c\2\2\u0132\u0133\7{\2\2\u0133(\3\2\2\2\u0134\u0135")
        buf.write("\7d\2\2\u0135\u0136\7t\2\2\u0136\u0137\7g\2\2\u0137\u0138")
        buf.write("\7c\2\2\u0138\u0139\7m\2\2\u0139*\3\2\2\2\u013a\u013b")
        buf.write("\7h\2\2\u013b\u013c\7n\2\2\u013c\u013d\7q\2\2\u013d\u013e")
        buf.write("\7c\2\2\u013e\u013f\7v\2\2\u013f,\3\2\2\2\u0140\u0141")
        buf.write("\7t\2\2\u0141\u0142\7g\2\2\u0142\u0143\7v\2\2\u0143\u0144")
        buf.write("\7w\2\2\u0144\u0145\7t\2\2\u0145\u0146\7p\2\2\u0146.\3")
        buf.write("\2\2\2\u0147\u0148\7q\2\2\u0148\u0149\7w\2\2\u0149\u014a")
        buf.write("\7v\2\2\u014a\60\3\2\2\2\u014b\u014c\7d\2\2\u014c\u014d")
        buf.write("\7q\2\2\u014d\u014e\7q\2\2\u014e\u014f\7n\2\2\u014f\u0150")
        buf.write("\7g\2\2\u0150\u0151\7c\2\2\u0151\u0152\7p\2\2\u0152\62")
        buf.write("\3\2\2\2\u0153\u0154\7h\2\2\u0154\u0155\7q\2\2\u0155\u0156")
        buf.write("\7t\2\2\u0156\64\3\2\2\2\u0157\u0158\7u\2\2\u0158\u0159")
        buf.write("\7v\2\2\u0159\u015a\7t\2\2\u015a\u015b\7k\2\2\u015b\u015c")
        buf.write("\7p\2\2\u015c\u015d\7i\2\2\u015d\66\3\2\2\2\u015e\u015f")
        buf.write("\7e\2\2\u015f\u0160\7q\2\2\u0160\u0161\7p\2\2\u0161\u0162")
        buf.write("\7v\2\2\u0162\u0163\7k\2\2\u0163\u0164\7p\2\2\u0164\u0165")
        buf.write("\7w\2\2\u0165\u0166\7g\2\2\u01668\3\2\2\2\u0167\u0168")
        buf.write("\7f\2\2\u0168\u0169\7q\2\2\u0169:\3\2\2\2\u016a\u016b")
        buf.write("\7h\2\2\u016b\u016c\7w\2\2\u016c\u016d\7p\2\2\u016d\u016e")
        buf.write("\7e\2\2\u016e\u016f\7v\2\2\u016f\u0170\7k\2\2\u0170\u0171")
        buf.write("\7q\2\2\u0171\u0172\7p\2\2\u0172<\3\2\2\2\u0173\u0174")
        buf.write("\7v\2\2\u0174\u0175\7t\2\2\u0175\u0176\7w\2\2\u0176\u0177")
        buf.write("\7g\2\2\u0177>\3\2\2\2\u0178\u0179\7q\2\2\u0179\u017a")
        buf.write("\7h\2\2\u017a@\3\2\2\2\u017b\u017c\7g\2\2\u017c\u017d")
        buf.write("\7n\2\2\u017d\u017e\7u\2\2\u017e\u017f\7g\2\2\u017fB\3")
        buf.write("\2\2\2\u0180\u0181\7k\2\2\u0181\u0182\7h\2\2\u0182D\3")
        buf.write("\2\2\2\u0183\u0184\7y\2\2\u0184\u0185\7j\2\2\u0185\u0186")
        buf.write("\7k\2\2\u0186\u0187\7n\2\2\u0187\u0188\7g\2\2\u0188F\3")
        buf.write("\2\2\2\u0189\u018a\7k\2\2\u018a\u018b\7p\2\2\u018b\u018c")
        buf.write("\7j\2\2\u018c\u018d\7g\2\2\u018d\u018e\7t\2\2\u018e\u018f")
        buf.write("\7k\2\2\u018f\u0190\7v\2\2\u0190H\3\2\2\2\u0191\u0192")
        buf.write("\7-\2\2\u0192J\3\2\2\2\u0193\u0194\7/\2\2\u0194L\3\2\2")
        buf.write("\2\u0195\u0196\7,\2\2\u0196N\3\2\2\2\u0197\u0198\7\61")
        buf.write("\2\2\u0198P\3\2\2\2\u0199\u019a\7\'\2\2\u019aR\3\2\2\2")
        buf.write("\u019b\u019c\7#\2\2\u019cT\3\2\2\2\u019d\u019e\7(\2\2")
        buf.write("\u019e\u019f\7(\2\2\u019fV\3\2\2\2\u01a0\u01a1\7~\2\2")
        buf.write("\u01a1\u01a2\7~\2\2\u01a2X\3\2\2\2\u01a3\u01a4\7?\2\2")
        buf.write("\u01a4\u01a5\7?\2\2\u01a5Z\3\2\2\2\u01a6\u01a7\7#\2\2")
        buf.write("\u01a7\u01a8\7?\2\2\u01a8\\\3\2\2\2\u01a9\u01aa\7>\2\2")
        buf.write("\u01aa^\3\2\2\2\u01ab\u01ac\7>\2\2\u01ac\u01ad\7?\2\2")
        buf.write("\u01ad`\3\2\2\2\u01ae\u01af\7@\2\2\u01afb\3\2\2\2\u01b0")
        buf.write("\u01b1\7@\2\2\u01b1\u01b2\7?\2\2\u01b2d\3\2\2\2\u01b3")
        buf.write("\u01b4\7<\2\2\u01b4\u01b5\7<\2\2\u01b5f\3\2\2\2\u01b6")
        buf.write("\u01b7\7*\2\2\u01b7h\3\2\2\2\u01b8\u01b9\7+\2\2\u01b9")
        buf.write("j\3\2\2\2\u01ba\u01bb\7]\2\2\u01bbl\3\2\2\2\u01bc\u01bd")
        buf.write("\7_\2\2\u01bdn\3\2\2\2\u01be\u01bf\7\60\2\2\u01bfp\3\2")
        buf.write("\2\2\u01c0\u01c1\7.\2\2\u01c1r\3\2\2\2\u01c2\u01c3\7=")
        buf.write("\2\2\u01c3t\3\2\2\2\u01c4\u01c5\7<\2\2\u01c5v\3\2\2\2")
        buf.write("\u01c6\u01c7\7}\2\2\u01c7x\3\2\2\2\u01c8\u01c9\7\177\2")
        buf.write("\2\u01c9z\3\2\2\2\u01ca\u01cb\7?\2\2\u01cb|\3\2\2\2\u01cc")
        buf.write("\u01cd\t\n\2\2\u01cd~\3\2\2\2\u01ce\u01cf\7a\2\2\u01cf")
        buf.write("\u0080\3\2\2\2\u01d0\u01d1\t\4\2\2\u01d1\u0082\3\2\2\2")
        buf.write("\u01d2\u01d5\5\177@\2\u01d3\u01d5\5}?\2\u01d4\u01d2\3")
        buf.write("\2\2\2\u01d4\u01d3\3\2\2\2\u01d5\u01db\3\2\2\2\u01d6\u01da")
        buf.write("\5\177@\2\u01d7\u01da\5}?\2\u01d8\u01da\5\u0081A\2\u01d9")
        buf.write("\u01d6\3\2\2\2\u01d9\u01d7\3\2\2\2\u01d9\u01d8\3\2\2\2")
        buf.write("\u01da\u01dd\3\2\2\2\u01db\u01d9\3\2\2\2\u01db\u01dc\3")
        buf.write("\2\2\2\u01dc\u0084\3\2\2\2\u01dd\u01db\3\2\2\2\u01de\u01e0")
        buf.write("\t\13\2\2\u01df\u01de\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1")
        buf.write("\u01df\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e3\3\2\2\2")
        buf.write("\u01e3\u01e4\bC\2\2\u01e4\u0086\3\2\2\2\u01e5\u01e6\13")
        buf.write("\2\2\2\u01e6\u01e7\bD\6\2\u01e7\u0088\3\2\2\2\u01e8\u01ec")
        buf.write("\7$\2\2\u01e9\u01eb\5\31\r\2\u01ea\u01e9\3\2\2\2\u01eb")
        buf.write("\u01ee\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ec\u01ed\3\2\2\2")
        buf.write("\u01ed\u01f0\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ef\u01f1\t")
        buf.write("\f\2\2\u01f0\u01ef\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f3")
        buf.write("\bE\7\2\u01f3\u008a\3\2\2\2\u01f4\u01f8\7$\2\2\u01f5\u01f7")
        buf.write("\5\31\r\2\u01f6\u01f5\3\2\2\2\u01f7\u01fa\3\2\2\2\u01f8")
        buf.write("\u01f6\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9\u01fb\3\2\2\2")
        buf.write("\u01fa\u01f8\3\2\2\2\u01fb\u01fc\5\35\17\2\u01fc\u01fd")
        buf.write("\bF\b\2\u01fd\u008c\3\2\2\2\34\2\u009d\u00ab\u00b4\u00bb")
        buf.write("\u00bf\u00c7\u00ca\u00ce\u00d3\u00df\u00e3\u00e9\u00f3")
        buf.write("\u00f7\u00fe\u0104\u010c\u0114\u01d4\u01d9\u01db\u01e1")
        buf.write("\u01ec\u01f0\u01f8\t\b\2\2\3\b\2\3\n\3\3\f\4\3D\5\3E\6")
        buf.write("\3F\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    COMMENT_C = 2
    COMMENT_CPLUS = 3
    INTLIT = 4
    FLOATLIT = 5
    BOOLLIT = 6
    STRING_LIT = 7
    AUTO = 8
    FALSE = 9
    INTERGER = 10
    VOID = 11
    ARRAY = 12
    BREAK = 13
    FLOAT = 14
    RETURN = 15
    OUT = 16
    BOOLEAN = 17
    FOR = 18
    STRING = 19
    CONTINUE = 20
    DO = 21
    FUNCTION = 22
    TRUE = 23
    OF = 24
    ELSE = 25
    IF = 26
    WHILE = 27
    INHERIT = 28
    ADDOP = 29
    SUBOP = 30
    MULOP = 31
    DIV = 32
    MOD = 33
    NOT = 34
    AND = 35
    OR = 36
    EQUAL = 37
    NOT_EQUAL = 38
    LESS = 39
    LESS_OR_EQUAL = 40
    GREATER = 41
    GREATER_OR_EQUAL = 42
    DOUBLE_COLON = 43
    LB = 44
    RB = 45
    LSB = 46
    RSB = 47
    DOT = 48
    COMMA = 49
    SEMICOLON = 50
    COLON = 51
    LP = 52
    RP = 53
    ASSIGN = 54
    ID = 55
    WS = 56
    ERROR_CHAR = 57
    UNCLOSE_STRING = 58
    ILLEGAL_ESCAPE = 59

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'func_decl'", "'auto'", "'false'", "'integer'", "'void'", "'array'", 
            "'break'", "'float'", "'return'", "'out'", "'boolean'", "'for'", 
            "'string'", "'continue'", "'do'", "'function'", "'true'", "'of'", 
            "'else'", "'if'", "'while'", "'inherit'", "'+'", "'-'", "'*'", 
            "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", 
            "'<='", "'>'", "'>='", "'::'", "'('", "')'", "'['", "']'", "'.'", 
            "','", "';'", "':'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT_C", "COMMENT_CPLUS", "INTLIT", "FLOATLIT", "BOOLLIT", 
            "STRING_LIT", "AUTO", "FALSE", "INTERGER", "VOID", "ARRAY", 
            "BREAK", "FLOAT", "RETURN", "OUT", "BOOLEAN", "FOR", "STRING", 
            "CONTINUE", "DO", "FUNCTION", "TRUE", "OF", "ELSE", "IF", "WHILE", 
            "INHERIT", "ADDOP", "SUBOP", "MULOP", "DIV", "MOD", "NOT", "AND", 
            "OR", "EQUAL", "NOT_EQUAL", "LESS", "LESS_OR_EQUAL", "GREATER", 
            "GREATER_OR_EQUAL", "DOUBLE_COLON", "LB", "RB", "LSB", "RSB", 
            "DOT", "COMMA", "SEMICOLON", "COLON", "LP", "RP", "ASSIGN", 
            "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "COMMENT_C", "COMMENT_CPLUS", "INT", "EXPONENT", 
                  "SIGN", "INTLIT", "FLOATFRAG", "FLOATLIT", "BOOLLIT", 
                  "STRING_LIT", "STRING_CHAR", "ESC_SEQ", "ESC_ILLEGAL", 
                  "AUTO", "FALSE", "INTERGER", "VOID", "ARRAY", "BREAK", 
                  "FLOAT", "RETURN", "OUT", "BOOLEAN", "FOR", "STRING", 
                  "CONTINUE", "DO", "FUNCTION", "TRUE", "OF", "ELSE", "IF", 
                  "WHILE", "INHERIT", "ADDOP", "SUBOP", "MULOP", "DIV", 
                  "MOD", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", "LESS", 
                  "LESS_OR_EQUAL", "GREATER", "GREATER_OR_EQUAL", "DOUBLE_COLON", 
                  "LB", "RB", "LSB", "RSB", "DOT", "COMMA", "SEMICOLON", 
                  "COLON", "LP", "RP", "ASSIGN", "LETTER", "UNDERSCORE", 
                  "DIGIT", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[6] = self.INTLIT_action 
            actions[8] = self.FLOATLIT_action 
            actions[10] = self.STRING_LIT_action 
            actions[66] = self.ERROR_CHAR_action 
            actions[67] = self.UNCLOSE_STRING_action 
            actions[68] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	self.text = (self.text).replace("_", "") 

     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
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
            	
     



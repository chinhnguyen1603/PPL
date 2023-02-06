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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2<")
        buf.write("\u01fa\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\3\2\3\2\3\2\3\2\7\2\u0090\n\2\f\2\16\2\u0093")
        buf.write("\13\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u009e\n")
        buf.write("\3\f\3\16\3\u00a1\13\3\3\3\3\3\3\4\3\4\7\4\u00a7\n\4\f")
        buf.write("\4\16\4\u00aa\13\4\3\4\3\4\6\4\u00ae\n\4\r\4\16\4\u00af")
        buf.write("\7\4\u00b2\n\4\f\4\16\4\u00b5\13\4\3\4\3\4\3\4\7\4\u00ba")
        buf.write("\n\4\f\4\16\4\u00bd\13\4\5\4\u00bf\n\4\3\5\3\5\5\5\u00c3")
        buf.write("\n\5\3\5\6\5\u00c6\n\5\r\5\16\5\u00c7\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\7\b\u00d2\n\b\f\b\16\b\u00d5\13\b\3\b")
        buf.write("\7\b\u00d8\n\b\f\b\16\b\u00db\13\b\3\b\5\b\u00de\n\b\3")
        buf.write("\b\3\b\6\b\u00e2\n\b\r\b\16\b\u00e3\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\6\b\u00ec\n\b\r\b\16\b\u00ed\3\b\3\b\5\b\u00f2")
        buf.write("\n\b\3\t\3\t\3\t\3\n\3\n\5\n\u00f9\n\n\3\13\3\13\7\13")
        buf.write("\u00fd\n\13\f\13\16\13\u0100\13\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\5\f\u0109\n\f\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\5\16\u0111\n\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3")
        buf.write("!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3$\3")
        buf.write("$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3*\3+\3+\3+\3")
        buf.write(",\3,\3,\3-\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3\61\3\61\3")
        buf.write("\61\3\62\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66")
        buf.write("\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3")
        buf.write(">\3>\3?\3?\3@\3@\3A\3A\5A\u01d1\nA\3A\3A\3A\7A\u01d6\n")
        buf.write("A\fA\16A\u01d9\13A\3B\6B\u01dc\nB\rB\16B\u01dd\3B\3B\3")
        buf.write("C\3C\3C\3D\3D\7D\u01e7\nD\fD\16D\u01ea\13D\3D\5D\u01ed")
        buf.write("\nD\3D\3D\3E\3E\7E\u01f3\nE\fE\16E\u01f6\13E\3E\3E\3E")
        buf.write("\3\u0091\2F\3\3\5\4\7\2\t\2\13\2\r\5\17\2\21\6\23\7\25")
        buf.write("\b\27\2\31\2\33\2\35\t\37\n!\13#\f%\r\'\16)\17+\20-\21")
        buf.write("/\22\61\23\63\24\65\25\67\269\27;\30=\31?\32A\33C\34E")
        buf.write("\35G\36I\37K M!O\"Q#S$U%W&Y\'[(])_*a+c,e-g.i/k\60m\61")
        buf.write("o\62q\63s\64u\65w\66y\67{\2}\2\177\2\u00818\u00839\u0085")
        buf.write(":\u0087;\u0089<\3\2\16\4\2\f\f\17\17\3\2\63;\3\2\62;\4")
        buf.write("\2GGgg\4\2--//\4\2$$^^\t\2))^^ddhhppttvv\n\2$$))^^ddh")
        buf.write("hppttvv\3\2^^\4\2C\\c|\5\2\n\f\16\17\"\"\7\3\n\f\16\17")
        buf.write("$$))^^\2\u020d\2\3\3\2\2\2\2\5\3\2\2\2\2\r\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3")
        buf.write("\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k")
        buf.write("\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2")
        buf.write("u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\3\u008b\3\2\2\2\5\u0099\3\2\2\2\7\u00be\3\2\2\2\t\u00c0")
        buf.write("\3\2\2\2\13\u00c9\3\2\2\2\r\u00cb\3\2\2\2\17\u00f1\3\2")
        buf.write("\2\2\21\u00f3\3\2\2\2\23\u00f8\3\2\2\2\25\u00fa\3\2\2")
        buf.write("\2\27\u0108\3\2\2\2\31\u010a\3\2\2\2\33\u0110\3\2\2\2")
        buf.write("\35\u0112\3\2\2\2\37\u0117\3\2\2\2!\u011d\3\2\2\2#\u0125")
        buf.write("\3\2\2\2%\u012a\3\2\2\2\'\u0130\3\2\2\2)\u0136\3\2\2\2")
        buf.write("+\u013c\3\2\2\2-\u0143\3\2\2\2/\u0147\3\2\2\2\61\u014f")
        buf.write("\3\2\2\2\63\u0153\3\2\2\2\65\u015a\3\2\2\2\67\u0163\3")
        buf.write("\2\2\29\u0166\3\2\2\2;\u016f\3\2\2\2=\u0174\3\2\2\2?\u0177")
        buf.write("\3\2\2\2A\u017c\3\2\2\2C\u017f\3\2\2\2E\u0185\3\2\2\2")
        buf.write("G\u018d\3\2\2\2I\u018f\3\2\2\2K\u0191\3\2\2\2M\u0193\3")
        buf.write("\2\2\2O\u0195\3\2\2\2Q\u0197\3\2\2\2S\u0199\3\2\2\2U\u019c")
        buf.write("\3\2\2\2W\u019f\3\2\2\2Y\u01a2\3\2\2\2[\u01a5\3\2\2\2")
        buf.write("]\u01a7\3\2\2\2_\u01aa\3\2\2\2a\u01ac\3\2\2\2c\u01af\3")
        buf.write("\2\2\2e\u01b2\3\2\2\2g\u01b4\3\2\2\2i\u01b6\3\2\2\2k\u01b8")
        buf.write("\3\2\2\2m\u01ba\3\2\2\2o\u01bc\3\2\2\2q\u01be\3\2\2\2")
        buf.write("s\u01c0\3\2\2\2u\u01c2\3\2\2\2w\u01c4\3\2\2\2y\u01c6\3")
        buf.write("\2\2\2{\u01c8\3\2\2\2}\u01ca\3\2\2\2\177\u01cc\3\2\2\2")
        buf.write("\u0081\u01d0\3\2\2\2\u0083\u01db\3\2\2\2\u0085\u01e1\3")
        buf.write("\2\2\2\u0087\u01e4\3\2\2\2\u0089\u01f0\3\2\2\2\u008b\u008c")
        buf.write("\7\61\2\2\u008c\u008d\7,\2\2\u008d\u0091\3\2\2\2\u008e")
        buf.write("\u0090\13\2\2\2\u008f\u008e\3\2\2\2\u0090\u0093\3\2\2")
        buf.write("\2\u0091\u0092\3\2\2\2\u0091\u008f\3\2\2\2\u0092\u0094")
        buf.write("\3\2\2\2\u0093\u0091\3\2\2\2\u0094\u0095\7,\2\2\u0095")
        buf.write("\u0096\7\61\2\2\u0096\u0097\3\2\2\2\u0097\u0098\b\2\2")
        buf.write("\2\u0098\4\3\2\2\2\u0099\u009a\7\61\2\2\u009a\u009b\7")
        buf.write("\61\2\2\u009b\u009f\3\2\2\2\u009c\u009e\n\2\2\2\u009d")
        buf.write("\u009c\3\2\2\2\u009e\u00a1\3\2\2\2\u009f\u009d\3\2\2\2")
        buf.write("\u009f\u00a0\3\2\2\2\u00a0\u00a2\3\2\2\2\u00a1\u009f\3")
        buf.write("\2\2\2\u00a2\u00a3\b\3\2\2\u00a3\6\3\2\2\2\u00a4\u00b3")
        buf.write("\t\3\2\2\u00a5\u00a7\t\4\2\2\u00a6\u00a5\3\2\2\2\u00a7")
        buf.write("\u00aa\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2")
        buf.write("\u00a9\u00ab\3\2\2\2\u00aa\u00a8\3\2\2\2\u00ab\u00ad\7")
        buf.write("a\2\2\u00ac\u00ae\t\4\2\2\u00ad\u00ac\3\2\2\2\u00ae\u00af")
        buf.write("\3\2\2\2\u00af\u00ad\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0")
        buf.write("\u00b2\3\2\2\2\u00b1\u00a8\3\2\2\2\u00b2\u00b5\3\2\2\2")
        buf.write("\u00b3\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00bf\3")
        buf.write("\2\2\2\u00b5\u00b3\3\2\2\2\u00b6\u00bf\7\62\2\2\u00b7")
        buf.write("\u00bb\t\3\2\2\u00b8\u00ba\t\4\2\2\u00b9\u00b8\3\2\2\2")
        buf.write("\u00ba\u00bd\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bb\u00bc\3")
        buf.write("\2\2\2\u00bc\u00bf\3\2\2\2\u00bd\u00bb\3\2\2\2\u00be\u00a4")
        buf.write("\3\2\2\2\u00be\u00b6\3\2\2\2\u00be\u00b7\3\2\2\2\u00bf")
        buf.write("\b\3\2\2\2\u00c0\u00c2\t\5\2\2\u00c1\u00c3\5\13\6\2\u00c2")
        buf.write("\u00c1\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c5\3\2\2\2")
        buf.write("\u00c4\u00c6\5\177@\2\u00c5\u00c4\3\2\2\2\u00c6\u00c7")
        buf.write("\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8")
        buf.write("\n\3\2\2\2\u00c9\u00ca\t\6\2\2\u00ca\f\3\2\2\2\u00cb\u00cc")
        buf.write("\5\7\4\2\u00cc\u00cd\b\7\3\2\u00cd\16\3\2\2\2\u00ce\u00cf")
        buf.write("\5\7\4\2\u00cf\u00d3\7\60\2\2\u00d0\u00d2\5\177@\2\u00d1")
        buf.write("\u00d0\3\2\2\2\u00d2\u00d5\3\2\2\2\u00d3\u00d1\3\2\2\2")
        buf.write("\u00d3\u00d4\3\2\2\2\u00d4\u00d9\3\2\2\2\u00d5\u00d3\3")
        buf.write("\2\2\2\u00d6\u00d8\5\t\5\2\u00d7\u00d6\3\2\2\2\u00d8\u00db")
        buf.write("\3\2\2\2\u00d9\u00d7\3\2\2\2\u00d9\u00da\3\2\2\2\u00da")
        buf.write("\u00f2\3\2\2\2\u00db\u00d9\3\2\2\2\u00dc\u00de\5\7\4\2")
        buf.write("\u00dd\u00dc\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00df\3")
        buf.write("\2\2\2\u00df\u00e1\7\60\2\2\u00e0\u00e2\5\177@\2\u00e1")
        buf.write("\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e1\3\2\2\2")
        buf.write("\u00e3\u00e4\3\2\2\2\u00e4\u00f2\3\2\2\2\u00e5\u00e6\5")
        buf.write("\7\4\2\u00e6\u00e7\5\t\5\2\u00e7\u00f2\3\2\2\2\u00e8\u00e9")
        buf.write("\5\7\4\2\u00e9\u00eb\7\60\2\2\u00ea\u00ec\5\177@\2\u00eb")
        buf.write("\u00ea\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00eb\3\2\2\2")
        buf.write("\u00ed\u00ee\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f0\5")
        buf.write("\t\5\2\u00f0\u00f2\3\2\2\2\u00f1\u00ce\3\2\2\2\u00f1\u00dd")
        buf.write("\3\2\2\2\u00f1\u00e5\3\2\2\2\u00f1\u00e8\3\2\2\2\u00f2")
        buf.write("\20\3\2\2\2\u00f3\u00f4\5\17\b\2\u00f4\u00f5\b\t\4\2\u00f5")
        buf.write("\22\3\2\2\2\u00f6\u00f9\5;\36\2\u00f7\u00f9\5\37\20\2")
        buf.write("\u00f8\u00f6\3\2\2\2\u00f8\u00f7\3\2\2\2\u00f9\24\3\2")
        buf.write("\2\2\u00fa\u00fe\7$\2\2\u00fb\u00fd\5\27\f\2\u00fc\u00fb")
        buf.write("\3\2\2\2\u00fd\u0100\3\2\2\2\u00fe\u00fc\3\2\2\2\u00fe")
        buf.write("\u00ff\3\2\2\2\u00ff\u0101\3\2\2\2\u0100\u00fe\3\2\2\2")
        buf.write("\u0101\u0102\7$\2\2\u0102\u0103\b\13\5\2\u0103\26\3\2")
        buf.write("\2\2\u0104\u0109\n\7\2\2\u0105\u0109\5\31\r\2\u0106\u0107")
        buf.write("\7^\2\2\u0107\u0109\7$\2\2\u0108\u0104\3\2\2\2\u0108\u0105")
        buf.write("\3\2\2\2\u0108\u0106\3\2\2\2\u0109\30\3\2\2\2\u010a\u010b")
        buf.write("\7^\2\2\u010b\u010c\t\b\2\2\u010c\32\3\2\2\2\u010d\u010e")
        buf.write("\7^\2\2\u010e\u0111\n\t\2\2\u010f\u0111\n\n\2\2\u0110")
        buf.write("\u010d\3\2\2\2\u0110\u010f\3\2\2\2\u0111\34\3\2\2\2\u0112")
        buf.write("\u0113\7c\2\2\u0113\u0114\7w\2\2\u0114\u0115\7v\2\2\u0115")
        buf.write("\u0116\7q\2\2\u0116\36\3\2\2\2\u0117\u0118\7h\2\2\u0118")
        buf.write("\u0119\7c\2\2\u0119\u011a\7n\2\2\u011a\u011b\7u\2\2\u011b")
        buf.write("\u011c\7g\2\2\u011c \3\2\2\2\u011d\u011e\7k\2\2\u011e")
        buf.write("\u011f\7p\2\2\u011f\u0120\7v\2\2\u0120\u0121\7g\2\2\u0121")
        buf.write("\u0122\7i\2\2\u0122\u0123\7g\2\2\u0123\u0124\7t\2\2\u0124")
        buf.write("\"\3\2\2\2\u0125\u0126\7x\2\2\u0126\u0127\7q\2\2\u0127")
        buf.write("\u0128\7k\2\2\u0128\u0129\7f\2\2\u0129$\3\2\2\2\u012a")
        buf.write("\u012b\7c\2\2\u012b\u012c\7t\2\2\u012c\u012d\7t\2\2\u012d")
        buf.write("\u012e\7c\2\2\u012e\u012f\7{\2\2\u012f&\3\2\2\2\u0130")
        buf.write("\u0131\7d\2\2\u0131\u0132\7t\2\2\u0132\u0133\7g\2\2\u0133")
        buf.write("\u0134\7c\2\2\u0134\u0135\7m\2\2\u0135(\3\2\2\2\u0136")
        buf.write("\u0137\7h\2\2\u0137\u0138\7n\2\2\u0138\u0139\7q\2\2\u0139")
        buf.write("\u013a\7c\2\2\u013a\u013b\7v\2\2\u013b*\3\2\2\2\u013c")
        buf.write("\u013d\7t\2\2\u013d\u013e\7g\2\2\u013e\u013f\7v\2\2\u013f")
        buf.write("\u0140\7w\2\2\u0140\u0141\7t\2\2\u0141\u0142\7p\2\2\u0142")
        buf.write(",\3\2\2\2\u0143\u0144\7q\2\2\u0144\u0145\7w\2\2\u0145")
        buf.write("\u0146\7v\2\2\u0146.\3\2\2\2\u0147\u0148\7d\2\2\u0148")
        buf.write("\u0149\7q\2\2\u0149\u014a\7q\2\2\u014a\u014b\7n\2\2\u014b")
        buf.write("\u014c\7g\2\2\u014c\u014d\7c\2\2\u014d\u014e\7p\2\2\u014e")
        buf.write("\60\3\2\2\2\u014f\u0150\7h\2\2\u0150\u0151\7q\2\2\u0151")
        buf.write("\u0152\7t\2\2\u0152\62\3\2\2\2\u0153\u0154\7u\2\2\u0154")
        buf.write("\u0155\7v\2\2\u0155\u0156\7t\2\2\u0156\u0157\7k\2\2\u0157")
        buf.write("\u0158\7p\2\2\u0158\u0159\7i\2\2\u0159\64\3\2\2\2\u015a")
        buf.write("\u015b\7e\2\2\u015b\u015c\7q\2\2\u015c\u015d\7p\2\2\u015d")
        buf.write("\u015e\7v\2\2\u015e\u015f\7k\2\2\u015f\u0160\7p\2\2\u0160")
        buf.write("\u0161\7w\2\2\u0161\u0162\7g\2\2\u0162\66\3\2\2\2\u0163")
        buf.write("\u0164\7f\2\2\u0164\u0165\7q\2\2\u01658\3\2\2\2\u0166")
        buf.write("\u0167\7h\2\2\u0167\u0168\7w\2\2\u0168\u0169\7p\2\2\u0169")
        buf.write("\u016a\7e\2\2\u016a\u016b\7v\2\2\u016b\u016c\7k\2\2\u016c")
        buf.write("\u016d\7q\2\2\u016d\u016e\7p\2\2\u016e:\3\2\2\2\u016f")
        buf.write("\u0170\7v\2\2\u0170\u0171\7t\2\2\u0171\u0172\7w\2\2\u0172")
        buf.write("\u0173\7g\2\2\u0173<\3\2\2\2\u0174\u0175\7q\2\2\u0175")
        buf.write("\u0176\7h\2\2\u0176>\3\2\2\2\u0177\u0178\7g\2\2\u0178")
        buf.write("\u0179\7n\2\2\u0179\u017a\7u\2\2\u017a\u017b\7g\2\2\u017b")
        buf.write("@\3\2\2\2\u017c\u017d\7k\2\2\u017d\u017e\7h\2\2\u017e")
        buf.write("B\3\2\2\2\u017f\u0180\7y\2\2\u0180\u0181\7j\2\2\u0181")
        buf.write("\u0182\7k\2\2\u0182\u0183\7n\2\2\u0183\u0184\7g\2\2\u0184")
        buf.write("D\3\2\2\2\u0185\u0186\7k\2\2\u0186\u0187\7p\2\2\u0187")
        buf.write("\u0188\7j\2\2\u0188\u0189\7g\2\2\u0189\u018a\7t\2\2\u018a")
        buf.write("\u018b\7k\2\2\u018b\u018c\7v\2\2\u018cF\3\2\2\2\u018d")
        buf.write("\u018e\7-\2\2\u018eH\3\2\2\2\u018f\u0190\7/\2\2\u0190")
        buf.write("J\3\2\2\2\u0191\u0192\7,\2\2\u0192L\3\2\2\2\u0193\u0194")
        buf.write("\7\61\2\2\u0194N\3\2\2\2\u0195\u0196\7\'\2\2\u0196P\3")
        buf.write("\2\2\2\u0197\u0198\7#\2\2\u0198R\3\2\2\2\u0199\u019a\7")
        buf.write("(\2\2\u019a\u019b\7(\2\2\u019bT\3\2\2\2\u019c\u019d\7")
        buf.write("~\2\2\u019d\u019e\7~\2\2\u019eV\3\2\2\2\u019f\u01a0\7")
        buf.write("?\2\2\u01a0\u01a1\7?\2\2\u01a1X\3\2\2\2\u01a2\u01a3\7")
        buf.write("#\2\2\u01a3\u01a4\7?\2\2\u01a4Z\3\2\2\2\u01a5\u01a6\7")
        buf.write(">\2\2\u01a6\\\3\2\2\2\u01a7\u01a8\7>\2\2\u01a8\u01a9\7")
        buf.write("?\2\2\u01a9^\3\2\2\2\u01aa\u01ab\7@\2\2\u01ab`\3\2\2\2")
        buf.write("\u01ac\u01ad\7@\2\2\u01ad\u01ae\7?\2\2\u01aeb\3\2\2\2")
        buf.write("\u01af\u01b0\7<\2\2\u01b0\u01b1\7<\2\2\u01b1d\3\2\2\2")
        buf.write("\u01b2\u01b3\7*\2\2\u01b3f\3\2\2\2\u01b4\u01b5\7+\2\2")
        buf.write("\u01b5h\3\2\2\2\u01b6\u01b7\7]\2\2\u01b7j\3\2\2\2\u01b8")
        buf.write("\u01b9\7_\2\2\u01b9l\3\2\2\2\u01ba\u01bb\7\60\2\2\u01bb")
        buf.write("n\3\2\2\2\u01bc\u01bd\7.\2\2\u01bdp\3\2\2\2\u01be\u01bf")
        buf.write("\7=\2\2\u01bfr\3\2\2\2\u01c0\u01c1\7<\2\2\u01c1t\3\2\2")
        buf.write("\2\u01c2\u01c3\7}\2\2\u01c3v\3\2\2\2\u01c4\u01c5\7\177")
        buf.write("\2\2\u01c5x\3\2\2\2\u01c6\u01c7\7?\2\2\u01c7z\3\2\2\2")
        buf.write("\u01c8\u01c9\t\13\2\2\u01c9|\3\2\2\2\u01ca\u01cb\7a\2")
        buf.write("\2\u01cb~\3\2\2\2\u01cc\u01cd\t\4\2\2\u01cd\u0080\3\2")
        buf.write("\2\2\u01ce\u01d1\5}?\2\u01cf\u01d1\5{>\2\u01d0\u01ce\3")
        buf.write("\2\2\2\u01d0\u01cf\3\2\2\2\u01d1\u01d7\3\2\2\2\u01d2\u01d6")
        buf.write("\5}?\2\u01d3\u01d6\5{>\2\u01d4\u01d6\5\177@\2\u01d5\u01d2")
        buf.write("\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d5\u01d4\3\2\2\2\u01d6")
        buf.write("\u01d9\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d7\u01d8\3\2\2\2")
        buf.write("\u01d8\u0082\3\2\2\2\u01d9\u01d7\3\2\2\2\u01da\u01dc\t")
        buf.write("\f\2\2\u01db\u01da\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01db")
        buf.write("\3\2\2\2\u01dd\u01de\3\2\2\2\u01de\u01df\3\2\2\2\u01df")
        buf.write("\u01e0\bB\2\2\u01e0\u0084\3\2\2\2\u01e1\u01e2\13\2\2\2")
        buf.write("\u01e2\u01e3\bC\6\2\u01e3\u0086\3\2\2\2\u01e4\u01e8\7")
        buf.write("$\2\2\u01e5\u01e7\5\27\f\2\u01e6\u01e5\3\2\2\2\u01e7\u01ea")
        buf.write("\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9")
        buf.write("\u01ec\3\2\2\2\u01ea\u01e8\3\2\2\2\u01eb\u01ed\t\r\2\2")
        buf.write("\u01ec\u01eb\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u01ef\b")
        buf.write("D\7\2\u01ef\u0088\3\2\2\2\u01f0\u01f4\7$\2\2\u01f1\u01f3")
        buf.write("\5\27\f\2\u01f2\u01f1\3\2\2\2\u01f3\u01f6\3\2\2\2\u01f4")
        buf.write("\u01f2\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5\u01f7\3\2\2\2")
        buf.write("\u01f6\u01f4\3\2\2\2\u01f7\u01f8\5\33\16\2\u01f8\u01f9")
        buf.write("\bE\b\2\u01f9\u008a\3\2\2\2\35\2\u0091\u009f\u00a8\u00af")
        buf.write("\u00b3\u00bb\u00be\u00c2\u00c7\u00d3\u00d9\u00dd\u00e3")
        buf.write("\u00ed\u00f1\u00f8\u00fe\u0108\u0110\u01d0\u01d5\u01d7")
        buf.write("\u01dd\u01e8\u01ec\u01f4\t\b\2\2\3\7\2\3\t\3\3\13\4\3")
        buf.write("C\5\3D\6\3E\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT_C = 1
    COMMENT_CPLUS = 2
    INTLIT = 3
    FLOATLIT = 4
    BOOLLIT = 5
    STRING_LIT = 6
    AUTO = 7
    FALSE = 8
    INTERGER = 9
    VOID = 10
    ARRAY = 11
    BREAK = 12
    FLOAT = 13
    RETURN = 14
    OUT = 15
    BOOLEAN = 16
    FOR = 17
    STRING = 18
    CONTINUE = 19
    DO = 20
    FUNCTION = 21
    TRUE = 22
    OF = 23
    ELSE = 24
    IF = 25
    WHILE = 26
    INHERIT = 27
    ADDOP = 28
    SUBOP = 29
    MULOP = 30
    DIV = 31
    MOD = 32
    NOT = 33
    AND = 34
    OR = 35
    EQUAL = 36
    NOT_EQUAL = 37
    LESS = 38
    LESS_OR_EQUAL = 39
    GREATER = 40
    GREATER_OR_EQUAL = 41
    DOUBLE_COLON = 42
    LB = 43
    RB = 44
    LSB = 45
    RSB = 46
    DOT = 47
    COMMA = 48
    SEMICOLON = 49
    COLON = 50
    LP = 51
    RP = 52
    ASSIGN = 53
    ID = 54
    WS = 55
    ERROR_CHAR = 56
    UNCLOSE_STRING = 57
    ILLEGAL_ESCAPE = 58

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
            "COMMENT_C", "COMMENT_CPLUS", "INTLIT", "FLOATLIT", "BOOLLIT", 
            "STRING_LIT", "AUTO", "FALSE", "INTERGER", "VOID", "ARRAY", 
            "BREAK", "FLOAT", "RETURN", "OUT", "BOOLEAN", "FOR", "STRING", 
            "CONTINUE", "DO", "FUNCTION", "TRUE", "OF", "ELSE", "IF", "WHILE", 
            "INHERIT", "ADDOP", "SUBOP", "MULOP", "DIV", "MOD", "NOT", "AND", 
            "OR", "EQUAL", "NOT_EQUAL", "LESS", "LESS_OR_EQUAL", "GREATER", 
            "GREATER_OR_EQUAL", "DOUBLE_COLON", "LB", "RB", "LSB", "RSB", 
            "DOT", "COMMA", "SEMICOLON", "COLON", "LP", "RP", "ASSIGN", 
            "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "COMMENT_C", "COMMENT_CPLUS", "INT", "EXPONENT", "SIGN", 
                  "INTLIT", "FLOATFRAG", "FLOATLIT", "BOOLLIT", "STRING_LIT", 
                  "STRING_CHAR", "ESC_SEQ", "ESC_ILLEGAL", "AUTO", "FALSE", 
                  "INTERGER", "VOID", "ARRAY", "BREAK", "FLOAT", "RETURN", 
                  "OUT", "BOOLEAN", "FOR", "STRING", "CONTINUE", "DO", "FUNCTION", 
                  "TRUE", "OF", "ELSE", "IF", "WHILE", "INHERIT", "ADDOP", 
                  "SUBOP", "MULOP", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", 
                  "NOT_EQUAL", "LESS", "LESS_OR_EQUAL", "GREATER", "GREATER_OR_EQUAL", 
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
            actions[5] = self.INTLIT_action 
            actions[7] = self.FLOATLIT_action 
            actions[9] = self.STRING_LIT_action 
            actions[65] = self.ERROR_CHAR_action 
            actions[66] = self.UNCLOSE_STRING_action 
            actions[67] = self.ILLEGAL_ESCAPE_action 
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
            	
     



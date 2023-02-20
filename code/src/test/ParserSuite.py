import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
 
    #test variable declaration
    def test_variable_declaration1(self):
        input = """a, b, c: integer = 3, 4, 6;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))

    #test variable declaration
    def test_variable_declaration2(self):
        input = """a, b, c, d: integer = 3, 4, 6;"""
        expect = "Error on line 1 col 29: ;"
        self.assertTrue(TestParser.test(input,expect,203))


    #test variable declaration
    def test_variable_declaration3(self):
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))        

    #test variable declaration
    def test_variable_declaration4(self):
        input = """delta: integer = fact(3);"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))
        
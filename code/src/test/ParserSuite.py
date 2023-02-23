import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    #test variable decleration
    def test_var_declare1(self):
        input = """a: integer = 5;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_var_declare2(self):
        input = """test_arr: array [0] of integer"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_var_declare3(self):
        input = """a: integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))

    def test_var_declare4(self):
        input = """Var: string = "welcome";"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))

    def test_var_declare5(self):
        input = """str1, str2, str3: float = 1.2, 1.3, 1.4 ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))

    def test_var_declare6(self):
        input = """str1, str2, str3: float = 1.2, 1.3 ;"""
        expect = "Error on line 1 col 35: ;"
        self.assertTrue(TestParser.test(input,expect,206))

    def test_var_declare7(self):
        input = """a: integer = 5 .;"""
        expect = "Error on line 1 col 15: ."
        self.assertTrue(TestParser.test(input,expect,207))

    def test_var_declare8(self):
        input = """a: boolean = true;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))
    
    def test_var_declare9(self):
        input = """a, b: string = "viet", "nam" ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))

    def test_var_declare10(self):
        input = """a, b,c: string = "viet","nam","net" ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))

    #test mix program
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))
 
    def test_variable_declaration1(self):
        input = """a, b, c: integer = 3, 4, 6;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))

    #test variable declaration
    def test_variable_declaration2(self):
        input = """a, b, c, d: integer = 3, 4, 6;"""
        expect = "Error on line 1 col 29: ;"
        self.assertTrue(TestParser.test(input,expect,213))


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
        self.assertTrue(TestParser.test(input,expect,214))        

    def test_variable_declaration4(self):
        input = """integer"""
        expect = "Error on line 1 col 0: integer"
        self.assertTrue(TestParser.test(input,expect,215))

    def test_mix6(self):
        input = """test_arr: array [4] of integer = 5;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))        

    def test_mix7(self):
        input = """{"Kangxi", "Yongzheng", "Qianlong"}"""
        expect = "Error on line 1 col 0: {"
        self.assertTrue(TestParser.test(input,expect,217))   

    def test_mix8(self):
        input = """test_arr: array [4] of integer = {1,2,3,4};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))           

    def test_mix9(self):
        input = """ inherit out id: boolean"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))         

    def test_mix10(self):
        input = """ out id: auto"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))    
import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    #test variable decleration
    def test_var_declare1(self):
        input = """a: integer = 5;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_var_declare2(self):
        input = """b[2][3]: array = {{2,3,4},{4,5,6}};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_var_declare3(self):
        input = """a: integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))

    def test_var_declare4(self):
        input = """Var: m, n[10];"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))

    def test_var_declare5(self):
        input = """Var: s="happyBirthDay";"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))

    def test_var_declare6(self):
        input = """Var: s_1="'"superMan is'".", s_2="happyBirthDay", arr = {**"toYou"**, 12, 99.4e2};"""
        expect = "Error on line 1 col 68: ,"
        self.assertTrue(TestParser.test(input,expect,206))

    def test_var_declare7(self):
        input = """Var: arr[10], c[99][3][2], arr2[];
                """
        expect = "Error on line 1 col 32: ]"
        self.assertTrue(TestParser.test(input,expect,207))

    def test_var_declare8(self):
        input = """Var: s="DaiH0cB4ckHo4", x= 12.2e54, c=0xF212;
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))
    
    def test_var_declare9(self):
        input = """Var: arr[2][3][5] = {{"string", "s!@#$"}, {{542.10e21, 2., 9e5}}, {{1023, 1024, 2098}, {0x2141, 0xF912}}};
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))
    def test_var_declare10(self):
        input = """Var: arr = {1,2}, a[10][22], e=40e5, c, d f=20;
                """
        expect = "Error on line 1 col 42: f"
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
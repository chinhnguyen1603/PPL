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
        input = """ inherit out id: void"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))         

    def test_mix10(self):
        input = """ out id: auto"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))    

    #test function decleration
    def test_func_declare1(self):
        input = """func1: function array [2,3,4] of float () {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,221))        

    def test_func_declare2(self):
        input = """func1: function string () """
        expect = "Error on line 1 col 26: <EOF>"
        self.assertTrue(TestParser.test(input,expect,222)) 

    def test_func_declare3(self):
        input = """func1: function boolean () {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,223)) 

    def test_func_declare4(self):
        input = """func1: function auto {}"""
        expect = "Error on line 1 col 21: {"
        self.assertTrue(TestParser.test(input,expect,224))        

    def test_func_declare5(self):
        input = """func1: integer () {};"""
        expect = "Error on line 1 col 15: ("
        self.assertTrue(TestParser.test(input,expect,225)) 

    def test_func_declare6(self):
        input = """ func_1: function auto(inherit out var: integer, delta: boolean,inherit var2: array [5] of string) {
            n = n + delta;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,226)) 

    def test_func_declare7(self):
        input = """ func_1: function array [1,2,3] of boolean(var1: float, inherit var2: array [5] of string) inherit func_2 {
            n = !a;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,227))        

    def test_func_declare8(self):
        input = """func1: function string () {
r, s: boolean;
r = 2.0;
a, b: array [5] of integer;
s = r * r * myPI;
a[0] = s;
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,228)) 

    def test_func_declare9(self):
        input = """ func_1: function integer() inherit id_2 {
            n = !a;
            b = -b;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,229)) 

    def test_func_declare10(self):
        input = """ func_1: function integer() inherit {
            n = !a;
            b = -b;
        }"""
        expect = "Error on line 1 col 36: {"  
        self.assertTrue(TestParser.test(input,expect,230)) 

   #test assign statement combine expression
    def test_ass_stmt1(self):
        input = """func1: function array [2,3,4] of float () {
              r, s: integer;
              r = 2.0;
              a: float;
              var = 2 + 3;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,231))        

    def test_ass_stmt2(self):
        input = """func1: function void () {
              r, s: integer;
              r = a && b && c ;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232)) 

    def test_ass_stmt3(self):
        input = """func1: function void () {
              r, s: integer;
              r = && b && c ;
        }"""
        expect = "Error on line 3 col 18: &&"
        self.assertTrue(TestParser.test(input,expect,233)) 

    def test_ass_stmt4(self):
        input = """func1: function void () {
              r, s: boolean;
              r = array1[2];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))        

    def test_ass_stmt5(self):
        input = """func1: function void () {
              r, s: boolean;
              r = array1[2,3];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235)) 

    def test_ass_stmt6(self):
        input = """ func_1: function auto(inherit out var: integer, delta: boolean,inherit var2: array [5] of string) {
            n = n + delta;
            a = -r;
            c = string1 :: string2;
            c = d==b; 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236)) 

    def test_ass_stmt7(self):
        input = """func1: function string () {
r, s: boolean;
r = 2.0;
a, b: array [5] of integer;
s = r * r + myPI;
a[0] = foo();
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))        

    def test_ass_stmt8(self):
        input = """ func_1: function array [1,2,3] of boolean(var1: float, inherit var2: array [5] of string) inherit func_2 {
            n = a != b;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238)) 

    def test_ass_stmt9(self):
        input = """ func_1: function integer() inherit id_2 {
            n = !a;
            f = f || f ||;
        }"""
        expect = "Error on line 3 col 25: ;"        
        self.assertTrue(TestParser.test(input,expect,239)) 

    def test_ass_stmt10(self):
        input = """ func_1: function integer() {
            n = a <= m;
            a = b >= f;
            a = b > f;         
            a = b < f;     
            b = b / v;
            b = b % j;
            b = n - m;            
            f = f || f || v;
        }"""
        expect = "successful"  
        self.assertTrue(TestParser.test(input,expect,240))         

   #test if statement combine expression
    def test_if_stmt1(self):
        input = """func1: function array [2,3,4] of float () {
              if (r > 2.0) a=b;
              if (r == 2.0) ;               
        }"""
        expect = "Error on line 3 col 28: ;"
        self.assertTrue(TestParser.test(input,expect,241))        

    def test_if_stmt2(self):
        input = """func1: function array [2,3,4] of float () {
              if (r > 2.0) a=b;
              if (r == 2.0) a=a+b;               
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242)) 

    def test_if_stmt3(self):
        input = """func1: function array [2,3,4] of float () {
              if (r > 2.0) a=b;
              else a = a/b;               
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,243)) 

    def test_if_stmt4(self):
        input = """func1: function array [2,3,4] of float () {
              if (r > 2.0) a=b
              else a = a/b;               
        }"""
        expect = "Error on line 3 col 14: else"
        self.assertTrue(TestParser.test(input,expect,244))        

    def test_if_stmt5(self):
        input = """func1: function void () {
            if (n == 0) a = a+2;
            else a = a - 2;             
            else return n * fact(n - 1);
        }"""
        expect = "Error on line 4 col 12: else"
        self.assertTrue(TestParser.test(input,expect,245)) 

    def test_if_stmt6(self):
        input = """func1: function array [2,3,4] of float () {
              if (r > 2.0) a=b;
              else a = a/b              
        }"""
        expect = "Error on line 4 col 8: }"
        self.assertTrue(TestParser.test(input,expect,246)) 

    def test_if_stmt7(self):
        input = """func1: function string () {
r, s: boolean;
r = 2.0;
a, b: array [5] of integer;
s = r * r + myPI;
a[0] = foo();
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,247))        

    def test_if_stmt8(self):
        input = """ func_1: function array [1,2,3] of boolean(var1: float, inherit var2: array [5] of string) inherit func_2 {
            n = a != b;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,248)) 

    def test_if_stmt9(self):
        input = """ func_1: function integer() inherit id_2 {
            n = !a;
            f = f || f ||;
        }"""
        expect = "Error on line 3 col 25: ;"        
        self.assertTrue(TestParser.test(input,expect,249)) 

    def test_if_stmt10(self):
        input = """ func_1: function integer() {
            n = a <= m;
            a = b >= f;
            a = b > f;         
            a = b < f;     
            b = b / v;
            b = b % j;
            b = n - m;            
            f = f || f || v;
        }"""
        expect = "successful"  
        self.assertTrue(TestParser.test(input,expect,250))     

   #test for statement combine expression
    def test_for_stmt1(self):
        input = """func1: function array [2,3,4] of float () {
          for (i = 1, i < 10, i + 1) {
            writeInt(i);
          }             
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,251))        

    def test_for_stmt2(self):
        input = """func1: function array [2,3,4] of float () {
          for (i = 5, i >= 10, i + 1) {
            writeInt(i);
            a = a + 2 * b;
          }             
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,252)) 

    def test_for_stmt3(self):
        input = """func1: function array [2,3,4] of float () {
          for (i = 5, i >= 10, i + 1) 
            writeInt(i);
            a = a + 2 * b;             
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,253)) 

    def test_for_stmt4(self):
        input = """func1: function array [2,3,4] of float () {
          for (i = 5, i >= 10, i + 1, i < 3) 
            writeInt(i);
            a = a + 2 * b;             
        }"""
        expect = "Error on line 2 col 36: ,"
        self.assertTrue(TestParser.test(input,expect,254))        

    def test_for_stmt5(self):
        input = """func1: function array [2,3,4] of float () {
          for (i = 5, , i + 1) 
            writeInt(i);
            a = a + 2 * b;             
        }"""
        expect = "Error on line 2 col 22: ,"
        self.assertTrue(TestParser.test(input,expect,255)) 

    def test_for_stmt6(self):
        input = """func1: function array [2,3,4] of float () {
          for (i = 5, i >= 10, i + 1) {      
          }
        }"""
        expect = "Error on line 3 col 10: }"
        self.assertTrue(TestParser.test(input,expect,256)) 

    def test_for_stmt7(self):
        input = """func1: function string () {
r, s: boolean;
r = 2.0;
a, b: array [5] of integer;
s = r * r + myPI;
a[0] = foo();
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,257))        

    def test_for_stmt8(self):
        input = """ func_1: function array [1,2,3] of boolean(var1: float, inherit var2: array [5] of string) inherit func_2 {
            n = a != b;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,258)) 

    def test_for_stmt9(self):
        input = """ func_1: function integer() inherit id_2 {
            n = !a;
            f = f || f ||;
        }"""
        expect = "Error on line 3 col 25: ;"        
        self.assertTrue(TestParser.test(input,expect,259)) 

    def test_for_stmt10(self):
        input = """ func_1: function integer() {
            n = a <= m;
            a = b >= f;
            a = b > f;         
            a = b < f;     
            b = b / v;
            b = b % j;
            b = n - m;            
            f = f || f || v;
        }"""
        expect = "successful"  
        self.assertTrue(TestParser.test(input,expect,260))            

   #test while statement combine expression
    def test_while_stmt1(self):
        input = """func1: function array [2,3,4] of float () {
          while (i < 10, i + 1) {
            writeInt(i);
          }             
        }"""
        expect = "Error on line 2 col 23: ,"
        self.assertTrue(TestParser.test(input,expect,261))        

    def test_while_stmt2(self):
        input = """func1: function array [2,3,4] of float () {
          while (i = 5) {
            writeInt(i);
            a = a + 2 * b;
          }             
        }"""
        expect = "Error on line 2 col 19: ="
        self.assertTrue(TestParser.test(input,expect,262)) 

    def test_while_stmt3(self):
        input = """func1: function array [2,3,4] of float () {
          while (i >= 10) 
            writeInt(i);
            a = a + 2 * b;             
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,263)) 

    def test_while_stmt4(self):
        input = """func1: function array [2,3,4] of float () {
          while (a || b && c) {
            writeInt(i);
            a = a + 2 * b;    
          }         
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,264))        

    def test_while_stmt5(self):
        input = """func1: function array [2,3,4] of float () {
          while (a || b && c) { 
          }         
        }"""
        expect = "Error on line 3 col 10: }"
        self.assertTrue(TestParser.test(input,expect,265)) 

    def test_while_stmt6(self):
        input = """func1: function array [2,3,4] of float () {
          for (i = 5, i >= 10, i + 1) {      
          }
        }"""
        expect = "Error on line 3 col 10: }"
        self.assertTrue(TestParser.test(input,expect,266)) 

    def test_while_stmt7(self):
        input = """func1: function string () {
r, s: boolean;
r = 2.0;
a, b: array [5] of integer;
s = r * r + myPI;
a[0] = foo();
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,267))        

    def test_while_stmt8(self):
        input = """ func_1: function array [1,2,3] of boolean(var1: float, inherit var2: array [5] of string) inherit func_2 {
            n = a != b;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,268)) 

    def test_while_stmt9(self):
        input = """ func_1: function integer() inherit id_2 {
            n = !a;
            f = f || f ||;
        }"""
        expect = "Error on line 3 col 25: ;"        
        self.assertTrue(TestParser.test(input,expect,269)) 

    def test_while_stmt10(self):
        input = """ func_1: function integer() {
            n = a <= m;
            a = b >= f;
            a = b > f;         
            a = b < f;     
            b = b / v;
            b = b % j;
            b = n - m;            
            f = f || f || v;
        }"""
        expect = "successful"  
        self.assertTrue(TestParser.test(input,expect,270))                             

   #test do while statement combine expression
    def test_do_while_stmt1(self):
        input = """func1: function array [2,3,4] of float () {
          do {
            writeInt(i);
          } while (i == 0);       
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,271))        

    def test_do_while_stmt2(self):
        input = """func1: function array [2,3,4] of float () {
          do {
            writeInt(i);
          } while (i = 0);       
        }"""
        expect = "Error on line 4 col 21: ="
        self.assertTrue(TestParser.test(input,expect,272)) 

    def test_do_while_stmt3(self):
        input = """func1: function array [2,3,4] of float () {
          do {
          } while (i :: 0);       
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,273)) 

    def test_do_while_stmt4(self):
        input = """func1: function array [2,3,4] of float () {
          do {
          } while (i :: 0)       
        }"""
        expect = "Error on line 4 col 8: }"
        self.assertTrue(TestParser.test(input,expect,274))        

    def test_do_while_stmt5(self):
        input = """func1: function array [2,3,4] of float () {
          for (i = 5, , i + 1) 
            writeInt(i);
            a = a + 2 * b;             
        }"""
        expect = "Error on line 2 col 22: ,"
        self.assertTrue(TestParser.test(input,expect,275)) 

    def test_do_while_stmt6(self):
        input = """func1: function array [2,3,4] of float () {
          for (i = 5, i >= 10, i + 1) {      
          }
        }"""
        expect = "Error on line 3 col 10: }"
        self.assertTrue(TestParser.test(input,expect,276)) 

    def test_do_while_stmt7(self):
        input = """func1: function string () {
r, s: boolean;
r = 2.0;
a, b: array [5] of integer;
s = r * r + myPI;
a[0] = foo();
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,277))        

    def test_do_while_stmt8(self):
        input = """ func_1: function array [1,2,3] of boolean(var1: float, inherit var2: array [5] of string) inherit func_2 {
            n = a != b;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,278)) 

    def test_do_while_stmt9(self):
        input = """ func_1: function integer() inherit id_2 {
            n = !a;
            f = f || f ||;
        }"""
        expect = "Error on line 3 col 25: ;"        
        self.assertTrue(TestParser.test(input,expect,279)) 

    def test_do_while_stmt10(self):
        input = """ func_1: function integer() {
            n = a <= m;
            a = b >= f;
            a = b > f;         
            a = b < f;     
            b = b / v;
            b = b % j;
            b = n - m;            
            f = f || f || v;
        }"""
        expect = "successful"  
        self.assertTrue(TestParser.test(input,expect,280))         

   #test break continue return statement combine expression
    def test_bcr_stmt1(self):
        input = """func1: function array [2,3,4] of float () {
          do {
            writeInt(i);
            break;
          } while (i == 0);       
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,281))        

    def test_bcr_stmt2(self):
        input = """func1: function array [2,3,4] of float () {
          do {
            writeInt(i);
            break
          } while (i = 0);       
        }"""
        expect = "Error on line 5 col 10: }"
        self.assertTrue(TestParser.test(input,expect,282)) 

    def test_bcr_stmt3(self):
        input = """func1: function array [2,3,4] of float () {
          do {
            continue;
          } while (i :: 0);       
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,283)) 

    def test_bcr_stmt4(self):
        input = """func1: function array [2,3,4] of float () {
          do {
            continue
          } while (i :: 0)       
        }"""
        expect = "Error on line 4 col 10: }"
        self.assertTrue(TestParser.test(input,expect,284))        

    def test_bcr_stmt5(self):
        input = """func1: function array [2,3,4] of float () {
          for (i = 5, i<=4 , i + 1) 
            writeInt(i);
            a = a + 2 * b;
            return;             
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,285)) 

    def test_bcr_stmt6(self):
        input = """func1: function array [2,3,4] of float () {
          for (i = 5, i >= 10, i + 1) {   
            return a +b;   
          }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,286)) 

    def test_bcr_stmt7(self):
        input = """func1: function string () {
r, s: boolean;
r = 2.0;
a, b: array [5] of integer;
s = r * r + myPI;
a[0] = foo();
return
}"""
        expect = "Error on line 8 col 0: }"
        self.assertTrue(TestParser.test(input,expect,287))        

    def test_bcr_stmt8(self):
        input = """ func_1: function array [1,2,3] of boolean(var1: float, inherit var2: array [5] of string) inherit func_2 {
            n = a != b;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,288)) 

    def test_bcr_stmt9(self):
        input = """ func_1: function integer() inherit id_2 {
            n = !a;
            f = f || f ||;
        }"""
        expect = "Error on line 3 col 25: ;"        
        self.assertTrue(TestParser.test(input,expect,289)) 

    def test_bcr_stmt10(self):
        input = """ func_1: function integer() {
            n = a <= m;
            a = b >= f;
            a = b > f;         
            a = b < f;     
            b = b / v;
            b = b % j;
            b = n - m;            
            f = f || f || v;
        }"""
        expect = "successful"  
        self.assertTrue(TestParser.test(input,expect,290))      

   #test all statement combine expression
    def test_all_stmt1(self):
        input = """func1: function array [2,3,4] of float () {
          return foo(2 + x, 4.0 / y);
          goo();
          do {
            writeInt(i);
            break;
          } while (i == 0);       
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,281))        

    def test_all_stmt2(self):
        input = """func1: function array [2,3,4] of float () {
          do {
            writeInt(i);
            break
          } while (i = 0);       
        }"""
        expect = "Error on line 5 col 10: }"
        self.assertTrue(TestParser.test(input,expect,282)) 

    def test_all_stmt3(self):
        input = """func1: function array [2,3,4] of float () {
          do {
            continue;
          } while (i :: 0);       
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,283)) 

    def test_all_stmt4(self):
        input = """func1: function array [2,3,4] of float () {
          do {
            continue
          } while (i :: 0)       
        }"""
        expect = "Error on line 4 col 10: }"
        self.assertTrue(TestParser.test(input,expect,284))        

    def test_all_stmt5(self):
        input = """func1: function array [2,3,4] of float () {
          for (i = 5, i<=4 , i + 1) 
            writeInt(i);
            a = a + 2 * b;
            return;             
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,285)) 

    def test_all_stmt6(self):
        input = """func1: function array [2,3,4] of float () {
          for (i = 5, i >= 10, i + 1) {   
            return a +b;   
          }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,286)) 

    def test_all_stmt7(self):
        input = """func1: function string () {
r, s: boolean;
r = 2.0;
a, b: array [5] of integer;
s = r * r + myPI;
a[0] = foo();
return
}"""
        expect = "Error on line 8 col 0: }"
        self.assertTrue(TestParser.test(input,expect,287))        

    def test_all_stmt8(self):
        input = """ func_1: function array [1,2,3] of boolean(var1: float, inherit var2: array [5] of string) inherit func_2 {
            n = a != b;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,288)) 

    def test_all_stmt9(self):
        input = """ func_1: function integer() inherit id_2 {
            n = !a;
            f = f || f ||;
        }"""
        expect = "Error on line 3 col 25: ;"        
        self.assertTrue(TestParser.test(input,expect,289)) 

    def test_all_stmt10(self):
        input = """ func_1: function integer() {
            n = a <= m;
            a = b >= f;
            a = b > f;         
            a = b < f;     
            b = b / v;
            b = b % j;
            b = n - m;            
            f = f || f || v;
        }"""
        expect = "successful"  
        self.assertTrue(TestParser.test(input,expect,290))                    
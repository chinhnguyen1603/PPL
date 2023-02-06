import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    #test ID
    def test_identifier1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))
    def test_identifier2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc xyz", "abc,xyz,<EOF>", 102))
    def test_identifier3(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("0bc xyz", "0,bc,xyz,<EOF>", 103))
    def test_identifier4(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("_bc x2yz1", "_bc,x2yz1,<EOF>", 104))
    def test_identifier5(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("WriteLn123__df xyAz _12mkds", "WriteLn123__df,xyAz,_12mkds,<EOF>", 105))
    def test_identifier6(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("mddsd _abc1 _12mckm","mddsd,_abc1,_12mckm,<EOF>", 106))
    def test_identifier7(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("%AAc xyz", "%,AAc,xyz,<EOF>", 107))
    def test_identifier8(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("bc \n 2xyz \f", "bc,2,xyz,<EOF>", 108))
    def test_identifier9(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc. xyz", "abc,.,xyz,<EOF>", 109))
    def test_identifier10(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("b*c xyz", "b,*,c,xyz,<EOF>", 110))

    #test comment
    def test_comment1(self):
        self.assertTrue(TestLexer.test("/*12.e0 -101*/ chinh","chinh,<EOF>",111))        
    def test_comment2(self):
        self.assertTrue(TestLexer.test("// *12.e0 -101*) 11.E //11.1e2","<EOF>",112))  
    def test_comment3(self):
        self.assertTrue(TestLexer.test("//dsa ccf \n vua3","vua3,<EOF>",113))            
    def test_comment4(self):
        self.assertTrue(TestLexer.test("/*dsa ccf*/ \n vua4","vua4,<EOF>",114))   
    def test_comment5(self):
        """ Test Inline Comment """
        self.assertTrue(TestLexer.test(
            r"""
            // This is a line comment
            """,
            "<EOF>",
            115
        ))
    def test_comment6(self):
        """ Test MultiLine Comment """
        self.assertTrue(TestLexer.test(
            r"""
            /* This is a multi line comment
            abc xyz
            */
            """,
            "<EOF>",
            116
        ))
    def test_comment7(self):
        """ Test MultiLine Comment """
        self.assertTrue(TestLexer.test(
            r"""
            /* This is a multi line comment
            abc xyz
            */
            variable
            """,
            "variable,<EOF>",
            117
        ))                                   
    def test_comment8(self):
        self.assertTrue(TestLexer.test(" \t vua8 \n /*dsa ccf*/ ","vua8,<EOF>",118))  
    def test_comment9(self):
        self.assertTrue(TestLexer.test(" \b \r vua9  // dsa ccf*/ ","vua9,<EOF>",119))          
    def test_comment10(self):
        self.assertTrue(TestLexer.test(" \f vua10  // dsa ccf*/ \n vua ","vua10,vua,<EOF>",120))          

    #test keyword
    def test_keyword1(self):
        self.assertTrue(TestLexer.test("auto false","auto,false,<EOF>",121))
    def test_keyword2(self):
        self.assertTrue(TestLexer.test("Out Do","Out,Do,<EOF>",122))
    def test_keyword3(self):
        self.assertTrue(TestLexer.test("integervoid","integervoid,<EOF>",123))   
    def test_keyword4(self):
        self.assertTrue(TestLexer.test("""Break DoEndDo""","Break,DoEndDo,<EOF>",124))  
    def test_keyword5(self):
        self.assertTrue(TestLexer.test("ElseIf IfElse","ElseIf,IfElse,<EOF>",125))
    def test_keyword6(self):
        self.assertTrue(TestLexer.test("array boolean string","array,boolean,string,<EOF>",126))
    def test_keyword7(self):
        self.assertTrue(TestLexer.test("continue DoD3","continue,DoD3,<EOF>",127))
    def test_keyword8(self):
        self.assertTrue(TestLexer.test("___","___,<EOF>",128))   
    def test_keyword9(self):
        self.assertTrue(TestLexer.test("float while","float,while,<EOF>",129))  
    def test_keyword10(self):
        self.assertTrue(TestLexer.test("ElseIf If1Else","ElseIf,If1Else,<EOF>",130))        

    #test operator
    def test_operator1(self):
        self.assertTrue(TestLexer.test("+-*/%","+,-,*,/,%,<EOF>",131))
    def test_operator2(self):
        self.assertTrue(TestLexer.test("===","==,=,<EOF>",132))
    def test_operator3(self):
        self.assertTrue(TestLexer.test("<>=<=||","<,>=,<=,||,<EOF>",133))
    def test_operator4(self):
        self.assertTrue(TestLexer.test("&&&&","&&,&&,<EOF>",134))
    def test_operator5(self):
        self.assertTrue(TestLexer.test("&&&=","&&,Error Token &",135))
    def test_operator6(self):
        self.assertTrue(TestLexer.test("::+-!!=","::,+,-,!,!=,<EOF>",136))
    def test_operator7(self):
        self.assertTrue(TestLexer.test(":::","::,:,<EOF>",137))
    def test_operator8(self):
        self.assertTrue(TestLexer.test("=or<=<><>=-<=>","=,or,<=,<,>,<,>=,-,<=,>,<EOF>",138))
    def test_operator9(self):                            
        self.assertTrue(TestLexer.test("not<>=and>=mod<=-and","not,<,>=,and,>=,mod,<=,-,and,<EOF>",139))
    def test_operator10(self):
        self.assertTrue(TestLexer.test("=?","=,Error Token ?",140))        

    #test seperator
    def test_seperator1(self):
        self.assertTrue(TestLexer.test("( )","(,),<EOF>",141))
    def test_seperator2(self):
        self.assertTrue(TestLexer.test(" [ \t \r ]","[,],<EOF>",142))
    def test_seperator3(self):
        self.assertTrue(TestLexer.test(". , ; :",".,,,;,:,<EOF>",143))
    def test_seperator4(self):   
        self.assertTrue(TestLexer.test(",=:abc",",,=,:,abc,<EOF>",144))
    def test_seperator5(self):
        self.assertTrue(TestLexer.test("{c1d_}","{,c1d_,},<EOF>",145))
    def test_seperator6(self):                 
        self.assertTrue(TestLexer.test("[_12ds]","[,_12ds,],<EOF>",146))
    def test_seperator7(self):
        self.assertTrue(TestLexer.test(":=::",":,=,::,<EOF>",147))
    def test_seperator8(self):
        self.assertTrue(TestLexer.test("((~","(,(,Error Token ~",148))
    def test_seperator9(self):                            
        self.assertTrue(TestLexer.test("abc@","abc,Error Token @",149))
    def test_seperator10(self):
        self.assertTrue(TestLexer.test("==#","==,Error Token #",150))  

    #test INTLIT
    def test_int1(self):
        self.assertTrue(TestLexer.test("01233 12034","0,1233,12034,<EOF>",151))
    def test_int2(self):                            
        self.assertTrue(TestLexer.test("000","0,0,0,<EOF>",152))
    def test_int3(self):
        self.assertTrue(TestLexer.test("12_345_67 12_abc 12__23","1234567,12,_abc,12,__23,<EOF>",153))  
    def test_int4(self):
        self.assertTrue(TestLexer.test("_123 12_34","_123,1234,<EOF>",154))  

    #test BOOLLIT
    def test_bool1(self):
        self.assertTrue(TestLexer.test("true false true","true,false,true,<EOF>",155))  

    #test FLOATLIT
    def test_float1(self):
        self.assertTrue(TestLexer.test("1_234_56.345 1_234_56.3_45","123456.345,123456.3,_45,<EOF>",156))         
    def test_float2(self):                                      
        self.assertTrue(TestLexer.test("0.5 00.1232 1234..345","0.5,0,0.1232,1234.,.345,<EOF>",157)) 
    def test_float3(self):                                      
        self.assertTrue(TestLexer.test("1.2e3 1.2E3 1_234.4E+123 ","1.2e3,1.2E3,1234.4E+123,<EOF>",158)) 
    def test_float4(self):
        self.assertTrue(TestLexer.test("123456. .123456 .123456E-10","123456.,.123456,.123456,E,-,10,<EOF>",159)) 
    def test_float5(self):
        self.assertTrue(TestLexer.test("7E-10 8e+12 1.e+2","7E-10,8e+12,1.e+2,<EOF>",160))                                 

    #test STRINGLIT
    def test_string1(self):
        self.assertTrue(TestLexer.test("""\"This is a string containing tab\"""","This is a string containing tab,<EOF>",161)) 
    def test_string2(self):
        self.assertTrue(TestLexer.test("\"ahihi\"","ahihi,<EOF>",162)) 
    def test_string3(self):
        self.assertTrue(TestLexer.test("\"This is a string containing tab \t\"","This is a string containing tab \t,<EOF>",163))
    def test_string4(self):   
        self.assertTrue(TestLexer.test("\"This is a string containing tab\\t\"","This is a string containing tab\\t,<EOF>",164))
    def test_string5(self):
        self.assertTrue(TestLexer.test(""" \"He asked me: \\"Where is John?\\"\" ""","""He asked me: \\"Where is John?\\",<EOF>""",165))
    def test_string6(self):                                                           
        self.assertTrue(TestLexer.test("\"abc\" 0 \"12ab\\fc0.1\"","abc,0,12ab\\fc0.1,<EOF>",166))
    def test_string7(self):
        self.assertTrue(TestLexer.test("\"(IFq+lq(\"IhK6we GdvS{(}","(IFq+lq(,IhK6we,GdvS,{,(,},<EOF>",167))
    def test_string8(self):                                            
        self.assertTrue(TestLexer.test("\"((~\"","((~,<EOF>",168))
    def test_string9(self):                           
        self.assertTrue(TestLexer.test("\"abc@\"","abc@,<EOF>",169))
    def test_string10(self):
        self.assertTrue(TestLexer.test("""\"((~\\"\" ""","""((~\\",<EOF>""",170))      

    #test Unclose String
    def test_uncls1(self):
        self.assertTrue(TestLexer.test("\"chinhnguyen123","Unclosed String: chinhnguyen123",171))         
    def test_uncls12(self):                                      
        self.assertTrue(TestLexer.test("""\"((~\\" ""","""Unclosed String: ((~\\" """,172)) 
    def test_uncls13(self):                                      
        self.assertTrue(TestLexer.test("\"acnv \" \"abc","acnv ,Unclosed String: abc",173)) 
    def test_uncls14(self):
        self.assertTrue(TestLexer.test("123456. .123456 .123456E-10","123456.,.123456,.123456,E,-,10,<EOF>",174)) 
    def test_uncls15(self):
        self.assertTrue(TestLexer.test("7E-10 8e+12 1.e+2","7E-10,8e+12,1.e+2,<EOF>",175))  
 
    #test iilegal String
    def test_iilegal1(self):
        self.assertTrue(TestLexer.test(""" \"abc\\h def\"  ""","""Illegal Escape In String: abc\\h""",176))         
    def test_iilegal2(self):                                      
        self.assertTrue(TestLexer.test("\"aabbcc\pabc\"","Illegal Escape In String: aabbcc\p",176)) #bắt tới \p gặp illegal nên vứt abc ở sau 
    def test_iilegal3(self):                                      
        self.assertTrue(TestLexer.test("1.2e3 1.2E3 1_234.4E+123 ","1.2e3,1.2E3,1234.4E+123,<EOF>",177)) 
    def test_iilegal4(self):
        self.assertTrue(TestLexer.test("123456. .123456 .123456E-10","123456.,.123456,.123456,E,-,10,<EOF>",178)) 
    def test_iilegal5(self):
        self.assertTrue(TestLexer.test("7E-10 8e+12 1.e+2","7E-10,8e+12,1.e+2,<EOF>",179))  

    #test mixture     
    def test_mix1(self):
        self.assertTrue(TestLexer.test("abcd efgh 123 20E+10","abcd,efgh,123,20E+10,<EOF>",181)) 
    def test_mix2(self):
        self.assertTrue(TestLexer.test("""{1, 5, 7, 12}""","""{,1,,,5,,,7,,,12,},<EOF>""",182)) 
    def test_mix3(self):
        self.assertTrue(TestLexer.test("Parameter:,Body:][}.}[}{(EndIfIf.);;","Parameter,:,,,Body,:,],[,},.,},[,},{,(,EndIfIf,.,),;,;,<EOF>",183))
    def test_mix4(self):   
        self.assertTrue(TestLexer.test("1.e","1.,e,<EOF>",184))
    def test_mix5(self):
        self.assertTrue(TestLexer.test("1.e2","1.e2,<EOF>",185))
    def test_mix6(self):                 
        self.assertTrue(TestLexer.test("00E+10","0,0E+10,<EOF>",186))
    def test_mix7(self):
        self.assertTrue(TestLexer.test("""{1.3,4}""","""{,1.3,,,4,},<EOF>""",187))
    def test_mix8(self):
        self.assertTrue(TestLexer.test("-0.e21 02.e-10  121E+4 0.E09 4060E12","-,0.e21,0,2.e-10,121E+4,0.E09,4060E12,<EOF>",188))
    def test_mix9(self):                                                       
        self.assertTrue(TestLexer.test("a == True || False","a,==,True,||,False,<EOF>",189))
    def test_mix10(self):
        self.assertTrue(TestLexer.test("+-=-+!","+,-,=,-,+,!,<EOF>",190))    

    #test Error Token        
    def test_error1(self):
        self.assertTrue(TestLexer.test("\f","<EOF>",191)) 
    def test_error2(self):
        self.assertTrue(TestLexer.test("\t","<EOF>",192)) 
    def test_error3(self):
        self.assertTrue(TestLexer.test("\\t","Error Token \\",193))
    def test_error4(self):   
        self.assertTrue(TestLexer.test("\r \n \b","<EOF>",194))
    def test_error5(self):
        self.assertTrue(TestLexer.test("ab12?svn","ab12,Error Token ?",195))
    def test_error6(self):                 
        self.assertTrue(TestLexer.test("[{}_12d2s]","[,{,},_12d2s,],<EOF>",196))
    def test_error7(self):
        self.assertTrue(TestLexer.test("abcd\nef\nhihiVx%%^&&","abcd,ef,hihiVx,%,%,Error Token ^",197))
    def test_error8(self):
        self.assertTrue(TestLexer.test("\\","Error Token \\",198))
    def test_error9(self):                            
        self.assertTrue(TestLexer.test("abc123$","abc123,Error Token $",199))
    def test_error10(self):
        self.assertTrue(TestLexer.test("==!=#","==,!=,Error Token #",200))       
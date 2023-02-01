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


    #test comment
    def test_comment1(self):
        self.assertTrue(TestLexer.test("/*12.e0 -101*/ chinh","chinh,<EOF>",168))        
    def test_comment2(self):
        self.assertTrue(TestLexer.test("// *12.e0 -101*) 11.E //11.1e2","<EOF>",169))  
    def test_comment3(self):
        self.assertTrue(TestLexer.test("//dsa ccf \n vua3","vua3,<EOF>",174))            
    def test_comment4(self):
        self.assertTrue(TestLexer.test("/*dsa ccf*/ \n vua4","vua4,<EOF>",176))   
    def test_comment5(self):
        """ Test Inline Comment """
        self.assertTrue(TestLexer.test(
            r"""
            // This is a line comment
            """,
            "<EOF>",
            178
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
            179
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
            180
        ))                                   
    def test_comment8(self):
        self.assertTrue(TestLexer.test(" \t vua8 \n /*dsa ccf*/ ","vua8,<EOF>",181))  
    def test_comment9(self):
        self.assertTrue(TestLexer.test(" \b \r vua9  // dsa ccf*/ ","vua9,<EOF>",182))          
    def test_comment10(self):
        self.assertTrue(TestLexer.test(" \f vua10  // dsa ccf*/ \n vua ","vua10,vua,<EOF>",183))          
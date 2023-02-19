# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_decl.
    def visitVar_decl(self, ctx:MT22Parser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#global_var_decl.
    def visitGlobal_var_decl(self, ctx:MT22Parser.Global_var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#local_var_decl.
    def visitLocal_var_decl(self, ctx:MT22Parser.Local_var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameter_of_func.
    def visitParameter_of_func(self, ctx:MT22Parser.Parameter_of_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#list_parameter.
    def visitList_parameter(self, ctx:MT22Parser.List_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_decl.
    def visitFunc_decl(self, ctx:MT22Parser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_prototype.
    def visitFunc_prototype(self, ctx:MT22Parser.Func_prototypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_body.
    def visitFunc_body(self, ctx:MT22Parser.Func_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_decl.
    def visitBlock_decl(self, ctx:MT22Parser.Block_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#list_expr.
    def visitList_expr(self, ctx:MT22Parser.List_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#id_list.
    def visitId_list(self, ctx:MT22Parser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#operator.
    def visitOperator(self, ctx:MT22Parser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#string_operator.
    def visitString_operator(self, ctx:MT22Parser.String_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relational_operator.
    def visitRelational_operator(self, ctx:MT22Parser.Relational_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logical_first_operator.
    def visitLogical_first_operator(self, ctx:MT22Parser.Logical_first_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#adding_operator.
    def visitAdding_operator(self, ctx:MT22Parser.Adding_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#multiplying_operator.
    def visitMultiplying_operator(self, ctx:MT22Parser.Multiplying_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logical_second_operator.
    def visitLogical_second_operator(self, ctx:MT22Parser.Logical_second_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#sign_operator.
    def visitSign_operator(self, ctx:MT22Parser.Sign_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#index_operator.
    def visitIndex_operator(self, ctx:MT22Parser.Index_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt_decl.
    def visitStmt_decl(self, ctx:MT22Parser.Stmt_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#list_stmt.
    def visitList_stmt(self, ctx:MT22Parser.List_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#boolean_literal.
    def visitBoolean_literal(self, ctx:MT22Parser.Boolean_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#literal.
    def visitLiteral(self, ctx:MT22Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atomic_typ.
    def visitAtomic_typ(self, ctx:MT22Parser.Atomic_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#index_array.
    def visitIndex_array(self, ctx:MT22Parser.Index_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_literal.
    def visitArray_literal(self, ctx:MT22Parser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#typ.
    def visitTyp(self, ctx:MT22Parser.TypContext):
        return self.visitChildren(ctx)



del MT22Parser
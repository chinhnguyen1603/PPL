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


    # Visit a parse tree produced by MT22Parser#program_body_list.
    def visitProgram_body_list(self, ctx:MT22Parser.Program_body_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#program_body_list_tail.
    def visitProgram_body_list_tail(self, ctx:MT22Parser.Program_body_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_decl_or_func_decl.
    def visitVar_decl_or_func_decl(self, ctx:MT22Parser.Var_decl_or_func_declContext):
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


    # Visit a parse tree produced by MT22Parser#assign_va_list_expr.
    def visitAssign_va_list_expr(self, ctx:MT22Parser.Assign_va_list_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameter_of_func.
    def visitParameter_of_func(self, ctx:MT22Parser.Parameter_of_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#list_parameter.
    def visitList_parameter(self, ctx:MT22Parser.List_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#id_list.
    def visitId_list(self, ctx:MT22Parser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_decl.
    def visitFunc_decl(self, ctx:MT22Parser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_prototype.
    def visitFunc_prototype(self, ctx:MT22Parser.Func_prototypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#list_parameter_rong.
    def visitList_parameter_rong(self, ctx:MT22Parser.List_parameter_rongContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_body.
    def visitFunc_body(self, ctx:MT22Parser.Func_bodyContext):
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


    # Visit a parse tree produced by MT22Parser#array_literal_type.
    def visitArray_literal_type(self, ctx:MT22Parser.Array_literal_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#list_literal.
    def visitList_literal(self, ctx:MT22Parser.List_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#typ.
    def visitTyp(self, ctx:MT22Parser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#list_expr.
    def visitList_expr(self, ctx:MT22Parser.List_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression.
    def visitExpression(self, ctx:MT22Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#string_expr.
    def visitString_expr(self, ctx:MT22Parser.String_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relation_expr.
    def visitRelation_expr(self, ctx:MT22Parser.Relation_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logical_first_expr.
    def visitLogical_first_expr(self, ctx:MT22Parser.Logical_first_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#adding_expr.
    def visitAdding_expr(self, ctx:MT22Parser.Adding_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#multiplying_expr.
    def visitMultiplying_expr(self, ctx:MT22Parser.Multiplying_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logical_second_expr.
    def visitLogical_second_expr(self, ctx:MT22Parser.Logical_second_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#sign_expr.
    def visitSign_expr(self, ctx:MT22Parser.Sign_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#index_expr.
    def visitIndex_expr(self, ctx:MT22Parser.Index_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#operand.
    def visitOperand(self, ctx:MT22Parser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_call_exp.
    def visitFunc_call_exp(self, ctx:MT22Parser.Func_call_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#list_expr_hoi.
    def visitList_expr_hoi(self, ctx:MT22Parser.List_expr_hoiContext):
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


    # Visit a parse tree produced by MT22Parser#assign_stmt.
    def visitAssign_stmt(self, ctx:MT22Parser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#index_operator_hoi.
    def visitIndex_operator_hoi(self, ctx:MT22Parser.Index_operator_hoiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#if_stmt.
    def visitIf_stmt(self, ctx:MT22Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#duoi_else.
    def visitDuoi_else(self, ctx:MT22Parser.Duoi_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#break_stmt.
    def visitBreak_stmt(self, ctx:MT22Parser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#for_stmt.
    def visitFor_stmt(self, ctx:MT22Parser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#while_stmt.
    def visitWhile_stmt(self, ctx:MT22Parser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#list_stmt_cong.
    def visitList_stmt_cong(self, ctx:MT22Parser.List_stmt_congContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#do_while_stmt.
    def visitDo_while_stmt(self, ctx:MT22Parser.Do_while_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call_stmt.
    def visitCall_stmt(self, ctx:MT22Parser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_stmt.
    def visitReturn_stmt(self, ctx:MT22Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression_hoi.
    def visitExpression_hoi(self, ctx:MT22Parser.Expression_hoiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continue_stmt.
    def visitContinue_stmt(self, ctx:MT22Parser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#list_stmt_rong.
    def visitList_stmt_rong(self, ctx:MT22Parser.List_stmt_rongContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_stmt.
    def visitBlock_stmt(self, ctx:MT22Parser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_body_list.
    def visitBlock_body_list(self, ctx:MT22Parser.Block_body_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_body_list_tail.
    def visitBlock_body_list_tail(self, ctx:MT22Parser.Block_body_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_decl_or_stmt_decl.
    def visitVar_decl_or_stmt_decl(self, ctx:MT22Parser.Var_decl_or_stmt_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#scalar_var.
    def visitScalar_var(self, ctx:MT22Parser.Scalar_varContext):
        return self.visitChildren(ctx)



del MT22Parser
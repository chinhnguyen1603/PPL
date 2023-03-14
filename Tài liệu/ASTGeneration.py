from typing import BinaryIO
from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *
from functools import reduce

class ASTGeneration(BKOOLVisitor):

    def visitProgram(self,ctx):
        return Program([self.visit(x) for x in ctx.classDecl()])
    def visitClassDecl(self,ctx):
        lst = reduce(lambda x,y: x + self.visit(y), ctx.member(), [])
        if ctx.EXTENDS():
            return ClassDecl(Id(ctx.ID(0).getText()), lst, Id(ctx.ID(1).getText()))
        return ClassDecl(Id(ctx.ID(0).getText()), lst, None)
    def visitMember(self,ctx):
        if ctx.attribute():
            return self.visit(ctx.attribute())
        else:
            x = self.visit(ctx.method())
            if ctx.STATIC():
                return [MethodDecl(Static(), x[0], x[1], x[2], x[3])]
            return [MethodDecl(Instance(),  x[0], x[1], x[2], x[3])]
    def visitAttribute(self,ctx):
        if ctx.mutable():
            if ctx.STATIC():
                return [AttributeDecl(Static(), x) for x in self.visit(ctx.mutable())]
            return [AttributeDecl(Instance(), x) for x in self.visit(ctx.mutable())]
        else:
            if ctx.STATIC():
                return [AttributeDecl(Static(), x) for x in self.visit(ctx.immutable())]
            return  [AttributeDecl(Instance(), x) for x in self.visit(ctx.immutable())]
    def visitMutable(self,ctx):
        lst = self.visit(ctx.tailMutable())
        return [VarDecl(x[0], self.visit(ctx.mType()), x[1]) for x in lst]
    def visitTailMutable(self,ctx):
        return [self.visit(x) for x in ctx.initialMutable()]
    def visitInitialMutable(self,ctx):
        if ctx.EQUAL():
            return Id(ctx.ID().getText()), self.visit(ctx.exp())
        return Id(ctx.ID().getText()), None
    def visitImmutable(self,ctx):
        lst = self.visit(ctx.tailImmutable())
        return [ConstDecl(x[0], self.visit(ctx.mType()), x[1]) for x in lst]
    def visitTailImmutable(self,ctx):
        return [self.visit(x) for x in ctx.initialImmutable()]
    def visitInitialImmutable(self,ctx):
        if ctx.EQUAL():
            return Id(ctx.ID().getText()), self.visit(ctx.exp())
        return Id(ctx.ID().getText()), None
    def visitClassType(self,ctx):
        return ClassType(Id(ctx.ID().getText()))
    def visitArrayType(self,ctx):
        return ArrayType(int(ctx.INTEGER_LITERAL().getText()), self.visit(ctx.elementType()))
    def visitElementType(self,ctx):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.VOID():
            return VoidType()
        return self.visit(ctx.classType())
    def visitMethod(self,ctx):
        if ctx.contructorMethod():
            return self.visit(ctx.contructorMethod())
        else:
            x = Id(ctx.ID().getText())
            y = self.visit(ctx.listParameter()) if ctx.listParameter() else []
            z = self.visit(ctx.mType())
            k = self.visit(ctx.blockStmt())
            return x,y,z,k
    def visitContructorMethod(self,ctx):
        x = Id("<init>")
        y = self.visit(ctx.listParameter()) if ctx.listParameter() else []
        z = self.visit(ctx.blockStmt())
        return x,y,None,z
    def visitMType(self,ctx):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.VOID():
            return VoidType()
        elif ctx.classType():
            return self.visit(ctx.classType())
        return self.visit(ctx.arrayType())
    def visitListParameter(self,ctx):
        return reduce(lambda x,y: x + self.visit(y), ctx.parameter(), [])
    def visitParameter(self,ctx):
        return [VarDecl(Id(x.getText()), self.visit(ctx.mType()), None) for x in ctx.ID()]
    def visitBlockStmt(self,ctx):
        return self.visit(ctx.contentBlock())
    def visitContentBlock(self,ctx):
        lst = reduce(lambda x,y: x + self.visit(y), ctx.listValDecl(), [])
        return Block(lst, [self.visit(x) for x in ctx.listStmt()] if ctx.listStmt() else [])
    def visitListValDecl(self,ctx):
        if ctx.FINAL():
            return self.visit(ctx.immutable())
        return self.visit(ctx.mutable())
    def visitListStmt(self,ctx):
        if ctx.blockStmt():
            return self.visit(ctx.blockStmt())
        elif ctx.assignmentStmt():
            return self.visit(ctx.assignmentStmt())
        elif ctx.ifStmt():
            return self.visit(ctx.ifStmt())
        elif ctx.forStmt():
            return self.visit(ctx.forStmt())
        elif ctx.breakStmt():
            return self.visit(ctx.breakStmt())
        elif ctx.continueStmt():
            return self.visit(ctx.continueStmt())
        elif ctx.returnStmt():
            return self.visit(ctx.returnStmt())
        return self.visit(ctx.methodInvocationStmt())
    def visitAssignmentStmt(self,ctx):
        return Assign(self.visit(ctx.exp(0)), self.visit(ctx.exp(1)))
    def visitIfStmt(self,ctx):
        if ctx.ELSE():
            return If(self.visit(ctx.exp()), self.visit(ctx.listStmt(0)), self.visit(ctx.listStmt(1)))
        return If(self.visit(ctx.exp()), self.visit(ctx.listStmt(0)), None)
    def visitForStmt(self,ctx):
        if ctx.TO():
            return For(Id(ctx.ID().getText()), self.visit(ctx.exp(0)), self.visit(ctx.exp(1)), True, self.visit(ctx.listStmt()))
        return For(Id(ctx.ID().getText()), self.visit(ctx.exp(0)), self.visit(ctx.exp(1)), False, self.visit(ctx.listStmt()))
    def visitBreakStmt(self,ctx):
        return Break()
    def visitContinueStmt(self,ctx):
        return Continue()
    def visitReturnStmt(self,ctx):
        return Return(self.visit(ctx.exp()))
    def visitMethodInvocationStmt(self,ctx):
        x = self.visit(ctx.methodCall())
        return CallStmt(self.visit(ctx.exp()), x[0], x[1])
    def visitExp(self,ctx):
        if ctx.LESSTHAN():
            return BinaryOp(ctx.LESSTHAN().getText(), self.visit(ctx.exp1(0)), self.visit(ctx.exp1(1)))
        elif ctx.GREATERTHAN():
            return BinaryOp(ctx.GREATERTHAN().getText(), self.visit(ctx.exp1(0)), self.visit(ctx.exp1(1)))
        elif ctx.LESSTHANOREQUAL():
            return BinaryOp(ctx.LESSTHANOREQUAL().getText(), self.visit(ctx.exp1(0)), self.visit(ctx.exp1(1)))
        elif ctx.GREATERTHANOREQUAL():
            return BinaryOp(ctx.GREATERTHANOREQUAL().getText(), self.visit(ctx.exp1(0)), self.visit(ctx.exp1(1)))
        return self.visit(ctx.exp1(0))
    def visitExp1(self,ctx):
        if ctx.EQ():
            return BinaryOp(ctx.EQ().getText(), self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))
        elif ctx.NOT_EQ():
            return BinaryOp(ctx.NOT_EQ().getText(), self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))
        return self.visit(ctx.exp2(0))
    def visitExp2(self,ctx):
        if ctx.AND():
            return BinaryOp(ctx.AND().getText(), self.visit(ctx.exp2()), self.visit(ctx.exp3()))
        elif ctx.OR():
            return BinaryOp(ctx.OR().getText(), self.visit(ctx.exp2()), self.visit(ctx.exp3()))
        return self.visit(ctx.exp3())
    def visitExp3(self,ctx):
        if ctx.SUB():
            return BinaryOp(ctx.SUB().getText(), self.visit(ctx.exp3()), self.visit(ctx.exp4()))
        elif ctx.ADD():
            return BinaryOp(ctx.ADD().getText(), self.visit(ctx.exp3()), self.visit(ctx.exp4()))
        return self.visit(ctx.exp4())
    def visitExp4(self,ctx):
        if ctx.MUL():
            return BinaryOp(ctx.MUL().getText(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))
        elif ctx.DIVINT():
            return BinaryOp(ctx.DIVINT().getText(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))
        elif ctx.DIVFLOAT():
            return BinaryOp(ctx.DIVFLOAT().getText(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))
        elif ctx.MOD():
            return BinaryOp(ctx.MOD().getText(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))
        return self.visit(ctx.exp5())
    def visitExp5(self,ctx):
        if ctx.CONCATENATION():
            return BinaryOp(ctx.CONCATENATION().getText(), self.visit(ctx.exp5()), self.visit(ctx.exp6()))
        return self.visit(ctx.exp6())
    def visitExp6(self,ctx):
        if ctx.NOT():
            return UnaryOp(ctx.NOT().getText(), self.visit(ctx.exp6()))
        return self.visit(ctx.exp7())
    def visitExp7(self,ctx):
        if ctx.ADD():
            return UnaryOp(ctx.ADD().getText(), self.visit(ctx.exp7()))
        elif ctx.SUB():
            return UnaryOp(ctx.SUB().getText(), self.visit(ctx.exp7()))
        return self.visit(ctx.exp8())
    def visitExp8(self,ctx):
        if ctx.indexExp():
            return ArrayCell(self.visit(ctx.exp9()), self.visit(ctx.indexExp()))
        return self.visit(ctx.exp9())
    def visitExp9(self,ctx):
        if ctx.ID():
            return FieldAccess(self.visit(ctx.exp9()), Id(ctx.ID().getText()))
        elif ctx.methodCall():
            x = self.visit(ctx.methodCall())
            return CallExpr(self.visit(ctx.exp9()), x[0], x[1])
        return self.visit(ctx.exp10())
    def visitMethodCall(self,ctx):
        x = Id(ctx.ID().getText())
        if ctx.listExp():
            y = self.visit(ctx.listExp())
            return x,y
        return x,[]
    def visitExp10(self,ctx):
        if ctx.NEW() and ctx.listExp():
            return NewExpr(Id(ctx.ID().getText()), self.visit(ctx.listExp()))
        elif ctx.NEW() and not ctx.listExp():
            return NewExpr(Id(ctx.ID().getText()), [])
        return self.visit(ctx.exp11())
    def visitExp11(self,ctx):
        if ctx.exp():
            return self.visit(ctx.exp())
        elif ctx.literal():
            return self.visit(ctx.literal())
        return Id(ctx.ID().getText())
    def visitLiteral(self,ctx):
        if ctx.INTEGER_LITERAL():
            return IntLiteral(int(ctx.INTEGER_LITERAL().getText()))
        elif ctx.FLOAT_LITERAL():
            return FloatLiteral(float(ctx.FLOAT_LITERAL().getText()))
        elif ctx.booleanLiteral():
            return self.visit(ctx.booleanLiteral())
        elif ctx.STRING_LITERAL():
            return StringLiteral(ctx.STRING_LITERAL().getText())
        elif ctx.NIL():
            return NullLiteral()
        elif ctx.THIS():
            return SelfLiteral()
        return self.visit(ctx.arrayLiteral())
    def visitArrayLiteral(self,ctx):
        return ArrayLiteral(self.visit(ctx.listElement()))
    def visitListElement(self,ctx):
        return [self.visit(x) for x in ctx.element()]  
    def visitElement(self,ctx):
        if ctx.INTEGER_LITERAL():
            return IntLiteral(int(ctx.INTEGER_LITERAL().getText()))
        elif ctx.FLOAT_LITERAL():
            return FloatLiteral(float(ctx.FLOAT_LITERAL().getText()))
        elif ctx.booleanLiteral():
            return self.visit(ctx.booleanLiteral())
        elif ctx.STRING_LITERAL():
            return StringLiteral(ctx.STRING_LITERAL().getText())
        elif ctx.NIL():
            return NullLiteral()
        return SelfLiteral()
    def visitBooleanLiteral(self,ctx):
        if ctx.TRUE():
            return BooleanLiteral(True)
        return BooleanLiteral(False)
    def visitIndexExp(self,ctx):
        return self.visit(ctx.exp())
    def visitListExp(self,ctx):
        return [self.visit(x) for x in ctx.exp()]
    

    

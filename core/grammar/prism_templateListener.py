# Generated from prism_template.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .prism_templateParser import prism_templateParser
else:
    from prism_templateParser import prism_templateParser

# This class defines a complete listener for a parse tree produced by prism_templateParser.
class prism_templateListener(ParseTreeListener):

    # Enter a parse tree produced by prism_templateParser#expression.
    def enterExpression(self, ctx:prism_templateParser.ExpressionContext):
        pass

    # Exit a parse tree produced by prism_templateParser#expression.
    def exitExpression(self, ctx:prism_templateParser.ExpressionContext):
        pass


    # Enter a parse tree produced by prism_templateParser#program.
    def enterProgram(self, ctx:prism_templateParser.ProgramContext):
        pass

    # Exit a parse tree produced by prism_templateParser#program.
    def exitProgram(self, ctx:prism_templateParser.ProgramContext):
        pass


    # Enter a parse tree produced by prism_templateParser#statements.
    def enterStatements(self, ctx:prism_templateParser.StatementsContext):
        pass

    # Exit a parse tree produced by prism_templateParser#statements.
    def exitStatements(self, ctx:prism_templateParser.StatementsContext):
        pass


    # Enter a parse tree produced by prism_templateParser#model_type.
    def enterModel_type(self, ctx:prism_templateParser.Model_typeContext):
        pass

    # Exit a parse tree produced by prism_templateParser#model_type.
    def exitModel_type(self, ctx:prism_templateParser.Model_typeContext):
        pass


    # Enter a parse tree produced by prism_templateParser#common_declarations.
    def enterCommon_declarations(self, ctx:prism_templateParser.Common_declarationsContext):
        pass

    # Exit a parse tree produced by prism_templateParser#common_declarations.
    def exitCommon_declarations(self, ctx:prism_templateParser.Common_declarationsContext):
        pass


    # Enter a parse tree produced by prism_templateParser#common_declaration.
    def enterCommon_declaration(self, ctx:prism_templateParser.Common_declarationContext):
        pass

    # Exit a parse tree produced by prism_templateParser#common_declaration.
    def exitCommon_declaration(self, ctx:prism_templateParser.Common_declarationContext):
        pass


    # Enter a parse tree produced by prism_templateParser#constant_declaration.
    def enterConstant_declaration(self, ctx:prism_templateParser.Constant_declarationContext):
        pass

    # Exit a parse tree produced by prism_templateParser#constant_declaration.
    def exitConstant_declaration(self, ctx:prism_templateParser.Constant_declarationContext):
        pass


    # Enter a parse tree produced by prism_templateParser#formula_declaration.
    def enterFormula_declaration(self, ctx:prism_templateParser.Formula_declarationContext):
        pass

    # Exit a parse tree produced by prism_templateParser#formula_declaration.
    def exitFormula_declaration(self, ctx:prism_templateParser.Formula_declarationContext):
        pass


    # Enter a parse tree produced by prism_templateParser#label_declaration.
    def enterLabel_declaration(self, ctx:prism_templateParser.Label_declarationContext):
        pass

    # Exit a parse tree produced by prism_templateParser#label_declaration.
    def exitLabel_declaration(self, ctx:prism_templateParser.Label_declarationContext):
        pass


    # Enter a parse tree produced by prism_templateParser#global_declaration.
    def enterGlobal_declaration(self, ctx:prism_templateParser.Global_declarationContext):
        pass

    # Exit a parse tree produced by prism_templateParser#global_declaration.
    def exitGlobal_declaration(self, ctx:prism_templateParser.Global_declarationContext):
        pass


    # Enter a parse tree produced by prism_templateParser#init_declaration.
    def enterInit_declaration(self, ctx:prism_templateParser.Init_declarationContext):
        pass

    # Exit a parse tree produced by prism_templateParser#init_declaration.
    def exitInit_declaration(self, ctx:prism_templateParser.Init_declarationContext):
        pass


    # Enter a parse tree produced by prism_templateParser#module_declarations.
    def enterModule_declarations(self, ctx:prism_templateParser.Module_declarationsContext):
        pass

    # Exit a parse tree produced by prism_templateParser#module_declarations.
    def exitModule_declarations(self, ctx:prism_templateParser.Module_declarationsContext):
        pass


    # Enter a parse tree produced by prism_templateParser#module_content.
    def enterModule_content(self, ctx:prism_templateParser.Module_contentContext):
        pass

    # Exit a parse tree produced by prism_templateParser#module_content.
    def exitModule_content(self, ctx:prism_templateParser.Module_contentContext):
        pass


    # Enter a parse tree produced by prism_templateParser#module_rename.
    def enterModule_rename(self, ctx:prism_templateParser.Module_renameContext):
        pass

    # Exit a parse tree produced by prism_templateParser#module_rename.
    def exitModule_rename(self, ctx:prism_templateParser.Module_renameContext):
        pass


    # Enter a parse tree produced by prism_templateParser#id_assign.
    def enterId_assign(self, ctx:prism_templateParser.Id_assignContext):
        pass

    # Exit a parse tree produced by prism_templateParser#id_assign.
    def exitId_assign(self, ctx:prism_templateParser.Id_assignContext):
        pass


    # Enter a parse tree produced by prism_templateParser#id_assign_block.
    def enterId_assign_block(self, ctx:prism_templateParser.Id_assign_blockContext):
        pass

    # Exit a parse tree produced by prism_templateParser#id_assign_block.
    def exitId_assign_block(self, ctx:prism_templateParser.Id_assign_blockContext):
        pass


    # Enter a parse tree produced by prism_templateParser#module_desc.
    def enterModule_desc(self, ctx:prism_templateParser.Module_descContext):
        pass

    # Exit a parse tree produced by prism_templateParser#module_desc.
    def exitModule_desc(self, ctx:prism_templateParser.Module_descContext):
        pass


    # Enter a parse tree produced by prism_templateParser#var_declarations.
    def enterVar_declarations(self, ctx:prism_templateParser.Var_declarationsContext):
        pass

    # Exit a parse tree produced by prism_templateParser#var_declarations.
    def exitVar_declarations(self, ctx:prism_templateParser.Var_declarationsContext):
        pass


    # Enter a parse tree produced by prism_templateParser#var_declaration.
    def enterVar_declaration(self, ctx:prism_templateParser.Var_declarationContext):
        pass

    # Exit a parse tree produced by prism_templateParser#var_declaration.
    def exitVar_declaration(self, ctx:prism_templateParser.Var_declarationContext):
        pass


    # Enter a parse tree produced by prism_templateParser#range_declaration.
    def enterRange_declaration(self, ctx:prism_templateParser.Range_declarationContext):
        pass

    # Exit a parse tree produced by prism_templateParser#range_declaration.
    def exitRange_declaration(self, ctx:prism_templateParser.Range_declarationContext):
        pass


    # Enter a parse tree produced by prism_templateParser#guard_declarations.
    def enterGuard_declarations(self, ctx:prism_templateParser.Guard_declarationsContext):
        pass

    # Exit a parse tree produced by prism_templateParser#guard_declarations.
    def exitGuard_declarations(self, ctx:prism_templateParser.Guard_declarationsContext):
        pass


    # Enter a parse tree produced by prism_templateParser#guard_declaration.
    def enterGuard_declaration(self, ctx:prism_templateParser.Guard_declarationContext):
        pass

    # Exit a parse tree produced by prism_templateParser#guard_declaration.
    def exitGuard_declaration(self, ctx:prism_templateParser.Guard_declarationContext):
        pass


    # Enter a parse tree produced by prism_templateParser#guard_updates.
    def enterGuard_updates(self, ctx:prism_templateParser.Guard_updatesContext):
        pass

    # Exit a parse tree produced by prism_templateParser#guard_updates.
    def exitGuard_updates(self, ctx:prism_templateParser.Guard_updatesContext):
        pass


    # Enter a parse tree produced by prism_templateParser#guard_update.
    def enterGuard_update(self, ctx:prism_templateParser.Guard_updateContext):
        pass

    # Exit a parse tree produced by prism_templateParser#guard_update.
    def exitGuard_update(self, ctx:prism_templateParser.Guard_updateContext):
        pass


    # Enter a parse tree produced by prism_templateParser#state_update.
    def enterState_update(self, ctx:prism_templateParser.State_updateContext):
        pass

    # Exit a parse tree produced by prism_templateParser#state_update.
    def exitState_update(self, ctx:prism_templateParser.State_updateContext):
        pass


    # Enter a parse tree produced by prism_templateParser#replacement.
    def enterReplacement(self, ctx:prism_templateParser.ReplacementContext):
        pass

    # Exit a parse tree produced by prism_templateParser#replacement.
    def exitReplacement(self, ctx:prism_templateParser.ReplacementContext):
        pass



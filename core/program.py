from typing import List
from core.grammar.PrismTemplateLexer import PrismTemplateLexer


class Program:
    def __init__(self, model, common_declarations, modules, init):
        self._model = model
        self._common_declarations = common_declarations
        self._modules = modules
        self._init_declaration = init

    @property
    def model(self):
        return self._model

    @property
    def common_declarations(self):
        return self._common_declarations

    @property
    def modules(self):
        return self._modules

    @property
    def init_declaration(self):
        return self._init_declaration

    def __str__(self):
        result = ""

        if self._model is not None:
            result = str(self._model)

        if self._modules is not None:
            for module_declaration in self._modules:
                if len(result) > 0:
                    result = "{}\n\n{}".format(result, str(module_declaration))
                else:
                    result = str(str(module_declaration))

        if self._init_declaration is not None:
            result = "{}\n\n{}".format(result, str(self._init_declaration))

        return result


class Model:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def __str__(self):
        return str(self._name)


class ModuleDesc:
    def __init__(self, name, var_declarations, guard_declarations):
        self._name = name
        self._var_declarations = var_declarations
        self._guard_declarations = guard_declarations

    @property
    def name(self):
        return self._name

    @property
    def var_declarations(self):
        return self._var_declarations

    @property
    def guard_declarations(self):
        return self._guard_declarations

    def __str__(self):
        literal_names = PrismTemplateLexer.literalNames
        result = "{} {}\n".format(literal_names[PrismTemplateLexer.MODULE], str(self._name))

        if self._var_declarations is not None:
            for var_declaration in self._var_declarations:
                result = "{}\n  {}".format(result, str(var_declaration))

        if self._guard_declarations is not None:
            result = "{}\n".format(result)
            for guard_declaration in self._guard_declarations:
                result = "{}\n  {}".format(result, str(guard_declaration))

        return "{}\n{}".format(result, literal_names[PrismTemplateLexer.ENDMODULE])


class ModuleRename:
    def __init__(self, id_assigns: List):
        self._id_assigns = id_assigns

    @property
    def id_assigns(self):
        return self._id_assigns

    def __str__(self):
        literal_names = PrismTemplateLexer.literalNames
        result = "{} {}".format(literal_names[PrismTemplateLexer.MODULE], str(self._id_assigns[0]))

        if len(self._id_assigns) > 1:
            str_assigns = list(map(lambda id_assign: str(id_assign), self._id_assigns[1:]))
            result = "{} [{}]".format(result, ", ".join(str_assigns))

        return "{}\n{}".format(result, literal_names[PrismTemplateLexer.ENDMODULE])


class GlobalVarDeclaration:
    def __init__(self, var_declaration: VarDeclaration):
        self._var_declaration = var_declaration

    @property
    def var_declaration(self):
        return self._var_declaration

    def __str__(self):
        literal_names = PrismTemplateLexer.literalNames
        global_token = literal_names[PrismTemplateLexer.GLOBAL]
        semicolon_token = literal_names[PrismTemplateLexer.SEMICOLON]
        return "{} {}{}".format(global_token, str(self._var_declaration), semicolon_token)


class VarDeclaration:
    def __init__(self, name, var_type):
        self._name = name
        self._var_type = var_type

    @property
    def name(self):
        return self._name

    @property
    def var_type(self):
        return self._var_type

    def __str__(self):
        literal_names = PrismTemplateLexer.literalNames
        colon_token = literal_names[PrismTemplateLexer.COLON]
        semicolon_token = literal_names[PrismTemplateLexer.SEMICOLON]
        return "{} {} {}{}".format(str(self._name), colon_token, str(self._var_type), semicolon_token)


class Formula:
    def __init__(self, name, expression):
        self._name = name
        self._expression = expression

    @property
    def name(self):
        return self._name

    @property
    def expression(self):
        return self._expression

    def __str__(self):
        literal_names = PrismTemplateLexer.literalNames
        eq_token = literal_names[PrismTemplateLexer.EQ]
        semicolon_token = literal_names[PrismTemplateLexer.SEMICOLON]

        return "{} {} {}{}".format(str(self._name), eq_token, str(self._expression), semicolon_token)


class Constant:
    def __init__(self, const_type, name, expression):
        self._const_type = const_type
        self._name = name
        self._expression = expression

    @property
    def const_type(self):
        return self._const_type

    @property
    def name(self):
        return self._name

    @property
    def expression(self):
        return self._expression

    def __str__(self):
        literal_names = PrismTemplateLexer.literalNames
        const_token = literal_names[PrismTemplateLexer.CONST]
        eq_token = literal_names[PrismTemplateLexer.EQ]
        semicolon_token = literal_names[PrismTemplateLexer.SEMICOLON]

        return "{} {} {} {}{}".format(const_token, str(self._name), eq_token, str(self._expression), semicolon_token)


class Init:
    def __init__(self, expression):
        self._expression = expression

    @property
    def expression(self):
        return self._expression

    def __str__(self):
        literal_names = PrismTemplateLexer.literalNames
        begin_init_token = literal_names[PrismTemplateLexer.INIT]
        end_init_token = literal_names[PrismTemplateLexer.ENDINIT]

        return "{}\n  {}\n{}".format(begin_init_token, str(self._expression), end_init_token)


class GuardDeclaration:
    def __init__(self, label, expression, updates):
        self._label = label
        self._expression = expression
        self._updates = updates

    @property
    def label(self):
        return self._label

    @property
    def expression(self):
        return self._expression

    @property
    def updates(self):
        return self._updates

    def __str__(self):
        literal_names = PrismTemplateLexer.literalNames
        rarrow_token = literal_names[PrismTemplateLexer.RARROW]
        plus_token = literal_names[PrismTemplateLexer.PLUS]
        semicolon_token = literal_names[PrismTemplateLexer.SEMICOLON]

        if self._label is not None:
            result = "[{}]".format(str(self._label))
        else:
            result = "[]"

        result = "{} {} {}".format(result, str(self._expression), rarrow_token)

        result = "{} {}".format(result, str(self._updates[0]))
        for update in self._updates[1:]:
            result = "{} {} {}".format(result, plus_token, str(update))

        return "{}{}".format(result, semicolon_token)


class GuardUpdate:
    def __init__(self, expression, state_updates):
        self._expression = expression
        self._state_updates = state_updates

    @property
    def expression(self):
        return self._expression

    @property
    def state_updates(self):
        return self._state_updates

    def __str__(self):
        literal_names = PrismTemplateLexer.literalNames
        colon_token = literal_names[PrismTemplateLexer.COLON]
        and_token = literal_names[PrismTemplateLexer.AND]

        statements = list(map(lambda update: str(update), self._state_updates))
        return "{}{}{}".format(str(self._expression), colon_token, and_token.join(statements))


class StateUpdate:
    def __init__(self, identifier, expression):
        self._identifier = identifier
        self._expression = expression

    @property
    def identifier(self):
        return self._identifier

    @property
    def expression(self):
        return self._expression

    def __str__(self):
        literal_names = PrismTemplateLexer.literalNames
        eq_token = literal_names[PrismTemplateLexer.EQ]

        return "{} {} {}".format(str(self._identifier), eq_token, str(self._expression))

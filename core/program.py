from typing import List


class Program:
    def __init__(self, model: Model, common_declarations: List, modules: List, init: Init):
        self._module_type = model
        self._common_declarations = common_declarations
        self._modules = modules
        self._init = init


class Model:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


class ModuleDesc:
    def __init__(self, name, var_declarations: List, guard_declarations: List):
        self._name = name
        self._var_declarations = var_declarations
        self._guard_declarations = guard_declarations


class ModuleRename:
    def __init__(self, id_assigns: List):
        self._id_assigns = id_assigns


class GlobalVarDeclaration:
    def __init__(self, var: VarDeclaration):
        self._var = var


class VarDeclaration:
    def __init__(self, name, var_type):
        self._name = name
        self._var_type = var_type


class Formula:
    def __init__(self, name, expression):
        self._name = name
        self._expression = expression


class Constant:
    def __init__(self, const_type, name, expression):
        self._const_type = const_type
        self._name = name
        self._expression = expression


class Init:
    def __init__(self, expression):
        self._expression = expression


class GuardDeclaration:
    def __init__(self, label, expression, updates):
        self._label = label
        self._expression = expression
        self._updates = updates


class GuardUpdate:
    def __init__(self, expression, state_updates):
        self._expression = expression
        self._state_updates = state_updates


class StateUpdate:
    def __init__(self, identifier, expression):
        self._identifier = identifier
        self._expression = expression
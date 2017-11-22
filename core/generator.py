from core.specification import MapSpecification, OrderSpecification
from pygraph.algorithms import minmax
from core.expression_builder import ExpressionBuilder, GuardBuilder
from core.base_expression import *
from enum import Enum


class TaxiGenerator:
    class Direction(Enum):
        RIGHT = 0
        UP = 1
        LEFT = 2
        DOWN = 3

        @staticmethod
        def direction_from(x_prev: int, y_prev: int, x_next: int, y_next: int):
            if x_prev < x_next and y_prev == y_next:
                return TaxiGenerator.Direction.RIGHT
            elif x_prev < x_next and y_prev < y_next:
                return TaxiGenerator.Direction.UP
            elif x_prev < x_next and y_prev > y_next:
                return TaxiGenerator.Direction.DOWN
            elif x_prev > x_next and y_prev == y_next:
                return TaxiGenerator.Direction.LEFT
            elif x_prev > x_next and y_prev < y_next:
                return TaxiGenerator.Direction.UP
            elif x_prev < x_next and y_prev > y_next:
                return TaxiGenerator.Direction.DOWN

            raise ValueError("Start and finish states must be different")

        @staticmethod
        def direction_to(x_prev: int, y_prev: int, x_next: int, y_next: int):
            if x_prev < x_next:
                return TaxiGenerator.Direction.RIGHT
            elif x_prev > x_next:
                return TaxiGenerator.Direction.LEFT

            if y_prev < y_next:
                return TaxiGenerator.Direction.UP
            elif y_prev > y_next:
                return TaxiGenerator.Direction.DOWN

    def __init__(self, map_spec: MapSpecification, order_spec: OrderSpecification):
        self._map_spec = map_spec
        self._order_spec = order_spec

        self._calculate_order_path()

    def can_satisfy_order(self) -> bool:
        return self._path is not None

    def move(self) -> str:
        self._raise_if_invalid()

        action_label = "move"
        x_id = "x"
        y_id = "y"

        guard_builder = GuardBuilder(action_label)
        for i in range(1, len(self._path)):
            y_cur, x_cur = divmod(self._path[i-1], self._map_spec.max_y + 1)
            y_new, x_new = divmod(self._path[i], self._map_spec.max_y + 1)

            cond_builder = ExpressionBuilder(Identifier(x_id))
            cond_builder.append_eq(Integer(x_cur))

            y_cur_builder = ExpressionBuilder(Identifier(y_id))
            y_cur_builder.append_eq(Integer(y_cur))

            cond_builder.append_and(y_cur_builder.expression)

            new_state_builder = ExpressionBuilder(Identifier(x_id))
            new_state_builder.wrap_next()
            new_state_builder.append_eq(Integer(x_new))
            new_state_builder.wrap_paranthesis()

            y_new_builder = ExpressionBuilder(Identifier(y_id))
            y_new_builder.wrap_next()
            y_new_builder.append_eq(Integer(y_new))
            y_new_builder.wrap_paranthesis()

            new_state_builder.append_and(y_new_builder.expression)

            guard_builder.add_guard(cond_builder.expression, new_state_builder.expression)

        return guard_builder.build()

    def max_x(self) -> int:
        self._raise_if_invalid()

        return self._map_spec.max_y

    def max_y(self) -> int:
        self._raise_if_invalid()

        return self._map_spec.max_x

    def max_direction(self) -> int:
        self._raise_if_invalid()

        return 4

    def init_x(self):
        self._raise_if_invalid()

        return self._order_spec.start[0]

    def init_y(self):
        self._raise_if_invalid()

        return self._order_spec.start[1]

    def init_direction(self):
        self._raise_if_invalid()

        return 0

    def _calculate_order_path(self):
        start_node = self._order_spec.start[1]*(self._map_spec.max_y + 1) + self._order_spec.start[0]
        finish_node = self._order_spec.finish[1]*(self._map_spec.max_y + 1) + self._order_spec.finish[0]

        spanning_tree, shortest_paths = minmax.shortest_path(self._map_spec.graph, start_node)

        if finish_node in shortest_paths:
            self._path = minmax.path(spanning_tree, finish_node)
            self._path.reverse()
        else:
            self._path = None

    def _raise_if_invalid(self):
        if not self.can_satisfy_order():
            raise ValueError("Can't build root automaton")

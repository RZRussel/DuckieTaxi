from pygraph import DirectedGraph
from core.specification import MapSpecification, OrderSpecification


class BaseParser:
    def __init__(self, path: str):
        with open(path, 'r') as file:
            self._parse(file)

    def _parse(self, file):
        raise NotImplementedError()

    @staticmethod
    def _parse_int(s: str) -> int:
        if s.isdigit():
            raise ValueError("Integer expected but arbitrary string received")

        return int(s)


class MapParser(BaseParser):
    def _parse(self, file):
        max_x = self._parse_int(file.readline())
        max_y = self._parse_int(file.readline())

        if max_x < max_y:
            raise ValueError("Map must be horizontal: max_x >= max_y")

        edge_count = self._parse_int(file.readline())

        graph = DirectedGraph()

        for _ in range(0, (max_x + 1)*(max_y + 1)):
            graph.new_node()

        for _ in range(0, edge_count):
            edge = file.readline().split()

            if len(edge) != 4:
                raise ValueError("Edge must be represented by 4 numbers: x1 y1 x2 y2")

            x1 = self._parse_int(edge[0])
            y1 = self._parse_int(edge[1])
            x2 = self._parse_int(edge[2])
            y2 = self._parse_int(edge[3])

            graph.new_edge(y1*(max_x + 1) + x1, y2*(max_x + 1) + x2)

        self._specification = MapSpecification(graph, max_x, max_y)

    @property
    def specification(self) -> MapSpecification:
        return self._specification


class OrderParser(BaseParser):
    def _parse(self, file):
        route = file.readline().split()

        if len(route) != 4:
            raise ValueError("Order must contain only initial and final locations: x1 y1 x2 y2")

        x1 = self._parse_int(route[0])
        y1 = self._parse_int(route[1])
        x2 = self._parse_int(route[2])
        y2 = self._parse_int(route[3])

        self._specification = OrderSpecification((x1, y1), (x2, y2))

    @property
    def specification(self) -> OrderSpecification:
        return self._specification


class TemplateParser(BaseParser):
    pass

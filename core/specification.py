from pygraph import DirectedGraph


class MapSpecification:
    def __init__(self, graph: DirectedGraph, max_x: int, max_y: int):
        self._graph = graph
        self._max_x = max_x
        self._max_y = max_y

    @property
    def graph(self):
        return self._graph

    @property
    def max_x(self):
        return self._max_x

    @property
    def max_y(self):
        return self._max_y


class OrderSpecification:
    def __init__(self, start: (int, int), finish: (int, int)):
        self._start = start
        self._finish = finish

    @property
    def start(self):
        return self._start

    @property
    def finish(self):
        return self._finish

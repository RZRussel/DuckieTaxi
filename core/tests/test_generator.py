from unittest import TestCase

from antlr4 import CommonTokenStream, InputStream
from io import StringIO

from core.generator import TaxiGenerator
from core.grammar.PrismTemplateLexer import PrismTemplateLexer
from core.grammar.PrismTemplateParser import PrismTemplateParser
from core.grammar.listeners import PrismErrorListener
from core.parser import MapParser, OrderParser


class TestTaxiGenerator(TestCase):
    map_path = "test_town"
    order_path = "test_order"

    def test_order_calculations(self):
        map_parser = MapParser(self.map_path)
        order_parser = OrderParser(self.order_path)
        generator = TaxiGenerator(map_parser.specification, order_parser.specification)

        self.assertTrue(generator.can_satisfy_order())
        self.assertIsNotNone(generator._path)

    def test_move(self):
        map_parser = MapParser(self.map_path)
        order_parser = OrderParser(self.order_path)
        generator = TaxiGenerator(map_parser.specification, order_parser.specification)

        input_stream = InputStream(generator.move())
        output_stream = StringIO()
        lexer = PrismTemplateLexer(input_stream, output=output_stream)
        stream = CommonTokenStream(lexer)
        parser = PrismTemplateParser(stream)

        error_listener = PrismErrorListener()
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)

        parser.guard_declarations()

        self.assertTrue(len(error_listener.msg_list) == 0)

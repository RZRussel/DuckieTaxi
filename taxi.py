import sys
import getopt
import os
from core.parser import MapParser, OrderParser
from core.compile import TaxiCompiler
from core.generator import TaxiGenerator

DEFAULT_OUTPUT_PREFIX = "out_"

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "m:o:s:t:h")
    except getopt.GetoptError:
        print(usage_string())
        sys.exit(2)

    map_path = None
    order_path = None
    template_path = None
    output_path = None

    for opt, arg in opts:
        if opt == "-h":
            print(usage_string())
            sys.exit(1)
        elif opt == "-m":
            map_path = arg
        elif opt == "-s":
            order_path = arg
        elif opt == "-t":
            template_path = arg
        elif opt == "-o":
            output_path = arg

    if map_path is None:
        print(usage_string())
        sys.exit(1)

    if order_path is None:
        print(usage_string())
        sys.exit(1)

    if template_path is None:
        print(usage_string())
        sys.exit(1)

    if output_path is None:
        name = os.path.basename(template_path)
        name = "{}{}".format(DEFAULT_OUTPUT_PREFIX, name)
        dir_path = os.path.dirname(template_path)
        output_path = os.path.join(dir_path, name)

    execute(template_path, map_path, order_path, output_path)


def execute(template_path: str, map_path: str, order_path: str, output_path):
    map_parser = MapParser(map_path)
    order_parser = OrderParser(order_path)
    generator = TaxiGenerator(map_parser.specification, order_parser.specification)

    compiler = TaxiCompiler(generator, template_path)
    program = compiler.compile()

    with open(output_path, "w") as out_file:
        out_file.writelines(str(program))


def usage_string() -> str:
    usage = "Usage: python taxi.py -m <map file path> -s <order file path> [-o <output path>] [-h]"
    usage = "{} \n\n -h\n Optional flag that prints usage of the script".format(usage)
    usage = "{} \n\n -m\n Path to map file".format(usage)
    usage = "{} \n\n -s\n Path to order file".format(usage)
    usage = "{} \n\n -t\n Path to model template file".format(usage)
    usage = "{} \n\n -o\n Output file path (optional)".format(usage)

    return usage

if __name__ == '__main__':
    main(sys.argv[1:])
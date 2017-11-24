import sys
import getopt
from core.parser import LogParser
from core.compile import TaxiPropertyCompiler


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "l:p:h")
    except getopt.GetoptError:
        print(usage_string())
        sys.exit(2)

    log_path = None
    prop_path = None

    for opt, arg in opts:
        if opt == "-h":
            print(usage_string())
            sys.exit(1)
        elif opt == "-l":
            log_path = arg
        elif opt == "-p":
            prop_path = arg

    if log_path is None:
        print(usage_string())
        sys.exit(1)

    if prop_path is None:
        print(usage_string())
        sys.exit(1)

    execute(log_path, prop_path)


def execute(log_path: str, prop_path: str):
    parser = LogParser(path=log_path, var_count=3)
    compiler = TaxiPropertyCompiler(parser.log_specification)

    expr_builder = compiler.compile()
    with open(prop_path, "w") as out_file:
        out_file.writelines(expr_builder.build())


def usage_string() -> str:
    usage = "Usage: python log2prop.py -l <log file path> -p <output path> [-h]"
    usage = "{} \n\n -h\n Optional flag that prints usage of the script".format(usage)
    usage = "{} \n\n -l\n Path to log file".format(usage)
    usage = "{} \n\n -p\n Path to result property file".format(usage)

    return usage

if __name__ == '__main__':
    main(sys.argv[1:])
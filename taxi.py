import sys
import getopt
import os


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "m:o:t:h")
    except getopt.GetoptError:
        print(usage_string())
        sys.exit(2)

    map_path = None
    order_path = None
    template_path = None

    for opt, arg in opts:
        if opt == "-h":
            print(usage_string())
            sys.exit(1)
        elif opt == "-m":
            map_path = arg
        elif opt == "-o":
            order_path = arg
        elif opt == "-t":
            template_path = arg

    if map_path is None:
        print(usage_string())
        sys.exit(1)

    if order_path is None:
        print(usage_string())
        sys.exit(1)

    if template_path is None:
        print(usage_string())
        sys.exit(1)

    execute(template_path, map_path, order_path)


def execute(template_path: str, map_path: str, order_path: str):
    pass


def usage_string() -> str:
    usage = "Usage: python taxi.py -m <map file path> -o <order file path> [-h]"
    usage = "{} \n\n -h\n Optional flag that prints usage of the script".format(usage)
    usage = "{} \n\n -m\n Path to map file".format(usage)
    usage = "{} \n\n -o\n Path to order file".format(usage)

    return usage

if __name__ == '__main__':
    main(sys.argv[1:])
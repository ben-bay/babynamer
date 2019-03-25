import argparse
import pprint as pp

def prep_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("operation", type=str, default="full", help="operation to perform. Options are full, first, or last")
    parser.add_argument("-n", "--number", type=int, default=1, help="number of baby names.")
    return parser


def first():
    return "Benj"


def last():
    return "Bay"


def process_args(args):
    args.operation = args.operation.lower()
    results = []
    if args.number <= 0:
        return
    for i in range(args.number):
        if args.operation == "full":
            results.append(f"{first()} {last()}")
        elif args.operation == "first":
            results.append(f"{first()}")
        elif args.operation == "last":
            results.append(f"{last()}")
    return results


def main():
    parser = prep_arg_parser()
    args = parser.parse_args()
    names = process_args(args)
    pp.pprint(names)


main()

import argparse
import pprint as pp
import random
import datetime
import pytz


def timestamp():
    def utc_to_local(utc_dt):
        local_tz = pytz.timezone('US/Pacific')
        local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
        return local_tz.normalize(local_dt)
    now = datetime.datetime.utcnow()
    dt = utc_to_local(now)
    formatted = dt.strftime("%Y%m%d-%H%M%S")
    return formatted


def prep_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("operation", type=str, default="full", help="operation to perform. Options are full, first, or last")
    parser.add_argument("-n", "--number", type=int, default=1, help="number of baby names.")
    parser.add_argument("-s", "--source", type=str, default="usa1990", help="desired source of baby names.")
    parser.add_argument("-g", "--gender", type=str, default="m", help="gender of baby.")
    return parser


def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile, 2):
        if random.randrange(num):
            continue
        line = aline
    return estimate_case(line.rstrip())


def get_data(filename):
    return open(f"data/{filename}")


def rnd_line_from_data(filename):
    f = get_data(filename)
    line = random_line(f)
    f.close()
    return line


def rnd_lines_from_data(filename, n):
    f = get_data(filename)
    line = random_line(f)
    f.close()
    return line


def estimate_case(name):
    result = name.lower()
    c1 = result[0].capitalize()
    result = c1 + result[1:]
    return result


def first(source, gender):
    return rnd_line_from_data(f"{source}_first_{gender}.txt")


def last(source):
    return rnd_line_from_data(f"{source}_last.txt")


def process_args(args):
    args.operation = args.operation.lower()
    results = []
    if args.number <= 0:
        return
    for i in range(args.number):
        if args.operation == "full":
            results.append(f"{first(args.source, args.gender)} {last(args.source)}")
        elif args.operation == "first":
            results.append(first(args.source, args.gender))
        elif args.operation == "last":
            results.append(last(args.source))
    return results


def main():
    parser = prep_arg_parser()
    args = parser.parse_args()
    names = process_args(args)
    print(*names, sep = "\n") 


main()

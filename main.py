import argparse
import os
import sys
import time
import warnings
from collections import Counter, defaultdict
from datetime import timedelta
from io import StringIO
from typing import List, Dict

from regexes import regex_dict
from utils import sizeof_fmt


def print_warning(text: str) -> Dict[str, List[str]]:
    regs = defaultdict(list)
    for reg_name, reg in regex_dict.items():
        for match in reg.finditer(text):
            if match is not None:
                if group := match.group():
                    regs[reg_name].append(group.strip())
                    warnings.warn(
                        f"There might be sensitive information in the text! "
                        f'"{group.strip()}" could be a(n) {reg_name}!'
                    )
    return regs


def check_buffers(buffers):
    stats = Counter()
    total_length = 0
    total_size = 0
    start = time.time()
    for buffer in buffers:
        text = buffer.read()
        total_size += sys.getsizeof(text)
        total_length += len(text)
        regs = print_warning(text)
        for reg_name, match_list in regs.items():
            stats[reg_name] += len(match_list)

    end = time.time()
    total = sum(stats.values())
    elapsed = timedelta(seconds=end - start)
    print(
        f"done, processed {sizeof_fmt(total_size)} text in {elapsed}, found {total} matches"
    )
    print("most common categories:", stats.most_common())


def get_args():
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "--file", "-f", nargs="+", help="Define specific files for the check"
    )
    argparser.add_argument(
        "--path",
        "-p",
        nargs="+",
        help="Define a directory or multiple directories in which all files will be checked",
    )
    argparser.add_argument(
        "--string", "-s", help="Pass a string directly to the method"
    )
    argparser.add_argument("-q", "--quiet", default=False, action="store_true")
    return argparser.parse_args()


def main():
    args = get_args()

    if args.file is None and args.path is None and args.string is None:
        warnings.warn("No file or string given for the check")

    if args.quiet:
        warnings.simplefilter("ignore")

    buffers = []

    if args.file is not None:
        buffers += [open(file) for file in args.file]

    if args.path is not None:
        buffers += [
            open(os.path.join(path, file))
            for path in args.path
            for file in os.listdir(path)
        ]

    if args.string is not None:
        buffers.append(StringIO(args.string))

    check_buffers(buffers)


if __name__ == "__main__":
    main()

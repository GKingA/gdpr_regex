from collections import defaultdict
from typing import List, Dict
from regexes import regex_dict
import warnings
import os
import argparse


def print_warning(text: str) -> Dict[str, List[str]]:
    regs = defaultdict(list)
    for reg_name, reg in regex_dict.items():
        for match in reg.finditer(text):
            if match is not None:
                if group := match.group():
                    regs[reg_name].append(group.strip())
                    warnings.warn(f"There might be sensitive information in the text! "
                                  f"\"{group.strip()}\" could be a(n) {reg_name}!")
    return regs


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--file", "-f", nargs="+",
                           help="Define specific files for the check")
    argparser.add_argument("--path", "-p", nargs="+",
                           help="Define a directory or multiple directories in which all files will be checked")
    argparser.add_argument("--string", "-s", help="Pass a string directly to the method")
    args = argparser.parse_args()

    if args.file is None and args.path is None and args.string is None:
        warnings.warn("No file or string given for the check")
    if args.file is not None:
        for file in args.file:
            print(file)
            with open(file) as check_file:
                print_warning(check_file.read())
    if args.path is not None:
        for path in args.path:
            for file in os.listdir(path):
                file_path = os.path.join(path, file)
                print(file_path)
                with open(file_path) as check_file:
                    print_warning(check_file.read())
    if args.string is not None:
        print_warning(args.string)

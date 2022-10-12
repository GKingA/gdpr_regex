from collections import defaultdict
from typing import List, Dict
from regexes import regex_dict
import warnings


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


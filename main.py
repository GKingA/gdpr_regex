from typing import Tuple, Union
from regexes import regex_dict
import warnings


def print_warning(text: str) -> Union[Tuple[str, str], None]:
    for reg_name, reg in regex_dict.items():
        if (res := reg.search(text)) is not None:
            res_string = text[res.regs[0][0]:res.regs[0][1]]
            warnings.warn(f"There might be sensitive information in the text! "
                          f"{res_string} seems to be a {reg_name}!")
            return reg_name, res_string

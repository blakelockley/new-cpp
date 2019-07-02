import re
from dataclasses import dataclass

@dataclass
class Method:
    return_type: str
    name: str
    args: str
    trailing: str

    def is_decl(self):
        return self.trailing == ';'

    def split_ref(self):
        if self.name[0] in ['&', '*']:
            return self.name[0], self.name[1:]
        else:
            return "", self.name

    def split_args(self):
        return self.args.split(',')


def main(args):

    if len(args) < 2:
        print(f"usage: python {args[0]} <header_file>")
        exit(-1)

    fname = args[1]
    header_file = None

    with open(fname) as f:
        header_file = f.readlines()

    class_name_match = re.search(r"class (\w+)", "\n".join(header_file))
    class_name = class_name_match.group(1)

    function_pattern = re.compile(r"(\w+)\s+((?:\*|\&)?\w+)\((.*)\)(;)?")
    methods = []

    for line in header_file:
        m = function_pattern.search(line)
        if m:
            methods.append(Method(*m.groups()))

    decl_methods = filter(Method.is_decl, methods)

    cpp_fname = fname.replace(".hpp", ".cpp")

    with open(cpp_fname, "w") as f:
        f.write(f"#include <{fname}>\n\n")
        for method in decl_methods:
            f.write(f"{method.return_type} {method.split_ref()[0]}{class_name}::{method.split_ref()[1]}({method.args})\n")
            f.write("{\n\n}\n\n")


if __name__ == "__main__":
    import sys
    main(sys.argv)
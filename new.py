#!/usr/bin/env python3

import os, sys

HEADER_EXT = ".hpp"
SOURCE_EXT = ".cpp"
HEADER_GUARD_SUFFIX = "_H"

HEADER_TEXT = """#ifndef {{header_guard}}
#define {{header_guard}}

class {{class_name}}
{
public:
    {{class_name}}();

private:

};

#endif
"""

SOURCE_TEXT = """#include \"{{header_name}}\"

{{class_name}}::{{class_name}}()
{

}
"""


def main(args):
    if len(args) < 2:
        print(f"usage: {args[0]} <path>/<class-name>")
        exit(1)

    fpath, raw_name = os.path.split(args[1])
    name = raw_name.lower() 

    header_path = os.path.join(fpath, name + HEADER_EXT)
    source_path = os.path.join(fpath, name + SOURCE_EXT)

    class_name = str().join(map(str.capitalize, name.split("_")))

    context = {
        "header_guard": name.upper() + HEADER_GUARD_SUFFIX,
        "class_name": class_name,
        "header_name": name + HEADER_EXT
        }

    rendered_header = HEADER_TEXT
    rendered_source = SOURCE_TEXT

    for (key, item) in context.items():
        tag = "{{" + key + "}}"
        rendered_header = rendered_header.replace(tag, item)
        rendered_source = rendered_source.replace(tag, item)

    with open(header_path, "w") as f:
        f.write(rendered_header)

    with open(source_path, "w") as f:
        f.write(rendered_source)


if __name__ == "__main__":
    main(sys.argv)

import re

def main(args):

    if len(args) < 2:
        print(f"usage: python {args[0]} <header_file>")
        exit(-1)

    fname = args[1]
    header_file = None

    with open(fname) as f:
        header_file = f.read()

    class_name_match = re.search(r"class (\w+)", header_file)
    class_name = class_name_match.group(1)
    

if __name__ == "__main__":
    import sys
    main(sys.argv)
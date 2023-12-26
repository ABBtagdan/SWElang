from compiler import *
from sys import *


def main():
    with open(argv[1], "r", encoding="utf-8") as f:
        source = f.read()


    lexer = Lexer(source)
    emitter = Emitter(argv[2]+".py")
    parser = Parser(lexer, emitter)

    parser.program()


if __name__ == "__main__":
    main()




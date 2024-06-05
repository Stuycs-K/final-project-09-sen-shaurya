from lexer import Lexer
from compiler import Compiler
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the program path.")
        sys.exit(1)

    program_path = sys.argv[1]

    lexer = Lexer(program_path)
    tokens = lexer.lex()
    print(tokens)

    Compiler = Compiler(tokens)
    code = Compiler.compile()
    print(code)
    exec(code)
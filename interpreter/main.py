from lexer import Lexer
from compiler import Compiler


if __name__ == "__main__":
    program_path = "programs/AddTwoNumbersOrStrings"

    lexer = Lexer(program_path)
    tokens = lexer.lex()
    print(tokens)

    Compiler = Compiler(tokens)
    code = Compiler.compile()
    print(code)
    exec(code)
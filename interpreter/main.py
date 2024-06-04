from lexer import Lexer
from compiler import Compiler


if __name__ == "__main__":
    program_path = "../programs/HelloWorld/"

    lexer = Lexer(program_path)
    tokens = lexer.lex()
    # print(tokens)

    Compiler = Compiler(tokens)
    code = Compiler.compile()
    
    exec(code)
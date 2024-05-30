from lexer import Lexer
from parser import Parser
from interpreter import Interpreter


if __name__ == "__main__":
    program_path = "../programs/HelloWorld/Command"
    lexer = Lexer(program_path)
    tokens = lexer.tokenize()
        
    print(tokens)
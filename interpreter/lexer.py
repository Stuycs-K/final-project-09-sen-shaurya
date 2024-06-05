
import os


class Token:

    COMMAND_TOKENS = ["IF", "WHILE", "DECLARE", "LET", "PRINT", "INPUT"]
    EXPRESSION_TOKENS = ["VARIABLE", "ADD", "SUBTRACT", "MULTIPLY", "DIVIDE", "LITERAL", "EQ", "GT", "LT"]

    (IF, WHILE, DECLARE, LET, PRINT, INPUT) = [
        i for i in range(6)
    ]
    (VARIABLE, ADD, SUBTRACT, MULTIPLY, DIVIDE, LITERAL, EQ, GT, LT) = [
        i for i in range(9)
    ]


    TYPES = ["INT", "FLOAT", "STRING", "CHAR"]

    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"<{self.type} : {self.value}>"

class Lexer:
    """
    Lexer walks through the folder structure and converts it into tokens 
    such as keywords, operators, and literals.
    """

    def __init__(self, root_folder):
        self.root_folder = root_folder
        self.tokens = []

    def lex(self):
        self._lex_commands(self.root_folder)
        return self.tokens

    def _lex_commands(self, path):
        command_dirs = self._get_sub_dirs(path)
        
        for command in command_dirs:
            sub_dirs = self._get_sub_dirs(command.path)
            command_len = len(self._get_sub_dirs(sub_dirs[0]))
            self._add_command_token(command_len, sub_dirs)
            
    def _get_sub_dirs(self, path):
        
        return sorted(
            [f for f in os.scandir(path) if f.is_dir()],
            key=lambda x: x.name
        )
        
    def _tokenize_expression(self, path): 
        expression_dirs = self._get_sub_dirs(path)
        # first subfolder is token
        expression_len = len(self._get_sub_dirs(expression_dirs[0]))
        if (expression_len == Token.ADD) :
            return Token("ADD", [
                self._tokenize_expression(expression_dirs[1]),
                self._tokenize_expression(expression_dirs[2])
            ])
        if (expression_len == Token.VARIABLE) :
            return Token("VARIABLE", self._tokenize_variable(expression_dirs[1]))
        if (expression_len == Token.LITERAL) :
            data_type = Token.TYPES[len(self._get_sub_dirs(expression_dirs[1]))]
            #second subfolder is data type and third is value
            if (data_type == "STRING"):
                value_folders = self._get_sub_dirs(expression_dirs[2].path)
                value = value_folders[0].name
            else:
                # tokenize
                value = "BOOM"
                pass
            return Token(Token.EXPRESSION_TOKENS[Token.LITERAL], [data_type, value])

    def _tokenize_variable(self, path) :
        expression_dirs = self._get_sub_dirs(path)
        
        return f"var{expression_dirs[0].name}"

    def _add_command_token(self, subfolder_count, sub_dirs):
        if subfolder_count == Token.IF:
            self.tokens.append("IF")
        elif subfolder_count == Token.WHILE:
            self.tokens.append("WHILE")
        elif subfolder_count == Token.DECLARE:
            self.tokens.append("DECLARE")
        elif subfolder_count == Token.LET:
            self.tokens.append ("LET")
        elif subfolder_count == Token.PRINT:
            self.tokens.append(Token("PRINT", self._tokenize_expression(sub_dirs[1])))
        elif subfolder_count == Token.INPUT:
            self.tokens.append(Token("INPUT" , self._tokenize_variable(sub_dirs[1]) ))

    def _add_expression_token(self, subfolder_count):
        if subfolder_count == Token.VARIABLE:
            self.tokens.append("VARIABLE")
        elif subfolder_count == Token.ADD:
            self.tokens.append("ADD")
        elif subfolder_count == Token.SUBTRACT:
            self.tokens.append("SUBTRACT")
        elif subfolder_count == Token.MULTIPLY:
            self.tokens.append("MULTIPLY")
        elif subfolder_count == Token.DIVIDE:
            self.tokens.append("DIVIDE")
        elif subfolder_count == Token.LITERAL:
            self.tokens.append("LITERAL")
        elif subfolder_count == Token.EQ:
            self.tokens.append("EQUAL_TO")
        elif subfolder_count == Token.GT:
            self.tokens.append("GREATER_THAN")
        elif subfolder_count == Token.LT:
            self.tokens.append("LESS_THAN")



import os
class Token:

    def __init__(self, token, value):
        self.token = token
        self.value = value

    def __repr__(self):
        return f"{self.token} : {self.value}"
    

class Lexer:
    """
    Lexer walks through the folder structure and converts it into tokens 
    such as keywords, operators, and literals.
    """

    def __init__(self, root_folder):
        self.root_folder = root_folder
        # command num : value
        self.tokens = []

    def lex(self):
        self.lex_commands(self.root_folder)
        return self.tokens

    def lex_commands(self, path):
        commands = []
        # list of DirEntry
        command_dirs = [f for f in os.scandir(path) if f.is_dir()] # get_dirs
        
        for command in command_dirs:
            sub_dirs = [f for f in os.scandir(command.path) if f.is_dir()]
            # first subfolder len determines which command it is
            command_len = len([f for f in os.scandir(sub_dirs[0]) if f.is_dir()])
            # self._add_command_token(command_len)
            if (command_len == 4) :
                #print
                # commands.append(self.tokenize_print(sub_dirs[1]))
                self.tokens.append(self.tokenize_print(sub_dirs[1]))

    def tokenize_print(self, expression_dir):

        # 4 means print
        return Token(4, "print lol")
        # return Token(4, self.lex_expression(expression_dir.path))


    def _add_command_token(self, subfolder_count):
        if subfolder_count == 0:
            self.tokens.append("IF")
        elif subfolder_count == 1:
            self.tokens.append("WHILE")
        elif subfolder_count == 2:
            self.tokens.append("DECLARE")
        elif subfolder_count == 3:
            self.tokens.append("LET")
        elif subfolder_count == 4:
            self.tokens.append("PRINT")
        elif subfolder_count == 5:
            self.tokens.append("INPUT")

    def _add_expression_token(self, subfolder_count):
        if subfolder_count == 0:
            self.tokens.append("VARIABLE")
        elif subfolder_count == 1:
            self.tokens.append("ADD")
        elif subfolder_count == 2:
            self.tokens.append("SUBTRACT")
        elif subfolder_count == 3:
            self.tokens.append("MULTIPLY")
        elif subfolder_count == 4:
            self.tokens.append("DIVIDE")
        elif subfolder_count == 5:
            self.tokens.append("LITERAL")
        elif subfolder_count == 6:
            self.tokens.append("EQUAL_TO")
        elif subfolder_count == 7:
            self.tokens.append("GREATER_THAN")
        elif subfolder_count == 8:
            self.tokens.append("LESS_THAN")


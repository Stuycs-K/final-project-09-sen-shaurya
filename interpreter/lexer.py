
import os

class Lexer:
    """
    Lexer walks through the folder structure and converts it into tokens 
    such as keywords, operators, and literals.
    """

    def __init__(self, root_folder):
        self.root_folder = root_folder
        self.tokens = []

    def tokenize(self):
        self._tokenize_command(self.root_folder)
        return self.tokens

    # def _traverse_folder(self, folder, depth=0):
    #     # traverse through all the commands
    #     subfolders = [ f.path for f in os.scandir(folder) if f.is_dir() ]
        
    #     if subfolders:
    #         first_subfolder = subfolders[0]
    #         command_count = len([f.path for f in os.scandir(first_subfolder) if f.is_dir()])
    #         self._add_command_token(command_count)

    def _tokenize_command(self, folder):
        # traverse through all the commands
        subfolders = [ f.path for f in os.scandir(folder) if f.is_dir() ]
        
        if subfolders:
            first_subfolder = subfolders[0]
            command_count = len([f.path for f in os.scandir(first_subfolder) if f.is_dir()])
            self._add_command_token(command_count)



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


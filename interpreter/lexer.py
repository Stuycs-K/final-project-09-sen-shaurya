
import os

class Lexer:
    """
    Lexer walks through the folder structure and converts it into tokens 
    such as keywords, operators, and literals.
    """

    def __init__(self, root_folder):
        self.root_folder = root_folder
        self.tokens = []

    def traverse(self, folder):
        for root, dirs, files in os.walk(folder):
            for file in files:
                # check for token
                pass
            for dir in dirs:
                # check for token
                pass

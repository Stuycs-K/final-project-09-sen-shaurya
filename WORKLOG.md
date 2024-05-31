# Work Log

## Shaurya Sen

### 5-23
Sometime this week I changed groups from working with Carmin and Jason to my own group and I had to think of a new idea. I had a few ideas like something to do with NFC, cryptography but I ended up deciding to work on a interpreter for the Folders Esoteric Programming language.

This is a esoteric language in which the program is encoded into a directory structure.

### 5-24
I did research on the Folders Esoteric Language and how to make an interpreter. I learned about using a lexer, parser, and evaluator as the different components of an interpreter.
A lexer converts source code (folders) into a series of tokens such as keywords, expressions, and literals.
The parser takes in the list of tokens and builds an abstract syntax tree for the program.
Evaluator takes in the abstract syntax tree and then evaluates the program.

### 5-28
In class today I started working on implementing the basic structure of the program. I created different classes for the lexer, parser, and interpreter and set them up with basic field variables. I also figured out the flow of initialization and execution that would take place in the main file.

At home, I began fleshing out the actual code for the lexer and am currently working on testing it to ensure it correctly tokenizes a hello world folders program.

### 5-30
Re-figure out the folder structure and rename folder files to help me understand. Start fleshing out lexer with tokenize command.


### 5-31
Add a token class
Write lexer class with lex, lex_commands, tokenize_print, get_sub_dirs, tokenize_expressions and all the other ones. Got MVP for print program lexing.

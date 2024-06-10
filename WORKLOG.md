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

### 6-3
Add Compiler class and removed parser and interpreter classes. After a lot of thinking and trying different thnigs I have figured out the final structure of my interpreter. I will simply have a Lexer class and a Compiler class. The lexer which I already have an MVP for creates tokens from the code, and the compiler will take that and compile it into real executable code that will then be run. Today I have created a very small scale MVP for the compiler working to parse the print command.

### 6-4
Added lexing and compiling and evaluating for input command. I also created a new Folders program to help test which just takes inputs and prints them. I also made it so that it casts correctly between different data types

### 6-5
I completed addition which allowed me to run a new sample program which takes in two inputs and then prints the sum. At first it only worked between strings but I got it working for numbers too. I then expanded on this to include all binary operations!

## References
Documentation: 
https://esolangs.org/wiki/Folders
https://danieltemkin.com/Esolangs/Folders
Creator of Folders: Daniel Temkin


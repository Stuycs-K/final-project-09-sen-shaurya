# Presentation
My Final project is a language interpreter for the esoteric programming language Folders: \
Folders is an esoteric programming language created by Daniel Temkin https://danieltemkin.com/Esolangs/Folders \
An [esoteric programming language](https://en.wikipedia.org/wiki/Esoteric_programming_language) is a programming language designed to test the boundaries of computer programming language design. These can be made as softare art, proof of concept, or just as a joke however the creators of these languages don't typically intend for them to be used mainstream.

### 1. Folders language explanation
(From Daniel Temkin's Site)[https://danieltemkin.com/Esolangs/Folders]:
Folders is a language where the program is encoded into a directory structure. All files within are ignored, as are the names of the folders. Commands and expressions are encoded by the pattern of folders within folders. 

Here are the rules of the Folders language:
#### Folders Commands
| Command | # of Folders |                                  Details                                  |
|:-------:|:------------:|:-------------------------------------------------------------------------:|
| if      | 0 folders    | Second sub-folder holds expression, third holds list of commands          |
| while   | 1 folder     | Second sub-folder holds expression, third holds list of commands          |
| declare | 2 folders    | Second sub-folder holds type, third holds var name (in number of folders) |
| let     | 3 folders    | Second holds var name (in number of folders), third holds expression      |
| print   | 4 folders    | Second sub-folder holds expression                                        |
| input   | 5 folders    | Second sub-folder holds var name                                          |

#### Folders Expressions
|      Type     | # of folders |                                                               Details                                                               |
|:-------------:|:------------:|:-----------------------------------------------------------------------------------------------------------------------------------:|
| Variable      | 0 folders    | Second sub-folder holds var name                                                                                                    |
| Add           | 1 folder     | Second sub-folder holds first expression to add, third holds second expression                                                      |
| Subtract      | 2 folders    | Second sub-folder holds first expression to subtract, third holds second expression                                                 |
| Multiply      | 3 folders    | Second sub-folder holds first expression to multiply, third holds second expression                                                 |
| Divide        | 4 folders    | Second sub-folder holds first expression to divide, third holds second expression                                                   |
| Literal Value | 5 folders    | Second sub-folder holds the type of the value (eg two folders for a string, third holds the value                                   |
| Equal To      | 6 folders    | Second and third folders hold expressions to compare                                                                                |
| Greater Than  | 7 folders    | Second and third folders hold expressions to compare (returns true if the second folder holds a larger value than the third folder) |
| Less Than     | 8 folders    | Second and third folders hold expressions to compare                                                                                |

#### Folders Data Types
|  Type  | # of Folders |                                       Details                                       |
|:------:|:------------:|:-----------------------------------------------------------------------------------:|
| int    | 0 folders    | Second sub-folder holds var name                                                    |
| float  | 1 folder     | Second sub-folder holds first expression to add, third holds second expression      |
| string | 2 folders    | Second sub-folder holds first expression to subtract, third holds second expression |
| char   | 3 folders    | Second sub-folder holds first expression to multiply, third holds second expression |

### 2. Write and test Hello World Program ( in video only )
### 3. Write and test input/adding Program ( in video only )
### 4. How is the interpreter organized?
There are two main parts, the `Lexer` and the `compiler`. The lexer takes in a Path to the root of the folders program. It will then walk through all of the subdirectories in the program and create a tokens list. This Tokens list is passed off to the Compiler which uses this list of tokens to create working python code that can be executed.


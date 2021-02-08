# Compiler-Design-Project-CS335
- Repository for the course project of Compilers course(CS335) taught at the Indian Institute of Technology, Kanpur.
- Contains the implementation of a compiler for C language, implemented in Python. 
- For instructions on how to run and installing the dependencies run: python src/main.py --help 
- Requires Python 3.x

### Usage: 
python3 main.py [--help | file names seperated by space] <br>
Options:<br>
--help : 	 Small tutorial on how to use the compiler

### Dependencies:
This compiler makes use of the following python3 packages:
- ply
- tabulate

### Instructions:
- To install the dependencies, simply run "pip install -r requirements.txt"(without quotes) from the root of the repo
- After this, to run the lexer on any file, run the following command from the root of the repo: "python src/main.py <CProgram_FileName_1.c> <CProgram_FileName_2.c>"
- The code will lex all the C files that are provided in the above command. These can be one or more in number. 


### Group Members:
- Jayesh Shaw | 180330
- Lavish Gupta | 180380
- Prakhar Neema | 180526
- Sarthak Kapoor | 180675
- Varun Goyal | 180850

### Milestones:
- Milestone 1: Lexer

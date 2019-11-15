# HangmanComp

To begin:
1. Choose language:
 - Java: Type "make JAVA_SETUP"
 - C: Type "make C_SETUP"
 - Python: Type "make PYTHON_SETUP"

2. Begin programming in the user_pgm file
 - Although you are free to implement this project however you want. I would reccomend using the functions and methods that I have included. In all of the program files, there is one function or method that gets in the input in some form and another function or method that when run gives the output.

3. Compile program
 - If you are using Java or C, run "make java" or "make c" respectively. If you are using python, skip this step

4. Run code:
 - To run the program, run the command "./handler <NUM LETTERS>" NUM_LETTERS representing the number of letters in the randomly chosen word.

5. Test code:
 - To run a larger test of the system, run "./test.sh" and watch it go.

words.txt from https://github.com/dwyl/english-words

Tips:
 - Keep in mind that the program can only take 26 guesses. If you guess a character that you have previously guessed, you will NOT get a warning and it WILL count towards your total number of guesses.
 - You will need to use file i/o in this program, but I have taken care of much of it for you. Other than accessing the word file, you probably will not have to use any i/o for any part of this if you write your code in the given functions/methods and do not change anything else about the programs.
 _ Make sure you compile using the make file (see step 3 above) before each test otherwise, you may have difficulty. If you want to test a specific length random word, just run "./handler <NUMBER>". Example: "./handler 9" to test for a 9 character word. If you choose a number too big it'll seg fault do pls don't.
 - As with any hastily made program, this program does have flaws. If you believe you know an input that can give you a lower score without actually figuring out the word, we want to see it.

GOOD LUCK!!! YOU'LL NEED IT!!!
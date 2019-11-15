import java.io.*;
import java.util.Scanner;

public class user_pgm {


    /* This method should contain all user code. You get strings representing the
       state of the code (some number of chars; '_' if the letter in that space has
       not been guessed yet or if it has been guessed, the correct character shows
       in that place). Example: the word is "apple" and 'a' and 'l' were previous
       correct guesses, then the state would look like "a__l_". guesses is a string
       of all guesses in no particular order. The letters will not have any separator.
       numGuesses is an int representing the number of previous guesses. This value
       will most likely not be useful to you, but I included it just in case.
    */
    public static char userCode(String state, String guesses, int numGuesses) {
        
    }
    
    public static void printChar(char toSend) {
	System.out.println(Character.toLowerCase(toSend));
	System.exit(0);
    }
    
    public static void main(String[] args) {
	Inputs inputs = new Inputs();
	inputs.setInputs();
	
	printChar(userCode(getState(), getGuesses(), getNumGuesses()));
    }

    public static class Inputs {
	String state, guesses;
	int numGuesses;

	public void setInputs() {
	    Scanner input = new Scanner(System.in);

	    state = input.next();
	    guesses = input.next();
	    numGuesses = input.nextInt();

	    input.close();
	}

	public String getState() {
	    return state;
	}

	public String getGuesses() {
	    return guesses;
	}

	public int getNumGuesses() {
	    return numGuesses;
	}
	
    }
    
}

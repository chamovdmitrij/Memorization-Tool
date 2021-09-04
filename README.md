Memorization Tool

Stage №1:

In this stage, I need to create  first flashcards.
When the program starts, it should print the menu below. 

It is our main menu (1):
	1. Add flashcards
	2. Practice flashcards
	3. Exit
If 1 is entered, the program should print the following sub-menu (2):
	1. Add a new flashcard
	2. Exit
By choosing the Add a new flashcard option, a user is prompted to enter a Question and an Answer. Once they are entered, the program automatically returns to the sub-menu (2). Iterate this process every time a user wants to add a new flashcard.

Flashcard practice:
The Practice flashcards option in the main menu (1) should print all the questions and answers that have been added previously. 
If there are no flashcards, print There is no flashcard to practice! and return to the main menu (1).

Flashcard should appear on the screen in the following way:
	Question: {your question}
	Please press "y" to see the answer or press "n" to skip:
If y is entered, the program should output Answer: {your answer} and go to the next flashcard.
If there are no flashcards to show, return to the main menu (1).

If n is entered, skip to the next flashcard. 
If there are no flashcards to show, return to the main menu (1).

Once the program has reached the end of a flashcard list, return to the main menu (1).

Conditions:

	In case of the wrong input, output the following message: {wrong key} is not an option. Wait for the right input.
	Questions and answers must be non-empty values. Otherwise, wait for the input.
	Output Bye! every time a user exits the program.

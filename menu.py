from classes import flashcard


first_menu = '\n1. Add flashcards\n' \
             '2. Practice flashcards\n' \
             '3. Exit'
second_menu = '\n1. Add a new flashcard\n' \
              '2. Exit'
flashcards = list()


def show_menu1():
    print(first_menu)


def show_menu2():
    print(second_menu)


def run_second_menu():
    global input_
    #  We display the second text menu and wait for user input.
    while True:
        show_menu2()
        try:
            input_ = input()
            case = int(input_)
            #  In this case, we ask the user for a question and answer.
            if case == 1:
                #  We ask for input until a non-empty string arrives.
                question = input('\nQuestion:\n')
                while question.isspace() or question == "":
                    question = input('Question:\n')
                #  We ask for input until a non-empty string arrives.
                answer = input('Answer:\n')
                while answer.isspace() or answer == "":
                    answer = input('Answer:\n')
                #  add the flashcard to the list of cards
                card = flashcard(question, answer)
                flashcards.append(card)
            #  EXIT to the first menu
            elif case == 2:
                break
            #  if you chose a nonexistent string option
            else:
                print(f"\n{input_} is not an option")
        #  #  if you chose a nonexistent number option
        except Exception:
            print(f"\n{input_} is not an option")


def run_first_menu():
    global input_
    #  display the first text menu and wait for user input.
    while True:

        show_menu1()
        try:
            input_ = input()
            case = int(input_)
            if case == 1:
                run_second_menu()
            # if list of cards is empty, then print msg
            elif case == 2:
                if len(flashcards) == 0:
                    print("\nThere is no flashcard to practice!")
                else:
                    #  For every card we prints its question and wait user input
                    for each in flashcards:
                        print(f'\nQuestion: {each.get_question()}')
                        inp = input('Please press "y" to see the answer or press "n" to skip:\n')
                        if inp == 'y':
                            print(f"\nAnswer: {each.get_answer()}")
                        elif inp == 'n':
                            continue
            #  clear the list of cards, print a farewell message and exit
            elif case == 3:
                flashcards.clear()
                print("\nBye!")
                break
            else:
                print(f"\n{input_} is not an option")
        except Exception:
            print(f"\n{input_} is not an option")

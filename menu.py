from classes import flashcard, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from options import *

engine = create_engine('sqlite:///flashcard.db?check_same_thread=False')
#  to create the corresponding table in the database.
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def show_first():
    print('\n1. Add flashcards\n'
          '2. Practice flashcards\n'
          '3. Exit')


def show_second():
    print('\n1. Add a new flashcard\n'
          '2. Exit')


def show_third():
    print('press "y" to see the answer:\n' 
          'press "n" to skip:\n' 
          'press "u" to update:')


def show_fourth():
    print('press "d" to delete the flashcard:\n' 
          'press "e" to edit the flashcard:\n')


def run_second_menu():
    #  We display the second text menu and wait for user input.
    while True:
        show_second()

        case = input()

        #  In this case, we ask the user for a question and answer.
        if case == ADD_NEW_CARD:
            #  We ask for input until a non-empty string arrives.
            question = input('\nQuestion:\n')
            while question.isspace() or question == "":
                question = input('Question:\n')
            #  We ask for input until a non-empty string arrives.
            answer = input('Answer:\n')
            while answer.isspace() or answer == "":
                answer = input('Answer:\n')
            #  add the flashcard to the list of cards
            session.add(flashcard(_question=question, _answer=answer))
            session.commit()
        #  EXIT to the first menu
        elif case == EXIT_2:
            break
        #  if you chose a nonexistent string option
        else:
            print(f"\n{case} is not an option")
    #  #  if you chose a nonexistent number option


def run_first_menu():
    #  display the first text menu and wait for user input.
    while True:

        show_first()

        case = input()

        if case == ADD_CARDS:
            run_second_menu()
        # if list of cards is empty, then print msg
        elif case == PRACTICE:
            flashcards = session.query(flashcard).all()
            if len(flashcards) == 0:
                print("\nThere is no flashcard to practice!")
            else:
                #  For every card we prints its question and wait user input
                for each in flashcards:
                    print(f'\nQuestion: {each._question}:')
                    show_third()
                    inp = input()
                    if inp == SHOW_ANSWER:
                        print(f"Answer: {each._answer}")
                    elif inp == NEXT:
                        continue
                    elif inp == UPDATE:
                        show_fourth()
                        inp_ = input()
                        if inp_ == EDIT:
                            new_question = input(f'\ncurrent question: {each._question}\n'
                                                 f'please write a new question:\n')
                            new_answer = input(f'\ncurrent answer: {each._answer}\n'
                                               f'please write a new answer:\n')
                            if new_question.isspace() and new_answer.isspace():
                                continue
                            elif new_question.isspace():
                                each._answer = new_answer
                            elif new_answer.isspace():
                                each._question = new_question
                            else:
                                each._question = new_question
                                each._answer = new_answer
                            session.commit()
                        elif inp_ == DELETE:
                            session.delete(each)
                            session.commit()
                        else:
                            print(f"\n{inp_} is not an option")
                    else:
                        print(f"\n{inp} is not an option")
        elif case == EXIT_1:
            print("\nBye!")
            break
        else:
            print(f"\n{case} is not an option")

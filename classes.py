# class Switch(object):
#     def __init__(self, value):
#         self.value = value  # the value to be looking for
#         self.emp = False  # for empty case blocks
#
#     def __iter__(self):
#         yield self.match
#         raise StopIteration
#
#     #  Indicates whether to enter the test case
#     def match(self, *args):
#         if self.emp or not args:
#             # an empty list of arguments means the last case block
#             # emp means that the condition was triggered earlier and you need to enter
#             # each case before the first break
#             return True
#         elif self.value in args:
#             self.emp = True
#             return True
#         return False


# def switch_first(f, input_):
#     try:
#         for case in Switch(input_):
#             if case('1'):
#                 print()
#                 f()
#                 switch_second(input())
#                 break
#             if case('2'): pass
#             if case('3'):
#                 print("\nBye!")
#                 return 'exit'
#             if case( ):
#                 if len(input_) != 0:
#                     print(f'\n{input_} is not an option\n')
#     except RuntimeError:
#         return True


# def switch_second(input_):
#     for case in Switch(input_):
#         if case('1'):
#             pass
#         if case('2'):
#             print()
#             break

class flashcard:
    __question: str
    __answer: str

    def __init__(self, question, answer):
        self.__question = question
        self.__answer = answer

    def get_question(self):
        return str(self.__question)

    def get_answer(self):
        return str(self.__answer)

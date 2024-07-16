# Create a class MultiOptionsQuestion which inherits from Question and implements constructor and the methods print and check from Question class.
# Constructor - should get string, list of strings and integer, and save them under the fields question, options  and answer_index accordingly.
# print method - prints the question in the format,

# [?] {question}

# [1] {options[0]}
# [2] {options[1]}
# .
# .
# .
# For example, if the question is 'How many states are in the USA?' and the options are ['49', '50', '51', '32'],

# [?] How many states are in the USA?

# [1] 49
# [2] 50
# [3] 51
# [4] 32
 

# check method - returns True if input string (the answer) is equal to answer_index + 1, otherwise False
# Note, the input of check method is string you must cast it to integer!

from abc import ABC, abstractmethod

class Question(ABC):
    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def check(self, user_string):
        pass



class YesNoQuestion(Question):
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    
    def print(self):
        print(f"[?] {self.question} (yes/no)")

    def check(self, user_string):
        if user_string.lower() == "yes" and self.answer == True:
            return True
        elif user_string.lower() == "no" and self.answer == False:
            return True
        else:
            return False

            
class OpenQuestion(Question):
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers

    def print(self):
        print(f"[?] {self.question}")

    def check(self, user_string):
        # Check if the user_string matches any of the possible answers
        return user_string.lower() in map(str.lower, self.answers)
    

class MultiOptionsQuestion(Question):
    def __init__(self, question, options, answer_index):
        self.question = question
        self.options = options
        self.answer_index = answer_index

    def print(self):
        print(f"[?] {self.question}")
        print()
        for i, option in enumerate(self.options, start=1):
            print(f"[{i}] {option}")

    def check(self, user_string):
        user_string = int(user_string)
        if user_string == self.answer_index + 1:
            return True
        else:
            return False
        

def main():
    # Example Yes/No Question
    yn_question = YesNoQuestion("Is the sky blue?", True)
    yn_question.print()
    yn_answer = input("Your answer (yes/no): ")
    if yn_question.check(yn_answer):
        print("Correct!")
    else:
        print("Incorrect.")

    # Example Open Question
    open_question = OpenQuestion("What is the capital of France?", ["paris"])
    open_question.print()
    open_answer = input("Your answer: ")
    if open_question.check(open_answer):
        print("Correct!")
    else:
        print("Incorrect.")

    multi_question = MultiOptionsQuestion("What is 2 + 2?", ["3", "4", "5", "6"], 1)
    multi_question.print()
    multi_answer = input("Your answer (enter option number): ")
    if multi_question.check(multi_answer):
        print("Correct!")
    else:
        print("Incorrect.")

if __name__ == "__main__":
    main()

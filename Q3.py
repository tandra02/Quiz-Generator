# Create a class OpenQuestion which inherits from Question and implements constructor and the methods print and check from Question class.
# Constructor - should get string and list of strings and save them under the fields question and answers accordingly.
# print method - prints the question in the format '[?] {question}'
# For example, if the question is 'Are you experienced programmer?', the method should print '[?] Are you experienced programmer?'
# check method - returns True if input string (the answer) included in answers field, otherwise False.
# For example, for answers = ['yes', 'maybe'] if check('yes') return True, if check('nope') return False 

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

q = OpenQuestion('Are you an experienced programmer?', ['yes', 'maybe'])
q.print()  # Output: [?] Are you an experienced programmer?
print(q.check('yes'))  # Output: True
print(q.check('nope')) # Output: False
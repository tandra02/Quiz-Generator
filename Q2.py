# Create class YesNoQuestion which inherits from Question and implements constructor and the methods print and check from Question class.
# Constructor - should get string and boolean and save them under the fields question and answer accordingly.
# print method - prints the question in the format '[?] {question} (yes/no)'
# For example, if the question is 'Are you experienced programmer?', the method should print '[?] Are you experienced programmer? (yes/no)'
# check method - returns True if input string is 'yes' and answer (class field) is True or if input string is 'no' and answer is False, otherwise False.

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
        

# q = YesNoQuestion('Are you an experienced programmer?', True)
# q.print()  # Output: [?] Are you an experienced programmer? (yes/no)
# print(q.check('yes'))  # Output: True
# print(q.check('no'))   # Output: False

q = YesNoQuestion('Are you tired?', False)
q.print()  # Output: [?] Are you an experienced programmer? (yes/no)
print(q.check('yes'))  # Output: True
print(q.check('no'))   # Output: False
print(q.check('Something else'))
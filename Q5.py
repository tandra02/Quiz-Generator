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


class Quiz:
    def __init__(self, questions):
        self.questions = questions

    def start(self):
        for question in self.questions:
            question.print()
            print()
            user_input = input('[+] ')
            print()
            print()


questions = [
    YesNoQuestion("Is the sky blue?", True),
    OpenQuestion("Name a programming language.", ["Python", "JavaScript", "C++"]),
    MultiOptionsQuestion("Select the smallest prime number.", ["1", "2", "3", "4"], 1)
]

quiz = Quiz(questions)
quiz.start()
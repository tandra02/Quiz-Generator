# Create abstract class named Question with the following methods:
# print- abstract method which takes no input.
# check- abstract method which takes string (the answer types by the user) as input.

from abc import ABC, abstractmethod

class Question(ABC):
    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def check(self, user_string):
        pass
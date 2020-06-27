#Create a Protected Var

class Protected:
    def__init__(self)
        self.protectedVar = 0

obj = Protected()
obj._protectedVar = "Salem"
print(obj._protectedVar)

#Create an object that makes use iof protected and private
import pythonclass
user = pythonclass.User("Example")

user.displayName()
user.name = "The Tech Academy"
user.displayName()
print(user._password)





#abc_base.py

import abc
class PluginBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load(self, input):
        """Retrieve data as input source
         and return an object"""
    @abc.abstractmethod
    def save(self, output, data):
        """save data ibject to that output"""

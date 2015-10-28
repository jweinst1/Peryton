#contains the spying objects for integers and dobules

import sys
import operator

class intspy(int):
    #class the simulates an integer but collects changes to it's value
    def __init__(self, val):
        self.val = val
        self.operations = []
    def __getattribute__(self, item):
        if item == 'operations':
            return object.__getattribute__(self, item)
        elif item == '__class__':
            return object.__getattribute__(self, item)
        elif item == '__dict__':
            return object.__getattribute__(self, item)
        else:
            self.operations.append((sys._getframe().f_code.co_name, item))
            return object.__getattribute__(self, item)
    def __repr__(self):
        self.operations.append((sys._getframe().f_code.co_name))
        return str(self.val)
    def __str__(self):
        self.operations.append((sys._getframe().f_code.co_name))
        return str(self.val)
    def __add__(self, other):
        self.operations.append((sys._getframe().f_code.co_name, other))
        return intspy(self.val + other)
    def __iadd__(self, other):
        self.operations.append((sys._getframe().f_code.co_name, other))
        self.val += other
        return self
    def __sub__(self, other):
        self.operations.append((sys._getframe().f_code.co_name, other))
        return intspy(self.val - other)
    def __isub__(self, other):
        self.operations.append((sys._getframe().f_code.co_name, other))
        self.val -= other
    def __eq__(self, other):
        self.operations.append((sys._getframe().f_code.co_name, other))
        return self.val == other
    def __ne__(self, other):
        self.operations.append((sys._getframe().f_code.co_name, other))
        return self.val != other
    def __gt__(self, other):
        self.operations.append((sys._getframe().f_code.co_name, other))
        return self.val > other
    def __lt__(self, other):
        self.operations.append((sys._getframe().f_code.co_name, other))
        return self.val < other




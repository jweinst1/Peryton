#object that allows lists to be spyed on through a process

import sys
import operator

class listspy(list):
    #class the simulates an integer but collects changes to it's value
    def __init__(self, *values):
        self.container = [elem for elem in values]
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
        return str(self.container)
    def __str__(self):
        self.operations.append((sys._getframe().f_code.co_name))
        return str(self.container)
    def __getitem__(self, item):
        self.operations.append((sys._getframe().f_code.co_name), item)
        return self.continer[item]
    def __setitem__(self, key, value):
        self.operations.append((sys._getframe().f_code.co_name), key, value)
        self.container[key] = value
    """def append(self, p_object):
        self.operations.append((sys._getframe().f_code.co_name), p_object)
        self.continer.append(p_object)
    def remove(self, value):
        self.operations.append((sys._getframe().f_code.co_name), value)
        self.container.remove(value)
    def insert(self, index, p_object):
        self.operations.append((sys._getframe().f_code.co_name), index, p_object)
        self.container.insert(index, p_object)
    def pop(self, index=None):
        self.operations.append((sys._getframe().f_code.co_name), index)
        self.container.pop(index)"""

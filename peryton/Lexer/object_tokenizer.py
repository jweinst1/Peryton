#contains classes and tools to get py file elements by inspection.

import types
import inspect

class module_tools(object):
    #class that handles basic functions of python module
    def get_py(name):
        mod = __import__(name)
        return mod
    def get_source(name):
        mod = __import__(name)
        return inspect.getsource(mod)
    def get_funcs(modulename):
        import importlib
        retval = {}
        opened = importlib.import_module(modulename)
        for name in opened.__dict__.keys():
            if isinstance(opened.__dict__[name], types.FunctionType):
                retval[name] = opened.__dict__[name]
        return retval
    def get_funcsource(modulename):
        funcobjects = module_tools.get_funcs(modulename)
        return {elem:inspect.getsourcelines(funcobjects[elem]) for elem in funcobjects.keys()}


class binding_tools(object):

    def get_ints(name):
        #doesnt work, needs to be replaced
        opened = __import__(name)
        retval = {}
        for name in opened.__dict__.keys():
            if isinstance(opened.__dict__[name], int):
                retval[name] = opened.__dict__[name]
        return retval



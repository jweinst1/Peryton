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
    def get_methods(modulename):
        import importlib
        retval = {}
        opened = importlib.import_module(modulename)
        for name in opened.__dict__.keys():
            if isinstance(opened.__dict__[name], types.MethodType):
                retval[name] = opened.__dict__[name]
        return retval

class func_tools(object):
    pass



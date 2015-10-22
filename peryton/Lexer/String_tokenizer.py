import re

#File for applying patterns to the py file and extracting string components

class slicer(object):
    #class that can open a py file and divide the text string in different ways.
    def openpy(name):
        python = open(name, 'r')
        return python.read()

    def pylines(name):
        python = open(name, 'r')
        return python.read().split('\n')

    def notab_lines(name):
        python = open(name, 'r')
        lines = python.read().split('\n')
        for line in lines:
            if '\t' in line:
                line = list(line)
                line.remove('\t')
                line = ''.join(line)
        return lines
    def line_by_tabs(name):
        #arranges lines in py file by the number of tabs in a dictionary.
        lines = slicer.pylines(name)
        tab_counts = [elem.count('\t') for elem in lines]
        tab_counts = set(tab_counts)
        return {num:[line for line in lines if line.count('\t') == num] for num in tab_counts}
    def line_phrase(name, phrase):
        #get lines if they contain a specific string.
        python = open(name, 'r')
        lines = python.read().split('\n')
        pattern = r"^.*%s.*$" %(phrase)
        temp = re.compile(pattern)
        return [line for line in lines if temp.match(line)]

class pytoken(object):
    #class that creates string tokens based on matchable python syntax.
    def find_assignments(name):
        lines = slicer.pylines(name)
        temp = re.compile(r"^.*[a-z]+.* = .+$")
        return [line for line in lines if temp.match(line)]
    def find_eq(name):
        lines = slicer.pylines(name)
        temp = re.compile(r"^.+ == .+$")
        return [line for line in lines if temp.match(line)]



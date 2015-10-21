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


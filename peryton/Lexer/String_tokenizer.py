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
    def pynumlines(name):
        python = open(name, 'r')
        lines = python.read().split('\n')
        return list(enumerate(lines))

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

class oper_tokens(object):
    #class that creates string tokens for python operators.
    def find_comments(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.*#.*$")
        return [line for line in lines if temp.match(line[1])]
    def find_assignments(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.*[a-z]+[^<>!]*=[^<>!]+$")
        return [line for line in lines if temp.match(line[1])]
    def find_eq(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.+==.+$")
        return [line for line in lines if temp.match(line[1])]
    def find_noteq(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.+!=.+$")
        return [line for line in lines if temp.match(line[1])]
    def find_greater(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.+>.+$")
        return [line for line in lines if temp.match(line[1])]
    def find_lesser(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.+<.+$")
        return [line for line in lines if temp.match(line[1])]
    def find_ge(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.+>=.+$")
        return [line for line in lines if temp.match(line[1])]
    def find_le(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.+<=.+$")
        return [line for line in lines if temp.match(line[1])]
    def find_alt_noteq(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.+<>.+$")
        return [line for line in lines if temp.match(line[1])]
    def find_add(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.+[+].+$")
        return [line for line in lines if temp.match(line[1])]
    def find_sub(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.+[-].+$")
        return [line for line in lines if temp.match(line[1])]
    def find_mul(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.+[*].+$")
        return [line for line in lines if temp.match(line[1])]
    def find_div(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.+[/].+$")
        return [line for line in lines if temp.match(line[1])]
    def find_floordiv(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.+[/][/].+$")
        return [line for line in lines if temp.match(line[1])]
    def find_modulus(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.+[%].+$")
        return [line for line in lines if temp.match(line[1])]
    def find_expo(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.+[*][*].+$")
        return [line for line in lines if temp.match(line[1])]
    def find_addAND(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.[+]=.+$")
        return [line for line in lines if temp.match(line[1])]
    def find_subAND(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.-=.+$")
        return [line for line in lines if temp.match(line[1])]
    def find_mulAND(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.[*]=.+$")
        return [line for line in lines if temp.match(line[1])]
    def find_divAND(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.[/]=.+$")
        return [line for line in lines if temp.match(line[1])]
    def find_modulusAND(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.[%]=.+$")
        return [line for line in lines if temp.match(line[1])]
    def find_floordivAND(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.[/][/]=.+$")
        return [line for line in lines if temp.match(line[1])]
    def find_expoAND(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.[*][*]=.+$")
        return [line for line in lines if temp.match(line[1])]

class logmem_oper_tokens(object):

    def find_not(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.+ not .+$")
        return [line for line in lines if temp.match(line[1])]
    def find_or(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.+ or .+$")
        return [line for line in lines if temp.match(line[1])]
    def find_and(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.+ and .+$")
        return [line for line in lines if temp.match(line[1])]
    def find_is(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.+ is .+$")
        return [line for line in lines if temp.match(line[1])]
    def find_in(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.+ in .+$")
        return [line for line in lines if temp.match(line[1])]
    def find_notin(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.+ not in .+$")
        return [line for line in lines if temp.match(line[1])]
    def find_is_not(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.+ is not .+$")
        return [line for line in lines if temp.match(line[1])]

class bitwise_oper_tokens(object):

    def find_and(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.+&.+$")
        return [line for line in lines if temp.match(line[1])]
    def find_or(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.+|.+$")
        return [line for line in lines if temp.match(line[1])]
    def find_xor(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.+^.+$")
        return [line for line in lines if temp.match(line[1])]
    def find_comp(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.+~.+$")
        return [line for line in lines if temp.match(line[1])]
    def find_lshift(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.+<<.+$")
        return [line for line in lines if temp.match(line[1])]
    def find_rshift(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.+>>.+$")
        return [line for line in lines if temp.match(line[1])]

class statement_tokens(object):

    def find_userdef(name):
        #finds all functions using def statement
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.* def .+$")
        return [line for line in lines if temp.match(line[1])]
    def find_for_in(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.*for [a-zA-Z0-9]+ in .+:$")
        return [line for line in lines if temp.match(line[1])]
    def find_while(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.*while .+:.*$")
        return [line for line in lines if temp.match(line[1])]
    def find_if(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.*if .+:.*$")
        return [line for line in lines if temp.match(line[1])]
    def find_elif(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.*elif .+:.*$")
        return [line for line in lines if temp.match(line[1])]
    def find_else(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.*else:.*$")
        return [line for line in lines if temp.match(line[1])]
    def find_return(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.*return .+$")
        return [line for line in lines if temp.match(line[1])]
    def find_pass(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.*pass.+$")
        return [line for line in lines if temp.match(line[1])]
    def find_try(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.*try:.*$")
        return [line for line in lines if temp.match(line[1])]
    def find_exception(name):
        lines = slicer.pynumlines(name)
        temp = re.compile(r"^.*except.+:$")
        return [line for line in lines if temp.match(line[1])]
#UNIT TESTS for Lexer Package
from peryton.Lexer.String_tokenizer import *
import re
class opertokentests(object):

    def findassign_test(name):
        try:
            lst = pytoken.find_eq(name)
            temp = re.compile(r"[^<>!]=[^<>!]")
            for elem in lst:
                assert re.search(elem)
            return 'passed'
        except AssertionError:
            return 'failed'


    def findeq_test(name):
        try:
            lst = pytoken.find_eq(name)
            for elem in lst:
                assert '==' in elem
            return 'passed'
        except AssertionError:
            return 'failed'
    def findle_test(name):
        try:
            lst = pytoken.find_eq(name)
            for elem in lst:
                assert '<=' in elem
            return 'passed'
        except AssertionError:
            return 'failed'
    def findge_test(name):
        try:
            lst = pytoken.find_eq(name)
            for elem in lst:
                assert '>=' in elem
            return 'passed'
        except AssertionError:
            return 'failed'
    def findnot_eq_test(name):
        try:
            lst = pytoken.find_eq(name)
            for elem in lst:
                assert '!=' in elem
            return 'passed'
        except AssertionError:
            return 'failed'



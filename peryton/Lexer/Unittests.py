#UNIT TESTS for Lexer Package
from peryton.Lexer.String_tokenizer import *
class pytokenstests(object):

    def findeq_test(name):
        try:
            lst = pytoken.find_eq(name)
            for elem in lst:
                assert '==' in elem
            return 'passed'
        except AssertionError:
            return 'failed'

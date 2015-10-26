#TEST FILE FOR TRANSPILER
#DO NOT IMPORT
#deep dict functions
f = 2
y = 5
ten = 7*7*7
def deep_dict_linear(lst):
	temp = {}
	searcher = temp
	count = 0
	while count < len(lst):
		searcher[lst[count]] = {}
		searcher = searcher[lst[count]]
		count += 1
	return temp

#Proof function

def test_proof(func1, func2, set):
	try:
		for elem in set:
			assert func1(elem) == func2(elem)
		return True
	except AssertionError:
		return False


#Bijections

def bijection(func, input, output):
	try:
		dict = {elem:[func(elem)] for elem in input}
		for mem in dict.values():
			if len(mem) > 1:
				raise AssertionError
		return True
	except AssertionError:
		return False

#inverse functions

def inverse(func1, func2, domain):
	#tests for bijection as well
	try:
		for elem in domain:
			assert elem == func1(func2(elem))
			assert elem == func2(func1(elem))
		return True
	except AssertionError:
		return False

#polynomials

def polynomial_sing(expression, domain):
	targ = 9
	if domain == 2:
		pass
	return [x for x in domain if eval(expression)]
def polynomial_double(expression, domain):
	return [(x, y) for x in domain for y in domain if eval(expression)]

class bing(object):
	ting = 5
	t = (7 == 8)


	def __init__(self, power):
		assert power < 5
		self.power = power
		self.strength = power * 2

	def foo(self):
		return 5


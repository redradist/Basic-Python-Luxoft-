def func1():
	"""Documentation"""
	
	"""Documentation 2"""
	pass

def func2(*args): # args = tuple
	"Documentation"
	
	"Documentation 2"
	pass

def func2(*args, **dict): # args = tuple, dict = dictionary
	"Documentation"
	
	"Documentation 2"
	print dict
	print "dict a = ", dict["a"]
	print "dict b = ", dict["b"]

def func3(a, b, c):
	print "a = ", a
	print "b = ", b
	print "c = ", c

#def func4(**dict, *args): # args = tuple, dict = dictionary
#	"Documentation"
#	
#	"Documentation 2"
#	print dict
#	print "dict a = ", dict["a"]
#	print "dict b = ", dict["b"]

#def func5(*args, **dict): # args = tuple, dict = dictionary
#	"Documentation"
#	x = False
#	def func6():
#		print "dict a = ", dict["a"]
#		print "dict b = ", dict["b"]

func3("0", b="1", c="2")
func2(b="1", a="2")


# globals()
# locals()



####################### Practice #######################
# Task 1
def even_print(*args):
	print args
	for arg in args:
		if arg % 2 == 0:
			print arg
even_print(1, 2, 3, 4, 5)

# Task 2
def even_print(*args):
	print args
	for arg in args:
		if arg % 2 == 0:
			print arg
even_print(*tuple(range(1, 101)))

# Task 3
def sum_elements(*args):
	print args
	sum = 0
	for arg in args:
		sum = sum + arg
	return sum
print sum_elements(*tuple(range(1, 21)))

# Task 4
vat = 23
def VAT_price_calculator(price):
	global vat
	return price+price*vat

print VAT_price_calculator(2.3)

# Task 5, Task 6, Task 7
# import function
# function.VAT_price_calculator(2.3)

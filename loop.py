# Task 1
a = 3
b = 'test'
c = [1,2,3]
d = 'none'
e = None
f = 0
print a or b
print bool(a or b)
print type(a or b)
print a and b
print bool(a and b)
print type(a and b)
print a and c
print bool(a and c)
print type(a and c)
print a and d
print bool(a and d)
print type(a and d)
print b or d
print bool(b or d)
print type(b or d)
print a and e
print bool(a and e)
print type(a and e)
print a and f
print bool(a and f)
print type(a and f)

# Task 2
value = 2
if type(value) is int and value >= 5:
	print "Yes"
elif type(value) is str:
	print "String"
elif type(value) is int and value < 5:
	print "No"
else:
	print "other"

# Task 3
l1 = [3, 5, 74, 8, 9]
for item in l1:
	print item

for index in range(len(l1)):
	print l1[index]

zipped = zip(range(len(l1)), l1)
for index, value in zipped:
	print "Index {} is {}".format(index, value)
	print "Index {1} is {0}".format(value, index)

# Task 4
for value in range(5, 48):
	if value % 2 == 0:
		print value

# Task 5
not_allowed = [20, 24, 36]
for value in range(5, 48):
	if value % 2 == 0 and value not in not_allowed:
		print value

print "-".join(["1","2"])



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

def func4(**dict, *args): # args = tuple, dict = dictionary
	"Documentation"
	
	"Documentation 2"
	print dict
	print "dict a = ", dict["a"]
	print "dict b = ", dict["b"]

def func5(**dict, *args): # args = tuple, dict = dictionary
	"Documentation"
	x = False
	def func6():
		print x # Захватит неявно
		print "dict a = ", dict["a"]
		print "dict b = ", dict["b"]

func3("0", b="1", c="2")
func2(b="1", a="2")


# globals() переменніе глобального контекста
# locals() переменніе контекста
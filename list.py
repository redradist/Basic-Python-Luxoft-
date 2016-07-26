l1 = ['abcd', 786 , 2.23, 'john', 70.2]
print l1
print l1[0]
print l1[2:]
l1 = l1 + l1
print l1

l2 = ['second', '123']

l3 = l1 + l2
l1[1] = 2313
print l3

l4 = l2
l2[0] = 4326
print l4

l5 = [2, 4, 7, 7]
l5[:2] = [1, 2]
print l5

aTuple = (7,7,7,7,7,7);
l5.insert(1, list(aTuple))
print l5
l5 = l5 + l5
del l5[:]      
print l5

l6  = l1 + l2 + l5
print l6
l1[0] = 24141
print l6

l1.sort()
print l1
print len(l1)
l2.sort()
print l2
print len(l2)
l3.sort()
print l3
print len(l3)



t1 = ('abcd', 786 , 2.23, 'john', 70.2)
#t1[0] = 0
print len(t1)
t2 = tuple(l2)
print t2
min_number = min(t2)
print "Min tuple number is " + str(min_number)



d1  = {'one':'First', 2:"Second", 3:3}
for (key, value) in d1.items():
	print "key is " + str(key)
	print "value is " + str(value)
print "'one' is "+str(d1.has_key('one'))
print d1['one']
#print d1['two']
d2 = {'one':d1['one']}
print d2
values = list(t1) + d2.values()
i = 0
d3 = dict(zip(tuple(l1),values))
print d3

str = None
if not str:
	print "str is empty"
	
zij = """ aAfsdfasfdg """ \
	  """ aAfsdfasfdg """
print zij

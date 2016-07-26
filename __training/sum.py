#!/usr/bin/python

##############################################
#Program for: calculating the sum of 2 numbers
#Example: sum value1 value2
##############################################

import sys

if (len(sys.argv) < 2 or len(sys.argv) > 3):
    print "Usage:\n You should use the following syntax: add value1 value2"
    sys.exit("Not enough paraments!!!")
else: 
    #the arguments that the script uses: add value1 value2
    # sys.argv[0] represents program name
    # the parameters need to be converted to int, as they are considered string
    value1 = int(sys.argv[1])
    value2 = int(sys.argv[2])

#the procedure returns the sum of 2 numbers given as parameters
def sum (a,b): 
    print "Add value1=",value1," with value2=",value2
    result = a + b
    return result


#calling the procedure
sum_value=sum(value1,value2)

print "Sum is:",sum_value



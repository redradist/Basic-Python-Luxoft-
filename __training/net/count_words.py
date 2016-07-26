# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more
def count_strings(words):
  count = 0
  for word in words:
    if len(word) >= 2 :
      count = count + 1
      # you can also use count+=1
  return count


l_words = ['aba', 'xyz', 'aa', 'x', 'bbb']
print "List:", l_words

cnt = count_strings(l_words)
print "Found", cnt, "strings with length higher than 2"

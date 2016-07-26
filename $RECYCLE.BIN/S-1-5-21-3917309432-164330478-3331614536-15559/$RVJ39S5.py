def mix_words(a, b):
  print b[:2],a[2:],a[:2],b[2:]
  a_swapped = b[:2] + a[2:]
  b_swapped = a[:2] + b[2:]
  return a_swapped + ' ' + b_swapped

a = "test"
b = "mix"
print 'Words to mix up:',a,',',b

mixed_string = mix_words(a,b)

print 'Mixed word:', mixed_string



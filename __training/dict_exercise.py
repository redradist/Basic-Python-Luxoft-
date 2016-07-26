def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""
  # +++your code here+++
  # LAB(begin solution)
  mimic_dict = {}
  f = open(filename, 'r')
  text = f.read()
  f.close()
  words = text.split()
  prev = ''
  for word in words:
    if not prev in mimic_dict:
      mimic_dict[prev] = [word]
    else:
      mimic_dict[prev].append(word)
    # Could write as: mimic_dict[prev] = mimic_dict.get(prev, []) + [word]
    # It's one line, but not totally satisfying.
    prev = word
  return mimic_dict


# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print 'usage: ./mimic.py file-to-read'
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


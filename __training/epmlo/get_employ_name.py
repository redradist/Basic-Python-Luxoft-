#!/usr/bin/python
import sys
import re

# procedure that reads a file and returns the text
def read_file (filename):
  # open file for reading
  fid = open(filename,'r')
  # read the entire text in variable text
  text = fid.read()
  # close file after reading
  fid.close()
 
  return text

# procedure that returns a tuple containing the name and surnames
# Each file line has format:   
#   Name: <name> Surname: <surname> Address: <address> Phone: <phone_number>
def parse_text (txt):
  tuples = re.findall(r'Name:\s*(\S+)\s+Surname:\s*(\S+)', txt)
  return tuples    

# write the Name and surname in the new file following format
def write_file (tuples):
  fout = open("filtered_employ_list.txt","w")

  for name_surname in tuples:
    # unpack the tuple into 2 vars
    (name,surname) = name_surname
    # generate the string in the correct format
    str_to_write = "Name: " + name + " Surname:" + surname + "\n"
    # write the string in the file 
    fout.write(str_to_write)
  fout.close()

def main():
  if len(sys.argv) != 2:
    print 'usage: ./get_employ_name.py file-to-read'
    sys.exit(1)

  file_text = read_file(sys.argv[1])
  print file_text
  filtered_text = parse_text(file_text)
  print filtered_text
  write_file(filtered_text)


if __name__ == '__main__':
  main()


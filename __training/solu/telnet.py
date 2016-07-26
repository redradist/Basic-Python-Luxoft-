import getpass
import sys
import telnetlib

# This is a public telnet server
HOST = "scn.org"
print HOST

# Enter telnet credentials
user = raw_input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

#tn.set_debuglevel(9)

# Enter username
tn.read_until("login: ")
tn.write(user + "\n")

# Enter password if available
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

# First iteration

r1 = tn.read_until("Press RETURN to Continue: ")
print "1: ", r1,"\n\n\n"
tn.write("quit\n")
tn.read_until("reading file")
tn.write("\n")

r2 = tn.read_until("Press RETURN to Continue: ")
print "2: ", r2,"\n\n\n"
tn.write("quit\n")
tn.read_until("reading file")
tn.write("\n")

tn.read_until("Press RETURN to continue: ")
tn.write("quit\n")

tn.read_until("Your Choice ==>")
tn.write("x\n")
tn.read_until("(y/n)")
tn.write("y\n")

#sess_op = tn.read_all()
#print sess_op

tn.close()


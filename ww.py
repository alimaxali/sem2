import random
import os
e = str(random.randint(1,3))


if e in "1":
   os.system("bash sem1.sh")
elif e in "2":
   os.system("bash sem2.sh")
elif e in "3":
   os.system("bash sem3.sh")
else :
   print "error"

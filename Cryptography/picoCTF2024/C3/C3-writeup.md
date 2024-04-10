![Screenshot 2024-03-18 231559](https://github.com/ashine92/picoCTF/assets/62413378/8dc457be-1d09-49ca-b86f-afda11bb41dc)# C3 

"""sh
lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

ciphertext = "DLSeGAGDgBNJDQJDCFSFnRBIDjgHoDFCFtHDgJpiHtGDmMAQFnRBJKkBAsTMrsPSDDnEFCFtIbEDtDCIbFCFtHTJDKerFldbFObFCFtLBFkBAAAPFnRBJGEkerFlcPgKkImHnIlATJDKbTbFOkdNnsgbnJRMFnRBNAFkBAAAbrcbTKAkOgFpOgFpOpkBAAAAAAAiClFGIPFnRBaKliCgClFGtIBAAAAAAAOgGEkImHnIl"
prev = 0

plain = ""
for char in ciphertext:
  cur_prev = lookup2.index(char) % 40
  cur = cur_prev + prev
  prev = cur
  while cur > 39:
    cur = cur - 40
  plain += lookup1[cur]
print(plain)
"""

Result:
"""sh
#asciiorder
#fortychars
#selfinput
#pythontwo

chars = ""
from fileinput import input
for line in input():
    chars += line
b = 1 / 1

for i in range(len(chars)):
    if i == b * b * b:
        print chars[i] #prints
        b += 1 / 1
"""

![Screenshot 2024-03-18 231559](https://github.com/ashine92/picoCTF/assets/62413378/7df85424-1ea0-4391-ad01-d7a41fa58926)
Flag: `picoCTF{adlibs}`

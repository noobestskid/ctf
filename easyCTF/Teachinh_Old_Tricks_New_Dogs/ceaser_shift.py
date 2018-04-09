shift = int(raw_input())
inp = raw_input()
out = ""
for i in inp:
 if (ord(i) != 32):
  out += unichr((ord(i)-ord('a')-shift)%26+ord('a'))
 else:
  out += " "
print out

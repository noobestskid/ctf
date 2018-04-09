
key = "soupy"
flag = "Fg4GCRoHCQ4TFh0IBxENAE4qEgwHMBsfDiwJRQImHV8GQAwBDEYvV11BCA=="

def encrypt(a, b):
  out = ""
  for i in range(len(a)):
    ca = ord(a[i % len(a)])
    cb = ord(b[i % len(b)])
    out += unichr(ca ^ cb);
  out = out.encode("base64")
  return out

def decrypt(a,b):
  a = a.decode("base64")
  f = ""
  for i in range(len(a)):
    cb = ord(b[i%len(b)])
    ca = ord(a[i])
    f += unichr(cb^ca) 
  print f
  return f

print decrypt(flag,key) 



key1 = "YOJPJSSPD^"
key2 = "NX]G]DDGSI"
flag = "CGPOGCMHTRMKHP"
out1 = ""
out2 = ""
for i in range(14):
 out1 += unichr(ord(key1[i%10])^ord(flag[i]))
 out2 += unichr(ord(key2[i%10])^ord(flag[i]))
print out1
print out2 
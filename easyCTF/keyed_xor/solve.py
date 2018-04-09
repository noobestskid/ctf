# -*- coding: utf-8 -*-
f1 = open("1cdfad12bcae77ef64defecc1f5f030639e517c4e2ccac33b7ca6a1e059aafe9_words.txt","r")
ct = """
�
	
"""
fkey = "surrounded"
for key in f1:
 out = ""
 key = fkey+key
 for i in range(len(key)):
  out += chr(ord(ct[i])^ord(key[i%len(key)]))
 print key+" "+out
 print "********************"
f1.close() 

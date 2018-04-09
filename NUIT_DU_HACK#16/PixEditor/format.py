import sys

inp = raw_input("Formating: ")

trun = [inp[x:x+3] for x in range(0,len(inp),3)]
for i in range(len(trun)):
	trun[i]=trun[i][::-1]
formated_inp = "".join(trun)
print "Formated input: "+formated_inp	


data = [0 for x in range(4096)]
for i in range(0,len(data),4):
	data[i]= 255
	data[i+3] = 255
print "Now building the BMP ..."

j=0;
for i in range(0,len(formated_inp),3):
	data[j] = ord(formated_inp[i])
	if i+1>=len(formated_inp):
		continue
	data[j+1] = ord(formated_inp[i+1])
	if i+2>=len(formated_inp):
		continue
	data[j+2] = ord(formated_inp[i+2])
	if i+3>=len(formated_inp):
		continue
	data[j+3] = 255
	j+=4
print str(data).replace(" ","")
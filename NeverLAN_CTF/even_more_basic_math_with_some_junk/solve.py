
f = open("even_more_numbers_with_some_mild_inconveniences.txt","r")
sum = 0
temp = 0
for line in f:
	last = 0
	for i in range(len(line)):
		if line[i]==" ":
			temp = line[last:i]
			print temp
			if temp=="":
				last = i+1
				continue
			else:
				temp = temp.split(",")
				for num in temp:
					if num != "" and num.isdigit():
						sum += int(num)
			last = i+1	
print sum
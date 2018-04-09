f = open("some_numbers.txt","r")
sum = 0
for num in f:
 sum += int(num)
print sum
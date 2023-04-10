import re
name = input("Enter file: ")
handle = open(name)
count = 0
total = 0
average = 0

for line in handle:
	num = re.findall('^New Revision: (\d+)', line)
	if len(num) > 0:
		count += 1
		total += int(num[0])

if count > 0:
	average = int(total / count)
	print(average)
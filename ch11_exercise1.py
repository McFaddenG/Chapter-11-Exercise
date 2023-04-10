import re
name = input("Enter file: ")
handle = open(name)
text = input("Enter a regular expression: ")
count = 0

for line in handle:
	if re.search(text, line):
		count += 1

print(f"mbox.txt had {count} lines that matched {text}")


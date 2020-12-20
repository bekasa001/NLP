import re

file_in = open('jawiki-england.txt')
strings = file_in.readlines()

for line in strings:
	matchobj = re.fullmatch('(?P<equals>==+) ?([^= ]+) ?(?P=equals)\n', line)
	if matchobj:
		print(matchobj.group(2), len(matchobj.group(1)) - 1)

import re

file_in = open('jawiki-england.txt')
string = file_in.read()

categs = re.findall('^.*(?:Category|カテゴリ):.*$', string, flags=re.MULTILINE)
for line in categs:
	print(line)

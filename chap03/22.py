import re

file_in = open('jawiki-england.txt')
string = file_in.read()

categs = re.findall('(?:Category|カテゴリ):(.+?)(?:\]|\|)', string, flags=re.MULTILINE)
for word in categs:
	print(word)

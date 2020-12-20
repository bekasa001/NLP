import re

file_in = open('jawiki-england.txt')
string = file_in.read()

baseinfo = re.search('{{基礎情報 国.+?\n}}\n', string, flags=re.DOTALL)
objs = re.findall('\|(.*?[^ ])(?: *)=(?: *)([^ ].*?)\n(?:(?=\|)|})', baseinfo.group(0), flags=re.DOTALL)
templates = dict(objs)
print(templates)
print(len(templates))

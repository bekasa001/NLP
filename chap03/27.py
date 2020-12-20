import re

file_in = open('jawiki-england.txt')
string = file_in.read()

baseinfo = re.search('{{基礎情報 国.+?\n}}\n', string, flags=re.DOTALL)
objs = re.findall('\|(.*?[^ ])(?: *)=(?: *)([^ ].*?)\n(?:(?=\|)|})', baseinfo.group(0), flags=re.DOTALL)
templates = dict(objs)

file_out = open('27.txt', mode='w')
file_out.write('{{基礎情報 国\n')

for key in templates:
	tmp_string = re.sub('\'\'+', '', templates[key])
	templates[key] = re.sub('\[\[(?!ファイル:)(?!Category:)(?:[^\]]*\|)?((?:[^\]\|{}]|{{[^{}]+}})+)\]\]', '\g<1>', tmp_string)
	file_out.write('|' + key + ' = ' + templates[key] + '\n')
file_out.write('}}\n')
file_out.close()

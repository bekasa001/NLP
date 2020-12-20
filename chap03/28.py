import re

file_in = open('jawiki-england.txt')
string = file_in.read()

baseinfo = re.search('{{基礎情報 国.+?\n}}\n', string, flags=re.DOTALL)
objs = re.findall('\|(.*?[^ ])(?: *)=(?: *)([^ ].*?)\n(?:(?=\|)|})', baseinfo.group(0), flags=re.DOTALL)
templates = dict(objs)

file_out = open('28.txt', mode='w')
file_out.write('{{基礎情報 国\n')

for key in templates:
	tmp_string = re.sub('\'\'+', '', templates[key])
	tmp_string = re.sub('\[\[ファイル:[^[\]]*]]', '', tmp_string)
	tmp_string = re.sub('{{lang\|[^|]*\|([^}]*)}}', '\g<1>', tmp_string)
	tmp_string = re.sub('{{center\|([^}]*)}}', '\g<1>', tmp_string)
	tmp_string = re.sub('\[\[(?!Category:)(?:[^\]]*\|)?((?:[^\]\|{}]|{{[^{}]+}})+)\]\]', '\g<1>', tmp_string)
	tmp_string = re.sub('<ref[^>]*(?:/>|(?<!/)>.*?</ref>)', '', tmp_string, flags=re.DOTALL)
	tmp_string = re.sub('<br />', '', tmp_string)
	tmp_string = re.sub('{{仮リンク\|([^|]*)\|(?:[^|]*)\|(?:[^}]*)}}', '\g<1>', tmp_string)
	tmp_string = re.sub('{{en icon}}', '', tmp_string)
	tmp_string = re.sub('{{[0]}}', ' ', tmp_string)
	templates[key] = tmp_string
	file_out.write('|' + key + ' = ' + templates[key] + '\n')

file_out.write('}}\n')
file_out.close()

import re
import pandas as pd

file_mecab = open('neko.txt.mecab')

states = []
flag = True
while flag:
	state = []
	while True:
		line = file_mecab.readline()
		if (not line):
			flag = False
			break
		if (line == 'EOS\n'):
			if (len(state) > 0):
				states.append(state)
			break
		matchobj = re.fullmatch('(.+)\t(.+),(.+),[^,]+,[^,]+,[^,]+,[^,]+,(?:(?:(.+),.+,.+)|\*)\n?', line)
		if (not matchobj):
			print('Error on line: ' + line)
			flag = False
			break
		if (len(state) == 0 and matchobj.group(1) == '　'):
			continue
		if (matchobj.group(4)):
			state.append({'surface': matchobj.group(1), 'base': matchobj.group(4), 'pos': matchobj.group(2), 'pos1': matchobj.group(3)})
		else:
			state.append({'surface': matchobj.group(1), 'base': '*', 'pos': matchobj.group(2), 'pos1': matchobj.group(3)})

words = [word for state in states for word in state]
table = pd.DataFrame(words)
# print(table)

# base が無いものについては surface で置換
table['base'][table['base'] == '*'] = table['surface'][table['base'] == '*']

word_unique = table.groupby(['base', 'pos', 'pos1']).size()
word_unique.sort_values(ascending = False, inplace = True)
print(word_unique)

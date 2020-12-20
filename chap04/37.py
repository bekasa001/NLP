import re
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']

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

# extract states with 猫
states_with_cat = []
for state in states:
	flag = False
	for word in state:
		if (word['surface'] == '猫'):
			flag = True
			break
	if flag:
		states_with_cat.append(state)

words = [word for state in states_with_cat for word in state]
table = pd.DataFrame(words)
table.drop(table.index[table['surface'] == '猫'], inplace=True)
# print(table)

# base が無いものについては surface で置換
table['base'][table['base'] == '*'] = table['surface'][table['base'] == '*']

word_unique = table.groupby(['base', 'pos', 'pos1']).size()
word_unique.sort_values(ascending = False, inplace = True)

plt.bar(range(0, 10), word_unique[0:10], tick_label = [base for (base, _, _) in word_unique[0:10].index.values])
plt.savefig('37.png')

import re

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

AnoBs = []
for state in states:
	for i in range(1, len(state) - 1):
		if (state[i]['surface'] == 'の' and state[i]['pos'] == '助詞' and state[i - 1]['pos'] == '名詞' and state[i + 1]['pos'] == '名詞'):
			AnoBs.append(state[i - 1]['surface'] + 'の' + state[i + 1]['surface'])

print(AnoBs)
print(len(AnoBs))
print(len(set(AnoBs)))

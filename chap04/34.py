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

combs = []
for state in states:
	count = 0
	comb = ''
	for word in state:
		if (word['pos'] == '名詞'):
			comb = comb + word['surface']
			count += 1
		else:
			if (count >= 2):
				combs.append(comb)
			count = 0
			comb = ''
	if (count >= 2):
		combs.append(comb)

print(combs)
print(len(combs))
print(len(set(combs)))

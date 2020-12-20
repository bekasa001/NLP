from morph import Morph

file_cabocha = open('ai.ja.txt.parsed')

states = []
flag = True
while flag:
	state = []
	while True:
		line = file_cabocha.readline()
		if (not line):
			flag = False
			break
		if (line == 'EOS\n'):
			if (len(state)):
				states.append(state)
			break
		morph = Morph.readMecabLine(line)
		if (morph):
			state.append(morph)

for morph in states[1]:
	print(morph.tostr())

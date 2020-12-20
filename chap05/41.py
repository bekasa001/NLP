from chunk import Chunk

file_cabocha = open('ai.ja.txt.parsed')

states = []
lines = file_cabocha.read().split('\n')
while len(lines):
	state = []
	while True:
		if (lines[0] == 'EOS' or lines[0] == ''):
			if (len(state) > 0):
				states.append(state)
			lines= lines[1:]
			break
		chunk = Chunk()
		lines = chunk.readChunk(lines)
		if (chunk.dst >= -1):
			state.append(chunk)

	for i in range(len(state)):
		chunk = state[i]
		if (chunk.dst == -1):
			continue
		state[chunk.dst].srcs.append(i)

for i in range(len(states[1])):
	print(str(i) + ': ' + states[1][i].tostr() + ', ' + str(states[1][i].dst))

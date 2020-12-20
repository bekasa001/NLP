from chunk import Chunk

file_cabocha = open('ai.ja.txt.parsed')

states = Chunk.getChunks(file_cabocha.read())

for i in range(len(states[1])):
	print(str(i) + ': ' + states[1][i].tostr() + ', ' + str(states[1][i].dst))

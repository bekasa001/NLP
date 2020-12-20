import re
from chunk import Chunk

file_cabocha = open('ai.ja.txt.parsed')
states = Chunk.getChunks(file_cabocha.read())

pairs = []
for state in states:
	for chunk in state:
		if (chunk.dst != -1):
			flag = False
			for morph in chunk.morphs:
				if flag:
					continue
				if (morph.pos == '名詞'):
					flag = True
			if not flag:
				continue
			flag = False
			for morph in state[chunk.dst].morphs:
				if flag:
					continue
				if (morph.pos == '動詞'):
					flag = True
			if not flag:
				continue

			string = chunk.tostr() + '\t' + state[chunk.dst].tostr()
			pairs.append(re.sub('[。、，？・()（）「」〈〉『』〔〕]', '', string))

file_out = open('43.txt', 'w')
for pair in pairs:
	file_out.write(pair + '\n')
file_out.close()

import re
from chunk import Chunk

file_cabocha = open('ai.ja.txt.parsed')
states = Chunk.getChunks(file_cabocha.read())

patterns = []
for state in states:
	verbs = []
	for chunk in state:
		dic = {'base': '', 'post': []}
		for morph in chunk.morphs:
			if (morph.pos == '動詞'):
				dic['base'] = morph.base
				dic['post'] = []
				break
		verbs.append(dic)

	for chunk in state:
		if (chunk.dst == -1):
			continue
		lastid = len(chunk.morphs) - 1
		while (lastid >= 0 and chunk.morphs[lastid].pos == '特殊'):
			lastid = lastid - 1
		if (lastid >= 0 and chunk.morphs[lastid].pos == '助詞'):
			if (verbs[chunk.dst]['base'] != ''):
				verbs[chunk.dst]['post'].append(chunk.morphs[lastid].base)

	for dic in verbs:
		if (dic['base'] != ''):
			dic['post'].sort()
			patterns.append(dic)

file_out = open('45.txt', 'w')
for pattern in patterns:
	file_out.write(pattern['base'] + '\t' + ' '.join(pattern['post']) + '\n')
file_out.close()

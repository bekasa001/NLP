import re
from chunk import Chunk

file_cabocha = open('ai.ja.txt.parsed')
sents = Chunk.getChunks(file_cabocha.read())

paths = []
for sent in sents:
	for chunk in sent:
		flag = False
		for morph in chunk.morphs:
			if (morph.pos == '名詞'):
				flag = True
				break
		if not flag:
			continue
		path = []
		nowChunk = chunk
		path.append(nowChunk)
		while (nowChunk.dst != -1):
			nowChunk = sent[nowChunk.dst]
			path.append(nowChunk)
		paths.append(path)

file_out = open('48.txt', 'w')
for path in paths:
	file_out.write(' -> '.join([re.sub('[。、，？・()（）「」〈〉『』〔〕]', '', chunk.tostr()) for chunk in path]) + '\n')
file_out.close()

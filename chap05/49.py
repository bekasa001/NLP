import copy
import re
from chunk import Chunk

file_cabocha = open('ai.ja.txt.parsed')
sents = Chunk.getChunks(file_cabocha.read())

# confirm that the destination appears after.
for sent in sents:
	for i_x in range(len(sent)):
		if (sent[i_x].dst != -1 and sent[i_x].dst < i_x):
			print('Error: dependent to chunk before.')

file_out = open('49.txt', 'w')
for sent in sents:
	for i_x in range(len(sent)):
		for j_x in range(len(sent[i_x].morphs)):
			if (sent[i_x].morphs[j_x].pos != '名詞'):
				continue
			for i_y in range(i_x, len(sent)):
				for j_y in range(len(sent[i_y].morphs)):
					if (i_x == i_y and j_x >= j_y):
						continue
					if (sent[i_y].morphs[j_y].pos != '名詞'):
						continue
					c_x = i_x   # current chunk No. of x
					c_y = i_y   # current chunk No. of y
					pathx = []
					pathy = []
					while (c_x != c_y):
						if (c_x < c_y):
							if (c_x == i_x):
								pathx.append(copy.deepcopy(sent[c_x]))
								pathx[-1].morphs[j_x].surface = 'X'
							else:
								pathx.append(sent[c_x])
							c_x = sent[c_x].dst
						else:
							if (c_y == i_y):
								pathy.append(copy.deepcopy(sent[c_y]))
								pathy[-1].morphs[j_y].surface = 'Y'
							else:
								pathy.append(sent[c_y])
							c_y = sent[c_y].dst
					if (c_y == i_y):
						pathx.append(copy.deepcopy(sent[i_y]))
						pathx[-1].morphs[j_y].surface = 'Y'
						if (i_x == i_y):
							pathx[-1].morphs[j_x].surface = 'X'
						file_out.write(' -> '.join([re.sub('[。、，？・()（）「」〈〉『』〔〕]', '', chunk.tostr()) for chunk in pathx]) + '\n')
					else:
						file_out.write(' -> '.join([re.sub('[。、，？・()（）「」〈〉『』〔〕]', '', chunk.tostr()) for chunk in pathx]) + ' | ' + ' -> '.join([re.sub('[。、，？・()（）「」〈〉『』〔〕]', '', chunk.tostr()) for chunk in pathy]) + ' | ' + re.sub('[。、，？・()（）「」〈〉『』〔〕]', '', sent[c_y].tostr()) + '\n')
file_out.close()

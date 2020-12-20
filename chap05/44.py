from graphviz import Digraph
import re
import numpy as np

from chunk import Chunk

def dependencyGraph(sent):
	graph = Digraph(format='png')
	for i in range(len(sent)):
		graph.node(str(i), label = re.sub('[。、，？・()（）「」〈〉『』〔〕]', '', sent[i].tostr()))
	for i in range(len(sent)):
		if (sent[i].dst != -1):
			graph.edge(str(i), str(sent[i].dst))
	return graph

file_cabocha = open('ai.ja.txt.parsed')
sents = Chunk.getChunks(file_cabocha.read())

dependencyGraph(sents[np.argmax(list(map(len, sents)))]).render('44')

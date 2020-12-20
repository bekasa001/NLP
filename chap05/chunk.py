import re
from re import match
from morph import Morph

class Chunk:
	def __init__(self):
		self.morphs = []
		self.dst = -2
		self.srcs = []

	def readChunk(self, lines):
		for i in range(len(lines)):
			line = lines[i]
			if (not line):
				return lines[i:]
			if (line == 'EOS'):
				return lines[i:]
			if (line[0] == '*'):
				if (i == 0):
					matchobj = re.fullmatch('\* \d+ ([-\d]\d*)D.*', line)
					if (not matchobj):
						print(line)
					self.dst = int(matchobj.group(1))
				else:
					return lines[i:]
			else:
				morph = Morph.readMecabLine(line)
				if (morph == None):
					print('Error on: ' + line)
					return lines[i:]
				self.morphs.append(morph)

	def appendsrc(self, N):
		self.srcs.append(N)

	def tostr(self):
		return ''.join(morph.surface for morph in self.morphs)

	@staticmethod
	def getChunks(string):
		states = []
		lines = string.split('\n')
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

		return states

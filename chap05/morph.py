import re

class Morph:
	def __init__(self, surface, base, pos, pos1):
		self.surface = surface
		self.base = base
		self.pos = pos
		self.pos1 = pos1

	@staticmethod
	def readMecabLine(string):
		matchobj = re.fullmatch('(.+)\t(.+),(.+),[^,]+,[^,]+,[^,]+,[^,]+,(?:(?:(.+),.+,.+)|\*)\n?', string)
		if (not matchobj):
			return None
		if (matchobj.group(4)):
			return Morph(matchobj.group(1), matchobj.group(4), matchobj.group(2), matchobj.group(3))
		else:
			return Morph(matchobj.group(1), matchobj.group(1), matchobj.group(2), matchobj.group(3))

	def tostr(self):
		return ', '.join([self.surface, self.base, self.pos, self.pos1])

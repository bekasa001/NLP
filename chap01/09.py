import random

def shuffle_inside_letters(string):
	if (len(string) <= 4):
		return string
	return string[0] + ''.join(random.sample(string[1:-1], len(string) - 2)) + string[-1]

string = input()
words = string.split(sep = ' ')
print(' '.join(map(shuffle_inside_letters, words)))

one_letters = [1, 5, 6, 7, 8, 9, 15, 16, 19]

string = input()
words = [word.strip(',.') for word in string.split(' ')]

elements = {}
for i in range (1, len(words) + 1):
	length = 2
	if (i in one_letters):
		length = 1
	element = words[i - 1][0:length]
	elements[element] = i

print(elements)

def ngram(array, n = 2):
	answer = [array[i - n: i] for i in range(n, len(array) + 1)]
	return answer

string = input()
print(ngram(string))
words = [word.strip(',.') for word in string.split(' ')]
print(ngram(words))

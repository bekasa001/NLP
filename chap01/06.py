def ngram(array, n = 2):
	answer = [array[i - n: i] for i in range(n, len(array) + 1)]
	return answer

stringX = input()
stringY = input()
X = set(ngram(stringX))
Y = set(ngram(stringY))

print(X | Y)
print(X & Y)
print(X - Y)

if ('se' in X):
	print('There is \"se\" in X.')
else:
	print('There is NOT \"se\" in X.')

if ('se' in Y):
	print('There is \"se\" in Y.')
else:
	print('There is NOT \"se\" in Y.')

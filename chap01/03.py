string = input()
lengths = [len(word.strip(',.')) for word in string.split(' ')]
print(lengths)

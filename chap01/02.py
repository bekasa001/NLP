string0 = input()
string1 = input()

answer = ''
for i in range(0, min(len(string0), len(string1))):
	answer = answer + string0[i]
	answer = answer + string1[i]
print(answer)

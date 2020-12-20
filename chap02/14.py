file_in = open('popular-names.txt')
N = int(input())
string = ''.join([file_in.readline() for _ in range(N)])
print(string, end = '')

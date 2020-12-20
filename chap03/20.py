import json

file_in = open('jawiki-country.json')
file_out = open('jawiki-england.txt', mode='w')

data = json.loads(file_in.readline())

while True:
	data = json.loads(file_in.readline())
	if (data['title'] == 'イギリス'):
		file_out.write(data['text'])
		file_out.write('\n')
		break

file_out.close()

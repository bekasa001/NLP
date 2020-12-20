import pandas as pd

file_out = open('19_py.txt', mode='w')
table = pd.read_table('popular-names.txt', header=None)
counts = table[0].value_counts()
for key in counts.index:
	file_out.write(str(counts[key]) + ' ' + key + '\n')
file_out.close()

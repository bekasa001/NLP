import numpy as np
import pandas as pd

N = int(input())
table = pd.read_table('popular-names.txt', header=None)
tables = np.array_split(table, N)
for i in range(N):
	tables[i].to_csv('16_py{}.txt'.format(i), sep = '\t', header=False, index=None)

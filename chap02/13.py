import pandas as pd

col1 = pd.read_table('col1_py.txt', header=None)
col2 = pd.read_table('col2_py.txt', header=None)
table = pd.concat([col1, col2], axis = 1)
table.to_csv('13_py.txt', sep = '\t', header=False, index=None)

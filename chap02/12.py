import pandas as pd

table = pd.read_table('popular-names.txt', header=None)
table[0].to_csv('col1_py.txt', header=False, index=None)
table[1].to_csv('col2_py.txt', header=False, index=None)

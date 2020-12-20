import pandas as pd

table = pd.read_table('popular-names.txt', header=None)
table.to_csv('11_py.txt', sep = ' ', header=None, index=None)

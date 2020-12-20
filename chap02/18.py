import pandas as pd

table = pd.read_table('popular-names.txt', header=None)
table.sort_values(by=2, ascending=False, inplace=True)
table.to_csv('18_py.txt', sep = '\t', header=False, index=None)

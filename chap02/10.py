import pandas as pd

table = pd.read_table('popular-names.txt', header=None)
print(len(table))

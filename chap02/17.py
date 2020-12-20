import pandas as pd

table = pd.read_table('popular-names.txt', header=None)
nameset = set(table[0])
print(nameset)
print(len(nameset))

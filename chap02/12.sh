cut -f 1 popular-names.txt > col1_sh.txt
cut -f 2 popular-names.txt > col2_sh.txt
diff col1_py.txt col1_sh.txt
diff col2_py.txt col2_sh.txt

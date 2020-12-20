cut -f 1 popular-names.txt | sort | uniq -c | sort -n -r | sed 's/^ *//g' > 19_sh.txt
diff 19_py.txt 19_sh.txt

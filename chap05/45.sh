sort 45.txt | uniq -c | sort -n -r | sed 's/^ *//g' > 45_sh0.txt
grep -E ^'(行う|なる|与える)'$'\t' 45.txt | sort | uniq -c | sort -n -r | sed 's/^ *//g' > 45_sh1.txt

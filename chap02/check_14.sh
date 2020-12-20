N=3
echo $N | bash 14.sh > 14_sh.txt
echo $N | python3 14.py > 14_py.txt
diff 14_py.txt 14_sh.txt

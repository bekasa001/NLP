N=4
echo $N | bash 15.sh > 15_sh.txt
echo $N | python3 15.py > 15_py.txt
diff 15_py.txt 15_sh.txt

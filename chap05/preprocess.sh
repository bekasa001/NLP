sed s/。/。\\n/g ai.ja/ai.ja.txt > ai.ja.txt.newline
cabocha -f1 ai.ja.txt.newline -o ai.ja.txt.parsed

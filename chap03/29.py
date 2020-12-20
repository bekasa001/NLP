import re
import requests

file_in = open('jawiki-england.txt')
string = file_in.read()

baseinfo = re.search('{{基礎情報 国.+?\n}}\n', string, flags=re.DOTALL)
objs = re.findall('\|(.*?[^ ])(?: *)=(?: *)([^ ].*?)\n(?:(?=\|)|})', baseinfo.group(0), flags=re.DOTALL)
templates = dict(objs)

S = requests.Session()
URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "titles": ("File:" + templates['国旗画像']),
	"iiprop": "url"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()
PAGES = DATA["query"]["pages"]

for k in PAGES:
	print(PAGES[k]['imageinfo'][0]['url'])

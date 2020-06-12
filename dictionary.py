import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
        import requests
        import lxml
        from lxml import etree
except:
        install('requests')
        install('lxml')

URL = 'http://dict.hjenglish.com/'
cookies = dict()
try:
	file = open('cookies.txt')
	str = file.read()
except:
	print('无法找到cookies文件, 请将cookies.txt文件放入同一目录下')
	exit()
for c in str.split(';'):
	cookies[c.split('=')[0].strip()]=c.split('=')[1].strip()

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

def err():
	print('Usage: python dictionary.py dict word [OPTION]\n')
	print('dict:')
	print('英汉汉英词典: w')
	print('德汉汉德词典: de')
	print('日汉词典: jp/jc')
	print('汉日词典: jp/cj')

try:
	dictionary = sys.argv[1]
	word = sys.argv[2]
except:
	err()
	exit()

if dictionary not in ['w', 'de', 'jp/jc', 'jp/cj']:
	err()
	exit()

try:
	mode = sys.argv[3]
except:
	mode = None
	print('获取详细释义及例句请使用 python dictionary.py dict word d')
url = URL + dictionary + '/' + word
html = requests.post(url, headers = headers, cookies = cookies)
res = etree.HTML(html.text)

try:
	main_content = res.xpath("//body/div/div/main/div/section/div/section/div")[0]
	header = main_content.xpath("//header[@class='word-details-pane-header']")[0]
	word_text = header.xpath("//div[@class='word-info']/div[@class='word-text']/h2")[0]
	pronounces = header.xpath("//div[@class='word-info']/div[@class='pronounces']")[0]
	simple = header.xpath("//div[@class='simple']")[0]
	detail = main_content.xpath("//div[@class='word-details-pane-content']")[0]
except:
	print('未查询到相关释义, 请确认拼写以及词典的正确选择')
	exit()

def output(l):
	for content in l:
		if content != "":
			print(content)

print("查询词汇: " + word_text.text) #title
print("\n")
dummy = [r.replace("\n","").strip() for r in pronounces.xpath(".//node()") if type(r) == lxml.etree._ElementUnicodeResult]
output(dummy)
print("\n")
print("简略释义")
dummy = [r.replace("\n","").strip() for r in simple.xpath(".//node()") if type(r) == lxml.etree._ElementUnicodeResult]
output(dummy)
if mode == 'd':
	print("\n")
	dummy = [r.replace("\n","").strip() for r in detail.xpath(".//node()") if type(r) == lxml.etree._ElementUnicodeResult]
	output(dummy)

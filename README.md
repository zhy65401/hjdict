# 命令行沪江小D词典（自用）

## Usage
python dictionary.py dict word [OPTION]

dict:
w: 英文词典
de: 德语词典
jp/jc: 日汉词典
jp/cj：汉日词典

OPTION：
d：（可选）获取详细释义

## pre-configuration （仅需要做一次）
1. 由于沪江词典访问有严格的cookies检查， 所以需要先去往 https://www.hjdict.com/ 然后随便查一个词
2. 按f12并进入console标签，在里面输入javascript:document.write(document.cookie); 并敲回车
3. 将网页上的内容全选并复制到与dictionary.py同一目录下的cookies.txt中
4. 然后运行 python dictionary.py dict word [OPTION] 即可

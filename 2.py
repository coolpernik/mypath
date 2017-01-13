import requests 
from bs4 import BeautifulSoup

r=requests.get(r"http://www.qiushibaike.com/")
r.encoding="UTF8"

t=BeautifulSoup(r.text,'html.parser')
sts=t.select('.content')
for st in sts:
	print(st.text)
input("press any key to finish")
#http://xorx.cf/thread0806.php
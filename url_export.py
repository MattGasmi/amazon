import requests
from bs4 import BeautifulSoup
import re


cat_dic = {}

req = requests.get("https://www.amazon.com/Best-Sellers/zgbs")
soup = BeautifulSoup(req.text, 'html.parser')
cat_list = soup.find('ul', attrs={'id': 'zg_browseRoot'})
cat_name = re.findall('<li>.+?>(.+?)<', str(cat_list))
cat_url = re.findall('href=\"(.+?)\"', str(cat_list))
for i in range(len(cat_name)):
    cat_dic.update({cat_name[i]:cat_url[i]})
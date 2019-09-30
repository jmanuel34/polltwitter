from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
try:
    html= urlopen("http://elecciones.mir.es/generales2016/es/formaciones-politicas/candidaturas-presentadas/congreso.htm")
#    html = urlopen("http://elecciones.mir.es/generales2016/es/formaciones-politicas/candidaturas-presentadas/senado.htm")
#    html = urlopen("https://www.python.org/")
except HTTPError as e:
    print(e)
else:
    res = BeautifulSoup(html.read(),"html5lib")
    # tags = res.findAll('ul')
    for link in res.findAll('ul', {'class':'provincias'}):
        for link in link.findAll('a', attrs={'href': re.compile("^http://")}):
            print (link.get('href'))

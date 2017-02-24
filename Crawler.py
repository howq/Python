import urllib.request
import http.cookiejar
from bs4 import BeautifulSoup

fp = urllib.request.urlopen("http://baike.baidu.com/view/21087.htm")

mybytes = fp.read()
# note that Python3 does not read the html code as string
# but as html code bytearray, convert to string with
mystr = mybytes.decode("utf8")

fp.close()

print(mystr)
print(fp.getcode())

cj = http.cookiejar.CookieJar()

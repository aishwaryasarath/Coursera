import urllib.request
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://www.dph.illinois.gov/topics-services/diseases-and-conditions/diseases-a-z-list/coronavirus'
html_h = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html_h,"html.parser")

row = soup.find('h3')
print(row)

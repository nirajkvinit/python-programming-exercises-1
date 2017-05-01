# Note: this is not the best solution, put the output is readable in my opinion

import requests
from bs4 import BeautifulSoup
from textwrap import TextWrapper

r = requests.get("http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture")
soup = BeautifulSoup(r.text, "html.parser")

p = soup.find_all("p")

fulltext = ""


# Last rows were commercials so I cut them off here

for i in range(len(p) - 6):
    fulltext += ("\n" + p[i].get_text(strip=True) + "\n")

wrapper = TextWrapper(replace_whitespace=False)

print(wrapper.fill(fulltext))
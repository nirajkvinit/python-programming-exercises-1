from bs4 import BeautifulSoup
import requests, string

r = requests.get("http://www.nytimes.com/")
data = r.text
soup = BeautifulSoup(data, "html.parser")

headings = soup.find_all(class_="story-heading")
heading_list = []

for i in headings:
    heading_list.append(i.get_text(strip=True))

print("\nCount of story count in frontpage: %d\n" % len(heading_list))

trump_count = 0

print("Following articles tells about something Trump has done lately: \n")

for i in heading_list:
    if "Trump" in i:
        print(i)
        trump_count += 1

print("\nTrump total count: %d.\n\n%d %% of this articles in this page exist because of Trump." % (trump_count, (trump_count / len(heading_list) * 100)))
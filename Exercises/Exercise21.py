from bs4 import BeautifulSoup
import requests, string, os

# Getting story headings from internet

r = requests.get("http://www.nytimes.com/")
data = r.text
soup = BeautifulSoup(data, "html.parser")

headings = soup.find_all(class_="story-heading")
heading_list = []

# Making a list of story headings

for i in headings:
    heading_list.append(i.get_text(strip=True))

# Not every character is worthy to be in our filename

valid_chars = string.ascii_letters + string.digits + "-_ "
is_valid = 0

while is_valid == 0:
    counter = 0
    filename = input("\nName the file: ")
    for i in filename:
        if i not in valid_chars:
            counter += 1

    if counter == 0 and filename[0] != "_" and filename[0] != "-":
        is_valid = 1
    else:
        print("Invalid filename.\n")

# Making the filename (and making it to be a .txt)
filename = "_".join(filename.split()) + ".txt"
filepath = os.getcwd() + filename


# Writing to file
with open(filename, 'w') as open_file:
    open_file.write("Story headings at http://www.nytimes.com/ are currently: \n\n")
    for i in range(len(heading_list)):
        open_file.write(heading_list[i] + "\n")

# Closing file
open_file.close()

print("Story headings were saved to %s successfully." % filepath)
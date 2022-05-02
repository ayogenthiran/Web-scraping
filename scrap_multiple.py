import requests
from bs4 import BeautifulSoup

# Get The HTML
root = 'https://subslikescript.com'  # this is the homepage of the website
website = f'{root}/movies'  # concatenating the homepage with the movies section
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify()) # prints the HTML of the website

# Locate the box that contains title and transcript
box = soup.find('article', class_ = 'main-article')

# Store each link in "links" list (href doesn't consider root  "homepage", so we have to concatenate it later)
links = []
for link in box.find_all('a', href=True):  # find_all returns a list
    links.append(link['href'])


print(links)

# Loop through the "links" list and sending a request to each link
for link in links:
    website = f'{root}/{link}'
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    # Locate the box that contains title and transcript
    box = soup.find('article', class_='main-article')
    # Locate title and transcript
    title = box.find('h1').get_text()
    transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

    # Exporting data in a text file with the "title" name
    with open(f'{title}.txt', 'w') as file:
        file.write(transcript)

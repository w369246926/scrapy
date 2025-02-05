from bs4 import BeautifulSoup
import requests
website ='https://subslikescript.com/movies'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content,'lxml')# print(soup.prettify())
box = soup.find('article',class_='main-article')
links = []
for link in box.find_all('a',href=True):
    links.append(link['href'])
print(links)
import urllib.request
import requests
from bs4 import BeautifulSoup
from pathlib import Path

def delete_query(link):
    if '?' in link:
        return link.split('?')[0]
    return link

def save_file(url, path=''):
    if not path:
        path = 'files/' 
    Path(path).mkdir(parents=True, exist_ok=True)
    try:
        response = requests.get(url)
        with open(path + url.split('/')[-1], 'wb') as file:
            file.write(response.content)
    except:
        pass

def file_urls(url, path=''):
    links = []
    response = requests.get('https://' + url)
    soup = BeautifulSoup(response.content, "html.parser")
    tags = ['audio','embed','ifreame','img','input','script','source','track','video', 'link']
    for tag in tags:
        for link in soup.find_all(tag):
            if tag == "link":
                attr = link.get("href")
            else:
                attr = link.get("src")
            if attr is not None:
                if attr.startswith('/'):
                    links.append(delete_query(url + attr))
                else:
                    links.append(delete_query(attr))

    for link in links:
        save_file(link, path)  























# import time
# timer = 0
# for times in range(10):
#     start = time.time()


#     end = time.time()
#     timer += end - start

# print(timer / 10)

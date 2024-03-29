# & c:/Users/addii.DESKTOP-IK1H1QG/OneDrive/Desktop/pythonProject/venv/Scripts/Activate.ps1
import requests
from bs4 import BeautifulSoup
import tldextract


def get_links(domain):
    response = requests.get(domain)
    soup = BeautifulSoup(response.content, "html.parser")
    links = []
    for link in soup.find_all("a"):
        href = link.get("href")
        if href is not None and href.startswith('http'):
            links.append(href)
    return links


def filter_others(url, links):
    ext = tldextract.extract(url)
    sld = ext.domain
    tld = ext.suffix
    domain_name = f'{sld}.{tld}'
    return [link for link in links if domain_name in link]


def get_crawl(url, depth=2):
    """you shode insert url without protocol """
    url = 'https://' + url
    links = []
    def crawl(url, depth=2):
        if depth <= 0:
            return
        for link in get_links(url):
            links.append(link)
            depth -= 1
            crawl(link, depth)

    crawl(url, depth)
    links = list(set(links))
    return filter_others(url, links)



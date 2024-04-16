# & c:/Users/addii.DESKTOP-IK1H1QG/OneDrive/Desktop/pythonProject/venv/Scripts/Activate.ps1
import requests
from bs4 import BeautifulSoup
import tldextract


def get_links(domain):
    try:
        response = requests.get(domain,timeout=4)
    except:
        return []
    soup = BeautifulSoup(response.content, "html.parser")
    links = []

    ext = tldextract.extract(domain)
    sld = ext.domain
    tld = ext.suffix
    main_domain = f"{domain.split('/')[0]}//{sld}.{tld}" # extract base url for links

    for link in soup.find_all("a"):
        href = link.get("href")
        if href and href.startswith('/'):
            links.append(f"{main_domain}{href}")
        if href and href.startswith('http'):
            links.append(href)
    return links


def filter_others(url, links):
    # ext = tldextract.extract(url)
    # sld = ext.domain
    # tld = ext.suffix
    # domain_name = f'{sld}.{tld}'
    # return [link for link in links if domain_name in link]

    return [link for link in links if url in link]


def get_crawl(url, depth=2):
    """you shode insert url without protocol """
    url1 = 'https://' + url
    url2 = 'http://' + url
    links = []
    def crawl(url, depth=2):
        if depth <= 0:
            return
        for link in get_links(url):
            links.append(link)
            depth -= 1
            crawl(link, depth)
    
    crawl(url1, depth) # request to https
    crawl(url2, depth) # request to http
    
    links = list(set(links))
    links.sort()
    return filter_others(url, links)

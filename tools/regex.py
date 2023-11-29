import re
from bs4 import BeautifulSoup
import requests


def regex_finder(url, type = '', pattern = ''):
    """insert url without protocol \n
        type: email or phoneNumber"""
    try:
        content = requests.get('https://' + url).text
    except:
        print(f'https request for regex field: {url}')
        content = ""

    if type == "email":
        pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    elif type == "number":
        pattern = r'(0|\+98)?([ ]|-|[()]){0,2}9[1|2|3|4]([ ]|-|[()]){0,2}(?:[0-9]([ ]|-|[()]){0,2}){8}'
    elif pattern == '' and type == '':
        return
    
    finds = []
    is_there = True
    while is_there:
        find = re.search(pattern, content)
        if find:
            finds.append(find.group())
            content = content.replace(find.group(), '')
        else:
            is_there = False
    return finds
        



# print(regex_finder("www.simcart.com/simcards/mci", 'number'))
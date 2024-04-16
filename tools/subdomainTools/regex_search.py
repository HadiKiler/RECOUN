import re
from bs4 import BeautifulSoup
import requests


def finder(pattern, content):
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



def regex_finder(url, type = 'both'):
    """insert url without protocol \n
        type: email or phoneNumber"""
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    number_pattern = r'(0|\+98)?([ ]|-|[()]){0,2}9[1|2|3|4]([ ]|-|[()]){0,2}(?:[0-9]([ ]|-|[()]){0,2}){8}'
    try:
        content = requests.get('https://' + url).text
    except:
        try:
            content = requests.get('http://' + url).text
        except:
            content = ""


    if type == 'both':
        emails = finder(email_pattern, content)
        numbers = finder(number_pattern, content)
        return {
            'email': emails,
            'numbers': numbers
            }
    elif type == "email":
        pattern = email_pattern
        return finder(pattern, content)
    elif type == "number":
        pattern = number_pattern
        return finder(pattern, content)
    elif type == '':
        return


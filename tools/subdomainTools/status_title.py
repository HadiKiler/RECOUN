
import requests
from bs4 import BeautifulSoup

def get_title(response):
    try:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string
        return title
    except:
        return ''

def https_sCode_title(domain):
    try:
        response = requests.get('https://' + domain)
        title = get_title(response)
        return f'{title} - {response.status_code}'
    except:
        try:
            response = requests.get('http://' + domain)
            title = get_title(response)
            return f'{title} - {response.status_code}'
        except:
            return f'statusCode" and title, field'


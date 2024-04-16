import whois
from ipwhois import IPWhois
from pprint import pprint
import socket

def get_whois(url):
    try:
        results = whois.whois(url)
        obj = IPWhois(socket.gethostbyname(url))
        results = results | obj.lookup()
        return results
    except:
        return {}

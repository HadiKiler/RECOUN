import argparse
from tools.sitemap import *
from tools.subDomains import *
from tools.status_title import *
from tools.ip import *
from tools.ports import *
from tools.regex import *
from tools.who_is import *

parser = argparse.ArgumentParser(description='Process app inputs.')
parser.add_argument('--url', required=True, type=str, help='takes input url.')
parser.add_argument('--level', type=int, help='process level of working.')
parser.add_argument('--all', type=str, help='Runs the entire program.')
args = parser.parse_args()
url = args.url

subdomains = get_subdomains(url, 'tools/subdomains.txt')
subdomains_info = []

for subdomain in subdomains:
    info = {}
    info['domain'] = subdomain
    info['ip'] = get_ip(subdomain)
    info['ports'] = get_ports(get_ip(subdomain))
    info['stautsCode_title'] = https_sCode_title(subdomain)
    info['phone_email'] = {
        'email': regex_finder(url, 'email'),
        'number': regex_finder(url, 'number')
        }
    subdomains_info.append(info)
    
informations = {
    "domain": url,
    'links': get_crawl(url),
    'whois_info': get_whois(url),
    "subdomains": subdomains_info
    }

for item in informations['links']:
    print(item)
for item in informations['subdomains']:
    print(item)

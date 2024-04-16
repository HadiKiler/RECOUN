import time
import argparse
from tools.sitemap import *
from tools.who_is import *
from tools.wappalyzer import *
from tools.gowitness import *
from tools.subdomainTools.subdomains import *
from concurrent.futures import ThreadPoolExecutor
execute = ThreadPoolExecutor()


parser = argparse.ArgumentParser(description='Process app inputs.')
parser.add_argument('--url', required=True, type=str, help='takes input url.')
parser.add_argument('--level', type=int, help='process level of working.')
parser.add_argument('--all', type=str, help='Runs the entire program.')
args = parser.parse_args()
url = args.url

witness_path = os.path.join(Path(__file__).parent, 'files/gowitness')
start = time.time()

functions = {
    get_crawl:[url],
    get_subdomains: [url, 'tools/subdomainTools/subdomains.txt'],
    go_witness: [url, witness_path],
    get_whois:[url],
    get_wappalyzer:[url]
    }

informations = {
    'domain': url
}
names = ['links','subdomains', 'gowitness', 'whois', 'wappalyzer']
tasks = [execute.submit(fun,*argument) for fun,argument in functions.items()]

for key, value in dict(zip(names, tasks)).items():
    informations[key] = value.result()
  


print(informations['domain'])
print('------------------------------------------------------------')
for link in informations['links']:
    print(link)
print('------------------------------------------------------------')
for subdomain in informations['subdomains']:
    print(subdomain)
print('------------------------------------------------------------')
for key, value in informations['whois'].items():
    print(f'{key}: {value}')
print('------------------------------------------------------------')
for key, value in informations['wappalyzer'].items():
    print(f'{key}: {value}')
print('------------------------------------------------------------')
print(informations['gowitness'])




print(time.time()-start)








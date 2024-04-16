# pip install dnspython
import time
import dns.resolver
from .status_title import *
from .ip import *
from .ports import *
from .regex_search import *
from concurrent.futures import ThreadPoolExecutor
execute = ThreadPoolExecutor()



def get_info(url):
    functions = {
        get_ip: [url],
        get_ports: [get_ip(url)],
        https_sCode_title:[url],
        regex_finder:[url,"both"]
        }
    info = {
        'domain':url
        }
    names = ['ip', 'ports', 'stautsCode_title', 'email_phone']
    tasks = [execute.submit(fun,*argument) for fun,argument in functions.items()]

    for key, value in dict(zip(names, tasks)).items():
        info[key] = value.result()
    return info



def check(domain, subdomain, method="A"):
    subdomains = []
    try:
        answers = dns.resolver.query(subdomain + "." + domain, "A")
        for ip in answers:
            if method == "A":
                subdomains.append(subdomain + "." + domain)
            if method == "B":
                subdomains.append(subdomain + "." + domain + " - " + str(ip))
    except:
        return
    return list(set(subdomains))
            



def get_subdomains(domain, file_name, test=50):
    activates = []
    with open(file_name) as file:
        tasks = []
        for index,sub in enumerate(file):
            if index > test: break
            tasks.append(execute.submit(check, domain, sub.strip()))
        
        for item in tasks:
            result = item.result()
            if result != None:
               activates.append(*result)

    informations = []
    for subdomain in activates:
        informations.append(get_info(subdomain))
    return informations
            


# start = time.time()
# info = get_subdomains('time.ir', 'subdomains.txt')
# for item in info:
#     print(item)
# print(time.time()-start)
# print(get_info('www.numberland.ir'))

            





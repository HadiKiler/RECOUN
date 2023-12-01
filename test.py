# from threading import Thread
# from time import sleep

# def fruits(fruit):
#     print(f'start {fruit}')
#     sleep(1)
#     print(f'end {fruit}')
#     return f'{fruit} is Delicious'

# def boom():
#     sleep(1)
#     print('start boommmmmmmmmm !')

# def peaer():
#     print('start peaer')
#     sleep(1)
#     print('end peaer')




# # tasks = []
# # for item in range(3):
# #     task = Thread(target = apple)
# #     task.start() 
# #     tasks.append(task)


# # for item in tasks:
# #     item.join()

# # print('me')




# from concurrent.futures import ThreadPoolExecutor

# # with concurrent.futures.ThreadPoolExecutor() as execute:
# #     inputs = ['apple', 'orange','pear']
# #     tasks = [execute.submit(fruits, i) for i in inputs]
    
#     # for task in concurrent.futures.as_completed(tasks):
#     #     task.result()
#     # for i in tasks:
#     #     print(i.result())

#     # execute.submit(boom)

# execute = ThreadPoolExecutor()
# # execute.submit()      
# inputs = ['apple', 'orange','pear']
# tasks = [execute.submit(fruits, i) for i in inputs]
    
# for i in tasks:
#     result = i.result()
#     print(result)


# print('me')

import argparse
from tools.sitemap import *
from tools.subdomains import *
from tools.status_title import *
from tools.ip import *
from tools.ports import *
from tools.regex import *
from tools.who_is import *
from tools.wappalyzer import *
from tools.gowitness import *
import time
from concurrent.futures import ThreadPoolExecutor
execute = ThreadPoolExecutor()








functions = {
    get_ip: [url],
    get_ports: [get_ip(url)],
    https_sCode_title:[url],
    regex_finder:[url,"both"]
    }

info = {}
names = ['ip', 'ports', 'stautsCode_title', 'email_phone']
tasks = [execute.submit(fun,*argument) for fun,argument in functions.items()]

for key, value in dict(zip(names, tasks)).items():
    info[key] = value.result()
  





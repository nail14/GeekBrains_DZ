from itertools import zip_longest, islice
import re

with open('nginx_logs.txt', 'r', encoding='utf-8') as filename:
# def reader(filename):
   regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    # with open(filename) as f:
   log = filename.read()
   remote_addr_1 = re.findall(regexp, log)
   remote_addr = remote_addr_1[0:]
    #print (remote_addr)

with open('nginx_logs.txt', 'r', encoding='utf-8') as get_name:
# def get_1(get_name):
   regexp = r'GET'
   # with open(get_name) as q:
   log = get_name.read()
   request_type_1 = re.findall(regexp, log)
   request_type = request_type_1[0:]
   #print(request_type)

with open('nginx_logs.txt', 'r', encoding='utf-8') as product_2:
# def get_1(product_2):
   regexp = r'/downloads/product_1 HTTP/1.1'[0:] or r'/downloads/product_2 HTTP/1.1'[0:]
   # with open(product_2) as z:
   log = product_2.read()
   requested_resource_1 = re.findall(regexp, log)
   requested_resource = requested_resource_1[0:]
   #print(requested_resource)

gen_mix = ((remote_addr, request_type, requested_resource) for remote_addr, request_type,requested_resource in zip_longest(remote_addr, request_type,requested_resource, fillvalue=None))

output_1 = (*islice(gen_mix, len(request_type)),)
print(output_1)

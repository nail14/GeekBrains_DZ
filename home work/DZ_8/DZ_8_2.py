import re
input_filename = "nginx_logs.txt"
result_filename = "result_dz8_2.txt"

remote_addr = open(input_filename, 'r', encoding='utf-8')
requests_type = open(result_filename, 'w', encoding='utf-8')

mytext = remote_addr.read()

remote_addr_1 = (r'(\d*\.\d*\.\d*\.\d*)\s+\-\s\-\s(\[\d+\/\w+\/\d+:\d+:\d+:\d+\s.\d+\])\s"([E-T]{3})\s(\/\w+\/\w+\s[H-T]{4}\/\d.\d)')
# request_datetime = r'[^]'
# remote_addr_1.groups()
results = re.findall(remote_addr_1, mytext)
for item in results:
    print(item)
    requests_type.writelines(f'{item}, \n')
print('total: ' + str(len(results)))

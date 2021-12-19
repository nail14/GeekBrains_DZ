####  Найти IP адрес спамера и количество отправленных им запросов по данным файла логов

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    remote_addr_list = [line[:line.find(' ')]for line in f]

addr_max = max(set(remote_addr_list), key=remote_addr_list.count)
print(addr_max, remote_addr_list.count(addr_max))
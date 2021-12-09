
from requests import get, utils
response = get('http://www.cbr.ru/scripts/XML_daily.asp')
print(type(response))
print(dir(response))

encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)
print(content)
# print(response.txt)

def main(argv):
    program, *argv = argv
    result = sum(map(int,argv))
    print(f'результат: {result}')

    return 0
if __name__ =='__main__':
    import sys

    print(sys.argv)

    main(sys.argv)

def currency_rates(argv):
    program, *argv = argv
    result = sum(map(int, argv))
    print(f'результат2: {result}')

# print(content.NumCode(float(840)).Value)

currency_rates(input("введите валюту в формате (USD,usd):"))
for n in content.split('</Value>'):
    print(n)
    head = requests.headers["date"]
    print(head())
# from requests import request, get, head, post, patch, put, delete, \
#                      options, utils, session, Session, codes
#import requests.utils
#request, get, utils
# from sys import getsizeof




#



#encodings = utils.get_encoding_from_headers(response.headers)





# print(head str["date"])
########float
########<Valute ID="R01235">
# <NumCode>840</NumCode>
# <CharCode>USD</CharCode>
# <Nominal>1</Nominal>
# <Name>Доллар США</Name>
# <Value>74,1399</Value>
# </Valute>
# def current_rates(*args):
#     pass
#http://www.cbr.ru/scripts/XML_daily.asp

# r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
# r.status_code
# 200
# r.headers['content-type']
# 'application/json; charset=utf8'
# r.encoding
# 'utf-8'
# r.text
# '{"type":"User"...'
# r.json()
# print({f'private_gists': 419, 'total_private_repos': 77, ...})
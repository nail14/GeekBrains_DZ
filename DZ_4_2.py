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
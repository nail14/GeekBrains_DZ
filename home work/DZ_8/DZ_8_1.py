import re

def email_parse(email_address):
    parsed = re.findall(r'([^@&]+)@([\w_-][\w_\.-]*\.[\w_-]{2,})$', email_address)    ###  ^\w+@\w+.\w{2,}$
    if not parsed:
        raise ValueError(f"wrong email: {email_address}")
    return dict(zip(['username', 'domain'], parsed[0]))

#print(email_parse('someone@geekbrainsru'))
print(email_parse('someone@geekbrains.ru'))

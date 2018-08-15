import re

some_text = 'alpha, beta,,,, gamma    delta'

data = re.split('[, ]+', some_text)

data01 = re.split('o+(o)', 'foobar')

data03 = re.split('[, ]+', some_text, maxsplit=2)

data04 = re.split('[, ]+', some_text, maxsplit=1)

print(data, data01, data03, data04)

pat = '[a-zA-Z]+'

text = '"Hm... Err -- are you sure?" he said, sounding insecure.'
data05 = re.findall(pat, text)

pat = r'[.?\-",]+'

data06 = re.findall(pat, text)

print(data05, data06)

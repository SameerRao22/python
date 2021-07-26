'''import requests 

link = "https://en.wikipedia.org/wiki/LeBron_James"
x = requests.get(link)
print(x.text)
'''
import requests

url = "https://www.universalsecurity.com/faqs/carbon-monoxide-alarm/what-are-some-common-sources-of-carbon-monoxide-co"

r = requests.get(url, stream=True)

for line in r.iter_lines():
    if line: print(line)


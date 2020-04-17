import re

url = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'(http[s]?://)(www.)?([a-z]+\.[a-z]+)')

matches = pattern.finditer(url)

# print group 3 to print out all the hostnames 
for match in matches:
  print(match[3])

# substitute url with group 3 and assign it to subbed_url
subbed_url = pattern.sub(r'\3', url)
print(subbed_url)

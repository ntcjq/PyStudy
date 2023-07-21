from bs4 import BeautifulSoup


soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
tag = soup.b



print(type(tag))


print(tag.name)

print(tag.attrs)

print(tag.string)

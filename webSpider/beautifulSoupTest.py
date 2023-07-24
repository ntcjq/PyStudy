from bs4 import BeautifulSoup

if __name__ == "__main__":
    soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
    tag = soup.b

    print(type(tag))

    print(tag.name)

    print(tag.attrs)

    print(tag.string)

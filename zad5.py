htmlString = '<h1 href="https://www.w3schools.com">this is a header1</h1> <h2>this is a medium header</h2> <h1>this is a header2</h1>'
hoptag = 'h1'

def getTagContent(html,tag):
    def endswith(string):
        return not string.endswith('>')

    def strip(string):
        novi_string = string.strip()
        return novi_string

    def count(string):
        if string.count(tag) == 0:
            return False
        else:
            return True

    def split(string):
        novi_string = string.split('>')
        return novi_string

    def izdvoji_poslednji_element(lista):
        return lista[1]

    x = html.split('<')
    c = list(map(strip,x))
    y = list(filter(endswith, c))
    z = list(filter(count, y))
    o = list(map(split, z))
    r = list(map(izdvoji_poslednji_element, o))
    print(r)

getTagContent(htmlString,hoptag)
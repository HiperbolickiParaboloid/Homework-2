htmlString = '<h1 href="https://www.w3schools.com"><a>this is a header1</a></h1> <h2>this is a medium header</h2> <h1>this is a header2</h1> <h2>this is a header2</h2>'
hoptag = 'h1'

def getTagContent(html,tag):
    def endswith(string):
        return string.endswith('</')

    def strip(string):
        novi_string = string.strip()
        return novi_string

    def find(string):
        x = string.find('>')
        y=x+1
        if x >=0:
            return string[y:]
        else:
            return string

    def length(string):
        d = len(string)-2
        return string[:d]

    x = html.split(tag+'>')
    c = list(map(strip,x))
    y = list(filter(endswith, c))
    z = list(map(find, y))
    o = list(map(length, z))
    print (o)

getTagContent(htmlString,hoptag)

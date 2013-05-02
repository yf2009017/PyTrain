from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    'An HTML passer that constructs the list of all href attribute values'
    def __init__(self):
        HTMLParser.__init__(self)
        self.l = []
        self.d = ''
        self.times = []
    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if attr[0] == 'href':
                self.l.append(attr[1])
            elif attr[0] == 'span':
                self.times.append(attr[1])
    def handle_data(self, data):
        self.d += ' ' + data
    def getTimes(self):
        return self.times
    def getLinks(self):
        return self.l
    def getData(self):
        return self.d

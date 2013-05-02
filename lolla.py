from urllib.request import urlopen
from urllib.parse import urljoin
import re
import sqlite3
import myparser

# Helper functions
class Driver(object):
    def __init__(self):
        self.l = []

    def getTimes(self, url):
        content = urlopen(url).read().decode('utf-8')
        parser = myparser.MyHTMLParser()
        parser.feed(content)
        raw = parser.getData()
        data = re.sub('\s', '', content)

        times = re.findall('<b>[Due|0-9|\-]*</b>[min]*', data)
        for i in range(len(times)):
            times[i] = re.sub('[<b>/|<\b>]*', '', times[i])

        return(times)
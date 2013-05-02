from urllib.request import urlopen
from urllib.parse import urljoin
import re
import sqlite3
import myparser

# Helper functions
class Driver(object):
    def __init__(self):
        self.l = []
    
    def hyperlinks(self, url):
        '''return a list of links contained in content,
        an html document with URL url; the links in the list
        should all be converted to absolute links'''
        content = urlopen(url).read().decode('utf-8')
        myparser = MyHTMLParser()
        myparser.feed(content)
        urls = myparser.getLinks()
        res = []
        
        for u in urls:
            absolute = urljoin(url,u)
            if absolute[0:4] == 'http':
                res.append(absolute)

        return(res)
    
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

    def getTrains(self, url):
        content = urlopen(url).read().decode('utf-8')
        parser = myparser.MyHTMLParser()
        parser.feed(content)
        raw = parser.getData()
        data = re.sub('\s', '', content)

        trains = re.findall('[\w]*\s?&gt;\s?[\w\'\-/]*', data)
        for i in range(len(trains)):
            trains[i] = re.sub('&gt;', ' ', trains[i])
        return(trains)

    def stopSelection(self, line):
        if (line.upper() == 'RED LINE'):
            stops = {'47th' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41230',
                     '63rd' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40910',
                     '69th' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40990',
                     '79th' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40240',
                     '87th' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41430',
                     '95th/Dan Ryan' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40450',
                     'Addison' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41420',
                     'Argyle' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41200',
                     'Belmont' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41320',
                     'Berwyn' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40340',
                     'Bryn Mawr' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41380',
                     'Cermak-Chinatown' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41000',
                     'Chicago' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41450',
                     'Clark/Division' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40630',
                     'Fullerton' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41220',
                     'Garfield' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41170',
                     'Grand' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40330',
                     'Granville' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40760',
                     'Harrison' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41490',
                     'Howard' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40900',
                     'Jackson' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40560',
                     'Jarvis' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41190',
                     'Lake' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41660',
                     'Lawrence' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40770',
                     'Loyola' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41300',
                     'Monroe' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41090',
                     'Morse' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40100',
                     'North/Clybourn' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40650',
                     'Roosevelt' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41400',
                     'Sheridan' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40080',
                     'Sox-35th' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40190',
                     'Thorndale' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40880',
                     'Wilson' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40540'
                     }
            return(stops)
        elif (line.upper() == 'BLUE LINE'):
            stops = {'Addison' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41240',
                     'Austin' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40010',
                     'Belmont' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40060',
                     'California' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40570',
                     'Chicago' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41410',
                     'Cicero' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40970',
                     'Clark/Lake' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40380',
                     'Clinton' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40430',
                     'Cumberland' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40230',
                     'Damen' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40590',
                     'Division' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40320',
                     'Forest Park' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40390',
                     'Grand' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40490',
                     'Harlem (FP)' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40980',
                     'Harlem (OH)' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40750',
                     'Illinois Medical District' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40810',
                     'Irving Park' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40550',
                     'Jackson' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40070',
                     'Jefferson Park' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41280',
                     'Kedzie-Homan' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40250',
                     'LaSalle' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41340',
                     'Logan Square' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41020',
                     'Monroe' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40790',
                     'Montrose' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41330',
                     'O\'Hare' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40890',
                     'Oak Park' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40180',
                     'Pulaski' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40920',
                     'Racine' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40470',
                     'Rosemont' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40820',
                     'UIC-Halsted' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40350',
                     'Washington' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40370',
                     'Western (FP)' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40220',
                     'Western (OH)' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40670'
                     }
            return(stops)

        elif (line.upper() == 'BROWN LINE'):
            stops = {'Adams/Wabash' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40680',
                     'Addison' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41440',
                     'Armitage' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40660',
                     'Belmont' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41320',
                     'Chicago' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40710',
                     'Clark/Lake' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40380',
                     'Damen' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40090',
                     'Diversey' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40530',
                     'Francisco' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40870',
                     'Fullerton' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41220',
                     'Library-State/Van Buren' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40850',
                     'Irving Park' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41460',
                     'Kedzie' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41180',
                     'Kimball' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41290',
                     'LaSalle/Van Buren' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40160',
                     'Madison/Wabash' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40640',
                     'Merchandise Mart' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40460',
                     'Montrose' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41500',
                     'Paulina' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41310',
                     'Quincy' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40040',
                     'Randoph/Wabash' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40200',
                     'Rockwell' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41010',
                     'Sedgwick' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40800',
                     'Southport' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40360',
                     'State/Lake' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40260',
                     'Washington/Wells' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40730',
                     'Wellington' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41210',
                     'Western' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41480'
                 }
            return(stops)
        elif (line.upper() == 'GREEN LINE'):
            stops = {
                     '35th-Bronzeville-IIT' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41120',
                     '43rd' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41270',
                     '47th' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41080',
                     '51st' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40130',
                     'Adams/Wabash' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40680',
                     'Ashland' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40170',
                     'Ashland/63rd' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40290',
                     'Austin' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41260',
                     'California' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41360',
                     'Central' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40280',
                     'Cicero' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40480',
                     'Clark/Lake' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40380',
                     'Clinton' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41160',
                     'Conservatory-Central Park Drive' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41670',
                     'Cottage Grove' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40720',
                     'Garfield' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40510',
                     'Halsted' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40940',
                     'Harlem/Lake' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40020',
                     'Indiana' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40300',
                     'Kedzie' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41070',
                     'King Drive' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41140',
                     'Laramie' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40700',
                     'Madison/Wabash' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40640',
                     'Oak Park' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41350',
                     'Pulaski' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40030',
                     'Randolph/Wabash' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40200',
                     'Ridgeland' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40610',
                     'Roosevelt' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41400',
                     'State/Lake' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40260'
                      }
            return(stops)
            
        elif (line.upper() == 'ORANGE LINE'):
            stops = {
                     '35th/Archer' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40120',
                     'Adams/Wabash' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40680',
                     'Ashland' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41060',
                     'Clark/Lake' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40380',
                     'Halsted' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41130',
                     'Library-State/Van Buren' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40850',
                     'Kedzie' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41150',
                     'LaSalle/Van Buren' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40160',
                     'Madison/Wabash' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40640',
                     'Midway' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40930',
                     'Pulaski' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40960',
                     'Quincy' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40040',
                     'Randolph/Wabash' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40200',
                     'Roosevelt' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41400',
                     'State/Lake' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40260',
                     'Washington/Wells' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40730',
                     'Western' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40310'
                    }
            return(stops)
        elif (line.upper() == 'PURPLE LINE'):
            stops = {
                     'Adams/Wabash' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40680',
                     'Armitage' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40660',
                     'Belmont' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41320',
                     'Central' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41250',
                     'Chicago' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40710',
                     'Clark/Lake' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40380',
                     'Davis' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40050',
                     'Dempster' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40690',
                     'Diversey' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40530',
                     'Foster' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40520',
                     'Fullerton' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41220',
                     'Library-State/Van Buren' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40850',
                     'Howard' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40900',
                     'LaSalle/Van Buren' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40160',
                     'Linden' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41050',
                     'Madison/Wabash' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40640',
                     'Main' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40270',
                     'Merchandise Mart' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40460',
                     'Noyes' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40400',
                     'Quincy' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40040',
                     'Randolph/Wabash' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40200',
                     'Sedgwick' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40800',
                     'South Boulevard' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40840',
                     'State/Lake' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40260',
                     'Washington Wells' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40730',
                     'Wellington' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41210'
                    }
            return(stops)
        elif (line.upper() == 'PINK LINE'):
            stops = {
                     '18th' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40830',
                     '54th/Cermak' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40580',
                     'Adams/Wabash' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40680',
                     'Ashland' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40170',
                     'California' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40440',
                     'Central Park' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40780',
                     'Cicero' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40420',
                     'Clark/Lake' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40380',
                     'Clinton' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41160',
                     'Damen' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40210',
                     'Library-State Van Buren' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40850',
                     'Kedzie' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41040',
                     'Kostner' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40600',
                     'LaSalle/Van Buren' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40160',
                     'Madison/Wabash' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40640',
                     'Polk' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=41030',
                     'Pulaski' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40150',
                     'Quincy' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40040',
                     'Randolph/Wabash' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40200',
                     'State/Lake' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40260',
                     'Washington/Wells' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40730',
                     'Western' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40740'
                    }
            return(stops)
        elif(line.upper() == 'YELLOW LINE'):
            stops = {
                     'Howard' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40900',
                     'Skokie' : 'http://www.transitchicago.com/mobile/traintrackerarrivals.aspx?sid=40140'
                     }
            return(stops)
            

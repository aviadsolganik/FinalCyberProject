from JOOMLADetector import JOOMLADetector
from MyDB import MyDB

import datetime


class Main(object):
    def main(self):
        today = str(datetime.date.today()).split("-")
        today_year = today[0]
        today_month = today[1]
        mydb = MyDB()
        mydb.connect()
        urls = ['www.nationalcrimeagency.gov.uk', 'www.nowarchitecture.com', 'www.uxbridge.ac.uk',
                'www.itwire.com', 'brw.nl', 'www.autocrescente.com', 'www.byronbay.com.au',
                'www.kentatearchitect.com', 'www.timclarkedesign.com', 'www.bssbfurniture.com']
        for url in urls:
            detector = JOOMLADetector(url)
            elements = detector.detect()
            print(url + ': ' + str(elements))
            if elements[0] == 'True' and elements[1] != 'version not found':
                if mydb.select(url) is not None:
                    date = str(mydb.select(url)[0][4]).split(" ")
                    date_t = date[0].split("-")
                    year = date_t[0]
                    month = date_t[1]
                    if int(year) < int(today_year):
                        mydb.delete(url)
                        mydb.insert_data(url, 'JOOMLA!', elements[1])
                    elif int(year) == int(today_year):
                        if int(today_month) > int(month):
                            mydb.delete(url)
                            mydb.insert_data(url, 'JOOMLA!', elements[1])
        mydb.disconnect()
        print('done')


main = Main()
main.main()

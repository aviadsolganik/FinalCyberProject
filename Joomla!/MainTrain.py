from JOOMLADetector import JOOMLADetector
from MyDB import MyDB


class Main(object):
    def main(self):
        mydb = MyDB()
        mydb.connect()
        urls = ['www.itwire.com', 'brw.nl', 'www.autocrescente.com', 'www.byronbay.com.au',
                'www.kentatearchitect.com', 'www.timclarkedesign.com', 'www.bssbfurniture.com']
        for url in urls:
            detector = JOOMLADetector(url)
            elements = detector.detect()
            print(url + ': ' + str(elements))
            if elements[0] is True and elements[1] != 'version not found':
                if mydb.select(url) is not None:
                    mydb.insert_data(url, 'JOOMLA!', elements[1])
        mydb.disconnect()


main = Main()
main.main()

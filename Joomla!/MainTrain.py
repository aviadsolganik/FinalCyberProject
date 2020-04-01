from JOOMLADetector import JOOMLADetector


class Main(object):
    def main(self):
        urls = ['www.itwire.com', 'brw.nl', 'www.autocrescente.com', 'www.byronbay.com.au',
                'www.kentatearchitect.com', 'www.timclarkedesign.com', 'www.bssbfurniture.com']
        for url in urls:
            detector = JOOMLADetector(url)
            print(url + ': ' + str(detector.detect()))


main = Main()
main.main()

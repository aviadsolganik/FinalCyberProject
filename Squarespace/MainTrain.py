from Squarespace.squarespace_detector import SquareSpaceDetector


class Main(object):
    def main(self):
        domain = 'www.devonstank.com'
        sd = SquareSpaceDetector(domain)
        res = sd.detect()
        print(res)


main = Main()
main.main()

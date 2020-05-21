
from WP.https_request_handler import HTTPRequestHandler
from WP.proxy import Proxy
from platformsdetector import PlatformsDetector


class SquareSpaceDetector(PlatformsDetector):

    def __init__(self, proxies=None):

        super().__init__(proxies)
        self._domain = ""
        if proxies is None:
            self._proxies = proxies
        else:
            tmp = []
            self._proxies = []
            for proxy in proxies:
                p = Proxy(proxy)
                tmp.append(p)
            self._proxies = tmp

    def get_platform_name(self):
        return "SquareSpace"

    def formaturl(self, url):
        if url.startswith('http://') or url.startswith('https://'):
            res = url
        else:
            res = 'http://' + url
        if res.endswith('/'):
            res = res.strip('/')
        return res

    def detect(self, domain, retries=0, timeout=5, aggressive=False, urls=None, proxies=None):
        """
                This function detects if the website on the domain runs over SquareSpace. if it is, it will detect the version
                :param domain:
                :param aggressive: if aggressive is False, the maximal number of HTTP requests is len(urls) + 2
                :param urls: URLs to analyze; make sure the URLs are relevant for the domain
                :param proxies: working via HTTP proxies. If None, the constructor's proxies are used (if any)
                :param retries: The number of tries that each HTTP request will be sent until it will succeed
                :param timeout: How much time each HTTP request will wait for an answer
                :return: a tuple: (whether the domain operates over SquareSpace, its version)
                """
        self._domain = domain
        if self.is_squarespace(urls=urls, proxies=proxies, timeout=timeout, retries=retries):
            res = self.get_info(timeout=timeout, retries=retries)
            if res:
                return 'SquareSpace', True, res
            else:
                return 'SquareSpace', False, "could'nt establish a connection"

        else:
            return 'SquareSpace', False, "Not running on SquareSpace platform"

    def is_squarespace(self, urls=None, proxies=None, timeout=5, retries=0):
        """
               This function detects if the website runs over SquareSpace
               :param urls: URLs to analyze; make sure the URLs are relevant for the domain
               :param proxies: working via HTTP proxies. If None, the constructor's proxies are used (if any)
               :param retries: The number of tries that each HTTP request will be sent until it will succeed
               :param timeout: How much time each HTTP request will wait for an answer
               :return: boolean: (whether the domain operates over SquareSpace)
               """
        url = self.formaturl(self._domain)
        if urls is None:
            httpreq = HTTPRequestHandler(proxies=proxies, retries=retries, timeout=timeout)
            r = httpreq.send_http_request(method='get', url=url)
            if r is None:
                pass
            if r.status_code is not (200 or 403):
                print(r.status_code)
                print("could'nt establish a connection")
                return False
            else:
                #url = url
                #http_handler = HTTPRequestHandler(proxies=proxies, retries=retries, timeout=15)
                #r = http_handler.send_http_request(method='get', url=url)
                if r.status_code is (200 or 403):
                    if r.text.find('<!-- This is Squarespace. -->') > -1:
                        if r.text.find('templateId') > -1 and r.text.find('templateVersion') > -1:
                            return True
                    else:
                        return False

                else:
                    return False

    def get_info(self, timeout, retries):
        """
            this function is resposable for checking the template id and version
                      """
        complete_url = 'https://' + str(self._domain)
        http_handler = HTTPRequestHandler(proxies=self._proxies, retries=retries, timeout=timeout)
        response = http_handler.send_http_request(method='get', url=complete_url)
        if response is None:
            return False
        if response.status_code == 200:
            text = response.text
            list = text.split('"')
            index = list.index('templateVersion')
            version = list[index + 2]
            index = list.index('templateId')
            template_id = list[index + 2]
            #return 'TemplateId: ' + template_id + ',version: ' + version
            return template_id+','+version
        else:
            return False

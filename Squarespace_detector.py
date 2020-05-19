from https_request_handler import HTTPRequestHandler
from proxy import Proxy
import enum


class squarspace_detector(object):

    def __init__(self, domain, proxies=None):

        self._domain = domain
        if proxies is None:
            self._proxies = proxies
        else:
            tmp = []
            self._proxies = []
            for proxy in proxies:
                p = Proxy(proxy)
                tmp.append(p)
            self._proxies = tmp

    def detect(self, retries=0, timeout=5, urls=None, proxies=None):

        if proxies is None:
            proxies = self._proxies

        if self.is_squarespace(urls=urls, proxies=proxies, timeout=timeout, retries=retries):
            return 'The url you have entered is running on SquareSpace platform' + '' + self.get_info(timeout=timeout,
                                                                                                      retries=retries)

        else:
            return False, "Not running on SquareSpace platform"

    def is_squarespace(self, urls=None, proxies=None, timeout=5, retries=0):
        if urls is None:
            url = 'https://' + str(self._domain)
            httpreq = HTTPRequestHandler(proxies=proxies, retries=retries, timeout=timeout)
            r = httpreq.send_http_request(method='get', url=url)
            if r is None:
                pass
            if r.status_code is not (200 or 403):
                print("could'nt establish a connection")
                return False
            else:
                url = url + 'config'
                r = httpreq.send_http_request(method='get',url=url)
                if r.status_code is 200:
                    if "https://assets.squarespace.com/" in str(r.content).lower():
                        return True
                    else:
                        return False

                else:
                    return False



    def templete_id_to_name(TemplateId):
        dict = {'515c7bd0e4b054dae3fcf003': ['Adversary', 'Alex', 'Marquee', 'Shift', 'Eamon']
            , '52a74dafe4b073a80cd253c5': ['Anya', 'Bedford', 'Bryant', 'Hayden']
            , '55f0aac0e4b0f0a5b7e0b22e': ['Vow', 'Pursuit']
                }

        return '7'

    def get_info(self, timeout, retries):
        complete_url = 'https://' + str(self._domain)
        http_handler = HTTPRequestHandler(proxies=self._proxies, retries=retries, timeout=timeout)
        response = http_handler.send_http_request(method='get', url=complete_url)
        text = response.text
        list = text.split('"')
        index = list.index('templateVersion')
        version = list[index + 2]
        index = list.index('templateId')
        TemplateId = list[index + 2]
        return ' ' + 'with the TemplateId: ' + TemplateId + ' ' + 'and it is running on version number: ' + version

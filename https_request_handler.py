import time
import requests

from WP.proxy import Proxy


class HTTPRequestHandler(object):
    def __init__(self, cookies=None, payload=None, proxies=None, timeout=5, retries=0):
        '''
        This function initializes the http request handler with parameters
        :param payload:Dictionary. {k:v,k:v}
        :param proxies: list. proxies to send the http request via
        :param timeout: int. how much time to wait if we don't get an answer
        :param retries: int. how many time to resend the request if we don't get an answer
        '''
        self._proxies = proxies
        self._timeout = timeout
        self._retries = retries
        self._payload = payload
        self._cookies = cookies

    def send_http_request(self, method, url):
        '''
        This function handles the https requests and send a post/get message with proxies,timeout and retries
        :param method: string get/post
        :param url: string. the url to send the message to
        :return: requests.models.Response
        '''
        if not url:
            raise Exception
        if self._retries == 0:
            if not self._proxies:
                proxy_dict = {}
            else:
                proxy_dict = Proxy.prepare_proxy_to_requests(proxy=Proxy.get_random_proxy(list_of_proxies=self._proxies))
            try:
                r = None
                if method == 'get':
                    r = requests.get(url, timeout=self._timeout, proxies=proxy_dict)
                if method == 'post':
                    r = requests.post(url, timeout=self._timeout, proxies=proxy_dict, data=self._payload, cookies=self._cookies)
                return r
            except Exception as e:
                print(e)
        else:
            for i in range(self._retries):
                if not self._proxies:
                    proxy_dict = {}
                else:
                    proxy_dict = Proxy.prepare_proxy_to_requests(proxy=Proxy.get_random_proxy(list_of_proxies=self._proxies))
                try:
                    r = None
                    if method == 'get':
                        r = requests.get(url, timeout=self._timeout, proxies=proxy_dict)
                    if method == 'post':
                        r = requests.post(url, timeout=self._timeout, proxies=proxy_dict, data=self._payload, cookies=self._cookies)
                    return r
                except Exception as e:
                    print(e)
                time.sleep(0.1)

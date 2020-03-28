import random


class Proxy(object):

    def __init__(self, proxy_string):
        '''
        This initializes the Proxy object by transfering a string to the classes data members
        :param proxy_string: string.
        '''
        proxy_string_as_list = proxy_string.split('://')
        self._protocol = proxy_string_as_list[0]
        proxy_strig_ip_port = proxy_string_as_list[1].split(':')
        self._ip = proxy_strig_ip_port[0]
        self._port = proxy_strig_ip_port[1]
        # self._previous_used = None

    @staticmethod
    def get_random_proxy(list_of_proxies):
        '''
        This function gets a random proxy from a list of proxies
        :param list_of_proxies: list.
        :return: Proxy
        '''
        i = random.randrange(len(list_of_proxies))
        # while (list_of_proxies[i] == self._previous_used) and len(list_of_proxies != 1):
        if len(list_of_proxies) != 1:
            i = random.randrange(len(list_of_proxies))
        # self._previous_used = list_of_proxies[i]
        return list_of_proxies[i]

    @staticmethod
    def prepare_proxy_to_requests(proxy):
        '''
        This function prepares all the Proxy's data members into the right order and structure for an https request
        :param proxy: Proxy
        :return:string
        '''
        return {proxy._protocol: proxy._protocol + '://' + proxy._ip + ":" + proxy._port}



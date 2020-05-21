from abc import ABCMeta, abstractmethod


class PlatformsDetector(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, proxies=None):
        pass

    @abstractmethod
    def detect(self, domain, retries=0, timeout=5, aggressive=False, urls=None, proxies=None):
        pass

    @abstractmethod
    def get_platform_name(self):
        pass

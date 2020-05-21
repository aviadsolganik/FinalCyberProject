from multiprocessing.pool import ThreadPool


class Model(object):
    def __init__(self, detectors):
        self.detectors = detectors

    def check_platform(self, domain, platform=None):
        """
        :param platform: string. the user know platform is the website, he looks for the version.
        :param domain: the domain the user want to check what platform it belongs to.
        :return: tuple. platform-name/false, version/'could not detect platform'.
        """
        try:
            optional_results = []
            if platform is None:
                pool = ThreadPool(4)
                for detector in self.detectors:
                    optional_results.append(pool.apply(detector.detect, args=(domain,)))
                pool.close()
                pool.join()
            else:
                for detector in self.detectors:
                    if detector.get_platform_name() == platform:
                        optional_results.append(detector.detect(domain))
                        break
            tuple_result = []
            for result in optional_results:
                if result[1]:
                    tuple_result.append(result)
            if len(tuple_result) > 1:
                platforms = "it might be: "
                for name in tuple_result:
                    platforms += name[0] + ", "
                return False, "could not detect platform " + platforms
            elif len(tuple_result) == 0:
                return False, "could not detect platform "
            else:
                return tuple_result[0][0], tuple_result[0][2]
        except Exception as e:
            print(e)

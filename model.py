from JOOMLADetector import JOOMLADetector
from MyDB import MyDB
from WP.wp_detector import WPDetector


class Model(object):
    def __init__(self):
        #self._platform = ['wordpress', 'joomla', 'drupal', 'squarspace']
        self._platform = ['WordPress', 'Joomla']

    def check_platform_helper(self, platform_name, domain):
        """
        :param platform_name: string. the name of the platform I want to check.
        :param domain: string. the domain which I want to check if it runs on platform.
        :return: tuple. platform-name, true/false, version(if found)
        """
        try:
            if platform_name == 'WordPress':
                return ('WordPress',) + WPDetector(domain).detect()
            if platform_name == 'Joomla':
                return ('Joomla',) + JOOMLADetector(domain).detect()
            '''if platform_name == 'drupal':
                return ('drupal',) + WPDetector(domain).detect()
            if platform_name == 'squarespace':
                return ('squarespace',) + JOOMLADetector(domain).detect()'''
        except Exception as e:
            print(e)

    def check_platform(self, domain, platform=None):
        """
        :param platform: string. the user know platform is the website, he looks for the version.
        :param domain: the domain the user want to check what platform it belongs to.
        :return: tuple. platform-name/false, version/'could not detect platform'.
        """
        try:
            optional_results = []
            if platform is None:
                for platform in self._platform:
                    optional_results.append(self.check_platform_helper(platform, domain))
            else:
                optional_results.append(self.check_platform_helper(platform, domain))
            tuple_result = []
            for result in optional_results:
                if result[1] == 'True':
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

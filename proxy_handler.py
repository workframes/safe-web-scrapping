# import
import requests
import random
from bs4 import BeautifulSoup

# main
class get_proxy(object):
    def __init__(self):
        self.__url = 'https://www.sslproxies.org/'
        self.__headers = {
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer': 'http://www.wikipedia.org/',
            'Connection': 'keep-alive',
        }
        self.rad_ip = []
        self.rad_port = []

    def __random_proxy(self):
        r = requests.get(url=self.__url, headers=self.__headers)
        soup = BeautifulSoup(r.text, 'html.parser')

        for x in soup.findAll('td')[::8]:
            self.rad_ip.append(x.get_text())

        for y in soup.findAll('td')[1::8]:
            self.rad_port.append(y.get_text())

        zfile = list(zip(self.rad_ip, self.rad_port))
        number = random.randint(0, len(zfile) - 50)
        ip_random = zfile[number]
        ip_random_string = "{}:{}".format(ip_random[0], ip_random[1])
        proxy = {'https': ip_random_string}
        return proxy

    def proxy_request(self, request_type='get', url='', own_proxy=None, **kwargs):
        """
        :param request_type: GET, POST, PUT
        :param url: URL to return HTML data from
        :param own_proxy: you can use your own proxy
        :param kwargs: extra parameters you want to pass
        :return: response
        """
        while True:
            try:
                if own_proxy == None:
                    proxy = self.__random_proxy()
                    print("current proxy {}".format(proxy))
                    r = requests.request(request_type, url, proxies=proxy, headers=self.__headers, timeout=8, **kwargs)
                    return r
                    break
                else:
                    proxy = own_proxy
                    print("current proxy {}".format(proxy))
                    r = requests.request(request_type, url, proxies=proxy, headers=self.__headers, timeout=8, **kwargs)
                    return r
                    break
            except:
                pass




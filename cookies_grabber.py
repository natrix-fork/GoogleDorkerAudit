from selenium.webdriver import Chrome, ChromeOptions
from termcolor import colored
import random
import time


class CookiesGrabber:
    def __init__(self):
        options = ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--incognito')
        self.options = options
        self.cookies = []
        self.pages = [
            'https://www.youtube.com/?gl=UA&hl=ru',
            'https://searchdns.netcraft.com/',
            'https://bootstrap-vue.js.org/',
            'https://habr.com/en/post/346344/',
            'https://learn.javascript.ru/'
        ]

    def grab_cookies(self):
        for i in range(0, 10, 1):
            driver = Chrome('/usr/bin/chromedriver', options=self.options)
            driver.get(random.choice(self.pages))
            cookies = driver.get_cookies()
            new_cookies = []
            for cookie in cookies:
                cookie = {str(k): str(v) for k, v in cookie.items()}
                new_cookies.append(cookie)
            self.cookies.append(new_cookies)
            print(colored('[!] New cookies has been created!', 'green'))
            for cook in new_cookies:
                print(colored('\t[+] {}'.format(cook), 'yellow'))
            time.sleep(random.uniform(1, 3))
            driver.quit()
        return self.cookies


# from config import Config
# from cookies_grabber import CookiesGrabber
#
# config = Config()
# cookies_grabber = CookiesGrabber()
# cookies = cookies_grabber.grab_cookies()


class User(object):
    def __init__(self, headers, cookies):
        self.headers = headers
        self.cookies = cookies
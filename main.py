import random
import sys

from config import Config
from user import User
from cookies_grabber import CookiesGrabber
from dorker import Dorker

url = sys.argv[1]

cookies_graber = CookiesGrabber()
all_cookies = cookies_graber.grab_cookies()
config = Config()
all_headers = config.headers

users = []
for i in range(0, 10, 1):
    headers = random.choice(all_headers)
    cookies = all_cookies[i]
    user = User(headers, cookies)
    users.append(user)

dorker = Dorker(url, users)
dorker.fulfill_dorks()
pass

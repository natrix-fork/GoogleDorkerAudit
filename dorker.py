from typing import List
from termcolor import colored
import requests
import time
import random
import json

from config import Config
from user import User
from parser import Parser

config = Config()


class Dorker:
    def __init__(self, url: str, users: List[User]):
        self.users = users
        self.dorks = config.dorks
        self.max_delay = config.max_delay
        self.min_delay = config.min_delay
        self.url = url
        self.result = {}

    def fulfill_dorks(self):
        for key in self.dorks:
            user = random.choice(self.users)
            cookies = dict(random.choice(user.cookies))
            response = requests.get(
                url=self.dorks[key].format(self.url),
                headers=user.headers,
                cookies=cookies,
                timeout=20
            )
            status_code = response.status_code
            while status_code != 200:
                print(colored('[!] User tries are blocking by google with status_code: {}.'.format(status_code), 'red'))
                print(colored('\t[!] Removing user from queue...', 'red'))
                print(colored(
                    '\t [-] Usernames headers: \n{}\n\t [-] Usernames cookies:\n{}'.format(user.headers, user.cookies),
                    'red'))
                self.users.remove(user)
                if not self.users:
                    print(colored('[-] Users queue is empty. Writing output to file and exiting!', 'red'))
                    with open('result.json', 'w') as f:
                        json.dump(self.result, f)
                    return
                user = random.choice(self.users)
                cookies = dict(random.choice(user.cookies))
                response = requests.get(
                    url=self.dorks[key].format(self.url),
                    headers=user.headers,
                    cookies=cookies,
                    timeout=20
                )
                status_code = response.status_code
            content = response.content
            decoded = content.decode('utf-8')
            parser = Parser(decoded)
            links = parser.find_links()
            links = [{'link': link} for link in links]
            self.result[key] = {'links': links}
            if links:
                print(colored('[!] Found {} links.'.format(key), 'green'))
                for link in links:
                    print(colored('\t[+] {}'.format(link['link'])))
            else:
                print(colored('[!] No {} links found.'.format(key), 'green'))
            time.sleep(random.uniform(self.min_delay, self.max_delay))
        with open('result.json', 'w') as f:
            json.dump(self.result, f)

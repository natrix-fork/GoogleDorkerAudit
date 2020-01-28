from bs4 import BeautifulSoup


class Parser:
    def __init__(self, html_content):
        self.html_content = html_content

    def find_links(self):
        soup = BeautifulSoup(self.html_content, 'html.parser')
        links = soup.select('div.r > a')
        links = [link['href'] for link in links]
        return links

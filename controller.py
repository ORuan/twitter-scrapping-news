from http.server import BaseHTTPRequestHandler, HTTPServer
from bs4 import BeautifulSoup
from utils import commit_errors
import urllib.request
import time
import sched

URL = "https://twitter.com/explore/tabs/trending/"


class Monitor():
    def __init__(self):
        self.url = URL

    def _get(self):
        req = urllib.request.Request(self.url)
        req.add_header(
            'User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36')
        try:
            with urllib.request.urlopen(req) as response:
                self.raw = response.read()
        except Exception as err:
            commit_errors(err, __file__)

    def process(self):
        self._get()
        try:
            data = BeautifulSoup(self.raw, 'html.parser')#.prettify() 
            print(data.find_all("div", class_=".css-1dbjc4n .r-bnwqim .r-16y2uox"))
        except Exception as err:
            commit_errors(err, __file__)

    def monitoring_daemon(self):
        s = sched.scheduler(time.time, time.sleep)
        while True:
            s.enter(3, 1, self.process)
            s.run()
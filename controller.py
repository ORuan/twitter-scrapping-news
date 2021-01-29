from http.server import BaseHTTPRequestHandler, HTTPServer  
import time, requests
from bs4 import BeautifulSoup
from utils import commit_errors
import sched, time

hostName = "localhost"
serverPort = 8080
URL = "https://twitter.com/explore/tabs/trending/"

class MyServer(BaseHTTPRequestHandler):
    print(f'[*] http://{hostName}:{serverPort}')
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

class Monitor():
    def __init__(self, url):
        self.url = url

    def _get(self):
        user_agent = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36'}
        try:
            self.raw = requests.get(self.url, headers=user_agent).text
        except Exception as err:
            commit_errors(err)
            raise err

    def process(self):
        self._get()
        content = self.raw
        try:
            data = BeautifulSoup(content, 'html.parser').prettify()
            print()
            print(data)
        except Exception as err:
            commit_errors(err)
            raise err


    def monitoring_daemon(self):
        s = sched.scheduler(time.time, time.sleep)
        while True:
            s.enter(3, 1, self.process)
            s.run()



webServer = HTTPServer((hostName, serverPort), MyServer)
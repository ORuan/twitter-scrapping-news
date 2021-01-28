#!.env/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import threading
from settings import TwitterScrappingBot

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    
   
    try:
        th_twitter = threading.Thread(daemon=True, target=TwitterScrappingBot().open)
        th_twitter.start()
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    
    th_twitter.close()
    webServer.server_close()
    print("Server stopped.")


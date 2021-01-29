#!.env/bin/python3
import threading
from controller import MyServer, webServer, Monitor
from http.server import HTTPServer
from controller import URL
from utils import commit_errors

if __name__ == "__main__":        
    monitor_server = Monitor(URL)
    monitor_server.process()
    
    th_monitor = threading.Thread(target=monitor_server.monitoring_daemon, daemon=True)
    th_monitor.start()

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        commit_errors(KeyboardInterrupt)
        pass
    webServer.server_close()
    print("Server stopped.")

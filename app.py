import time
from http.server import HTTPServer, BaseHTTPRequestHandler
import currencyRequest

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # get the page
        path = self.path
        if path == '/':
            currencyRequest.sendRequest()
            with open('index.html', 'rb') as page:
                self.wfile.write(page.read())


try:
    server = HTTPServer(('localhost', 8080), Server)
    server.serve_forever()
except:
    pass

server.server_close()

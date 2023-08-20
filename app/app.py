import http.server
import os
import socket
import json

HOSTNAME = socket.gethostname()
AUTHOR = os.environ.get('AUTHOR', 'NoneName Author')
UUID = os.environ.get('UUID')
APP_ENV = os.environ.get('APP_ENV', 'development')

class MyRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/hostname':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {'hostname': HOSTNAME}
            self.wfile.write(json.dumps(response).encode())

        elif self.path == '/author':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {'author': AUTHOR}
            self.wfile.write(json.dumps(response).encode())

        elif self.path == '/id':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {'id': UUID}
            self.wfile.write(json.dumps(response).encode())

        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {'error': 'Not Found'}
            self.wfile.write(json.dumps(response).encode())

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, MyRequestHandler)
    print(f"Starting server in {APP_ENV} mode...", flush=True)
    httpd.serve_forever()

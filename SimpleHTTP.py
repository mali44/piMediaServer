#!/usr/bin/env python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urlparse import parse_qs

import StatusFunctions
import json
import time


class MainHandler(BaseHTTPRequestHandler):

    def _set_headers(self, content_type="text/html"):
        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        self._set_headers("application/json")

        if self.path == "/systemStatus":
            print (StatusFunctions.StatusFunc())
            self.wfile.write((StatusFunctions.StatusFunc()))

    def do_POST(self):
        self._set_headers()

        if self.path == '/downloadFile':
            post_parameters = parse_qs(self.rfile.read(int(self.headers['Content-Length'])))
            self.wfile.write(json.dumps(post_parameters))


def run(server_class=HTTPServer, handler_class=MainHandler, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print '[%s] Listener Started' % time.strftime("%H:%M:%S")
    httpd.serve_forever()


if __name__ == "__main__":
    run(HTTPServer, MainHandler, 1025)

#!/usr/bin/python3
"""
Create a simple web server
"""

import http.server
import json


class my_server(http.server.BaseHTTPRequestHandler):
    """
    create a simple web server with http.server
    """

    def do_GET(self):
        """
        get user commands and returns accurate data
        """
        if self.path == "/data":
            self.send_response(200)
            john_data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(john_data)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_data.encode("utf-8"))
        elif self.path == "/info":
            self.send_response(200)
            info = {"version": "1.0",
                    "description": "A simple API built with http.server"}
            json_info = json.dumps(info)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_info.encode("utf-8"))
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        elif self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


server = http.server.HTTPServer(('localhost', 8000), my_server)
print("serveur en cours")
server.serve_forever()

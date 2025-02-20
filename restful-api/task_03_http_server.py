import http.server
import json


class SimpleAPI(http.server.BaseHTTPRequestHandler):
    """
    Class to manage HTTP requests.

    It defines methods to manage GET requests.
    """
    def do_GET(self):
        """
        Treat GET requests.
        Send to correct answer to the correct request.
        """
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data_info = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data_info).encode('utf-8'))
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data_info = {"status": "OK"}
            self.wfile.write(b"OK")
        elif self.path == '/info':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data_info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(data_info).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run_server(server_class=http.server.HTTPServer,
        handler_class=SimpleAPI, port=8000):
    """
    Run the HTTP server

    Args:
        port: default port: 8000
    """
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()

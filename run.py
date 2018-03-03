from os import curdir, sep
import BaseHTTPServer

HOST_NAME = ''
PORT_NUMBER = 8000

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        """Respond to a GET request."""
        if self.path == '/':
            code = 200
            body = 'Hello World!'
            body += '\n\nYou accessed path: ' + self.path
        else:
            try:
                with open(curdir + sep + 'files' + sep + self.path) as f:
                    body = f.read()
                code = 200
            except IOError:
                body = 'Sorry, page not found.'
                code = 404

        self.send_response(code)
        # Need to dynamically determine content type to send
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(body)

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

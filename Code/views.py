from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class Views:
    @staticmethod
    def home(handler, query_params):
        file_path = "index.html"
        with open(file_path, 'r') as f:
            html = f.read()
            
        print("test")
        handler.send_response(200)
        handler.send_header('Content-type', 'text/html')
        handler.end_headers()
        handler.wfile.write(bytes(html, "utf8"))

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        query_string = parsed_url.query
        query_params = parse_qs(query_string)
        if path == "/":
            Views.home(self, query_params)
        


    def do_POST(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print(parsed_url)
        parsed_data = parse_qs(post_data.decode('utf-8'))
        if path == "/login_form":
            print(parsed_data)
            print(parsed_data.get("username")[0])
          
        



def run(server_class=HTTPServer, handler_class=MyHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(F"Server running on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
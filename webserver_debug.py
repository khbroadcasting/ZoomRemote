from http.server import SimpleHTTPRequestHandler
import socketserver, os
from pyautogui import hotkey

PORT = 80

class MyRequestHandler(SimpleHTTPRequestHandler):

    def do_POST(self):
        print(self.headers)
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        print(post_data)

        keys = [key.split('=')[1] for key in post_data.split('&')]
        print(keys)
        if "index.html" in self.headers.get('Referer'):
            print(f"Sending keys: {'+'.join(str(k) for k in keys)}...", end=' ')
            hotkey(*keys)
            print("Done!")
        self.do_GET()

def main():
    print(f"Starting HTTP server on port {PORT}...", end=' ')
    with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
        print("Done!")
        print(os.popen('ipconfig').read())
        httpd.serve_forever()

if __name__ == '__main__':
    main()

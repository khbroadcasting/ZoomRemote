from http.server import SimpleHTTPRequestHandler
import socketserver, os
from pyautogui import hotkey

PORT = 80

class MyRequestHandler(SimpleHTTPRequestHandler):

    def do_POST(self):
        if "toggle_hand.html" in self.headers.get('Referer'):
            print("Toggling Hand...", end=' ')
            hotkey('alt', 'y')
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

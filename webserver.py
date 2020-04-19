from http.server import SimpleHTTPRequestHandler
import socketserver, socket, os
from pyautogui import hotkey

PORT = 80

def ip_address_helper():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        print(f"Type '{host_ip}' into your web browser (e.g. Chrome) exactly as you see here to access the remote.")
    except:
        print("Unable to get Hostname and IP")

class MyRequestHandler(SimpleHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')

        keys = [key.split('=')[1] for key in post_data.split('&')]

        if self.path == '/index.html':
            print(f"Sending keys: {'+'.join(str(k) for k in keys)}...", end=' ')
            hotkey(*keys)
            print("Done!")

        self.do_GET()

    def do_GET(self):
        if self.path == '/':
            self.send_index()
        elif self.path == '/index.html':
            f = self.send_index()
        else:
            super().do_GET()

    def send_index(self):
        if os.path.exists('index.html'):
            super().do_GET()
        else:
            self.encoded_html = index_html.encode('utf-8')
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.send_header("Content-Length", len(self.encoded_html))
            self.end_headers()
            self.wfile.write(self.encoded_html)


def main():
    print(f"Starting HTTP server on port {PORT}...", end=' ')
    with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
        print("Done!")
        #print(os.popen('ipconfig').read())
        ip_address_helper()
        httpd.serve_forever()

index_html = """
<html>
<head>
<meta charset="UTF-8">
<title>ZoomRemote</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
body { padding: 1rem; }

.button {
  background-color: dodgerblue;
  color: white;
  padding: 1rem;
  height: 10rem;
  font-size:2.5rem;
  white-space:normal;
  border-radius:1rem;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-gap: 1rem;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
}
</style>
</head>
<body>
<div class="container">
<form action="/index.html" method="post">
<input type="hidden" id="toggle_hand_key_1" name="toggle_hand_key_1" value="alt">
<input type="hidden" id="toggle_hand_key_2" name="toggle_hand_key_2" value="y">
<input type="submit" value="&#x270B TOGGLE HAND" class="button">
</form>
<form action="/index.html" method="post">
<input type="hidden" id="toggle_video_key_1" name="toggle_video_key_1" value="alt">
<input type="hidden" id="toggle_video_key_2" name="toggle_video_key_2" value="v">
<input type="submit" value="&#x1F3A5 TOGGLE VIDEO" class="button">
</form>
<form action="/index.html" method="post">
<input type="hidden" id="toggle_mute_key_1" name="toggle_mute_key_1" value="alt">
<input type="hidden" id="toggle_mute_key_2" name="toggle_mute_key_2" value="a">
<input type="submit" value="&#x1F3A4 TOGGLE MUTE" class="button">
</form>
<form action="/index.html" method="post">
<input type="hidden" id="toggle_mute_all_key_1" name="toggle_mute_all_key_1" value="alt">
<input type="hidden" id="toggle_mute_all_key_2" name="toggle_mute_all_key_2" value="m">
<input type="submit" value="&#x1F92B MUTE ALL" class="button">
</form>
<form action="/index.html" method="post">
<input type="hidden" id="toggle_screen_share_key_1" name="toggle_screen_share_key_1" value="alt">
<input type="hidden" id="toggle_screen_share_key_2" name="toggle_screen_share_key_2" value="s">
<input type="submit" value="&#x1F4BB TOGGLE SCREEN SHARE" class="button">
</form>
<form action="/index.html" method="post">
<input type="hidden" id="exit_meeting_key_1" name="exit_meeting_key_1" value="alt">
<input type="hidden" id="exit_meeting_key_2" name="exit_meeting_key_2" value="q">
<input type="submit" value="&#x1F6D1 EXIT MEETING" class="button">
</form>
</div>
</body>
</html>
"""

if __name__ == '__main__':
    main()

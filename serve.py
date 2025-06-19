# save this as serve.py
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

class COOPHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        super().end_headers()

PORT = 8080
ThreadingHTTPServer(('', PORT), COOPHandler).serve_forever()


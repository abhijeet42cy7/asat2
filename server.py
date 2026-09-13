"""
ASAT-2: Lightweight Local Web Server & API Gateway
Allows running ASAT-2 locally via `python server.py`
"""

import http.server
import socketserver
import json
import os
import sys
from gis_engine import EucalyptusSpectralClassifier, STACSatelliteClient

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

classifier = EucalyptusSpectralClassifier()
stac_client = STACSatelliteClient()

class ASATRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_POST(self):
        # API Endpoint: /api/classify
        if self.path == '/api/classify':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                body = json.loads(post_data.decode('utf-8'))
                bands = body.get('bands', {})
                result = classifier.classify_pixel(bands)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(result).encode('utf-8'))
            except Exception as e:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))
            return

        # API Endpoint: /api/stac/search
        if self.path == '/api/stac/search':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                body = json.loads(post_data.decode('utf-8'))
                bbox = body.get('bbox', [-8.0, 40.5, -7.8, 40.7])
                scenes = stac_client.search_scenes(bbox=bbox)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"scenes": scenes}).encode('utf-8'))
            except Exception as e:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))
            return

        super().do_POST()

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), ASATRequestHandler) as httpd:
        print(f"🌍 ASAT-2 GIS Server running at http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")
            httpd.server_close()

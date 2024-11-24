import http.server
import ssl

# Server address and port
server_address = ('localhost', 4443)

# Request handler
httpd = http.server.HTTPServer(
    server_address, http.server.SimpleHTTPRequestHandler)

# SSL setup
httpd.socket = ssl.wrap_socket(
    httpd.socket,
    keyfile="/Users/parijatpurohit/dummy_certificate/private.key",
    certfile="/Users/parijatpurohit/dummy_certificate/dummy_certificate.crt",
    server_side=True
)

print("Serving on https://localhost:4443")
httpd.serve_forever()

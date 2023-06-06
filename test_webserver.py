import http.server
import pathlib
import functools


class WebServer(http.server.HTTPServer):
    def __init__(self):
        address = "localhost"
        port = 8000
        directory = pathlib.Path(__file__).parent
        print(directory)
        handler = functools.partial(
            http.server.SimpleHTTPRequestHandler, directory=str(directory)
        )

        super().__init__((address, port), handler)


if __name__ == "__main__":
    httpd = WebServer()
    httpd.serve_forever()

import tornado.ioloop
import tornado.web
import sys
import os


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(f"Server process: {os.getpid()}")


def init_app(port):
    app = tornado.web.Application([(r"/", MainHandler)])
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    port = 8080
    if sys.argv.__len__() > 1:
        port = sys.argv[1]

    init_app(port)

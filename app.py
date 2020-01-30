#-*- coding:utf-8 -*-

import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options
import handlers,os

urls = [
    (r"/", handlers.IndexHandler),
    (r"/insim", handlers.Insim),
    (r"/bachelor", handlers.DevWeb),
    (r"/login", handlers.Login),
    (r"/verification", handlers.Verif),
    (r"/(.*)", tornado.web.StaticFileHandler, {"path":r"{0}".format(os.path.join(os.path.dirname(__file__),"static"))}),
]

settings = dict({
    "template_path": os.path.join(os.path.dirname(__file__),"templates"),
    "static_path": os.path.join(os.path.dirname(__file__),"static"),
    "cookie_secret": os.urandom(12),
    "xsrf_cookies": True,
    "debug": True,
    "compress_response": True,
    "login_url": "/admination",
    "ui_modules":
    {'Detail': handlers.DetailModule,
    }

})

application = tornado.web.Application(urls,**settings)


if __name__ == "__main__":
    options.parse_command_line()
    server = tornado.httpserver.HTTPServer(application)
    server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()

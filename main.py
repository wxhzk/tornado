#!/usr/bin/env python
#-*- coding:utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.autoreload

import textwrap
import os.path

import poemhandler
import bookshandler
import replacehandler
from hello import *


from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

handler_list = [
	(r'/', IndexnHandler),                   #poem的首页
	(r'/reverse/(\w+)', ReverseHandler),     #字符串逆转
	(r'/wrap', WrapHandler),                 #参数的获取处理
	(r'/poem', poemhandler.PoemPageHandler), #模板变量
	(r'/books', bookshandler.BooksHandler),  #模板的控制结构
	(r'/replace', replacehandler.ReplaceHandler), #模板里包含Python函数
	(r'/source', replacehandler.IndexHandler),    #replacehandler的首页
]

settings = dict(
	template_path = os.path.join(os.path.dirname(__file__), 'templates'),
	static_path = os.path.join(os.path.dirname(__file__), "static"),
	#debug = False,
	debug = True,
)


def main():
	'''主函数'''
	tornado.options.parse_command_line()
	app = tornado.web.Application(handlers=handler_list, **settings)
	srv = tornado.httpserver.HTTPServer(app)
	srv.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
	
if __name__=="__main__":
	main()

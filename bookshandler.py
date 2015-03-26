#!/usr/bin/env python
#-*- coding:utf-8 -*-

import tornado.web

class BooksHandler(tornado.web.RequestHandler):
	def get(self):
		self.render(
			'books.html', 
			title="Books desc", 
			header="Books that are great", 
			books=["The C programing", "Python Tornado Web", "The Shell Programing"]
		)
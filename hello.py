#!/usr/bin/env python
#-*- coding:utf-8 -*-

import tornado.web

import textwrap

class IndexnHandler(tornado.web.RequestHandler):

	def get(self):
		#greeting = self.get_argument('greeting', 'Hello')
		#self.write(greeting + ', friendly user!')
		self.render('index.html')
		
	def write_error(self, status_code, **kwargs):
		'''error'''
		self.write("oh oh! error happened, error code: %d"%status_code)
		
class ReverseHandler(tornado.web.RequestHandler):

	def get(self, input):
		'''get method handler'''
		self.write(input[::-1])
		
	def write_error(self, status_code, **kwargs):
		'''error'''
		self.write("oh oh! error happened, error code: %d"%status_code)
		
class WrapHandler(tornado.web.RequestHandler):

	def post(self):
		text = self.get_argument('text')
		width = self.get_argument('width',20);
		self.write(textwrap.fill(text, width))
		
	def write_error(self, status_code, **kwargs):
		'''error'''
		self.write("oh oh! error happened, error code: %d"%status_code)
		

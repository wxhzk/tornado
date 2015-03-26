#!/usr/bin/env python
#-*- coding:utf-8 -*-

import tornado.web


class PoemPageHandler(tornado.web.RequestHandler):
	'''handle with something about poem html file'''
	def post(self):
		''''''
		noun1 = self.get_argument('noun1')
		noun2 = self.get_argument('noun2')
		verb = self.get_argument('verb')
		noun3 = self.get_argument('noun3')
		self.render('poem.html',roads=noun1, wood=noun2, made=verb, difference=noun3)
		
		
		
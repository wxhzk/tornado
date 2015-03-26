#!/usr/bin/env python
#-*- coding:utf-8 -*-

import random
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('source.html');

class ReplaceHandler(tornado.web.RequestHandler):
	'''replace the string'''
	def get_source_letter(self, text):
		'''make replace letter map'''
		letter_map = dict()
		for line in text.split('\r\n'):
			for letter in line.split(' '):
				if letter and len(letter) > 0:
					if letter[0] not in letter_map:
						letter_map[letter[0]] = []
					letter_map[letter[0]].append(letter)
		return letter_map
		
	def post(self):
		'''handle html post'''
		source_text = self.get_argument('SourceText')
		replace_text = self.get_argument('ReplaceText')
		letter_map = self.get_source_letter(source_text)
		change_lines = replace_text.split("\r\n")
		self.render(
			'replace.html',
			source_map = letter_map,
			change_lines = change_lines,
			choice = random.choice
		)
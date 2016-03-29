# author: Xiaochuan Wang
# email: deanwang@umich.edu
# Personal Portfolio
# March 17th, 2016

import webapp2
import os
import logging
import jinja2
import webapp2

# set it up so we know where we stored the template files
JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True)

class IndexHandler(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', IndexHandler),
	('/index', IndexHandler),
], debug=True)

# exception handler, redirect


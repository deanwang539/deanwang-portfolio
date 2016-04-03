# author: Xiaochuan Wang
# email: deanwang@umich.edu
# Personal Portfolio
# March 17th, 2016

import webapp2
import os
import logging
import jinja2
import webapp2
from google.appengine.api import mail

# set it up so we know where we stored the template files
JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True)

class IndexHandler(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render())

class AaacfHandler(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('templates/aaacf.html')
        self.response.write(template.render())

class AoreHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/aore.html')
        self.response.write(template.render())

class ECHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/ecommunity.html')
        self.response.write(template.render())

class UCHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/umclinical.html')
        self.response.write(template.render())

class CandcHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/candc.html')
        self.response.write(template.render())

class DbHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/dobbinIII.html')
        self.response.write(template.render())

class MailHandler(webapp2.RequestHandler):
    def post(self):
        name = self.request.get("yourName")
        email = self.request.get("yourEmail")
        phone = self.request.get("yourPhone")
        # logging.info("1"+name)
        msg = self.request.get("yourMsg")
        mail.send_mail(sender="deanwang@umich.edu",
              to="deanwong1993@gmail.com",
              subject="From Portfolio",
              body=name+", "+email+", "+phone+", "+msg)
        # template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        # self.response.write(template.render())
        self.redirect('/index')

app = webapp2.WSGIApplication([
    ('/', IndexHandler),
	('/index', IndexHandler),
	('/aaacf', AaacfHandler),
    ('/aore', AoreHandler),
    ('/ecommunity', ECHandler),
    ('/umclinical', UCHandler),
    ('/candc', CandcHandler),
    ('/dobbinIII', DbHandler),
    ('/sendMail', MailHandler)
], debug=True)

# exception handler, redirect


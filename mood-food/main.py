#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2

env = jinja2.Environment(loader=jinja2.FileSystemLoader('template'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('''
        <!DOCTYPE html>
        <head> <link rel="stylesheet" href="stylesheet.css"> </head>
        <title> Mood Food </title>
        <body bgcolor="red">

        <center>

        <h1>
        Mood Food
        </h1>

        </center>
        '''
        )
class MainHandler(webapp2.RequestHandler):
    def get(self):
        Quizine
quizine_template = env.get_template('Quizine.html')
data = {'Quizine': Quizine}
self.respone.write(friend_template.render(data))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/Quizine', QuizineHandler)
], debug=True)

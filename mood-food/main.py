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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('''
        <!DOCTYPE html>
        <head><link rel="stylesheet" href="stylesheet.css">
        </head>
        <title>
            Mood Food
        </title>
        <body bgcolor="red">
        <center>
        <h1>
            Mood Food
        </h1>
        <h2><link rel="sign up" href="">
            sign up
        </h2>
        <h2>
            sign in
        </h2>
        </center>
        '''
        )
class QuizineHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('''
        <!DOCTYPE html>
        <head><link rel="stylesheet" href="stylesheet.css">
        </head>
        <title>Quizine</title>
        <body bgcolor="red">

        <center>
        <h1>
        Quizine
        </h1>

        <div class="quiz">

        <h2 class="Quizine">: What is your mood?</h2>
        <ul data-quiz-question="Quizine">
            <li class="quiz-answer" data-quiz-answer="a">a. Happy</li>
            <li class="quiz-answer" data-quiz-answer="b">b. Angry</li>
            <li class="quiz-answer" data-quiz-answer="c">c. Sad</li>
            <li class="quiz-answer" data-quiz-answer="d">d. Tired</li>
        </ul>
        </div>
        <div class="quiz-result"></div>
        </center>
        ''')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/Quizine', QuizineHandler)
], debug=True)

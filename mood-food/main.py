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
        <body bgcolor = "#fcbfac">
        <center>
        <img src="resources/moodfood.jpg" alt="logo">
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
class AngryHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('''
        <!DOCTYPE html>
        <head>
        <title>Happy</title>
        </head>

        <body bgcolor = Teal>
        <h1>Angry</h1>
        <ul>
            <ls>Barley <ul> Description </ul> </ls>
            <ls>Celery <ul> Description </ul> </ls>
            <ls>Purple Cabbage <ul> Description </ul> </ls>
            <ls>Apples and Peanut Butter <ul> Boots energy which can help to improve mood </ul> </ls>
            <ls>Walnuts <ul> Rich in Omgea-1 fatty acids which have been proven to make you happier </ul> </ls>
            <ls>Bananas <ul> Rich in potassium and vitamin B. Slows down heart rate and helps to control blood pressure </ul> </ls>
            <ls>Grilled Cheese on Whole Wheat Bread <ul> A mixture of carbs and calcium help to improve mood </ul> </ls>
            <ls>Peanuts and Popcorn <ul> Description </ul> </ls>
            <ls>Mac and Cheese <ul> Pasta is a carbohydrate which releases serotonin which causes a feeling of comfort, thus helping to reduce anger levels </ul> </ls>
            <ls>Chocolate <ul> Releases endorphins which boosts moods </ul> </ls>
            <ls>Strawberries <ul> Rich in vitamin C which helps to release endorphins </ul> </ls>
            <ls>Hot Peppers <ul> The body's natural reaction to pain is to release endorphins, so when eating spicy foods, it releases endorphins to subside the pain </ul> </ls>
            <ls>Salsa <ul> Description </ul> </ls>
            <ls>Wasabi <ul> Description </ul> </ls>
            <ls>Ice Cream <ul> It is high in sugar and fats which would release dopamine which causes pleasure </ul> </ls>
            <ls>Baked Potato <ul> Rich in vitamin B which reduces stress levels and reduces blood pressure </ul> </ls>
            </html>
        ''')


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/Quizine', QuizineHandler),
], debug=True)

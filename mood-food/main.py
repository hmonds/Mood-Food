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
        <a href="/Angry"><img id="angry-face" src="resources/angry.png" alt= "logo"></a>
        <a href="/Tired"><img src="resources/Sleeping_Emoji.png" alt="Sleepy"></a>
        <a href="/Sad"><img src="resources/Sad_Face_Emoji.png" alt="Sad"></a>
        <a href="/Happy"><img src="resources/Happy_Emoji_Icon.png" alt="Happy"></a>
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
        <title>Angry</title>
        </head>

        <body bgcolor = Teal>
        <h1>Angry</h1>
        <ul>
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
            </body>
            </html>
        ''')

class HappyHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('''
        <!DOCTYPE html>
        <head>
        <title>Happy</title>
        </head>

        <body bgcolor = Teal>
        <h1>Happy</h1>
        <ul>
            <ls> Black Bean Brownies <ul> Rich in iron, fiber, copper, zinc, and potassium  </ul> </ls>
            <ls> Apricots <ul> Rich in vitamin B6 and antioxidants which are linked to happier moods </ul> </ls>
            <ls> Halibut <ul> Boost weight-loss and increases serotonin levels </ul> </ls>
            <ls> Seaweed <ul> Rich in iodine which fights depression </ul> </ls>
            <ls> Blueberry Juice <ul> Rich in vitamin C which can fight fatigue and depression </ul> </ls>
            <ls> Chamomile Tea <ul> Helps to readjust the circadian rhythm so that you can get a good night sleep </ul> </ls>
            </html>
        ''')

class TiredHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('''
        <!DOCTYPE html>
        <head>
        <title>Tired</title>
        </head>

        <body bgcolor = Teal>
        <h1>Tired</h1>
        <ul>
            <ls> Salmon <ul> This fish's hefty dose of protein speeds metabolism, which increases energy.</ul> </ls>
            <ls> Oatmeal <ul> High in fiber and protein and stabilizes blood sugar all day with diabetes, fiber can slow the absorption of sugar and help improve blood sugar levels, lowers the risk of developing type 2 diabetes. </ul> </ls>
            <ls> Quinoa <ul> Protein and amino acids in this gluten free grain aid in muscle repair and post workout recovery. </ul> </ls>
            <ls> Blueberries <ul> Potent antixodants combat free radicals like cancer that can injure cells and lead to fatigue. Boost the brain by relieving stress, neurotoxicity, and degeneration. in iodine which fights depression. </ul> </ls>
        </html>
    ''')

class SadHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('''
        <!DOCTYPE html>
        <head>
        <title>Sad</title>
        </head>

        <body bgcolor = Teal>
        <h1>Sad</h1>
        <ul>
            <ls> Cold-Water Fish <ul> Fish is also a great source of lean protein, which stabilizes blood sugar. Eating small amounts of protein with meals can help keep your mood on a more even keel.</ul> </ls>
            <ls> Ancient Grains <ul> Complex carbohydrates take longer to digest, which means they don't cause spikes in blood sugar that can create roller-coaster moods. Complex carbs also increase levels of serotonin in the brain.</ul> </ls>
            <ls> Nuts and seeds <ul> Magnesium, a mineral found naturally in nuts and seeds, influences production of serotonin, a "feel-good" brain chemical. Magnesium also affects overall energy production.</ul> </ls>
            <ls> Baked potato <ul> Potatos are rich in Vitamin B complex, reduce stress and lower blood pressure. </ul> </ls>
            <ls> Apple and Peanut Butter <ul> A great combo of carbs and protein: satisfying, energy-boosting and nourishing for the brain. The perfect comfort food!</ul> </ls>
            </body>
            </html>
        ''')



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/Quizine', QuizineHandler),
    ('/Angry', AngryHandler),
    ('/Happy', HappyHandler),
    ('/Sad', SadHandler),
    ('/Tired', TiredHandler)
], debug=True)

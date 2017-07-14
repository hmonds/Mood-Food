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
class SignUpHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('''
        <!DOCTYPE html>
        <title>Mood Food</title>
        <form action="/action_page.php">
          <div class="container">
            <label><b>Email</b></label>
            <input type="text" placeholder="Enter Email" name="email" required>

            <label><b>Password</b></label>
            <input type="password" placeholder="Enter Password" name="psw" required>

            <label><b>Repeat Password</b></label>
            <input type="password" placeholder="Repeat Password" name="psw-repeat" required>
            <input type="checkbox" checked="checked"> Remember me
            <p>By creating an account you agree to our <a href="#">Terms & Privacy</a>.</p>

            <div class="clearfix">
              <button type="button"  class="cancelbtn">Cancel</button>
              <button type="submit" class="signupbtn">Sign Up</button>
            </div>
          </div>
        </form>
        ''')
class SignInHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('''
<!DOCTYPE html>
<head>
<title>Mood Food</title>
<link rel="stylesheet" href="stylesheet.css"
<body bgcolor="##ff4d4d">
<form action="/action_page.php">

  <div class="imgcontainer">
    <img src="img_avatar2.png" alt="Avatar" class="avatar">
  </div>

  <div class="container">
    <label><b>Username</b></label>
    <input type="text" placeholder="Enter Username" name="uname" required>

    <label><b>Password</b></label>
    <input type="password" placeholder="Enter Password" name="psw" required>

    <button type="submit">Login</button>
    <input type="checkbox" checked="checked"> Remember me
  </div>

  <div class="container" style="background-color:#f1f1f1">
    <button type="button" class="cancelbtn">Cancel</button>
    <span class="psw">Forgot <a href="#">password?</a></span>
  </div>
</form>
</body>
</html>
        ''')
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/Quizine', QuizineHandler)
    ('/SignUp', SignUpHandler)
], debug=True)

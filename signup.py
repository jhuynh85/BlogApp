import webapp2
import re
from escape import *

page = """
<!DOCTYPE html>

<html>
  <head>
    <title>Sign Up</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>

  </head>

  <body>
    <h2>Signup</h2>
    <form method="post">
      <table>
        <tr>
          <td class="label">
            Username
          </td>
          <td>
            <input type="text" name="username" value="%(username)s">
          </td>
          <td class="error">
            %(userErr)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Password
          </td>
          <td>
            <input type="password" name="password" value="">
          </td>
          <td class="error">
            %(pwErr)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Verify Password
          </td>
          <td>
            <input type="password" name="verify" value="">
          </td>
          <td class="error">
            %(verifyErr)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Email (optional)
          </td>
          <td>
            <input type="text" name="email" value="%(email)s">
          </td>
          <td class="error">
            %(emailErr)s
          </td>
        </tr>
      </table>

      <input type="submit">
    </form>
  </body>

</html>
"""

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return USER_RE.match(username)

PW_RE = re.compile("^.{3,20}$")
def valid_password(password):
    return PW_RE.match(password)

EMAIL_RE = re.compile("^[\S]+@[\S]+\.[\S]+$")
def valid_email(email):
    return EMAIL_RE.match(email)

class SignupHandler(webapp2.RequestHandler):
    def write_form(self, userErr="", pwErr="", verifyErr="", emailErr="", username="", password="", verify="", email=""):
        self.response.out.write(page % {"userErr": userErr,
                                        "pwErr": pwErr,
                                        "verifyErr": verifyErr,
                                        "emailErr": emailErr,
                                        "username": escape_html(username),
                                        "email": escape_html(email)})
        
    def get(self):
        self.write_form()
    
    def post(self):
        userErr=""
        pwErr=""
        verifyErr=""
        emailErr=""
    
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')
        
        usernameValid = valid_username(username)
        pwValid = valid_password(password)
        verifyValid = password==verify
        emailValid = valid_email(email) or email==""
        
        if not usernameValid:
            userErr = "That's not a valid username."
        if not pwValid:
            pwErr = "That wasn't a valid password."
        if not verifyValid:
            verifyErr = "Your passwords didn't match."
        if not emailValid:
            emailErr = "That's not a valid email."
        
        if not (usernameValid and pwValid and verifyValid and emailValid):
            self.write_form(userErr, pwErr, verifyErr, emailErr, username, "", "",email)
        else:
            self.redirect("/unit2/welcome?username=%s" % username)

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Welcome, %s!" % escape_html(self.request.get('username')))
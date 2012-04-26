import webapp2
from escape import *

alphabet = 'abcdefghijklmnopqrstuvwxyz'

# H -> U
# 7 -> 20

#  o -> b
# 14 -> 1

def rot13(str):
    s = ''
    for c in str:
        d = c
        index = alphabet.find(c.lower())
        if index != -1:
            index = (index + 13) % 26
            d = alphabet[index]
            if (c.isupper()):
                d = d.upper()
        s += d
    return s

page="""
<html>
    <head>
        <title>Unit 2 Rot 13</title>
    </head>

    <body>
        <h2>Enter some text to ROT13:</h2>
        <form method="post">
            <textarea name="text" style="height: 100px; width: 400px;">%s</textarea>
            <br>
            <input type="submit">
        </form>
    </body>
</html>
"""


class ROT13Handler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(page % "")

    def post(self):
        t = self.request.get('text')
        t = escape_html(rot13(t))
        self.response.out.write(page % t)

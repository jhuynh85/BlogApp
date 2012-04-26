# import webapp2

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

form="""
<form method="post">
    What is your birthday?
    <br>
    
    <label> Month
        <input type="text" name="month" value="%(month)s">
    </label>
    
    <label> Day
        <input type="text" name="day" value="%(day)s">
    </label>
    
    <label> Year
        <input type="text" name="year" value="%(year)s">
    </label>
    <div style="color: red">%(error)s</div>
    <br>
    <br>
    <input type="submit">
</form>
"""

"""
class ROT13Handler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(form)

    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')
        
        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)
        
        if not (month and day and year):
            self.write_form("That doesn't look valid to me, friend.",
            user_month, user_day, user_year)
        else:
            self.redirect("/thanks")
"""

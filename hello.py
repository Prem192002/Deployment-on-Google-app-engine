import webapp2

def hello(request):
    return webapp2.Response("Hello, world!, welcome to VIT")

app = webapp2.WSGIApplication([
    ('/', hello)
], debug=True)

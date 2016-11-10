#!/usr/bin/env python
import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")

    def post(self):
        my_message = "input 'nd result:    "
        num1 = self.request.get("num1")
        space = "____"
        num2 = self.request.get("num2")
        operator = self.request.get("operator")

        for x in operator:
            if operator == "+":
                result = float(num1) + float(num2)
            elif operator == "-":
                result = float(num1) - float(num2)
            elif operator == "/":
                result = float(num1) / float(num2)
            else:
                result = float(num1) * float(num2)
                print result

        join_strings = my_message + num1 + space + num2 + space + str(result)
        return self.write(join_strings)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)

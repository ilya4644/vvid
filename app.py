# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
#
# if __name__ == '__main__':
#     app.run()
import jinja2
env = jinja2.Environment()
template = env.from_string("Hello, {{ name }}!")
template.render(name="Something")
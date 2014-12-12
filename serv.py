
from bottle import route, run, template, static_file

@route('/')
def index():
    return static_file("index.html", root='.')

@route('/hexweb')
def index():
    return static_file("index.html", root='.')

@route('/data/json/<name>')
def data(name):
    return static_file(name, root='data/json')

@route('/data/bed/<name>')
def data(name):
    return static_file(name, root='data/bed')

@route('/data/<name>')
def data(name="index.json"):
    return static_file(name, root='data')

@route('/style/<file>')
def style(file="main.css"):
    return static_file(file, root='style')

@route('/js/<file>')
def lib(file):
    return static_file(file, root="js")

run(host='localhost', port=8080)

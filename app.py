from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/user/<name>')
def user(name):
    personal = f'<h1>Hello, {name}!</h1>'
    # above - the curly braces {} hold a variable; when this runs,
    # the value will replace the braces and the variable name
    instruc = '<p>Change the name in the <em>browser address bar</em> \
        and reload the page.</p>'
    return personal + instruc

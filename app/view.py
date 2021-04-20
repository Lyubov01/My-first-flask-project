from app import app
from flask import render_template

# we use the route() decorator to tell Flask what URL should trigger our function.
@app.route('/')
def index():
    name = 'Ivan'
    return render_template('index.html', n=name)

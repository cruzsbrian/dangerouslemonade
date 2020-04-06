from flask import render_template
from srv import app

@app.route('/')
def home():
    return render_template('home.html', pagetitle='Brian Cruz\'s Projects')

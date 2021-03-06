from flask import render_template

from srv import app
from srv import posts

@app.route('/')
def home():
    return render_template('home.html', allposts=posts.allposts)

@app.route('/post/<name>')
def post(name):
    markdown = posts.getpost(name)
    return render_template('post.html', post_content=markdown)

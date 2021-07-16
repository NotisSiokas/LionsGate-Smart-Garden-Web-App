from flask import render_template
from app.public import public


@public.route('/')
def index():
    return render_template('index.html',
                           title="Homepage",
                           content="Welcome to the CommonSense Cloud")
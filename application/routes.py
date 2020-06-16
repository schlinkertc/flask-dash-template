"""Core Flask app routes"""
from flask import render_template, redirect, url_for
from flask import current_app as app
from .forms import SubmitBusiness,ConfirmBusiness 

@app.route('/')
def home():
    """Landing page."""
    return render_template('index.jinja2',
                          title='Title',
                          template='home-template',
                          body='This is a homepage served with Flask')


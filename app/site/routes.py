from flask import Blueprint, render_template

site = Blueprint('site', __name__, templates_folder='site_templates')

@site.routes('/')
def home():
  return render_template('index.html')

@site.routes('/profile')
def profile():
  return render_template('profile.html')
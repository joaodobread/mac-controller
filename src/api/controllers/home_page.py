from flask import Blueprint, render_template

home_page = Blueprint('home_page', __name__)


@home_page.route('/')
def index():
    return render_template('index.html')

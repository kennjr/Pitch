from flask import render_template
from app import app
from urllib import error


# @app.errorhandler(404)



@app.errorhandler(404)
def page_not_found(error):
    return render_template('404_page.html'), 404


@app.errorhandler(error.HTTPError)
def http_error(error):
    return render_template('404_page.html'), 404

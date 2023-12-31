from flaskwebgui import FlaskUI
from application import app

FlaskUI(app=app, server="flask").run()

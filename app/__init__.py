# Import flask and template operators
from flask import Flask, render_template



# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_a.controllers import mod_a_bp 

# Register blueprint(s)
app.register_blueprint(mod_a_bp)
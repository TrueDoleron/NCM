from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from config import *

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

engine = create_engine(SQLALCHEMY_DATABASE_URI)
db_session = scoped_session(sessionmaker(bind=engine))

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_ncm.controllers import mod_ncm as ncm_module

# Register blueprint(s)
app.register_blueprint(ncm_module)
# ..

# Build the database:
Base.metadata.create_all(bind=engine)

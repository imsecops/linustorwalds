from flask import Flask

app = Flask(__name__)

app.config['SERVER_NAME']='hacktober.net'
from app import views

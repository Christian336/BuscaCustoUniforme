from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = "#Cyber336"
from app import routes
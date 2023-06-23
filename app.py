from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from helpers import login_required
from tempfile import mkdtemp

app = Flask(__name__)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

app.debug = True

db = SQL("sqlite:///gym.db")

import routes.login
import routes.index
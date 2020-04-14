from config import Config
from flask import abort, flash, g, jsonify, redirect, render_template, request, url_for
import json
from app import app

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('blog.html')


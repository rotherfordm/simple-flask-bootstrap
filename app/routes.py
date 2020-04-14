from config import Config
from flask import abort, flash, g, jsonify, redirect, render_template, request, url_for
import json
from app import app

@app.route("/", methods=["GET", "POST"])
def index():
    head_post = {'title': 'Top post body' , 'body': ' Multiple lines of text that form the lede, informing new readers quickly and efficiently about what’s most interesting in this post’s contents.' , 'date': 'Feb 12'}
    post1 = {'title': 'Featured post', 'body': 'This is a wider card with supporting text below as a natural lead-in to additional content.', 'date': 'Feb 11'}
    post2= {'title': 'Post 2', 'body': 'This is a wider card with supporting text below as a natural lead-in to additional content.', 'date': 'Feb 10'}
    topics = [
        'World',
        'U.S.',
        'Technology',
        'Design',
        'Culture',
        'Business',
        'Politics',
        'Opinion',
        'Science',
        'Health',
        'Style',
        'Travel',
    ]

    return render_template('blog.html',topics=topics, head_post=head_post, post1=post1, post2=post2)


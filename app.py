import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())


@app.route('/about/')
def about():
    return render_template('about.html')

    
@app.route('/comments/')
def comments():
    comments = ['This is the first comment.',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.'
                ]

    return render_template('comments.html', comments=comments)

    
@app.route('/comments2/')
def comments2():
    comments = ['This is the first comment.',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.'
                ]

    return render_template('comments2.html', comments=comments)

    
@app.route('/comments3/')
def comments3():
    comments = ['This is the first comment.',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.'
                ]

    return render_template('comments3.html', comments=comments)


@app.route('/list/')
def building_list():
    return render_template('list.html')


@app.route('/login/')
def login():
    return render_template('login.html')


@app.route('/reservations/')
def reservations():
    return render_template('reservations.html')


@app.route('/rooms/')
def rooms():
    return render_template('rooms.html')
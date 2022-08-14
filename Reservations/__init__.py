from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = '728169f6a1448fba21d5312b'


from Reservations import routes

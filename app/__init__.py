from flask import Flask


app = Flask(__name__)
app.config.update(
    SECRET_KEY='hashing_app'
)


from app import routes

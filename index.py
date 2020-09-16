# /index.py
from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

# define app routes
@app.route("/")
def index():
    return render_template("index.html")

# function for the bot response


@app.route("/get")
def get_bot_response():
    import chatbotFunc
    message = request.args.get('msg')
    answer = chatbotFunc.response(message)
    return answer


# run Flask app
if __name__ == "__main__":
    app.run()

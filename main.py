from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, Flask app is running on Render!"

if __name__ == "__main__":
    app.run(debug=True)

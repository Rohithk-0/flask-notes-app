from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask Notes App – Render is working! 🎉"

if __name__ == "__main__":
    app.run(debug=True)

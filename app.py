from flask import Flask, render_template
import flask

app = Flask(__name__)

@app.route('/')
def Hello_World():
    return render_template('algorism.html')

if __name__ == "__main__":
    app.run()
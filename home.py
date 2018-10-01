from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
        url = url_for('static', filename='style.css')
        return render_template('home.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

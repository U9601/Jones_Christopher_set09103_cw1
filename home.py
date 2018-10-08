from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
        return render_template('home.html')

@app.route('/lighttank')
def lighttank():
        return render_template('LightTanks.html')

@app.route('/mediumtank')
def mediumtank():
        return render_template('MediumTanks.html')

@app.route('/heavytank')
def heavytank():
    name = "Object 277"
    name = "Challenger 2"
    name = "Maus"
    name = "Tiger"
        return render_template('HeavyTanks.html')

@app.route('/tankdestroyers')
def tankdestroyers():
        return render_template('TankDestroyers.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

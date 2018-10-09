from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
        return render_template('home.html')

@app.route('/lighttank')
def lighttank():
        return render_template('LightTanks.html')

@app.route('/lighttank/T-100LT/')
def T100LT():
    name = 'T-100LT'
    return render_template('LightTanks.html', name = name)

@app.route('/lighttank/M3Stuart/')
def M3Stuart():
    name = 'M3Stuart'
    return render_template('LightTanks.html', name = name)

@app.route('/lighttank/Sheridan/')
def Sheridan():
    name = 'Sheridan'
    return render_template('LightTanks.html', name = name)

@app.route('/lighttank/PanzerII/')
def PanzerII():
    name = 'PanzerII'
    return render_template('LightTanks.html', name = name)

@app.route('/mediumtank')
def mediumtank():
        return render_template('MediumTanks.html')

@app.route('/mediumtank/Object140/')
def Object140():
    name = 'Object140'
    return render_template('MediumTanks.html', name = name)

@app.route('/mediumtank/CenturionActionX/')
def CenturionActionX():
    name = 'CenturionActionX'
    return render_template('MediumTanks.html', name = name)

@app.route('/mediumtank/T-54/')
def T54():
    name = 'T-54'
    return render_template('MediumTanks.html', name = name)

@app.route('/mediumtank/M46Pershing/')
def M46Pershing():
    name = 'M46Pershing'
    return render_template('MediumTanks.html', name = name)


@app.route('/heavytank/')
def HeavyTank():
    return render_template('HeavyTanks.html')

@app.route('/heavytank/Object277/')
def Object277():
    name = 'Object277'
    return render_template('HeavyTanks.html', name = name)

@app.route('/heavytank/Challenger2/')
def Challenger2():
    name = 'Challenger2'
    return render_template('HeavyTanks.html', name = name)

@app.route('/heavytank/Maus/')
def Maus():
    name = 'Maus'
    return render_template('HeavyTanks.html', name = name)

@app.route('/heavytank/Tiger/')
def Tiger():
    name = 'Tiger'
    return render_template('HeavyTanks.html', name = name)

@app.route('/tankdestroyers')
def tankdestroyers():
        return render_template('TankDestroyers.html')

@app.route('/tankdestroyers/JagdTiger/')
def JagdTiger():
    name = 'JagdTiger'
    return render_template('TankDestroyers.html', name = name)

@app.route('/tankdestroyers/StrvS1/')
def StrvS1():
    name = 'StrvS1'
    return render_template('TankDestroyers.html', name = name)

@app.route('/tankdestroyers/ChurchillGunCarrier/')
def ConqueorGunCarrier():
    name = 'ChurchillGunCarrier'
    return render_template('TankDestroyers.html', name = name)

@app.route('/tankdestroyers/Hellcat/')
def Hellcat():
    name = 'Hellcat'
    return render_template('TankDestroyers.html', name = name)





if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

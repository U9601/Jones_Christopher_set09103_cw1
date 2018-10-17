from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)

@app.route('/')
def home():
        return render_template('home.html')

@app.route('/lighttank')
def lighttank():
    name = ''
    return render_template('LightTanks.html', name = name)

@app.route('/lighttanks')
def lightanks():
        return redirect( url_for ('lighttank') )

@app.route('/LightTank')
def LightTank():
        return redirect( url_for ('lighttank') )

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
    name = ''
    return render_template('MediumTanks.html', name = name)

@app.route('/MediumTank')
def MediumTank():
        return redirect( url_for ('mediumtank') )

@app.route('/mediumtanks')
def mediumtanks():
        return redirect( url_for ('mediumtank') )

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

@app.route('/mediumtank/M26Pershing/')
def M2Pershing():
    name = 'M26Pershing'
    return render_template('MediumTanks.html', name = name)


@app.route('/heavytank/')
def heavytank():
    name = ''
    return render_template('HeavyTanks.html', name = name)

@app.route('/HeavyTank')
def HeavyTank():
        return redirect( url_for ('heavytank') )

@app.route('/heavytanks')
def heavytanks():
        return redirect( url_for ('heavytank') )

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
    name = ''
    return render_template('TankDestroyers.html', name = name)

@app.route('/TankDestroyers')
def TankDestroyers():
        return redirect( url_for ('tankdestroyers') )

@app.route('/tankdestroyer')
def tankdestroyer():
        return redirect( url_for ('tankdestroyers') )


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

@app.route('/nations')
def nations():
    name = ''
    return render_template('Nations.html', name = name)

@app.route('/Nations')
def Nations():
    return redirect( url_for ('nations') )

@app.route('/nation')
def nation():
    return redirect( url_for ('nations') )

@app.route('/nations/German')
def German():
    name = 'German'
    return render_template('Nations.html', name = name)

@app.route('/nations/Russian')
def Russian():
    name = 'Russian'
    return render_template('Nations.html', name = name)

@app.route('/nations/British')
def British():
    name = 'British'
    return render_template('Nations.html', name = name)

@app.route('/nations/American')
def American():
    name = 'American'
    return render_template('Nations.html', name = name)

@app.route('/nations/Swedish')
def Swedish():
    name = 'Swedish'
    return render_template('Nations.html', name = name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

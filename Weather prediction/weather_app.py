import numpy as np
from flask import Flask, render_template, request, redirect
import pickle
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('Home_1.html')

@app.route('/Predict')
def prediction():
    return render_template('Index.html')
@app.route('/home')
def homee():
    return render_template('Home_1.html')

@app.route('/form', methods=["POST"])
def brain():
    precipitation=float(request.form['precipitation'])
    tempmax=float(request.form['tempmax'])
    tempmin=float(request.form['tempmin'])
    Wind=float(request.form['Wind'])
     
    values=[precipitation,tempmax,tempmin,Wind]
  
    arr = [values]
    ot = model.predict(arr)
    if(ot==0):
        r="Drizzle"
    elif(ot==1):
        r="Fog"
    elif(ot==2):
        r="Rain"
    elif(ot==3):
        r="Snow"
    elif(ot==4):
        r="Sun"
    else:
        r="No prediction"
    return render_template('prediction.html', prediction="According to given parameters the weather is likely to be:  "+r)




if __name__ == '__main__':
    app.run(debug=True)
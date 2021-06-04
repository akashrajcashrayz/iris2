from flask import Flask, request, render_template

import numpy as np
import pickle

# Create Flask object to run
app = Flask(__name__,template_folder= 'templates' )

@app.route('/')
def home():
    return render_template('indexxxx.html')

@app.route('/predict',methods=['POST'])
def predict():
  try:
    knnIrisModel = pickle.load(open('irismodelcat.pkl', 'rb'))
    int_features = [float(x) for x in request.form.values()]

    SepalLength = request.form.get('SepalLength')
    SepalWidth = request.form.get('SepalWidth')
    PetalLength = request.form.get('PetalLength')
    Irisclass = int(request.form.get('Iris class'))

    k = []
    for i in range(0,3,1):
      if i == Irisclass:
        k.append(float(1))
      if i != Irisclass:
        k.append(float(0))
    print(k)
    del k[-1]
    print(k)
    listofcontinuos = [float(SepalLength),float(SepalWidth),float(PetalLength)]
    print(listofcontinuos)
    listofcontinuos.extend(k)
    print(listofcontinuos)


    prediction = knnIrisModel.predict([listofcontinuos])
    output =prediction[0]
    return render_template('indexxxx.html', prediction_text= output)
  except:
    return render_template('indexxxx.html', prediction_text= 'invalid input')
    
    
if __name__ == "__main__":
	app.run()


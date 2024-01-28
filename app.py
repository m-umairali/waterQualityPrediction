from flask import Flask, render_template, request
import os 
import numpy as np
from waterQualityPrediction.pipeline.prediction import PredictionPipeline

app = Flask(__name__) 


@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")



@app.route('/train',methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!" 



@app.route('/predict', methods=['POST', 'GET'])  # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #for debugging
            #print(request.form)

            # reading the inputs given by the user
            ph = float(request.form['ph'])
            hardness = float(request.form['hardness'])
            solids = float(request.form['solids'])
            chloramines = float(request.form['chloramines'])
            sulfate = float(request.form['sulfate'])
            conductivity = float(request.form['conductivity'])
            organic_carbon = float(request.form['organic_carbon'])
            trihalomethanes = float(request.form['trihalomethanes'])
            turbidity = float(request.form['turbidity'])


            # print(request.form.keys())

            obj = PredictionPipeline()
            prediction = obj.predict([[ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]])

            # prediction is a binary result (0 or 1)
            result_message = "You Water Is Safe For Drink (Potable)" if prediction[0] == 1 else "Your Water Is Not Safe For Drink"

            return render_template('results.html', prediction=result_message)
        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'

    else:
        return render_template('index.html')



if __name__ == "__main__":
    
    # app.run()
	app.run(host="0.0.0.0", port = 8080)
 
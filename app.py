from flask import Flask, request, render_template
import sklearn
import pickle
import pandas as pd
import os

app = Flask(__name__)   # Initializing flask
# Loading our model:
model = pickle.load(open("RFmodel.pkl", "rb"))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict", methods = ["GET", "POST"])
def predict():
    if request.method == "POST":
        
        # Nitrogen
        nitrogen = float(request.form["nitrogen"])
        
        # Phosphorus
        phosphorus = float(request.form["phosphorus"])
        
        # Potassium
        potassium = float(request.form["potassium"])
        
        # Temperature
        temperature = float(request.form["temperature"])
        
        # Humidity Level
        humidity = float(request.form["humidity"])
        
        # PH level
        phLevel = float(request.form["ph-level"])
        
        # Rainfall
        rainfall = float(request.form["rainfall"])
        
        # Making predictions from the values:
        predictions = model.predict([[nitrogen, phosphorus, potassium, temperature, humidity, phLevel, rainfall]])
        
        output = predictions[0]
        finalOutput = output.capitalize()
        
        if (output == "rice" or output == "blackgram" or output == "pomegranate" or output == "papaya"
            or output == "cotton" or output == "orange" or output == "coffee" or output == "chickpea"
            or output == "mothbeans" or output == "pigeonpeas" or output == "jute" or output == "mungbeans"
            or output == "lentil" or output == "maize" or output == "apple"):
            cropStatement = finalOutput + " should be harvested. It's a Kharif crop, so it must be sown at the beginning of the rainy season e.g between April and May."
                            

        elif (output == "muskmelon" or output == "kidneybeans" or output == "coconut" or output == "grapes" or output == "banana"):
            cropStatement = finalOutput + " should be harvested. It's a Rabi crop, so it must be sown at the end of monsoon and beginning of winter season e.g between September and October."
            
        elif (output == "watermelon"):
            cropStatement = finalOutput + " should be harvested. It's a Zaid Crop, so it must be sown between the Kharif and rabi season i.e between March and June."
        
        elif (output == "mango"):
            cropStatement = finalOutput + " should be harvested. It's a cash crop and also perennial. So you can grow it anytime."
        
              
                
    return render_template('CropResult.html', prediction_text=cropStatement)
        

if __name__ == '__main__':
    app.run(debug=True)
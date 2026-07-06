from flask import Flask,render_template,request
import pickle
import numpy as np

app = Flask(__name__)

# Pickle Files of Crop
with open("model/crop_model.pkl","rb") as file:
    crop_model = pickle.load(file)

with open("model/crop_scaler.pkl","rb") as file:
    crop_scaler = pickle.load(file)

with open("model/crop_label_encoder.pkl","rb") as file:
    crop_label_encoder = pickle.load(file)


# Pickle Files of Fertilizer
with open("model/fertilizer_model.pkl","rb") as file:
    fertilizer_model = pickle.load(file)

with open("model/fertilizer_scaler.pkl","rb") as file:
    fertilizer_scaler = pickle.load(file)

with open("model/fertilizer_encoder.pkl","rb") as file:
    fertilizer_label_encoder = pickle.load(file)

with open("model/fertilizer_soil_encoder.pkl","rb") as file:
    fertilizer_soil_encoder = pickle.load(file)

with open("model/fertilizer_crop_encoder.pkl","rb") as file:
    fertilizer_crop_encoder = pickle.load(file)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/crop')
def crop():
    return render_template("crop.html")


@app.route('/crop_predict',methods=["POST"])
def crop_predict():
    N = float(request.form["N"])
    P = float(request.form["P"])
    K = float(request.form["K"])
    temperature = float(request.form["temperature"])
    humidity = float(request.form["humidity"])
    rainfall = float(request.form["rainfall"])
    ph = float(request.form["ph"])

    data = np.array([[N,P,K,temperature,humidity,ph,rainfall]])
    data = crop_scaler.transform(data)
    prediction = crop_model.predict(data)[0]

    crop = crop_label_encoder.inverse_transform([prediction])[0]

    return render_template(
        "crop_predict.html",
        result=crop
    )


@app.route('/fertilizer')
def fertilizer():
    return render_template("fertilizer.html")

@app.route('/fertilizer_predict',methods=["POST"])
def fertilizer_predict():

    Temperature = float(request.form["Temperature"])
    Moisture = float(request.form["Moisture"])
    Rainfall = float(request.form["Rainfall"])
    PH = float(request.form["PH"])
    Nitrogen = float(request.form["Nitrogen"])
    Phosphorous = float(request.form["Phosphorous"])
    Potassium = float(request.form["Potassium"])
    Carbon = float(request.form["Carbon"])
    Soil = request.form["Soil"]
    Crop = request.form["Crop"]


    Soil = fertilizer_soil_encoder.transform([Soil])[0]
    Crop = fertilizer_crop_encoder.transform([Crop])[0]

    data = np.array([[Temperature,Moisture,Rainfall,PH,Nitrogen,Phosphorous,Potassium,Carbon,Soil,Crop]])
    data = fertilizer_scaler.transform(data)
    prediction = fertilizer_model.predict(data)[0]

    fertilizer = fertilizer_label_encoder.inverse_transform([prediction])[0]

    return render_template(
        "fertilizer_predict.html",
        prediction=fertilizer
    )

if __name__ == "__main__":
    app.run(debug=True)
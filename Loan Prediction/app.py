from flask import Flask,render_template,request
import warnings
import pickle
import numpy as np
warnings.filterwarnings("ignore")

app = Flask(__name__)


with open("model/credit.pkl","rb") as file:
    model = pickle.load(file)

with open("model/encoders.pkl","rb") as file:
    encoders = pickle.load(file)

with open("model/scaler.pkl","rb") as file:
    scaler = pickle.load(file)



@app.route("/")
def home():
    return render_template('index.html')

@app.route('/Search')
def Search():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predict():
    person_age = int(request.form["person_age"])
    person_income = float(request.form["person_income"])
    person_home_ownership =  request.form["person_home_ownership"]
    person_emp_length =  float(request.form["person_emp_length"])
    loan_intent =  request.form["loan_intent"]
    loan_grade =  request.form["loan_grade"]
    loan_amnt =  float(request.form["loan_amnt"])
    loan_int_rate = float(request.form["loan_int_rate"])
    loan_percent_income = float(request.form["loan_percent_income"])
    cb_person_default_on_file = request.form["cb_person_default_on_file"]
    cb_person_cred_hist_length = int(request.form["cb_person_cred_hist_length"])


    person_home_ownership = encoders['person_home_ownership'].transform([person_home_ownership])[0]   # encoding
    loan_intent = encoders['loan_intent'].transform([loan_intent])[0]   
    loan_grade = encoders['loan_grade'].transform([loan_grade])[0]   
    cb_person_default_on_file = encoders['cb_person_default_on_file'].transform([cb_person_default_on_file])[0]   



    data = np.array([[person_age,person_income,person_home_ownership,person_emp_length,loan_intent,loan_grade,loan_amnt,loan_int_rate,loan_percent_income,cb_person_default_on_file,cb_person_cred_hist_length]])

    data = scaler.transform(data)
    prediction = model.predict(data)[0]

    result = "Loan Approved" if(prediction == 1) else "Loan Rejected"

    return render_template('result.html',result=result)


if(__name__ == "__main__"):
    app.run(debug=True)





# from flask import Flask,render_template,request
# import warnings

# warnings.filterwarnings("ignore")

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template('index.html')

# @app.route('/search')
# def search(): 
#     name =  request.args.get("name")
#     age =  request.args.get("age")

#     return f"Welcome {name} and age is {age}" 

# if(__name__ == "__main__"):
#     app.run(debug=True)





# from flask import Flask, render_template, request
# import warnings

# warnings.filterwarnings("ignore")

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/login", methods=["POST"])
# def login():
#     Username = request.form["username"]
#     Password = request.form["password"]

#     return f"Welcome {Username}"

# if __name__ == "__main__":
#     app.run(debug=True)





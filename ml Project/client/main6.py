# get the Flask class imported
from flask import Flask, request, render_template
import pickle


# create an application of Flask
app = Flask(__name__)


@app.route("/")
def root():
    return render_template('index2.html')


@app.route("/predict", methods=["POST"])
def predict():
    bedrooms = request.form['bedrooms']
    bathroom = request.form['bathrooms']
    parking = request.form['parking']
    area = request.form['area']
    state = request.form['state']

    # Map state names to numeric values if your model expects numeric input for state
    state_mapping = {
        "VIC": 5,
        "TAS": 4,
        "QLD": 2,
        "NSW": 0,
        "WA": 6,
        "SA": 3,
        "NT": 1
    }

    state_value = state_mapping[state]

    # load the model from model.pkl file
    with open('./model.pkl', 'rb') as file:
        model = pickle.load(file)

    # get the prediction using model
    prediction = model.predict([[bedrooms, bathroom, parking, area, state_value]])
    print(f"prediction = {prediction}")
    #
    # if prediction[0] == 1:
    #     result = "Pass"
    # else:
    #     result = "Fail"

    result = prediction

    # print(f"age = {age}, score = {score}")
    return render_template('index3.html', result=result)


# start the application
app.run(host="0.0.0.0", port=4000, debug=True)

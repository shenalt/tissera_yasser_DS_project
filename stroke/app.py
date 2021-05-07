import flask
import os
import pickle
import pandas as pd
from skimage import io
from skimage import transform


app = flask.Flask(__name__, template_folder='templates')

path_to_model = 'models/rfc.pkl'

with open(path_to_model, 'rb') as f:
    model = pickle.load(f)


@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('input_values.html'))

    if flask.request.method == 'POST':
        # Get the input from the user.
        age = flask.request.form['age_in']
        bmi = flask.request.form['bmi_in']
        glucose = flask.request.form['glucose_in']
        hypertension = flask.request.form['hypertension_in']
        heart_disease = flask.request.form['heart_in']

        list_of_inputs = [age, bmi, glucose, hypertension, heart]

        return(flask.render_template('input_values.html', 
            returned_age=age,
            returned_bmi=bmi,
            returned_glucose=glucose,
            returned_hyp=hypertension,
            returned_heart=heart_disease
            returned_list=list_of_inputs))

    return(flask.render_template('input_values.html'))


@app.route('/bootstrap/')
def bootstrap():
    return flask.render_template('bootstrap.html')

if __name__ == '__main__':
    app.run(debug=True)
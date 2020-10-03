from flask import Flask, render_template
import pandas as pd
import csv
from sklearn.linear_model import LinearRegression


app = Flask(__name__)

@app.route("/")
def main():
    df = pd.read_csv('data/business_dynamics.csv')

    

    #Render main page
    return render_template("index.html", tables=[df.to_html(classes='data')], titles=df.columns.values)

if __name__ == "__main__":
    app.run(debug = True)
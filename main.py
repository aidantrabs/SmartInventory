from flask import Flask, render_template, request
#import train
import pandas as pd
import sqlite3
from train.training import LinReg

app = Flask(__name__, static_url_path='/static')

# @app.errorhandler(404)
# def pageNotFound(error):
#     return "no response :("

# @app.errorhandler(500)
# def internal_error(error):
#     return "the code is broken :("

@app.route("/", methods=["POST", 'GET'])
def main():
 
    if request.method == 'POST':
        file = request.files['filename']    
        #we can also have inpt = file.read() <- hmm we actually need the file as a pandas Dataframe 
        # idk if this will work but we can try 
        inpt = LinReg( file )
        output = inpt.Calculate()
        return render_template("predictions.html", output = output)
    else: 
        #Render main page
        return render_template("index.html")

@app.route("/predictions", methods=["POST", 'GET'])
def predictions():
    if request.method == 'POST':
        file = request.files['filename']    
        #we can also have inpt = file.read() <- hmm we actually need the file as a pandas Dataframe 
        # idk if this will work but we can try 
        inpt = LinReg( file )
        output = inpt.Calculate()
        return render_template("predictions.html")
    return render_template("predictions.html")

if __name__ == "__main__":
    app.run(debug = True)
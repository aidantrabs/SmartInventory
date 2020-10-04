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
        inpt = pd.read_csv( file ) 
       
        output = LinReg.Calculate( inpt )

        return render_template("output.html", output = output)
    else: 
        #Render main page
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)
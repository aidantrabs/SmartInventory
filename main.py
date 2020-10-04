from flask import Flask, render_template, request
#import train

app = Flask(__name__)

@app.route("/", methods=["POST", 'GET'])
def main():    
    if request.method == 'POST':
        filename = request.form['filename']
        #output = train.linearRegression( filename )
        return render_template("output.html", output = filename)
    else: 
        #Render main page
        return render_template("index.html")#, #tables=[df.to_html(classes='data')], titles=df.columns.values)

if __name__ == "__main__":
    app.run(debug = True)
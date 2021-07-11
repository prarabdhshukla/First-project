import json
from flask import Flask, render_template, request, jsonify   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("InputOutput.html")    
    

@app.route("/submitJSON", methods=["POST"])
def processJSON(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    
    response = ""
    fname=jsonObj['fname']
    lname=jsonObj['lname']
    response+="<b> Welcome <b>"+fname+" "+lname+" to the IC100 course</b><br>"
        
    #f1=((float(temp1)*9.0)/5.0)+32.0
    #f2=((float(temp2)*9.0)/5.0)+32.0
    
   # response+="<b> The output temparatures in Fahrenheit are: <b>"+str(f1)+" and "+str(f2)+"</b><br>"
    	    
    return response
    
    
if __name__ == "__main__":
    app.run(debug=True)
    
    

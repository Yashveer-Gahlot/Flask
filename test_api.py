from flask import Flask,request,jsonify,render_template
app=Flask(__name__)

@app.route('/form')
def show_form():                                        
    return render_template('index.html')

@app.route('/submit_data',methods=['POST'])
def check_password():
    name=request.form.get('username')                   # if we have to pass the data using html file in flask we use methods=POST
    password=request.form.get('password')

    return "username and password received"
 
if __name__=="__main__":
    app.run(host='0.0.0.0',port=8000)
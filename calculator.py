from flask import Flask,request,render_template,jsonify
app=Flask(__name__)

@app.route('/form')
def cal_page():
    return render_template('calculate.html')

@app.route("/math",methods=['POST'])
def calculator():
    op=request.form['operation']
    first_num=int(request.form['num1'])
    second_num=int(request.form['num2'])

    if op=="add":
        a=first_num+second_num
        return f"addition of {first_num} and {second_num} is {a}"
    if op=="subtract":
        a=first_num+second_num
        return f"subtraction of {first_num} and {second_num} is {a}"
    if op=="multiply":
        a=first_num*second_num
        return f"multiplication of {first_num} and {second_num} is {a}"
    if op=="divide":
        a=first_num/second_num
        return f"division of {first_num} and {second_num} is {a}"

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5001)
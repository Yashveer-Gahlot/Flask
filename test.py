from flask import Flask,request         # for taking input we need to import request
app=Flask(__name__)


@app.route('/yash')
def add():
    return f"this is test function bhai nhi chl rha"            #this is a simple example how we can call this function in flask webpage

@app.route('/user')
def data():
    data=request.args.get('name')           # this is how we take input from user in our flask webpage
    return f"{data}"                        # we for input user have to write in url ?var_name=value


if __name__=='__main__':
    app.run(host="0.0.0.0",port=8000)      # this host here is helping us to give a open port to share this flask webpage to anybody

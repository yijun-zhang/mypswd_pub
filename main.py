from flask import Flask,jsonify,request,render_template, redirect, url_for
import json
from datetime import date,datetime
import hashlib


app = Flask(__name__)

APP_CLIENTS={
    "gdghdfgjdkfgdfklghjdfruiwlvmcv674dvbbgd" :1
}



f = open('resource/en.json', "r")
MESSAGES = json.loads(f.read())
f.close()



"""
 index.html
"""
@app.route("/")
def home():
    return render_template('index.html')


"""
login html
"""
# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login_html():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


"""
 input: email, password 
 output: ret = {"message": "success",
           "user":req_data["email"],
           "jwt":"testtoken"}
    return jsonify(ret)
"""
@app.route("/api/login",methods=['POST'])
def login():
   return


"""
 input: email, password , addtional (nest json string)
 output: ret = {"message": "success",
           "user":req_data["email"]}
    return jsonify(ret)
"""
@app.route("/api/account",methods=['PUT'])
def create_acount():
    return
    


"""
 input: jwttoken, email, password , addtional (nest json string)
 output: ret = {"message": "success",
           "user":req_data["email"]}
    return jsonify(ret)
"""

@app.route("/api/account",methods=['POST'])
def update_acount():
    return
    



"""
 input: jwttoken 
 output: ret = {"message": "success",
                 
           "user":req_data["email"]}
    return jsonify(ret)
"""


@app.route("/api/account",methods=['DELETE'])
def del_acount():
    return
    



"""
 input: jwttoken , filter ( a string used to search secret name include it) 
 output: ret = {"message": "success",
           "passwords":[{"id":101 ,"name":"password name1"},
                      {"id":102 ,"name":"password name2"}
           ]
           }
    """
@app.route("/api/passwords",methods=['GET'])
def get_passwords():
    return
    


"""
 input: jwttoken ,secret_id  
 output: ret = {"message": "success",
           "id":101 ,
           "name":"password name1",
           "password":"encrpt password",
           "description":"my description"
           }
    """
@app.route("/api/password",methods=['GET'])
def get_password():
    return
    


"""
 input: jwttoken ,password detail include ("name":"password name1",
           "password":"encrpt password",
           "description":"my description")
             
 output: ret = {"message": "success",
             
           "name":"password name1"
           }
    """
@app.route("/api/password", methods=['PUT'])
def create_password():
    return
    


"""
 input: jwttoken ,password detail include ("id":101, "name":"password name1",
           "password":"encrpt password",
           "description":"my description")

 output: ret = {"message": "success",
           "id":101 ,
           "name":"password name1"
           }
    """
@app.route("/api/password", methods=['POST'])
def update_password():
    return
    


"""
 input: jwttoken ,password detail include ("id":101)
 output: ret = {"message": "success",
           "id":101 
           }
    """
@app.route("/api/password", methods=['DELETE'])
def del_password():
    return
    


"""
 create a message
 input: jwttoken ,content

 output: ret = {"message": "success"
           }
    """


@app.route("/api/message", methods=['PUT'])
def create_message():
    return
    


"""
 get user message
 input: jwttoken 

 output: ret = {"message": "success",
           "contents":[{"id":101 ,"content":"abc", "createtime":"2020-01-01 09:00:01", "reply":"hello","replytime":"2020-01-03 10:00:11" },
                      {"id":102 ,"content":"abc2", "createtime":"2020-01-04 19:00:01", "reply":"hello2","replytime":"2020-03-03 10:00:11" }
           ]
           }
    """
@app.route("/api/messages", methods=['GET'])
def get_messages():
    return
   


#--------------admin api begin-------------------------
"""
 admin user has id =1
 input: email, password 
 output: ret = {"message": "success",
           "user":req_data["email"],
           "jwt":"testtoken"}
    return jsonify(ret)
"""
@app.route("/api/adminlogin",methods=['POST'])
def adminlogin():
    return
    




"""
 Admin get messages
 input: jwttoken ,  id must be 1
        filter { "replyed" : "no",
                 "user_id" :23
               }

 output: ret = {"message": "success",
           "contents":[{"id":101 ,"user_id":23, "content":"abc", "createtime":"2020-01-01 09:00:01", "reply":"hello","replytime":"2020-01-03 10:00:11" },
                      {"id":103 ,"user_id":24, "content":"abc2", "createtime":"2020-01-04 19:00:01", "reply":"hello2","replytime":"2020-03-03 10:00:11" }
           ]
           }
    """
@app.route("/api/adminmessages", methods=['GET'])
def get_adminmessages():
    return
    




"""
 Admin reply message
 input: jwttoken , id , reply)

 output: ret = {"message": "success",
           "id":101 
           }
    """
@app.route("/api/adminreply", methods=['POST'])
def reply_message():
    return
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)


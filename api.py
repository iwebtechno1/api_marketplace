from flask import Flask,jsonify,request,render_template
from database import Database
from flask_cors import CORS

# loginid - sys     
# password - qytaUOeguv7P8BmaVCty0SxBvzXuuNpPHIj1XmLRzueJJTgDLg

db = Database()
app = Flask(__name__)

CORS(app)
# @app.route("/login", methods=["GET"])
# def get_login():
#     return render_template("LoginPage()")

@app.route("/login", methods=["POST"])
def post_login():
    loginID = request.form.get("login_id")  
    password = request.form.get("password")
    
    print(loginID, password)
    # testing = db.select_records(f"select * from m_user")
    user = db.select_records(f"select login_id, password from m_user where login_id = '{loginID}' and password = '{password}'")
    if len(user) == 0:
        # return testing
        return "Login Failed", 403 
    else:
        return "Welcome", 200

app.run(host="0.0.0.0", port="42536", debug=True) 
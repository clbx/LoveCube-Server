import flask
import mysql.connector
from flask import request
import config as cfg


app = flask.Flask(__name__)
app.config["DEBUG"] = True
mydb = mysql.connector.connect(
    host="localhost",
    user=cfg.sqlCreds["user"],
    password=cfg.sqlCreds["pass"],
    database="LoveCube"
)

cur = mydb.cursor()
cur.execute("USE LoveCube")
target = "1"

def getNewestMessage(target):
    print("SELECT Message FROM Messages WHERE TARGET = " + target)
    cur.execute("SELECT Message FROM Messages WHERE TARGET = " + str(target) + " ORDER BY TIMESTAMP DESC LIMIT 1;")
    result = cur.fetchall()
    return result[0][0]    

@app.route('/', methods=['GET'])
def home():
    return "LoveCube"

@app.route('/api/newMessage', methods=['POST'])
def setMessage():
    token = request.args["token"]
    message = request.args["message"]
    cur.execute("INSERT INTO Messages (TARGET,MESSAGE,TIMESTAMP) VALUES (" + str(token) +","+ str(message) + ",NOW());")
    mydb.commit()
    return "Added Message"

@app.route('/api/getMessage', methods=['GET'])
def getMessage():
    if "token" in request.args:
        token = request.args['token']
        return getNewestMessage(token)

if __name__ == '__main__':
    app.run()
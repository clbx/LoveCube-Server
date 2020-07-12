import flask
from flask import request
import sqlite3
from sqlite3 import Error


app = flask.Flask(__name__)
app.config["DEBUG"] = True
conn = sqlite3.connect(r"messages.db")

def getNewestMessage(id):
    query = ("SELECT Message FROM Messages WHERE ID is " + id + "LIMIT 1")
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit(0)
    message = cursor.fetchall()
    print(message)
    return message
    

def setNewMessage(newMsg, id):
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commmit(0)



@app.route('/', methods=['GET'])
def home():
    return "LoveCube"


@app.route('/api/newMessage', methods=['POST'])

@app.route('/api/getMessage', methods=['GET'])
def getMessage():
    if "token" in request.args:
        token = request.args['token']
        getNewestMessage(token)

if __name__ == '__main__':
    app.run()
from flask import Flask, request, jsonify
from passlib.hash import pbkdf2_sha256

app = Flask(__name__)

def convert(password):
    ans =  pbkdf2_sha256.hash(password)
    print(type(ans))
    return ans

def check_pass(password , hashed_password):
    return pbkdf2_sha256.verify(password,hashed_password)

@app.route('/api/hash',methods = ['GET'])
def API():
    if request.method == 'GET':
        password = str(request.args['p'])
        hashed_password = convert(password)
        return jsonify({'password' : hashed_password})

@app.route('/api/check/hash',methods = ['GEaT'])
def check():
    if request.method == 'GET':
        p = str(request.args['p'])
        h = str(request.args['h'])
        ans = check_pass(p,h)
        return jsonify({'answer' : ans})


from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
import os
import json
from pymongo import MongoClient
import hashlib
from secrets import token_urlsafe
import dotenv

# Setting up Flask app
app = Flask(__name__)
CORS(app)
dotenv.load_dotenv()
app.config['DEBUG'] = os.getenv('DEBUG', False)

# Setting up MongoDB Database
client = MongoClient(f'mongodb+srv://silicoflare:{os.getenv("MONGODB_PASS")}@silicoverse.aoepe6c.mongodb.net/?retryWrites=true&w=majority')
# client = MongoClient('mongodb://localhost:27017')
db = client['linkhub']
lh_pages = db['pages']
lh_users = db['users']

# Dictionary to store logged-in data
logged_in_users = {}


def getHash(text):
    return hashlib.sha256(text.encode()).hexdigest()

@app.route('/<username>', methods=['GET'])
def get_link_meta(username):
    userdata = lh_pages.find_one({"link": username})
    if userdata:
        meta = userdata['meta']
        return jsonify(meta)
    else:
        return jsonify({
            "status": 404,
            "message": "User not found"
        })


@app.route('/<username>', methods=['POST'])
def set_link_meta(username):
    access_token = request.cookies.get('access_token_cookie')
    if username in logged_in_users:
        if access_token:
            if logged_in_users[username] == access_token:
                if not request.is_json:
                    return jsonify(msg='Data is not JSON'), 400
                elif not 'meta' in request.json:
                    return jsonify(msg='Metadata missing'), 400
                else:
                    if lh_pages.find_one({"link": username}):
                        return jsonify(msg=f'Metadata already exists for user {username}'), 401
                    else:
                        lh_pages.insert_one({"link": username, "meta": request.json.get('meta')})
                        return jsonify(msg=f'Added metadata for user {username}'), 200
            else:
                return jsonify(msg='Not logged in: Wrong token'), 403
        else:
            return jsonify(msg='Not logged in: No token'), 403
    else:
        return jsonify(msg='Not logged in: User not logged in'), 403


@app.route('/signup', methods=['POST'])
def signup():
    if not request.is_json:
        return jsonify(message='Data is not in JSON format'), 415
    username = request.json.get('username')
    password = request.json.get('password')
    if not username or not password:
        return jsonify(message='Missing credentials'), 401
    if lh_users.find_one({ "username": username }):
        return jsonify({
            "status": 901,
            "message": "User already exists"
        })
    else:
        lh_users.insert_one({
            "username": username,
            "password": getHash(password)
        })
        return jsonify({
            "status": 900,
            "message": "User created",
            "username": username
        })


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    if not request.cookies.get('access_token_cookie'):
        user = lh_users.find_one({ "username": username })
        if user:
            psw = getHash(password)
            if psw == user['password']:
                access_token = token_urlsafe(16)
                resp = make_response(jsonify(message="User logged in"))
                logged_in_users[username] = access_token
                resp.set_cookie('access_token_cookie', access_token)
                return resp
            else:
                return jsonify(message="Wrong Password"), 401
        else:
            return jsonify(message="User not found"), 404
    else:
        return jsonify(msg='Already logged in'), 401


@app.route('/<username>/edit', methods=['POST'])
def edit_stuff(username):
    access_token = request.cookies.get('access_token_cookie')
    if username in logged_in_users:
        if access_token:
            if logged_in_users[username] == access_token:
                if not request.is_json:
                    return jsonify(msg='Data is not JSON'), 400
                elif not 'meta' in request.json:
                    return jsonify(msg='Metadata missing'), 400
                lh_pages.update_one({"link": username}, {"$set": {"meta": request.json.get('meta')}})
                return jsonify(msg=f'Updated metadata for user {username}'), 200
            else:
                return jsonify(msg='Not logged in: Wrong token'), 403
        else:
            return jsonify(msg='Not logged in: No token'), 403
    else:
        return jsonify(msg='Not logged in: User not logged in'), 403


@app.route('/logout', methods=['GET'])
def logout():
    access_token = request.cookies.get('access_token_cookie')
    if access_token:
        resp = make_response(jsonify(msg='Logged out successfully')) 
        resp.set_cookie('access_token_cookie', '', expires=0)
        for key in logged_in_users:
            if logged_in_users[key] == access_token:
                del logged_in_users[key]
                break
        return resp
    else:
        return jsonify(msg='User not logged in'), 404

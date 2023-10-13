from labproject1 import app
from datetime import datetime
from flask import jsonify, request
import uuid

@app.route('/healthcheck')
def healthcheck_page():
    cur_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    response = {
        "status": "succes",
        "message": "Code of response: 200",
        "current_date": cur_date    
    }
    return jsonify(response)

users = {}
categories = {}
records = {}

@app.post('/user')
def create_user():
    user_data = request.get_json()
    user_id = uuid.uuid4().hex
    user = {"id": user_id, **user_data}
    users[user_id] = user

    return user

@app.route('/user/<string:user_id>', methods=['GET', 'DELETE'])
def get_delete_user(user_id):
    for userid in users.keys():
        if userid == user_id:
            if request.method == 'GET':
                return {user_id:users[user_id]}
            elif request.method == 'DELETE':
                del users[user_id]
                return {'message':'deleted',
                        'id':user_id}
    return {'message':'user is not found'}

@app.route('/users', methods=['GET'])
def get_users():
    return users

@app.route('/category', methods=['GET', 'POST'])
def work_category():
    if request.method == 'GET':
        return categories
    elif request.method == 'POST':
        cat_data = request.get_json()
        cat_id = uuid.uuid4().hex
        cat = {"id": cat_id, **cat_data}
        categories[cat_id] = cat
        return cat
    else:
        return {'message':'bad request'}

@app.route('/category/<string:category_id>', methods=['DELETE'])
def delete_category(category_id):
    del categories[category_id]
    return {'message':'deleted',
            'id':category_id}

@app.route('/record', methods=['POST'])
def post_record():
    record_data = request.get_json()
    record_id = uuid.uuid4().hex
    record = {"id": record_id, "time":datetime.now().strftime("%Y-%m-%d %H:%M:%S"), **record_data}
    records[record_id] = record
    return record

@app.route('/record', methods=['GET'])
def get_record_by_ides():
    id_data = request.get_json()
    user_id = id_data.get('user_id', None)
    category_id = id_data.get('category_id', None)

    if not user_id and not category_id:
        return "Any parametres are given", 400

    filtered_records = []

    
    f_records = {}

    if user_id:
        f_records = {i:records[i] for i in records if records[i]['user_id'] == user_id}

    if category_id:
        f_records = {i:f_records[i] for i in f_records if f_records[i]['category_id'] == category_id}

    return f_records


@app.route('/record/<string:record_id>', methods=['GET', 'DELETE'])
def get_delete_record(record_id):
    for recordid in records.keys():
        if recordid == record_id:
            if request.method == 'GET':
                return {record_id:records[record_id]}
            elif request.method == 'DELETE':
                del records[record_id]
                return {'message':'deleted',
                        'id':record_id}

    return {'message':'record is not found'}

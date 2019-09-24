from flask import jsonify
from . import api
from flask import request
from models import UserModel
from models import db


@api.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        userid = data.get('userid')
        password = data.get('password')
        birthdate = data.get('birthdate')

        if not (userid and username and password):
            return jsonify({'error': 'No arguments'}), 400

        user = UserModel()
        user.id = userid
        user.name = username
        user.birthdate = birthdate
        user.password = password

        db.session.add(user)
        db.session.commit()
        return jsonify(), 201

    else:
        users_info = UserModel.query.all()

    return jsonify([user_info.serialize for user_info in users_info])


@api.route('/users/<uid>', methods=['GET', 'PUT', 'DELETE'])
def user_detail(uid):
    if request.method == 'GET':
        user = UserModel.query.filter(UserModel.id == uid).first()
        return jsonify(user.serialize)

    elif request.method == 'DELETE':
        UserModel.query.delete(UserModel.id == uid)
        return jsonify('deletion completed'), 204

    else:
        data = request.get_json()
        username = data.get('username')
        userid = data.get('userid')
        password = data.get('password')
        birthdate = data.get('birthdate')

        updated_data = {}

        if userid:
            updated_data['userid'] = userid

        if username:
            updated_data['username'] = username

        if password:
            updated_data['password'] = password

        if birthdate:
            updated_data['birthdate'] = birthdate

        UserModel.query.filter(uid == UserModel.id).update(updated_data)
        users_info = UserModel.query.all()
        return jsonify([user_info.serialize for user_info in users_info])

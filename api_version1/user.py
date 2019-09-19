from flask import jsonify
from . import api
from flask import request
from models import userModel
from models import db


@api.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        username = request.form.get('username')
        userid = request.form.get('userid')
        password = request.form.get('password')
        birthdate = request.form.get('birthdate')

        if not (userid and username and password):
            return jsonify({'error': 'No arguments'}), 400

        user = userModel()
        user.id = userid
        user.name = username
        user.birthdate = birthdate
        user.password = password
        
        db.session.add(user)
        db.session.commit()
        return jsonify(), 201

    return jsonify()

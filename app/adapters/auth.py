# -*- coding: utf-8 -*-
from flask import request, jsonify
from flask import Blueprint
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth_adapter', __name__)


@auth_bp.route('/register', methods=['POST'])
def register():
    result = {'status': '', 'msg': ''}
    '''
    :param
    {
        'phone_num': '15828296486',
        'account': 'denghaowen',
        'password': '123456'
    }
    :return:
    {
        'status': 'success',
        'msg': ''
    }
    '''
    data = request.json
    phone_num = data.get('phone_num')
    account = data.get('account')
    password = data.get('password')
    # password: add salt and hash
    password = generate_password_hash(password)
    return jsonify(result)


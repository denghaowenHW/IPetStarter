# -*- coding: utf-8 -*-
from flask import request, jsonify
from flask import Blueprint
from log import logger
from app.controllers.user_controller import *

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
    try:
        data = request.json
        phone_num = data.get('phone_num')
        account = data.get('account')
        password = data.get('password')
        args = (phone_num, account, password)
        create_user(args=args, result=result)
    except Exception as e:
        logger.error('register exception: %s' % str(e))
        result['status'] = 'fail'
        result['msg'] = str(e)
    return jsonify(result)


@auth_bp.route('/login', methods=['GET'])
def login():
    # login by phone_num
    result = {'status': '', 'msg': ''}
    '''
    :param
    {
        'phone_num': '15828296486',
        'input_pwd': '123456'
    }
    :return:
    {
        'status': 'success',
        'msg': ''
    }
    '''
    try:
        data = request.json
        phone_num = data.get('phone_num')
        input_pwd = data.get('input_pwd')
        args = (phone_num, input_pwd)
        check_password(args=args, result=result)
    except Exception as e:
        logger.error('login exception: %s' % str(e))
        result['status'] = 'fail'
        result['msg'] = str(e)
    return jsonify(result)

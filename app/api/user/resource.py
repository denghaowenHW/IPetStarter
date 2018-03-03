from flask_restplus import Namespace, Resource
from app.controllers.user_controller import *
from flask import request, jsonify
from app.api import api
from log import logger

ns = Namespace('user')


@ns.route('/<string:action>')
class User(Resource):
    def put(self, action):
        print action
        if action == 'delete':
            pass
        elif action == 'edit':
            pass
        elif action == 'add':
            pass

        return action


@ns.route('/change_balance')
class Recharge(Resource):
    def put(self):
        result = {'status': '', 'msg': ''}
        '''
        :param
        {
            'phone_num': '15828296486',
            'money': '100'
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
            money = data.get('money')
            change_balance(phone_num=phone_num, money=money, result=result)
            return jsonify(result)
        except Exception as e:
            logger.error('change balance exception: %s' % str(e))
            result['status'] = 'fail'
            result['msg'] = str(e)
            return result

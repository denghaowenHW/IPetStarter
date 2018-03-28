from flask_restplus import Namespace, Resource
from app.controllers.user_controller import *
from flask import request, jsonify
from log import logger

ns = Namespace('user')


@ns.route('/info/<string:type>')
class GetBaseInfo(Resource):
    def get(self, type):
        try:
            data = request.json
            phone_num = data.get('phone_num')
            user_info = get_user_info(phone_num=phone_num, info_type=type)
            return jsonify(user_info)
        except Exception as e:
            result = {'status': 'fail', 'msg': str(e)}
            return jsonify(result)


@ns.route('/change_balance')
class ChangeBalance(Resource):
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
            args = (phone_num, money)
            change_balance(args=args, result=result)
        except Exception as e:
            logger.error('change balance exception: %s' % str(e))
            result['status'] = 'fail'
            result['msg'] = str(e)
        return jsonify(result)


@ns.route('/add_pet')
class AddPet(Resource):
    def post(self):
        result = {'status': '', 'msg': ''}
        '''
        :param
        {
            'phone_num': '15828296486',
            'pet_name': 'miao',
            'pet_age': '100',
            'pet_type': 'cat'
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
            pet_name = data.get('pet_name')
            pet_age = data.get('pet_age')
            pet_type = data.get('pet_type')
            args = (phone_num, pet_name, pet_age, pet_type)
            create_pet(args=args, result=result)
        except Exception as e:
            logger.error('add pet exception: %s' % str(e))
            result['status'] = 'fail'
            result['msg'] = str(e)
        return jsonify(result)


@ns.route('/del_pets')
class DelPets(Resource):
    def post(self):
        result = {'status': '', 'msg': ''}
        '''
        :param
        {
            'phone_num': '15828296486',
            'pet_id_list': ['8592fd40207711e899a4086266229d1b'],
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
            pet_id_list = data.get('pet_id_list')
            args = (phone_num, pet_id_list)
            remove_pets(args=args, result=result)
        except Exception as e:
            logger.error('del pets exception: %s' % str(e))
            result['status'] = 'fail'
            result['msg'] = str(e)
        return jsonify(result)


@ns.route('/notice/<string:action>')
class Notice(Resource):
    def post(self, action):
        result = {'status': '', 'msg': ''}
        if action == 'add' or action == 'edit':
            '''
            :param
            {
                'phone_num': '15828296486',
                'pet_id': '1fc44180207811e899ca086266229d1b',
                'notice_content': 'take a shower',
                'time': '20:00',
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
                pet_id = data.get('pet_id')
                notice_content = data.get('notice_content')
                time = data.get('time')
                args = (phone_num, pet_id, notice_content, time)
                add_notice(args, result)
            except Exception as e:
                logger.error('add notice exception: %s' % str(e))
                result['status'] = 'fail'
                result['msg'] = str(e)
        elif action == 'del':
            '''
            :param
            {
                'phone_num': '15828296486',
                'pet_id': '1fc44180207811e899ca086266229d1b',
                'time': '20:00',
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
                pet_id = data.get('pet_id')
                time = data.get('time')
                args = (phone_num, pet_id, time)
                del_notice(args, result)
            except Exception as e:
                logger.error('del notice exception: %s' % str(e))
                result['status'] = 'fail'
                result['msg'] = str(e)
        return jsonify(result)

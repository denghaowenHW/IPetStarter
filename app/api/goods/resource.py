from flask_restplus import Namespace, Resource
from app.controllers.goods_controller import *
from flask import request, jsonify
from log import logger

ns = Namespace('goods')


@ns.route('/<string:action>')
class OperateGoods(Resource):
    def post(self, action):
        result = {'status': '', 'msg': ''}
        if action == 'add':
            '''
             :param
             {
                 'name': 'dog food',
                 'price': '49.9'
             }
             :return:
             {
                 'status': 'success',
                 'msg': ''
             }
             '''
            try:
                data = request.json
                name = data.get('name')
                price = data.get('price')
                args = (name, price)
                add_goods(args=args, result=result)
            except Exception as e:
                logger.error('add goods exception: %s' % str(e))
                result['status'] = 'fail'
                result['msg'] = str(e)
        elif action == 'del':
            '''
             :param
             {
                 'goods_id': '5aa68a637c03ee13f05b3547'
             }
             :return:
             {
                 'status': 'success',
                 'msg': ''
             }
             '''
            try:
                data = request.json
                goods_id = data.get('goods_id')
                del_goods(goods_id=goods_id, result=result)
            except Exception as e:
                logger.error('del goods exception: %s' % str(e))
                result['status'] = 'fail'
                result['msg'] = str(e)
        return jsonify(result)

    def put(self, action):
        result = {'status': '', 'msg': ''}
        if action == 'edit':
            '''
             :param
             {
                 'goods_id': '5aa68b477c03ee25f4fd3b28',
                 'edit_type': 'price',
                 'edit_content': '39.9',
             }
             :return:
             {
                 'status': 'success',
                 'msg': ''
             }
             '''
            try:
                data = request.json
                goods_id = data.get('goods_id')
                edit_type = data.get('edit_type')
                edit_content = data.get('edit_content')
                args = (goods_id, edit_type, edit_content)
                edit_goods(args=args, result=result)
            except Exception as e:
                logger.error('edit goods exception: %s' % str(e))
                result['status'] = 'fail'
                result['msg'] = str(e)
        return jsonify(result)

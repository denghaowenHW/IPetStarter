from flask_restplus import Namespace, Resource
from app.controllers.article_controller import *
from flask import request, jsonify
from log import logger

ns = Namespace('article')


@ns.route('/<string:action>')
class OperateArticle(Resource):
    def post(self, action):
        result = {'status': '', 'msg': ''}
        if action == 'add':
            '''
             :param
             {
                 'title': 'xxx',
                 'author': 'denghaowen',
                 'content': 'i love u'
             }
             :return:
             {
                 'status': 'success',
                 'msg': ''
             }
             '''
            try:
                data = request.json
                title = data.get('title')
                author = data.get('author')
                content = data.get('content')
                args = (title, author, content)
                add_article(args=args, result=result)
            except Exception as e:
                logger.error('add article exception: %s' % str(e))
                result['status'] = 'fail'
                result['msg'] = str(e)
        elif action == 'del':
            '''
             :param
             {
                 'article_id': '5aa68a637c03ee13f05b3547'
             }
             :return:
             {
                 'status': 'success',
                 'msg': ''
             }
             '''
            try:
                data = request.json
                article_id = data.get('article_id')
                del_article(article_id=article_id, result=result)
            except Exception as e:
                logger.error('del article exception: %s' % str(e))
                result['status'] = 'fail'
                result['msg'] = str(e)
        return jsonify(result)

    def put(self, action):
        if action == 'edit':
            pass

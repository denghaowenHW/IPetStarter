from flask_restplus import Namespace, Resource
from app.controllers.article_controller import *
from flask import request, jsonify
from log import logger

ns = Namespace('article')


@ns.route('/all')
class GetArticleInfo(Resource):
    def get(self):
        try:
            article_info = get_all_article()
            return jsonify(article_info)
        except Exception as e:
            result = {'status': 'fail', 'msg': str(e)}
            return jsonify(result)


@ns.route('/search')
class SearchArticles(Resource):
    def get(self):
        # http://127.0.0.1:8088/api/v1/article/search?label=love,story
        try:
            label = request.args.get('label')
            if label:
                required_label = label.split(',')
                goods_list = search_articles_by_label(required_label)
                return jsonify(goods_list)
            else:
                result = {'status': 'fail', 'msg': 'no label'}
                return jsonify(result)
        except Exception as e:
            result = {'status': 'fail', 'msg': str(e)}
            return jsonify(result)


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
                 'content': 'i love u',
                 'label': ['love', 'story']
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
                label = data.get('label')
                args = (title, author, content, label)
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
        result = {'status': '', 'msg': ''}
        if action == 'edit':
            '''
             :param
             {
                 'article_id': '5aa68b477c03ee25f4fd3b28',
                 'edit_type': 'content',
                 'edit_content': 'i love u forever',
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
                edit_type = data.get('edit_type')
                edit_content = data.get('edit_content')
                args = (article_id, edit_type, edit_content)
                edit_article(args, result)
            except Exception as e:
                logger.error('edit article exception: %s' % str(e))
                result['status'] = 'fail'
                result['msg'] = str(e)
        return jsonify(result)


@ns.route('/likes')
class ArticleLikes(Resource):
    def get(self):
        try:
            id = request.args.get('id')
            likes_num = get_likes_num(id)
            return likes_num
        except Exception as e:
            logger.error('get article likes exception: %s' % str(e))
            result = {'status': 'fail', 'msg': str(e)}
            return jsonify(result)

    def put(self):
        result = {'status': '', 'msg': ''}
        try:
            '''
             :param
             {
                 'id': '5aa68b477c03ee25f4fd3b28',
                 'phone_num': '15828296486'
             }
             :return:
             {
                 'status': 'success',
                 'msg': ''
             }
             '''
            data = request.json
            id = data.get('id')
            phone_num = data.get('phone_num')
            args = (id, phone_num)
            click_likes(args, result)
        except Exception as e:
            logger.error('change article likes exception: %s' % str(e))
            result['status'] = 'fail'
            result['msg'] = str(e)
        return jsonify(result)


@ns.route('/likes_status')
class ArticleLikesStatus(Resource):
    def get(self):
        result = {'is_like': False}
        '''
         :param
         {
             'id': '5aa68b477c03ee25f4fd3b28',
             'phone_num': '15828296486'
         }
         :return:
         {
             'is_like': True,
         }
         '''
        try:
            data = request.json
            id = data.get('id')
            phone_num = data.get('phone_num')
            args = (id, phone_num)
            get_likes_status(args, result)
        except Exception as e:
            logger.error('get article likes status exception: %s' % str(e))
            result['status'] = 'fail'
            result['msg'] = str(e)
        return jsonify(result)


@ns.route('/comment')
class ArticleComment(Resource):
    def get(self):
        try:
            id = request.args.get('id')
            comment_list = get_comments(id)
            return jsonify(comment_list)
        except Exception as e:
            logger.error('get comment exception: %s' % str(e))
            result = {'status': 'fail', 'msg': str(e)}
            return jsonify(result)

    def post(self):
        result = {'status': '', 'msg': ''}
        '''
         :param
         {
             'phone_num': '15828296486',
             'comment': 'i love u',
             'id': '5aa68b477c03ee25f4fd3b28'
         }
         :return:
         {
             'status': 'success',
             'msg': ''
         }
         '''
        try:
            data = request.json
            id = data.get('id')
            phone_num = data.get('phone_num')
            comment = data.get('comment')
            args = (id, phone_num, comment)
            add_comment(args, result)
        except Exception as e:
            logger.error('add comment exception: %s' % str(e))
            result['status'] = 'fail'
            result['msg'] = str(e)
        return jsonify(result)


@ns.route('/del_comment')
class ArticleCommentDelete(Resource):
    def put(self):
        result = {'status': '', 'msg': ''}
        '''
         :param
         {
             'comment_id': '7efce35e3bfc11e88443dc85def89886',
             'article_id': '5aa68b477c03ee25f4fd3b28'
         }
         :return:
         {
             'status': 'success',
             'msg': ''
         }
         '''
        try:
            data = request.json
            comment_id = data.get('comment_id')
            article_id = data.get('article_id')
            args = (comment_id, article_id)
            del_comment(args, result)
        except Exception as e:
            logger.error('del comment exception: %s' % str(e))
            result['status'] = 'fail'
            result['msg'] = str(e)
        return jsonify(result)
# -*- coding: utf-8 -*-
import requests
import json
import unittest
import time


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.headers = {'Content-Type': 'application/json; Charset=utf-8'}

    def test_api_register(self):
        print 'test api: /register'
        url = 'http://127.0.0.1:8088/register'
        param = {
            'phone_num': '15828296487',
            'account': 'dengh',
            'password': 'deng@1995'
        }
        try:
            response = requests.post(url=url, data=json.dumps(param), headers=self.headers)
            data = response.json()
            print data
            self.assertTrue(data['status'] == 'success')
        except Exception as e:
            print 'Exception: %s' % str(e)

    def test_api_login(self):
        print 'test api: /login'
        url = 'http://127.0.0.1:8088/login'
        param = {
            'phone_num': '1582829648',
            'input_pwd': 'deng@199'
        }
        try:
            response = requests.get(url=url, data=json.dumps(param), headers=self.headers)
            data = response.json()
            print data
            self.assertTrue(data['status'] == 'success')
        except Exception as e:
            print 'Exception: %s' % str(e)

    def test_api_change_balance(self):
        print 'test api: /api/v1/user/change_balance'
        url = 'http://127.0.0.1:8088/api/v1/user/change_balance'
        param = {
            'phone_num': '15828296486',
            'money': '100'
        }
        try:
            response = requests.put(url=url, data=json.dumps(param), headers=self.headers)
            data = response.json()
            print data
            self.assertTrue(data['status'] == 'success')
        except Exception as e:
            print 'Exception: %s' % str(e)

    def test_api_add_pet(self):
        print 'test api: /api/v1/user/add_pet'
        url = 'http://127.0.0.1:8088/api/v1/user/add_pet'
        param = {
            'phone_num': '15828296486',
            'pet_name': 'miao',
            'pet_age': '100',
            'pet_type': 'cat'
        }
        try:
            response = requests.post(url=url, data=json.dumps(param), headers=self.headers)
            data = response.json()
            print data
            self.assertTrue(data['status'] == 'success')
        except Exception as e:
            print 'Exception: %s' % str(e)

    def test_api_del_pets(self):
        print 'test api: /api/v1/user/del_pets'
        url = 'http://127.0.0.1:8088/api/v1/user/del_pets'
        param = {
            'phone_num': '15828296486',
            'pet_id_list': ['1d492f61207811e88476086266229d1b', '1dfc79cf207811e8a899086266229d1b'],
        }
        try:
            response = requests.post(url=url, data=json.dumps(param), headers=self.headers)
            data = response.json()
            print data
            self.assertTrue(data['status'] == 'success')
        except Exception as e:
            print 'Exception: %s' % str(e)

    def test_api_add_article(self):
        print 'test api: /api/v1/article/add'
        url = 'http://127.0.0.1:8088/api/v1/article/add'
        param = {
            'title': 'xxx',
            'author': 'denghaowen',
            'content': 'i love u',
            'label': ['love', 'story']
        }
        try:
            response = requests.post(url=url, data=json.dumps(param), headers=self.headers)
            data = response.json()
            print data
            self.assertTrue(data['status'] == 'success')
        except Exception as e:
            print 'Exception: %s' % str(e)

    def test_api_del_article(self):
        print 'test api: /api/v1/article/del'
        url = 'http://127.0.0.1:8088/api/v1/article/del'
        param = {
            'article_id': '5aa7d6867c03ee2150ff91fc'
        }
        try:
            response = requests.post(url=url, data=json.dumps(param), headers=self.headers)
            data = response.json()
            print data
            self.assertTrue(data['status'] == 'success')
        except Exception as e:
            print 'Exception: %s' % str(e)

    def test_api_edit_article(self):
        print 'test api: /api/v1/article/edit'
        url = 'http://127.0.0.1:8088/api/v1/article/edit'
        param = {
            'article_id': '5ad354af7c03ee2c84097fa9',
            'edit_type': 'label',
            'edit_content': ['love', 'story', 'i']
        }
        try:
            response = requests.put(url=url, data=json.dumps(param), headers=self.headers)
            data = response.json()
            print data
            self.assertTrue(data['status'] == 'success')
        except Exception as e:
            print 'Exception: %s' % str(e)

    def test_api_add_goods(self):
        print 'test api: /api/v1/goods/add'
        url = 'http://127.0.0.1:8088/api/v1/goods/add'
        param = {
            'name': 'dog food',
            'price': '49.9',
            'label': ['dog', 'food']
        }
        try:
            response = requests.post(url=url, data=json.dumps(param), headers=self.headers)
            data = response.json()
            print data
            self.assertTrue(data['status'] == 'success')
        except Exception as e:
            print 'Exception: %s' % str(e)

    def test_api_del_goods(self):
        print 'test api: /api/v1/goods/del'
        url = 'http://127.0.0.1:8088/api/v1/goods/del'
        param = {
            'goods_id': '5ad341147c03ee1f9c596911'
        }
        try:
            response = requests.post(url=url, data=json.dumps(param), headers=self.headers)
            data = response.json()
            print data
            self.assertTrue(data['status'] == 'success')
        except Exception as e:
            print 'Exception: %s' % str(e)

    def test_api_edit_goods(self):
        print 'test api: /api/v1/goods/edit'
        url = 'http://127.0.0.1:8088/api/v1/goods/edit'
        param = {
            'goods_id': '5ad3425e7c03ee1f9c596912',
            'edit_type': 'label',
            'edit_content': ['dog', 'food'],
        }
        try:
            response = requests.put(url=url, data=json.dumps(param), headers=self.headers)
            data = response.json()
            print data
            self.assertTrue(data['status'] == 'success')
        except Exception as e:
            print 'Exception: %s' % str(e)

    def test_api_add_notice(self):
        print 'test api: /api/v1/user/notice/add'
        url = 'http://127.0.0.1:8088/api/v1/user/notice/add'
        param = {
            'phone_num': '15828296486',
            'pet_id': '1fc44180207811e899ca086266229d1b',
            'notice_content': 'eat',
            'time': '21:00'
        }
        try:
            response = requests.post(url=url, data=json.dumps(param), headers=self.headers)
            data = response.json()
            print data
            self.assertTrue(data['status'] == 'success')
        except Exception as e:
            print 'Exception: %s' % str(e)

    def test_api_del_notice(self):
        print 'test api: /api/v1/user/notice/del'
        url = 'http://127.0.0.1:8088/api/v1/user/notice/del'
        param = {
            'phone_num': '15828296486',
            'pet_id': '1fc44180207811e899ca086266229d1b',
            'time': '21:00'
        }
        try:
            response = requests.post(url=url, data=json.dumps(param), headers=self.headers)
            data = response.json()
            print data
            self.assertTrue(data['status'] == 'success')
        except Exception as e:
            print 'Exception: %s' % str(e)

    def test_api_edit_notice(self):
        print 'test api: /api/v1/user/notice/edit'
        url = 'http://127.0.0.1:8088/api/v1/user/notice/edit'
        param = {
            'phone_num': '15828296486',
            'pet_id': '1fc44180207811e899ca086266229d1b',
            'notice_content': 'take a shower',
            'time': '21:00'
        }
        try:
            response = requests.post(url=url, data=json.dumps(param), headers=self.headers)
            data = response.json()
            print data
            self.assertTrue(data['status'] == 'success')
        except Exception as e:
            print 'Exception: %s' % str(e)

    def test_api_get_user_base_info(self):
        print 'test api: /api/v1/user/info/base'
        url = 'http://127.0.0.1:8088/api/v1/user/info/base'
        param = {
            'phone_num': '15828296486'
        }
        try:
            response = requests.get(url=url, data=json.dumps(param), headers=self.headers)
            data = response.json()
            print data
            self.assertTrue(not data['status'] == 'fail')
        except Exception as e:
            print 'Exception: %s' % str(e)

    def test_api_get_user_pets_info(self):
        print 'test api: /api/v1/user/info/pets'
        url = 'http://127.0.0.1:8088/api/v1/user/info/pets'
        param = {
            'phone_num': '15828296486'
        }
        try:
            response = requests.get(url=url, data=json.dumps(param), headers=self.headers)
            data = response.json()
            print data
            self.assertTrue(not data['status'] == 'fail')
        except Exception as e:
            print 'Exception: %s' % str(e)

    def test_api_get_all_article(self):
        print 'test api: /api/v1/article/all'
        url = 'http://127.0.0.1:8088/api/v1/article/all'
        try:
            response = requests.get(url=url, headers=self.headers)
            data = response.json()
            print data
            self.assertTrue(not data['status'] == 'fail')
        except Exception as e:
            print 'Exception: %s' % str(e)

    def test_api_get_all_goods(self):
        print 'test api: /api/v1/goods/all'
        url = 'http://127.0.0.1:8088/api/v1/goods/all'
        try:
            response = requests.get(url=url, headers=self.headers)
            data = response.json()
            print data
            self.assertTrue(not data['status'] == 'fail')
        except Exception as e:
            print 'Exception: %s' % str(e)

    def test_api_get_article_likes_length(self):
        print 'test GET api: /api/v1/article/likes'
        url = 'http://127.0.0.1:8088/api/v1/article/likes?id=5aa68b477c03ee25f4fd3b28'
        try:
            response = requests.get(url=url, headers=self.headers)
            data = response.json()
            print data
            self.assertTrue(type(data) == int)
        except Exception as e:
            print 'Exception: %s' % str(e)

    def test_api_click_likes(self):
        print 'test PUT api: /api/v1/article/likes'
        url = 'http://127.0.0.1:8088/api/v1/article/likes'
        param = {
            'phone_num': '15828296487',
            'id': '5aa68b477c03ee25f4fd3b28'
        }
        try:
            response = requests.put(url=url, data=json.dumps(param), headers=self.headers)
            data = response.json()
            print data
            self.assertTrue(data['status'] == 'success')
        except Exception as e:
            print 'Exception: %s' % str(e)

    def test_api_get_article_likes_status(self):
        print 'test GET api: /api/v1/article/likes_status'
        url = 'http://127.0.0.1:8088/api/v1/article/likes_status'
        param = {
            'phone_num': '15828296486',
            'id': '5aa68b477c03ee25f4fd3b28'
        }
        try:
            response = requests.get(url=url, data=json.dumps(param), headers=self.headers)
            data = response.json()
            print data
            self.assertTrue(type(data['is_like']) == bool)
        except Exception as e:
            print 'Exception: %s' % str(e)

    def test_api_add_comment(self):
        print 'test POST api: /api/v1/article/comment'
        url = 'http://127.0.0.1:8088/api/v1/article/comment'
        param = {
            'phone_num': '15828296487',
            'comment': 'i love u',
            'id': '5aa68b477c03ee25f4fd3b28'
        }
        try:
            response = requests.post(url=url, data=json.dumps(param), headers=self.headers)
            data = response.json()
            print data
            self.assertTrue(data['status'] == 'success')
        except Exception as e:
            print 'Exception: %s' % str(e)

    def test_api_get_comments(self):
        print 'test GET api: /api/v1/article/comment'
        url = 'http://127.0.0.1:8088/api/v1/article/comment?id=5aa68b477c03ee25f4fd3b28'
        try:
            response = requests.get(url=url, headers=self.headers)
            data = response.json()
            print data
            self.assertTrue(type(data) == list)
        except Exception as e:
            print 'Exception: %s' % str(e)

    def test_api_del_comments(self):
        print 'test api: /api/v1/article/del_comment'
        url = 'http://127.0.0.1:8088/api/v1/article/del_comment'
        param = {
            'comment_id': '7efce35e3bfc11e88443dc85def89886',
            'article_id': '5aa68b477c03ee25f4fd3b28'
        }
        try:
            response = requests.put(url=url, data=json.dumps(param), headers=self.headers)
            data = response.json()
            print data
            self.assertTrue(data['status'] == 'success')
        except Exception as e:
            print 'Exception: %s' % str(e)

    def test_api_search_goods_by_label(self):
        print 'test api: /api/v1/goods/search'
        url = 'http://127.0.0.1:8088/api/v1/goods/search?label=dog'
        try:
            response = requests.get(url=url, headers=self.headers)
            data = response.json()
            print data
            self.assertTrue(type(data) == list)
        except Exception as e:
            print 'Exception: %s' % str(e)

    def test_api_search_article_by_label(self):
        print 'test api: /api/v1/article/search'
        url = 'http://127.0.0.1:8088/api/v1/article/search?label=love'
        try:
            response = requests.get(url=url, headers=self.headers)
            data = response.json()
            print data
            self.assertTrue(type(data) == list)
        except Exception as e:
            print 'Exception: %s' % str(e)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    start = time.clock()
    suite.addTest(TestUtils('test_api_search_goods_by_label'))
    print 'cost %s seconds' % (time.clock() - start)
    unittest.TextTestRunner().run(suite)

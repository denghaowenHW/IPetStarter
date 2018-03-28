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
            'content': 'i love u'
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
            'article_id': '5aa7d6827c03ee2150ff91f7'
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
            'article_id': '5aa68b477c03ee25f4fd3b28',
            'edit_type': 'author',
            'edit_content': 'shidong'
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
            'price': '49.9'
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
            'goods_id': '5aaa78d57c03ee26704c7a4a'
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
            'goods_id': '5aaa78c17c03ee26704c7a49',
            'edit_type': 'price',
            'edit_content': '99.9',
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


if __name__ == '__main__':
    suite = unittest.TestSuite()
    start = time.clock()
    suite.addTest(TestUtils('test_api_get_user_pets_info'))
    print 'cost %s seconds' % (time.clock() - start)
    unittest.TextTestRunner().run(suite)

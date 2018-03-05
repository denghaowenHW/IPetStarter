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
            'phone_num': '15828296486',
            'account': 'denghaowen',
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


if __name__ == '__main__':
    suite = unittest.TestSuite()
    start = time.clock()
    suite.addTest(TestUtils('test_api_del_pets'))
    print 'cost %s seconds' % (time.clock() - start)
    unittest.TextTestRunner().run(suite)

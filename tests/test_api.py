import requests
import json
import unittest
import time


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.headers = {'Content-Type': 'application/json; Charset=utf-8'}

    def test_api_register(self):
        url = 'http://127.0.0.1:8088/register'
        param = {
            'phone_num': '15828296486',
            'account': 'denghaowen',
            'password': '123456'
        }
        try:
            response = requests.post(url=url, data=json.dumps(param), headers=self.headers)
            data = response.json()
            print data
            self.assertTrue(data['status'] == 'success')
        except Exception as e:
            print 'Exception: %s' % str(e)


if __name__ == '__main__':
    print 'test api'
    suite = unittest.TestSuite()
    start = time.clock()
    suite.addTest(TestUtils('test_api_register'))
    print 'cost %s seconds' % (time.clock() - start)
    unittest.TextTestRunner().run(suite)

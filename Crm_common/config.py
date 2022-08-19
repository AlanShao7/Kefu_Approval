#企微test
# host = "https://lixiao-test.ikcrm.com"

#独立test
# "host": 'https://lxcrm-test.weiwenjia.com'

#staging 独立
# "host": 'https://lxcrm-staging.weiwenjia.com'
import requests

class AllConfig():

    def __init__(self):
        self.host = 'https://lxcrm-test.weiwenjia.com'
        self.a_token = ''
        self.corp_id = 'wwjLhngunzq1XVgPd6cS'
        self.login_url = self.host + '/api/v2/auth/login'
        self.data = {'login': 17300000006,
                     'password': 'Ik123456',
                     'corp_id': self.corp_id}

    def token(self):
        req = requests.post(url=self.login_url, params=self.data)
        if req.status_code != 200:
            print("请求失败", req.status_code)
            return 0
        else:
            if req.json()['code'] != 0:
                print("接口请求错误", req.json()['code'], req.json()['message'])
                return 0
            else:
                user_token = req.json()['data']['user_token']
                return user_token

    def get_headers_config(self):
        if 'lixiao' in self.host:
            header = {
                "Authorization": self.a_token,
                'Content-Type': "application/x-www-form-urlencoded"
            }
            return header
        else:
            user_token = self.token()
            if user_token == 0:
                print("参数获取错误")
                return
            else:
                token = 'Token token=' + user_token
                header = {
                    "Authorization": token,
                    'Content-Type': "application/x-www-form-urlencoded"
                }
                return header


if __name__ == '__main__':
    a = AllConfig()
    b = a.get_headers_config()
    print(b)
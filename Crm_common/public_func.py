import requests
import sys
import os
from Crm_common.config import AllConfig


class HttpRequest(object):

    def __init__(self):
        user_token = AllConfig().token()
        if user_token == 0:
            print(self.url)
            return
        else:
            token = 'Token token=' + user_token
            host = AllConfig().host
            self.url = host
            self.header = {
                "Authorization": token,
                'Content-Type': "application/x-www-form-urlencoded"
            }

    def get(self, api_name, data):
        response = requests.get(self.url + api_name, data=data, headers=self.header)
        return response

    def post(self, api_name, data):
        response = requests.post(self.url + api_name, data=data, headers=self.header)
        return response


if __name__ == '__main__':
    a = HttpRequest()
    print(a)
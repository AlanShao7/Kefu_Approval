import time
import os
import sys
file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(file_path)
from Crm_common.public_func import HttpRequest
from common import timetochinese
print(file_path)


class Creat_customers:
    def __init__(self):
        self.api_name = '/api/customers'
        self.time = timetochinese.get_time()

    def post_creat(self, count, parent_id=''):
        """
        :param parent_id: 上级客户ID值
        :param count:创建的用户个数
        :return:
        """
        for i in range(count):
            self.name = "运营测试"+self.time
            self.data = {
                "customer[name]": self.name,
                # "customer[approve_status]": 'applying',
                "customer[parent_id]": parent_id
            }
            res = HttpRequest().post(api_name=self.api_name, data=self.data)
            if res.status_code != 200:
                print("res", res.status_code)
                if res.status_code == 401:
                    print("你没有新增客户的权限")
                break
            else:
                if res.json()['code'] != '0':
                    print("res_code", res.json()['code'], res.json()['msg'])
                    break
                else:
                    print(res.json())
            time.sleep(0.5)
            return res.json()['data']['name']


if __name__ == '__main__':
    a = Creat_customers()
    res = a.post_creat(1)
    print(res)


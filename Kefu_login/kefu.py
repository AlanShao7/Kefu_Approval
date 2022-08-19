import time
from selenium import webdriver
from Create_customer.Crm_create import Creat_customers
# import pywin32

class Comn:
    """
    kefu  UI测试
    """
    def __init__(self):
        """
        构造函数，创建对象的时候会执行
        初始化浏览器
        """
        self.driver = webdriver.Chrome()
        self.name = '运营测试二零二二年零八月一九日一四时零七分三七秒'
        # self.name = Creat_customers().post_creat(1) #测试时不开启

    def login(self):
        """
        进入运营平台系统
        :return:
        """
        self.driver.get('https://kefu-test.weiwenjia.com/user/login/#/user/login')
        # 登录网站
        self.driver.implicitly_wait(5)
        # 隐式等待5s
        self.driver.find_element_by_id('username').send_keys('17300000006')
        # 输入账号
        self.driver.find_element_by_id('password').send_keys('Ik123456')
        # 输入密码
        self.driver.find_element_by_xpath('//*[@id="root"]//..//button').click()
        # 点击登录
        self.driver.implicitly_wait(5)
        # 隐式等待5s


    def register_crm(self):
        self.login()
        self.driver.find_element_by_link_text('客户管理').click()
        #跳转到客户管理
        self.driver.implicitly_wait(5)
        # 隐式等待5s
        self.driver.find_element_by_xpath('//div[@class="ant-pro-table-list-toolbar-left"]').click()
        #点击更多操作
        self.driver.implicitly_wait(5)
        # 隐式等待5s
        self.driver.find_elements_by_class_name('ant-dropdown-menu-item-only-child')[0].click()
        #点击注册账号
        self.driver.implicitly_wait(5)
        # 隐式等待5s
        self.driver.find_element_by_id('product').click()
        #点击选择产品
        time.sleep(2)
        # 隐式等待5s
        self.driver.find_elements_by_xpath('//div[@class="rc-virtual-list-holder-inner"]/div')[3].click()
        #选择下拉框中的第四个励销CRM独立版创建
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//input[@id="client_name"]').send_keys('这是账号名称')
        # self.driver.find_element_by_xpath('//input[@id="client_name"]').send_keys(self.name)  先不请求接口
        #输入账号名称
        self.driver.find_element_by_xpath('//input[@id="name"]').send_keys('运营专用')
        #输入用户姓名
        self.driver.find_element_by_xpath('//input[@id="phone"]').send_keys('17300000006')
        #输入手机号码
        self.driver.find_elements_by_xpath('//div[@class="ant-modal-footer"]/button')[1].click()
        #点击确认按钮

    def add_custmoer_name(self):
        self.login()
        self.driver.find_element_by_link_text('客户管理').click()
        #跳转到客户管理
        self.driver.implicitly_wait(5)
        # 隐式等待5s
        self.driver.find_element_by_xpath('//div[@class="ant-pro-table-list-toolbar-left"]').click()
        #点击更多操作
        self.driver.implicitly_wait(5)
        # 隐式等待5s
        self.driver.find_elements_by_class_name('ant-dropdown-menu-item-only-child')[1].click()
        #点击添加客户法定名称
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//span[@class="ant-descriptions-item-content"]//input').send_keys(self.name)
        #输入客保客户信息
        self.driver.find_elements_by_xpath('//div[@class="ant-modal-footer"]/button')[1].click()
        #点击确定
        self.driver.implicitly_wait(5)
        #进行必填输入
        self.driver.find_element_by_xpath('//input[@id="operational_industry_id"]').click()
        #点击二级行业
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//div[@label="综合医院"]').click()
        #所属行业选择综合医院
        self.driver.find_element_by_xpath('//input[@id="province_id"]').click()
        #点击省份
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@label="北京"]').click()
        #选择北京
        self.driver.find_element_by_xpath('//input[@id="city_id"]').click()
        #点击省份
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@label="北京市"]').click()
        #选择北京

        #上传营业执照

if __name__ == '__main__':
    comn = Comn()
    # comn.register_crm()
    comn.add_custmoer_name()
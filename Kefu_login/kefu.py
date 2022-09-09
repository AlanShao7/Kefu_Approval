import time
from selenium import webdriver
from Create_customer.Crm_create import Creat_customers
from selenium.webdriver.common.action_chains import ActionChains
import clipboard
from pynput.keyboard import Controller, Key
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Comn:
    """
    kefu  UI测试
    """

    def __init__(self, pic_name):
        """
        :param pic: 图片地址
        """
        self.pic_name = pic_name
        self.driver = webdriver.Chrome()
        # self.name = '运营测试二零二二年零八月二二日一零时二五分零六秒'
        self.name = Creat_customers().post_creat(1) #测试时不开启

    def login(self):
        """
        进入运营平台系统
        :return:
        """
        self.driver.get('https://kefu-test.weiwenjia.com/user/login/#/user/login')
        self.driver.maximize_window()
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
        """
        注册账号
        :return:
        """
        self.login()
        time.sleep(2)
        self.driver.get('https://kefu-test.weiwenjia.com/#/my/client/accountList')
        #进入账号列表
        self.driver.implicitly_wait(5)
        # 隐式等待5s
        self.driver.find_element_by_xpath('//button[@class="ant-btn ant-btn-default ant-dropdown-trigger"]').click()
        # 点击更多操作
        time.sleep(3)
        # 隐式等待5s
        self.driver.find_elements_by_xpath('//li[@class="ant-dropdown-menu-item ant-dropdown-menu-item-only-child"]')[0].click()
        # 点击注册账号
        self.driver.implicitly_wait(5)
        # 隐式等待5s
        self.driver.find_element_by_id('product').click()
        # 点击选择产品
        time.sleep(2)
        # 隐式等待5s
        self.driver.find_elements_by_xpath('//div[@class="rc-virtual-list-holder-inner"]/div')[3].click()
        # 选择下拉框中的第四个励销CRM独立版创建
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//input[@id="client_name"]').send_keys(self.name)
        # self.driver.find_element_by_xpath('//input[@id="client_name"]').send_keys(self.name)  先不请求接口
        # 输入账号名称
        self.driver.find_element_by_xpath('//input[@id="name"]').send_keys('运营专用')
        # 输入用户姓名
        self.driver.find_element_by_xpath('//input[@id="phone"]').send_keys('17300000006')
        # 输入手机号码
        self.driver.find_elements_by_xpath('//div[@class="ant-modal-footer"]/button')[1].click()
        # 点击确认按钮

    def add_custmoer_name(self):
        """
        添加客户法定名称
        :return:
        """
        self.register_crm()
        # self.login()
        time.sleep(2)
        # self.driver.find_element_by_link_text('客户管理').click()
        # 跳转到客户管理
        self.driver.implicitly_wait(5)
        # 隐式等待5s
        self.driver.find_element_by_xpath('//button[@class="ant-btn ant-btn-default ant-dropdown-trigger"]').click()
        # 点击更多操作
        self.driver.implicitly_wait(5)
        # 隐式等待5s
        self.driver.find_elements_by_xpath('//li[@class="ant-dropdown-menu-item ant-dropdown-menu-item-only-child"]')[1].click()
        # 点击添加客户法定名称
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//span[@class="ant-descriptions-item-content"]//input').send_keys(self.name)
        # 输入客保客户信息
        time.sleep(1)
        self.driver.find_elements_by_xpath('//div[@class="ant-modal-footer"]/button')[1].click()
        # 点击确定
        WebDriverWait(self.driver, 10, 0.5).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//span[@class="ant-upload"]'))
        )
        # 等待弹框出现
        # 进行必填输入
        # 先添加图片减少加载时间
        pic = self.driver.find_element_by_xpath('//span[@class="ant-upload"]')
        clipboard.copy(self.pic_name)
        ActionChains(self.driver).click(pic).perform()
        time.sleep(2)
        # 上传营业执照
        kb = Controller()
        # 实例化控制键盘
        with kb.pressed(
                Key.ctrl,
                'v'
        ):
            pass
        # 摁下黏贴
        # time.sleep(1)
        with kb.pressed(Key.enter):
            pass
        # 摁下回车,上传文件成功

        self.driver.find_element_by_xpath('//input[@id="operational_industry_id"]').click()
        # 点击二级行业
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//div[@label="综合医院"]').click()
        # 所属行业选择综合医院
        self.driver.find_element_by_xpath('//input[@id="province_id"]').click()
        # 点击省份
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@label="北京"]').click()
        # 选择北京
        self.driver.find_element_by_xpath('//input[@id="city_id"]').click()
        # 点击省份
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@label="北京市"]').click()
        # 选择北京
        self.driver.find_element_by_xpath('//input[@id="address"]').send_keys('公司地址')
        # 在公司地址输入
        self.driver.find_element_by_xpath('//input[@id="contactName"]').send_keys('运营专用')
        self.driver.find_element_by_xpath('//input[@id="contactPhone"]').send_keys('17300000006')
        self.driver.find_element_by_xpath('//input[@id="email"]').send_keys('815@qq.com')

        WebDriverWait(self.driver, 10, 0.5).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//img[@class="ant-image-img"]'))
        )
        # 等待图片加载成功
        time.sleep(1)
        print('11111111111111111')
        self.driver.find_elements_by_xpath('//div[@class="ant-modal-footer"]/button')[1].click()
        WebDriverWait(self.driver, 10, 0.5).until_not(
            EC.visibility_of_element_located(
                (By.XPATH, '//img[@class="ant-image-img"]'))
        )

    def replenish_info(self):
        """
        完善企业信息
        :return:
        """
        self.add_custmoer_name()
        time.sleep(2)
        # self.driver.find_element_by_link_text('客户管理').click()
        # 跳转到客户管理
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//tbody[@class="ant-table-tbody"]/tr[2]/td[3]/a').click()
        # 进入完善企业信息页面
        time.sleep(1)
        self.driver.find_element_by_xpath('//input[@id="name"]').send_keys(self.name)
        time.sleep(1)
        self.driver.find_element_by_xpath('//span[@class="ant-pro-select-item-option-content-light"]').click()
        # 选择刚才创建的客户法定名称
        WebDriverWait(self.driver, 10, 0.5).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//img[@class="ant-image-img"]'))
        )
        # 等待图片加载成功
        self.driver.find_elements_by_xpath('//div[@class="ant-modal-footer"]/button')[1].click()
        WebDriverWait(self.driver, 10, 0.5).until_not(
            EC.visibility_of_element_located(
                (By.XPATH, '//img[@class="ant-image-img"]'))
        )
        # 等待弹窗关闭(等待图片消失)

    def customer_summary(self):
        """
        客户成功小结
        :return:
        """
        self.replenish_info()
        # self.login()
        self.driver.implicitly_wait(5)
        self.driver.refresh()
        # 页面刷新
        # self.driver.find_element_by_link_text('客户管理').click()
        time.sleep(5)
        # 隐式等待5s
        self.driver.find_element_by_xpath('//tbody[@class="ant-table-tbody"]/tr[2]/td[last()]').click()
        time.sleep(1)
        self.driver.find_elements_by_xpath('//span[@class="ant-dropdown-menu-title-content"]')[0].click()
        # 点击新价提单
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//input[@id="customer_address"]').send_keys('地址')
        # 客户地址输入
        self.driver.find_elements_by_xpath('//input[@class="ant-input"]')[4].send_keys('职位')
        # 联系人的职位
        self.driver.find_element_by_xpath('//textarea[@id="dep_num"]').send_keys('使用人员规模')
        # 使用人员规模
        self.driver.find_element_by_xpath('//textarea[@id="buy_reason"]').send_keys('客户需求及购买软件目的')
        # 客户需求及购买软件目的
        self.driver.find_element_by_xpath('//textarea[@id="problems"]').send_keys('客户当前业务潜在痛点/阻力')
        # 客户当前业务潜在痛点/阻力
        self.driver.find_element_by_xpath('//textarea[@id="business_process"]').send_keys('客户的业务流程及拓客方式')
        # 客户的业务流程及拓客方式
        self.driver.find_element_by_xpath('//textarea[@id="target_people"]').send_keys('客户目标群体')
        # 客户目标群体
        self.driver.find_element_by_xpath('//textarea[@id="special_note"]').send_keys('特别说明')
        # 特别说明
        self.driver.find_elements_by_xpath('//div[@class="ant-modal-footer"]/button')[1].click()

        WebDriverWait(self.driver, 10, 0.5).until_not(
            EC.visibility_of_element_located(
                (By.XPATH, '//textarea[@id="special_note"]'))
        )
        # 等待弹窗关闭(等待特别说明消失)

    def bill_of_lading(self, x=0):
        """
        提单
        默认为正常提单，无需业务审批
        X=1时，需要业务审批
        :return:
        """
        if x == 0 or x == 1:
            self.customer_summary()
            self.driver.implicitly_wait(5)
            self.driver.refresh()
            time.sleep(3)

            pic = self.driver.find_elements_by_xpath("//button[@class='ant-btn ant-btn-default']")[0]
            clipboard.copy(self.pic_name)
            print(self.pic_name)

            js = "var q=document.documentElement.scrollTop=10000"  # documentElement表示获取根节点元素
            self.driver.execute_script(js)  # 定位到页面底部
            time.sleep(3)

            ActionChains(self.driver).click(pic).perform()

            time.sleep(2)
            # 上传营业执照
            kb = Controller()
            # 实例化控制键盘

            with kb.pressed(
                    Key.ctrl,
                    'v'
            ):
                pass
            # 摁下黏贴
            time.sleep(1)
            with kb.pressed(Key.enter):
                pass
            # 摁下回车,上传文件成功

            contract_type = self.driver.find_element_by_xpath('//input[@id="base_contract_type"]')
            ActionChains(self.driver).move_to_element(contract_type).perform()
            contract_type.click()
            self.driver.implicitly_wait(5)
            self.driver.find_elements_by_xpath('//div[@class="rc-virtual-list-holder-inner"]/div')[x].click()
            # 选择非正常合同  除0外都是非正常合同
            WebDriverWait(self.driver, 10, 0.5).until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//div[@class="ant-upload-list-item-info"]'))
            )
            # 等待图片加载成功
            self.driver.find_elements_by_xpath('//div[@class="ant-pro-footer-bar"]//button')[1].click()
            # 点击下一步
            if x == 1:
                self.driver.implicitly_wait(5)
                self.driver.find_element_by_xpath('//textarea[@id="approveForm_reason"]').send_keys('申请原因')
                # 输入申请原因
                self.driver.find_elements_by_xpath('//div[@class="ant-pro-footer-bar"]//button')[1].click()
                # 点击下一步
                time.sleep(10)
                self.driver.quit()


if __name__ == '__main__':
    comn = Comn(pic_name="D:\Alan_Files\Kefu_Approval\pic\\1111111111111111111111111.png")
    # comn.register_crm()
    # comn.add_custmoer_name()
    # comn.replenish_info()
    # comn.customer_summary()
    comn.bill_of_lading(x=1)
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary  
# from selenium.webdriver.common.action_chains import ActionChains #模拟键盘鼠标输入

def wait(seconds):
    time.sleep(seconds)
class terminal_test(unittest.TestCase):#���Ի���Ϊϵͳ�����нڵ�
    @classmethod
    def setUpClass(cls):
        print(u"虚拟桌面管理测试开始")
    @classmethod
    def tearDownClass(cls):
        print(u"虚拟桌面管理测试")
    def setUp(self):
        #
        binary = FirefoxBinary(r"C:\Program Files\Mozilla Firefox\firefox.exe")
        self.driver = webdriver.Firefox(firefox_binary=binary)
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30) #智能等待30s 
        self.driver.maximize_window()
        self.driver.get("http://192.168.20.215/dashboard")
        self.driver.find_element_by_id('id_username').send_keys('admin')
        self.driver.find_element_by_id('id_password').send_keys('123qwe') 
        self.driver.find_element_by_id('loginBtn').click()
        locator=(By.XPATH,"/html/body/div[1]/div[1]/div/ul/li[2]/a" )
        WebDriverWait(self.driver,20,0.5).until(EC.presence_of_element_located(locator))
        #创建虚拟机备用
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/ul/li[2]/a").click()
        wait(1)
        locator=(By.ID,"instances__action_launch")
        WebDriverWait(self.driver,60,0.5).until(EC.visibility_of_element_located(locator))
        self.driver.find_element_by_id("instances__action_launch").click()
        wait(5)
        self.driver.find_element_by_id("id_name").send_keys("Auto-Test-for-terminal")
        self.driver.find_element_by_id("id_count").clear()
        self.driver.find_element_by_id("id_count").send_keys("2")
        self.driver.find_element_by_id("id_image_id").send_keys(Keys.ARROW_DOWN)
        self.driver.find_element_by_xpath(".//a[@href='#launch_instance__setnetworkaction']").click()
        items=self.driver.find_elements_by_xpath(".//input[@name='network']")
        if len(items)>1:
            for item in items:
                item.click()
                item.click()
            items[0].click()
        self.driver.find_element_by_xpath("/html/body/div[3]/div/form/div/div/div[3]/input").click()
        wait(3)
        locator=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr[1]/td[8]")
        WebDriverWait(self.driver,300,0,5).until(EC.text_to_be_present_in_element(locator,U'无'))
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/ul/li[3]/a").click()
        wait(5)

          
    def tearDown(self): 
        driver=self.driver
        #删除创建的虚拟机
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/ul/li[2]/a").click()
        wait(5)
        driver.find_element_by_xpath("//input[@class='table-row-multi-select']").click()
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/thead/tr[1]/th/div/div[2]/a").click()
        wait(3)
        driver.find_element_by_id("instances__action_terminate").click()
        wait(1)    
        driver.find_element_by_xpath(".//a[@class='btn btn-primary btn-danger']").click()
        url= driver.current_url    
        while url != "http://192.168.20.215/dashboard/instances_manager/trash":
            driver.find_element_by_id("instances__action_trash").click()
            wait(5)
            url= driver.current_url
        wait(3)
        driver.refresh()
        wait(10)
        locator=(By.XPATH,".//input[@class='table-row-multi-select']")
        WebDriverWait(driver,30,0.5).until(EC.element_to_be_clickable(locator))
        driver.find_element_by_xpath(".//input[@class='table-row-multi-select']").click()
        driver.find_element_by_id("trash__action_trashinstance").click()
        wait(1)
        driver.find_element_by_xpath(".//a[@class='btn btn-primary btn-danger']").click()
        wait(10) 
        self.driver.quit()
    def test_terminal(self):
        driver=self.driver
         
        #创建节点
        driver.find_element_by_xpath(".//li[@data-nodeid]").click()
        wait(3)
        driver.find_element_by_id("tree_add").click()
        wait(3)
        driver.find_element_by_id("tree_node_edit").send_keys("Auto-Test-1")
        driver.find_element_by_xpath(".//input[@name='radio_node']").click()
        driver.find_element_by_id("button_add").click()
        wait(5)
           
        driver.find_element_by_id("tree_add").click()
        driver.find_element_by_id("tree_node_edit").send_keys("Auto-Test-1.1")
        driver.find_element_by_xpath(".//input[@value='add_chlid']").click()
        driver.find_element_by_id("button_add").click()
        wait(5)
           
        driver.find_element_by_xpath(".//li[@data-nodeid]").click()
        wait(3)
        driver.find_element_by_id("tree_add").click()
        wait(3)
        driver.find_element_by_id("tree_node_edit").send_keys("Auto-Test-2")
        driver.find_element_by_xpath(".//input[@value='add_brother']").click() 
        driver.find_element_by_id("button_add").click()
        wait(5)
        #创建终端用户
        driver.find_element_by_xpath(".//li[@data-nodeid]").click()
        wait(1)
        driver.find_element_by_xpath(".//li[@data-nodeid='1']").click()
        wait(1)
        driver.find_element_by_id("user vm__action_create").click()
        wait(3)
        driver.find_element_by_id("id_user").clear()
        driver.find_element_by_id("id_user").send_keys("Auto-Test")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys('1')
        driver.find_element_by_id("id_confirm_password").clear()
        driver.find_element_by_id("id_confirm_password").send_keys('1')
          
        driver.find_element_by_xpath(".//a[@data-target='#create_terminal_user__select_instances']").click()
        driver.find_element_by_xpath(".//a[@href='#add_remove']").click()
        driver.find_element_by_xpath(".//a[@href='#add_remove']").submit()
        wait(5)
        #编辑终端用户
        driver.find_element_by_id("user vm__row_1__action_edit").click()
        wait(3)
        driver.find_element_by_id("id_pic_quality").send_keys(Keys.ARROW_DOWN)
        driver.find_element_by_id("id_identy_info").send_keys(Keys.ARROW_DOWN)
        driver.find_element_by_id("id_identy_info").submit()
        wait(5)
        #下拉菜单
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[5]/div/div/div[2]/form/table/tbody/tr/td[7]/div/a[2]").click()
        wait(1)
        #添加虚拟机
        driver.find_element_by_id("user vm__row_1__action_add").click()
        wait(2)
        driver.find_element_by_xpath(".//a[@data-target='#add_vm__select_instances']").click()
        driver.find_element_by_xpath(".//a[@href='#add_remove']").click()
        driver.find_element_by_xpath(".//a[@href='#add_remove']").submit()
        wait(3)
        #修改密码
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[5]/div/div/div[2]/form/table/tbody/tr/td[7]/div/a[2]").click()
        wait(1)
        driver.find_element_by_id("user vm__row_1__action_update").click()
        wait(2)
        driver.find_element_by_id("id_user").clear()
        driver.find_element_by_id("id_user").send_keys("Edit")
        driver.find_element_by_id("id_password").send_keys("1")
        driver.find_element_by_id("id_confirm_password").send_keys("1")
        driver.find_element_by_id("id_confirm_password").submit()
        wait(3)
        #禁用/激活用户
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[5]/div/div/div[2]/form/table/tbody/tr/td[7]/div/a[2]").click()
        wait(1)
        driver.find_element_by_id("user vm__row_1__action_toggle").click()
        wait(2)
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[5]/div/div/div[2]/form/table/tbody/tr/td[7]/div/a[2]").click()
        wait(1)
        driver.find_element_by_id("user vm__row_1__action_toggle").click()
        wait(5)
        #删除虚拟机
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[5]/div/div/div[2]/form/table/tbody/tr/td[7]/div/a[2]").click()
        wait(1)
        driver.find_element_by_id("user vm__row_1__action_delete user vm").click()
        wait(3)
        driver.find_element_by_xpath(".//a[@href='#add_remove']").click()
        driver.find_element_by_xpath(".//a[@href='#add_remove']").submit()
        wait(5)
        #删除终端用户
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[5]/div/div/div[2]/form/table/tbody/tr/td[7]/div/a[2]").click()
        wait(1)
        driver.find_element_by_id("user vm__row_1__action_delete").click()
        wait(2)
        driver.find_element_by_link_text(u"删除终端用户")
        wait(2)
        driver.find_element_by_xpath(".//a[@class='btn btn-primary btn-danger']").click()
        wait(3)
        #删除节点
        driver.find_element_by_xpath(".//li[@data-nodeid='2']").click()
        wait(2)
        driver.find_element_by_id("tree_delete").click()
        wait(3)   
        elem=driver.switch_to_alert() 
        elem.accept() # elem.dismiss 
        wait(5)
   
        driver.find_element_by_xpath(".//li[@data-nodeid='0']").click()
        wait(2)
        driver.find_element_by_xpath(".//li[@data-nodeid='1']").click()
        wait(2)
        driver.find_element_by_id("tree_delete").click()
        wait(3)
        elem=driver.switch_to_alert() #获取对话框对象
        elem.accept() #点击确认  elem.dismiss 是点击取消
        wait(5)
        
        driver.find_element_by_id("tree_delete").click()
        wait(3)
        elem=driver.switch_to_alert() #获取对话框对象
        elem.accept() #点击确认  elem.dismiss 是点击取消
        wait(5)
        
    
        
    
if __name__ == "__main__":
    unittest.main()
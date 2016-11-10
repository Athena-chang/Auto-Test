# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.common.keys import Keys   
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary 
# from selenium.common.exceptions import TimeoutException
def wait(seconds):
    time.sleep(seconds)
class instance_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(u"虚拟机管理测试开始")
    @classmethod
    def tearDownClass(cls):
        print(u"虚拟机管理测试结束")
    def setUp(self):
        #完成登录
        binary = FirefoxBinary(r"C:\Program Files\Mozilla Firefox\firefox.exe")
        self.driver = webdriver.Firefox(firefox_binary=binary)
        self.driver.implicitly_wait(30) # 隐性等待，最长等30秒
        self.driver.maximize_window()
        self.driver.get("http://192.168.20.215/dashboard")
        self.driver.find_element_by_id('id_username').send_keys('admin')
        self.driver.find_element_by_id('id_password').send_keys('123qwe') 
        self.driver.find_element_by_id('loginBtn').click()
        wait(5)
    def tearDown(self):        
        self.driver.quit()
      
#     @unittest.skip("test")
    def test_instances(self):
        print("test_instances begin")
        driver=self.driver
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/ul/li[2]/a").click()
        wait(3)
        
        #创建虚拟机    
        driver.find_element_by_id("instances__action_launch").click()
        wait(5)
        driver.find_element_by_id("id_name").send_keys("Auto-Test")
        driver.find_element_by_id("id_count").clear()
        driver.find_element_by_id("id_count").send_keys("2")
        driver.find_element_by_id("id_image_id").send_keys(Keys.ARROW_DOWN)
        driver.find_element_by_xpath(".//a[@href='#launch_instance__setnetworkaction']").click()
        items=driver.find_elements_by_xpath(".//input[@name='network']")
        if len(items)>1:
            for item in items:
                item.click()
                item.click()
            items[0].click()
        driver.find_element_by_xpath("/html/body/div[3]/div/form/div/div/div[3]/input").click()
        wait(3)
        locator=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr[1]/td[8]")
        WebDriverWait(driver,300,0,5).until(EC.text_to_be_present_in_element(locator,U'无'))
        wait(3)   
        #编辑虚拟机
        driver.find_element_by_xpath(u".//a[@title='编辑虚拟机']").click()
        wait(1)
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id('id_name').send_keys('Auto-Test-3')
        driver.find_element_by_id('id_name').submit()
        wait(5)
        #删除虚拟机
        driver.find_element_by_xpath(u".//button[@title='删除虚拟机' and @class='btn btn-default btn-sm btn-danger btn-confirm']").click()
        wait(3)
        driver.find_element_by_xpath(".//a[@class='btn btn-primary btn-danger']").click()
        wait(5)
                    
        #下拉菜单
        locator=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr/td[9]")
                    
        try:
            WebDriverWait(driver,300,0.5).until(EC.text_to_be_present_in_element(locator,u'运行中'))
            driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr/td[10]/div/a[2]").click()
        finally:
            wait(1)
        #虚拟机备份       
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr/td[10]/div/ul/li[3]/a").click()
        wait(3) 
        driver.find_element_by_id("id_name").send_keys("Auto-Test")
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div/form/div[2]/input").click()
        wait(5)    
        #定时备份    
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr/td[10]/div/a[2]").click()
        wait(3)    
        driver.find_element_by_xpath(".//ul[@class='dropdown-menu row_actions dropdown-menu-right clearfix']/li[4]").click()
        driver.find_element_by_id("id_Intervals").clear()
        driver.find_element_by_id("id_Intervals").send_keys("1")
        driver.find_element_by_id("id_Hours").clear()
        driver.find_element_by_id("id_Hours").send_keys("18")
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div/form/div[2]/input").click() 
        wait(5)
        #取消定时备份
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr/td[10]/div/a[2]").click()
        wait(3)
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr[1]/td[10]/div/ul/li[5]/button").click()
        wait(5) 
        #调整大小  
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr/td[10]/div/a[2]").click()
        wait(3)
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr/td[10]/div/ul/li[5]/a").click()
        driver.find_element_by_id("id_flavor").click()
        driver.find_element_by_xpath(".//option[@value='2']").click()
        driver.find_element_by_xpath("/html/body/div[3]/div/form/div/div/div[3]/input").click()
        driver.find_element_by_xpath("//a[@class='btn btn-default btn-sm dropdown-toggle']").click()
                    
        locator = (By.XPATH,'/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr/td[10]/div/ul/li[1]/button')
        try:
            WebDriverWait(driver,300,0.5).until(EC.presence_of_element_located(locator))  
            driver.find_element_by_xpath("//a[@class='btn btn-default btn-sm dropdown-toggle']").click()
            driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr/td[10]/div/ul/li[1]/button').click()
        finally:  
            driver.refresh()
            wait(10)
                
        #制作模板
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr/td[10]/div/a[2]").click()
        wait(3)
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr/td[10]/div/ul/li[6]/a").click()
        wait(3)
        driver.find_element_by_id("id_name").send_keys("Auto-Test")
        driver.find_element_by_id("id_description_label").send_keys("Auto-Test")
        driver.find_element_by_id("id_description_label").submit()
        locator=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr[1]/td[5]")
        WebDriverWait(driver,20,0.5).until(EC.text_to_be_present_in_element(locator,u'运行中'))
        wait(1)
        #删除掉模板
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr[1]/td[9]/div/a[2]").click()
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr[1]/td[9]/div/ul/li[2]/button").click()
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[3]/a[1]").click()
        wait(5)
                                   
                    
        #回到虚拟机界面
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/ul/li[2]/a").click()
                     
        #关闭虚拟机
        wait(3)
        driver.find_element_by_xpath(".//button[@class='btn btn-default btn-sm stop_instance']").click()    
        #添加IP（自动）
        locator=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr/td[9]")
        try:
            WebDriverWait(driver,60,0.5).until(EC.text_to_be_present_in_element(locator, u"关闭"))
            driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr/td[10]/div/a[2]").click()
        finally:
            wait(2) 
                              
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr/td[10]/div/ul/li[4]/a").click()
        items=driver.find_elements_by_xpath(".//input[@name='network']")
        if len(items)>1:
            for item in items:
                item.click()
                item.click()
            items[0].click()
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div/form/div[2]/input").click()
        wait(5)
                 
        #删除IP
        locator=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr/td[10]/div/ul/li[5]/a")
        try:        
            driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr/td[10]/div/a[2]").click()
            wait(3)
            WebDriverWait(driver,60,0.5).until(EC.visibility_of_element_located(locator)) 
            driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr/td[10]/div/ul/li[5]/a").click()
        finally:
            wait(3)
        m=driver.find_element_by_id("id_method")
        m.find_element_by_xpath("./option[2]").click()
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div/form/div[2]/input").click()
        wait(5)
                   
        #修改IP
        locator=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr/td[10]/div/ul/li[5]/a")
        try:
            WebDriverWait(driver,60,0.5).until(EC.presence_of_element_located(locator))      
            driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr/td[10]/div/a[2]").click()
        finally:
            wait(3)
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr/td[10]/div/ul/li[5]/a").click()
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div/form/div[2]/input").click()
        wait(5)    
                 
        #开机启动/监听虚拟机
        items=driver.find_elements_by_xpath("//input[@class='table-row-multi-select']")
        while len(items)<2:
            items=driver.find_elements_by_xpath("//input[@class='table-row-multi-select']")
            wait(1)
        items[1].click()
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/thead/tr[1]/th/div/div[2]/a").click()
        driver.find_element_by_id("instances__action_Boot").click()
        wait(5)
                   
        items=driver.find_elements_by_xpath("//input[@class='table-row-multi-select']")
        items[1].click()
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/thead/tr[1]/th/div/div[2]/a").click()
        driver.find_element_by_id("instances__action_CancelBoot").click()
        wait(5)
             
        items=driver.find_elements_by_xpath("//input[@class='table-row-multi-select']")
        items[1].click()       
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/thead/tr[1]/th/div/div[2]/a").click()
        driver.find_element_by_id("instances__action_Filter").click()
        wait(5)
            
        items=driver.find_elements_by_xpath("//input[@class='table-row-multi-select']")
        items[1].click()        
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/thead/tr[1]/th/div/div[2]/a").click()
        driver.find_element_by_id("instances__action_CancelFilter").click()
        wait(5)
                
        #重启/强制重启
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr/td[10]/div/button[1]").click()#先启动
        wait(5)
        items=driver.find_elements_by_xpath("//input[@class='table-row-multi-select']")
        items[1].click()
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/thead/tr[1]/th/div/div[2]/a").click()    
        driver.find_element_by_id("instances__action_soft_reboot").click()
        locator=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr/td[8]")
        wait(3)
        try:
            WebDriverWait(driver,300,2).until(EC.text_to_be_present_in_element(locator,u'无'))
            items=driver.find_elements_by_xpath("//input[@class='table-row-multi-select']")
            items[1].click()
            driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/thead/tr[1]/th/div/div[2]/a").click()
            wait(1)
            driver.find_element_by_id("instances__action_reboot").click()
        finally:
            wait(1)
        driver.find_element_by_xpath(".//a[@class='btn btn-primary btn-danger']").click()
        wait(3)
        locator=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr/td[8]")
        try:
            WebDriverWait(driver,300,2).until(EC.text_to_be_present_in_element(locator,u'无'))
        finally:
            wait(5)
        #批量删除（包含回收站）
            
        items=driver.find_elements_by_xpath("//input[@class='table-row-multi-select']")
        items[1].click()
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
        print ("test_instances end")
       
#     @unittest.skip("test")
    def test_flaver(self):
        print("test_flaver begin")
        driver=self.driver
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/ul/li[2]/a").click()
        wait(3)
        driver.find_element_by_xpath(".//a[@tabindex='2']").click()
        wait(2)
        #创建配置(2个）
        driver.find_element_by_xpath(".//a[@title='创建虚拟机配置']").click()
        wait(1)
        items=driver.find_elements_by_xpath(".//div[@class='form-group required']")
        items=items[1:]        
        for item in items:
            item.click()
            item.send_keys(Keys.ARROW_UP)
            item.send_keys(Keys.ARROW_UP)
            item.send_keys(Keys.ARROW_DOWN)
        driver.find_element_by_id("id_name").send_keys('Auto-Test-1')        
        driver.find_element_by_id("id_name").submit()
        wait(5)
        driver.find_element_by_xpath(".//a[@title='创建虚拟机配置']").click()
        wait(1)
        items=driver.find_elements_by_xpath(".//div[@class='form-group required']")
        items=items[1:]        
        for item in items:
            item.click()
            item.send_keys(Keys.ARROW_UP)
            item.send_keys(Keys.ARROW_UP)
            item.send_keys(Keys.ARROW_DOWN)
        driver.find_element_by_id("id_name").send_keys('Auto-Test-2')        
        driver.find_element_by_id("id_name").submit()
        wait(5)
        #编辑配置
        items=driver.find_elements_by_xpath(".//a[@title='编辑虚拟机配置']")
        items[1].click()
        items=driver.find_elements_by_xpath(".//div[@class='form-group required']")
        items=items[1:]
        for item in items:
            item.click()
            item.send_keys(Keys.ARROW_UP)
            item.send_keys(Keys.ARROW_DOWN)
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys('Auto-Test-3')
        driver.find_element_by_id("id_name").submit()
        wait(5)
        #删除配置
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr[2]/td[7]/div/a[2]").click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr[2]/td[7]/div/ul/li/button').click()
        driver.find_element_by_xpath(".//a[@class='btn btn-primary btn-danger']").click()
        wait(3)
        #测试选择框
        items=driver.find_elements_by_xpath(".//input[@class='table-row-multi-select']")
        for item in items:
            item.click()
            wait(0.5)
            item.click()    
        #删除
        items[2].click()
        driver.find_element_by_xpath(".//button").click()
        driver.find_element_by_xpath(".//a[@class='btn btn-primary btn-danger']").click()
        wait(10)
        print("test_flaver end")
         
    @unittest.skip("test")   
    def test_volumes(self):
        print("test_volumes begin")
        driver=self.driver
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/ul/li[2]/a").click()
        wait(3)
  
        #创建虚拟机备用
        driver.find_element_by_id("instances__action_launch").click()
        wait(3)
        driver.find_element_by_id("id_name").send_keys("Auto-Test-for-volumes")
        driver.find_element_by_id("id_image_id").send_keys(Keys.ARROW_DOWN)
        driver.find_element_by_xpath(".//a[@href='#launch_instance__setnetworkaction']").click()
        items=driver.find_elements_by_xpath(".//input[@name='network']")
        if len(items)>1:
            for item in items:
                item.click()
                item.click()
            items[0].click()
        driver.find_element_by_xpath("/html/body/div[3]/div/form/div/div/div[3]/input").click()
        wait(3)
          
        driver.find_element_by_xpath(".//a[@tabindex='3']").click()
        wait(3)
           
        #创建虚拟机硬盘 (两个）
        driver.find_element_by_id("volumes__action_create").click()
        wait(1)
        driver.find_element_by_id("id_name").send_keys("Auto-Test-1")
        driver.find_element_by_id("id_description").send_keys("Auto-Test-1")
        driver.find_element_by_id("id_size").send_keys(Keys.ARROW_UP)
        driver.find_element_by_id("id_size").send_keys(Keys.ARROW_DOWN)
        driver.find_element_by_id("id_size").submit()
        locator=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/div/div[1]/div/form/table/tbody/tr[1]/td[2]/a")
        WebDriverWait(driver,20,0.5).until(EC.text_to_be_present_in_element(locator,'Auto-Test-1'))
        wait(1)
          
        driver.find_element_by_id("volumes__action_create").click()
        wait(1)
        driver.find_element_by_id("id_name").send_keys("Auto-Test-2")
        driver.find_element_by_id("id_description").send_keys("Auto-Test-2")
        driver.find_element_by_id("id_size").send_keys(Keys.ARROW_UP)
        driver.find_element_by_id("id_size").send_keys(Keys.ARROW_DOWN)
        driver.find_element_by_id("id_size").submit()
        locator=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/div/div[1]/div/form/table/tbody/tr[1]/td[2]/a")
        WebDriverWait(driver,20,0.5).until(EC.text_to_be_present_in_element(locator,'Auto-Test-2'))
        wait(1)
          
        #删除卷 
        driver.find_element_by_xpath(".//input[@class='table-row-multi-select' and @name='object_ids']").click()
        driver.find_element_by_id("volumes__action_delete").click()
        wait(1)
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[3]/a[1]").click()
        wait(1)
        locator=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/div/div[1]/div/form/table/tbody/tr/td[5]")
        WebDriverWait(driver,30,0.5).until(EC.text_to_be_present_in_element(locator,u'可用配额'))
        wait(1)
        #编辑卷
        driver.find_element_by_xpath(".//a[@title='编辑卷']").click()
        wait(1)
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys("Auto-Test-3")
        driver.find_element_by_id("id_description").send_keys("Auto-Test-3")
        driver.find_element_by_id('id_bootable').click()
        driver.find_element_by_id('id_bootable').click()
        driver.find_element_by_id("id_description").submit()
        wait(10)
            
        #下拉菜单
        driver.find_element_by_xpath(".//a[@class='btn btn-default btn-sm dropdown-toggle']").click()
        wait(1)
        #扩展硬盘
        driver.find_element_by_xpath(u".//a[@title='扩展虚拟机硬盘']").click()
        wait(2)
        driver.find_element_by_id("id_new_size").send_keys(Keys.ARROW_UP)
        driver.find_element_by_id("id_new_size").send_keys(Keys.ARROW_UP)
        driver.find_element_by_id("id_new_size").submit()
        wait(3)
        #管理挂载 
        driver.find_element_by_xpath(".//a[@class='btn btn-default btn-sm dropdown-toggle']").click()
        wait(1)
        driver.find_element_by_xpath(u".//a[@title='管理挂载']").click()
        wait(1)
        driver.find_element_by_id("id_fuzzy_select").click()
#         driver.find_element_by_link_text("Auto-Test-for-volumes").click()
        driver.find_element_by_xpath(".//a[@onclick]").click()
        driver.find_element_by_id("id_fuzzy_select").submit()
        wait(1)
        locator=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/div/div[1]/div/form/table/tbody/tr/td[5]")
        WebDriverWait(driver,30,0.5).until(EC.text_to_be_present_in_element(locator,u'正在使用'))
            
        driver.find_element_by_xpath(".//a[@class='btn btn-default btn-sm dropdown-toggle']").click()
        wait(1)
        driver.find_element_by_xpath(u".//a[@title='管理挂载']").click()
        wait(2)
        driver.find_element_by_xpath(".//button[@class='btn btn-default btn-sm btn-danger btn-detach']").click()
        wait(3)
        driver.find_element_by_link_text(u"卸载虚拟机硬盘").click()
        wait(1)
        locator=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/div/div[1]/div/form/table/tbody/tr/td[5]")
        WebDriverWait(driver,30,0.5).until(EC.text_to_be_present_in_element(locator,u'可用配额'))
        wait(3)
        #创建快照
        driver.find_element_by_xpath(".//a[@class='btn btn-default btn-sm dropdown-toggle']").click()
        wait(1)
        driver.find_element_by_xpath(u".//a[@title='创建快照']").click()
        wait(2)
        driver.find_element_by_id("id_name").send_keys("Auto-Test-1")
        driver.find_element_by_id("id_description").send_keys("Auto-Test-1")
        driver.find_element_by_id("id_description").submit()
        wait(5)
        #编辑快照
        driver.find_element_by_xpath(".//a[@href='?tab=volumes_and_snapshots__snapshots_tab']").click()
        wait(2)
        driver.find_element_by_xpath(u".//a[@title='编辑快照']").click()
        wait(1)
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys("Auto-edit-volumes")
        driver.find_element_by_id("id_description").clear()
        driver.find_element_by_id("id_description").send_keys("Auto-edit-volumes")
        driver.find_element_by_id("id_description").submit()
        wait(5)
        #恢复快照
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/div/div[2]/div/form/table/tbody/tr/td[7]/div/a[2]").click()
        driver.find_element_by_xpath(".//button[@title='恢复卷快照']").click()
        wait(1)
        driver.find_element_by_link_text(u'恢复卷快照').click()
        wait(5)
        #再次创建快照
        driver.find_element_by_xpath(".//a[@href='?tab=volumes_and_snapshots__volumes_tab']").click()
        wait(2)
        driver.find_element_by_xpath(".//a[@class='btn btn-default btn-sm dropdown-toggle']").click()
        wait(1)
        driver.find_element_by_xpath(u".//a[@title='创建快照']").click()
        wait(2)
        driver.find_element_by_id("id_name").send_keys("Auto-Test-2")
        driver.find_element_by_id("id_description").send_keys("Auto-Test-2")
        driver.find_element_by_id("id_description").submit()
        wait(5)
        driver.find_element_by_xpath(".//a[@href='?tab=volumes_and_snapshots__volumes_tab']").click()
        driver.find_element_by_xpath(".//a[@class='btn btn-default btn-sm dropdown-toggle']").click()
        wait(1)
        driver.find_element_by_xpath(u".//a[@title='创建快照']").click()
        wait(2)
        driver.find_element_by_id("id_name").send_keys("Auto-Test-3")
        driver.find_element_by_id("id_description").send_keys("Auto-Test-3")
        driver.find_element_by_id("id_description").submit()
        wait(5)
            
        #删除快照
        driver.find_element_by_xpath(".//a[@href='?tab=volumes_and_snapshots__snapshots_tab']").click()
        wait(2)
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/div/div[2]/div/form/table/tbody/tr/td[7]/div/a[2]").click()
        wait(3)
        items=driver.find_elements_by_xpath(u".//button[@title='删除卷快照']")
        items[1].click()
        wait(2)
        driver.find_element_by_link_text(u"删除卷快照").click()
        locator=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/div/div[2]/div/form/table/tbody/tr/td[5]")
        wait(1)
        WebDriverWait(driver,30,0.5).until_not(EC.text_to_be_present_in_element(locator,u'删除中'))   
        wait(3) 
  
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/div/div[2]/div/form/table/thead/tr[2]/th[1]/input").click()
        driver.find_element_by_id("volume_snapshots__action_delete").click()
        wait(3)
        driver.find_element_by_link_text(u"删除卷快照").click()
        locator=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/div/div[2]/div/form/table/tbody/tr/td")
        wait(1)
        WebDriverWait(driver,30,0.5).until(EC.text_to_be_present_in_element(locator,u'没有条目显示'))
          
        #删除卷
        driver.find_element_by_xpath(".//a[@href='?tab=volumes_and_snapshots__volumes_tab']").click()
        wait(2)
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/div/div[1]/div/form/table/thead/tr[2]/th[1]/input").click()
        driver.find_element_by_xpath(".//button[@value='volumes__delete']").click()
        driver.find_element_by_xpath(".//a[@class='btn btn-primary btn-danger']").click()
        print("test_volumes end")
        wait(5)
          
#     @unittest.skip("test")   
    def test_image(self):
        print("test_image begin")
        driver=self.driver
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/ul/li[2]/a").click()
        wait(3)
        driver.set_window_size(1000,800)
        wait(5)
        driver.find_element_by_xpath(".//a[@tabindex='4']").click()
        driver.maximize_window()
        wait(5)
        #创建模板
        driver.find_element_by_id("images__action_create").click()
        items=driver.find_elements_by_xpath(".//input[@class='form-control']")
        for item in items:
            item.send_keys('Auto-Test-1')
        driver.find_element_by_id("id_source_type").click()
        driver.find_element_by_xpath(".//option[@value='url']").click()
        driver.find_element_by_id("id_image_url").send_keys("http://192.168.20.8/Software/SystemImage/openstack-images/cirros")
        driver.find_element_by_id("id_disk_format").click()
        driver.find_element_by_xpath(".//option[@value='qcow2']").click()
        driver.find_element_by_id("id_system_format").click()
        driver.find_element_by_xpath(".//option[@value='linux']").click()
        driver.find_element_by_id("id_system_format").submit()
        locator=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr[1]/td[5]")
        WebDriverWait(driver,20,0.5).until(EC.text_to_be_present_in_element(locator,u'运行中'))
        wait(2)
        driver.find_element_by_id("images__action_create").click()
        wait(3)
        items=driver.find_elements_by_xpath(".//input[@class='form-control']")
        for item in items:
            item.send_keys('Auto-Test-2')
        driver.find_element_by_id("id_source_type").click()
        driver.find_element_by_id("id_source_type").send_keys(Keys.ARROW_DOWN)
        driver.find_element_by_id("id_image_file").click()
        driver.find_element_by_id("id_image_file").send_keys(u'C:\\cirros')
        driver.find_element_by_id("id_disk_format").click()
        driver.find_element_by_xpath(".//option[@value='qcow2']").click()
        driver.find_element_by_id("id_system_format").click()
        driver.find_element_by_xpath(".//option[@value='linux']").click()
        driver.find_element_by_id("id_system_format").submit() 
        locator=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr[1]/td[5]")
        WebDriverWait(driver,20,0.5).until(EC.text_to_be_present_in_element(locator,u'运行中'))
        wait(5)
        #创建虚拟机
        driver.find_element_by_xpath(u".//a[@title='创建虚拟机']").click()
        wait(3)
        driver.find_element_by_id("id_name").send_keys("image")
        driver.find_element_by_xpath(".//a[@href='#launch_instance__setnetworkaction']").click()
        items=driver.find_elements_by_xpath(".//input[@name='network']")
        if len(items)>1:
            for item in items:
                item.click()
                item.click()
            items[0].click()
        driver.find_element_by_xpath("/html/body/div[3]/div/form/div/div/div[3]/input").click()
        wait(3)
        driver.find_element_by_xpath(".//a[@tabindex='4']").click()
        wait(5)  
        #编辑模板
        driver.find_element_by_xpath(".//a[@class='btn btn-default btn-sm dropdown-toggle']").click()
        wait(1)
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr[1]/td[9]/div/ul/li[1]/a").click()
        driver.find_element_by_id("id_protected").click()
        items=driver.find_elements_by_xpath(".//input[@class='form-control']")
        for item in items:
            item.clear()
            item.send_keys('Auto-Test-3')
        items=driver.find_elements_by_xpath(".//select")
        for item in items:
            item.click()
            item.send_keys(Keys.ARROW_DOWN)
            item.send_keys(Keys.ARROW_UP)
        driver.find_element_by_id("id_protected").click()
        driver.find_element_by_id("id_name").submit()
        wait(3)
        #检测复选框
        items=driver.find_elements_by_xpath(".//input[@class='table-row-multi-select']")
        for item in items:
            item.click()
            wait(0.5)
            item.click()
        #删除模板   
        items[1].click()
        driver.find_element_by_id("images__action_delete").click()
        driver.find_element_by_xpath(".//a[@class='btn btn-primary btn-danger']").click()
        wait(3)
        driver.find_element_by_xpath(".//a[@class='btn btn-default btn-sm dropdown-toggle']").click()
        wait(2)
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr[1]/td[9]/div/ul/li[2]/button").click()
        wait(2)
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[3]/a[1]").click()
        #删除创建的虚拟机
        driver.find_element_by_xpath(".//a[@tabindex='1']").click()
        wait(3)
        locator=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr/td[8]")
        WebDriverWait(driver,60,0.5).until(EC.text_to_be_present_in_element(locator,u'无'))
        driver.find_element_by_xpath(".//button[@class='btn btn-default btn-sm btn-danger btn-confirm']").click()
        driver.find_element_by_xpath(".//a[@class='btn btn-primary btn-danger']").click()
        wait(3)
        driver.find_element_by_id("instances__action_trash").click() 
#         driver.refresh()
        wait(3)
        driver.find_element_by_xpath(".//input[@class='table-row-multi-select']").click()
        driver.find_element_by_id("trash__action_trashinstance").click()
        wait(1)
        driver.find_element_by_xpath(".//a[@class='btn btn-primary btn-danger']").click()
        print("test_image end")
        wait(5)
          
#     @unittest.skip("test")
    def test_network(self):
        print("test_network begin")
        driver=self.driver
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/ul/li[2]/a").click()
        wait(3)
        driver.find_element_by_xpath(".//a[@tabindex='5']").click()
        wait(2)
          
        #创建网络
        driver.find_element_by_id("networks__action_create").click()
        wait(2)
        driver.find_element_by_id("id_name").send_keys("Auto-Test")
        driver.find_element_by_id("id_name").submit()
           
        #编辑网络
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/form/table/tbody/tr[2]/td[8]/div/a[1]").click()
        wait(2)
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys("Auto-Test-Edit")
        elem=driver.find_element_by_id("id_admin_state")
        elem.send_keys(Keys.ARROW_DOWN)
        elem.send_keys(Keys.ARROW_UP)
        items=driver.find_elements_by_xpath(".//input[@checked]")
        for item in items:
            item.click()
            item.click()
        elem.submit()   
        wait(3)
              
        #点击名称进入详情
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/form/table/tbody/tr[2]/td[2]/a").click()
        wait(3)
          
        #创建子网
        driver.find_element_by_id("subnets__action_create").click()
        wait(3)
        driver.find_element_by_id("id_subnet_name").send_keys("Auto-Test")
        driver.find_element_by_id("id_cidr").send_keys("20.20.20.0/24")
        driver.find_element_by_id("id_gateway_ip").send_keys("20.20.20.1")
        driver.find_element_by_xpath(".//button[@class='btn btn-primary button-next']").click()
        driver.find_element_by_id("id_dns_nameservers").send_keys("192.168.0.1")
        driver.find_element_by_id("id_dns_nameservers").submit()
        wait(3)
           
        #编辑子网
        driver.find_element_by_xpath(".//a[@title='编辑子网']").click()
        driver.find_element_by_id("id_subnet_name").clear()
        driver.find_element_by_id("id_subnet_name").send_keys("Auto-Test_Edit")
        driver.find_element_by_id("id_no_gateway").click()
        driver.find_element_by_xpath(".//button[@class='btn btn-primary button-next']").click()
        driver.find_element_by_id("id_allocation_pools").clear()
        driver.find_element_by_id("id_allocation_pools").send_keys("20.20.20.10,20.20.20.100")
        driver.find_element_by_id("id_dns_nameservers").clear()
        driver.find_element_by_id("id_dns_nameservers").send_keys("192.168.10.1")
        driver.find_element_by_id("id_dns_nameservers").submit()
        wait(3)
        #删除子网
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/div[2]/div/form/table/tbody/tr/td[6]/div/a[2]").click()
        wait(1)
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/div[2]/div/form/table/tbody/tr/td[6]/div/ul/li/button").click()
        wait(2)
        driver.find_element_by_xpath(".//a[@class='btn btn-primary btn-danger']").click()
        wait(3)
          
        #删除网络
        driver.find_element_by_xpath(".//a[@tabindex='5']").click()
        wait(3)
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/form/table/tbody/tr[2]/td[8]/div/a[2]").click()
        wait(1)
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/form/table/tbody/tr[2]/td[8]/div/ul/li/button").click()
        wait(2)
        driver.find_element_by_xpath(".//a[@class='btn btn-primary btn-danger']").click()
        wait(3)
        print("test_network end")
            
#     @unittest.skip("test")
    def test_access_and_security(self):
        print("test_access_and_security begin")  
        driver=self.driver
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/ul/li[2]/a").click()
        wait(3)
        driver.find_element_by_xpath(".//a[@tabindex='6']").click()
        wait(2)    
          
        #创建安全组
        driver.find_element_by_id("security_groups__action_create").click()
        wait(3)
        driver.find_element_by_id("id_name").send_keys("Auto-Test")
        driver.find_element_by_id("id_name").submit()
        wait(3)
        #管理规则
        driver.find_element_by_xpath(u".//a[@title='管理规则']").click()
        wait(3)
        driver.find_element_by_id("rules__action_add_rule").click()
        wait(2)
        driver.find_element_by_id("id_port").send_keys("20")
        driver.find_element_by_id("id_port").submit()
        wait(3)
        driver.find_element_by_xpath(".//input[@type='checkbox']").click()
        driver.find_element_by_id("rules__action_delete").click()
        driver.find_element_by_xpath(".//a[@class='btn btn-primary btn-danger']").click()
        wait(3)
          
        #编辑安全组
        driver.find_element_by_xpath(".//a[@tabindex='6']").click()
        wait(2)
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/div/div/div/form/table/tbody/tr[1]/td[4]/div/a[2]").click()
        wait(1)
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/div/div/div/form/table/tbody/tr[1]/td[4]/div/ul/li[1]/a").click()
        wait(3)
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys("Auto-Test-Edit")
#         driver.find_element_by_id("id_name").submit()
        driver.find_element_by_xpath(".//input[@value='编辑安全组']").click()
        wait(3)
          
        #删除安全组
        driver.find_element_by_xpath(".//a[@tabindex='6']").click()
        wait(2)
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/div/div/div/form/table/tbody/tr[1]/td[4]/div/a[2]").click()
        wait(1)
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/div/div/div/form/table/tbody/tr[1]/td[4]/div/ul/li[2]/button").click()
        driver.find_element_by_xpath(".//a[@class='btn btn-primary btn-danger']").click()
        wait(3)
        print("test_access_and_security end")
        
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
class system_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(u"系统管理测试开始")
    @classmethod
    def tearDownClass(cls):
        print(u"系统管理测试结束")
    def setUp(self):
        #完成登录
        binary = FirefoxBinary(r"C:\Program Files\Mozilla Firefox\firefox.exe")
        self.driver = webdriver.Firefox(firefox_binary=binary)
#         self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30) # 隐性等待，最长等30秒
        self.driver.maximize_window()
        self.driver.get("http://192.168.20.215/dashboard")
        self.driver.find_element_by_id('id_username').send_keys('admin')
        self.driver.find_element_by_id('id_password').send_keys('123qwe') 
        self.driver.find_element_by_id('loginBtn').click()
        locator=(By.XPATH,"/html/body/div[1]/div[1]/div[2]/ul/li[4]/a" )
        WebDriverWait(self.driver,20,0.5).until(EC.presence_of_element_located(locator))
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/ul/li[4]/a").click()
        locator=(By.XPATH,".//a[@tabindex='1']")
        WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located(locator))
    def tearDown(self): 
        dr=self.driver    
        wait(10)
        dr.quit()
#     @unittest.skip("test")
    def test_compute_node_and_4_to_8(self):
        dr=self.driver
        #########计算主机#############
        dr.find_element_by_xpath(".//a[@tabindex='1']").click()
        wait(2)
        #开关服务
        dr.find_element_by_id("compute_host__row_centos7__action_disable").click()
        wait(3)
        dr.find_element_by_id("compute_host__row_centos7__action_enable").click()
        wait(3)
        #自动疏散 
        dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr/td[7]/div/a").click()
        wait(1)
        dr.find_element_by_id("compute_host__row_centos7__action_enable auto evacuate").click()
        wait(3)
        dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr/td[7]/div/a").click()
        wait(1)
        dr.find_element_by_id("compute_host__row_centos7__action_disable auto evacuate").click()
        wait(3)
        #批量操作
        items=dr.find_elements_by_xpath(".//input[@type='checkbox']")
        for item in items:
            item.click()
            item.click()
        items[0].click()
        actions=dr.find_elements_by_xpath(".//ul[@class='dropdown-menu clearfix']/li")
        for i in range(0,len(actions)):
            actions=dr.find_elements_by_xpath(".//ul[@class='dropdown-menu clearfix']/li")
            dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/thead/tr[1]/th/div/div[2]/a").click()
            actions[i].click()
            wait(3)
            dr.find_element_by_xpath(".//input[@type='checkbox']").click()
        dr.find_element_by_xpath(".//input[@type='checkbox']").click()
    
        ############关机设置####################
        #创建关机时间
        dr.find_element_by_xpath(".//a[@tabindex='4']").click()
        locator=(By.ID,"timing automatic closing physical machine__action_create")
        WebDriverWait(dr,30,0.5).until(EC.element_to_be_clickable(locator))
        dr.find_element_by_id("timing automatic closing physical machine__action_create").click()
        wait(3)
        dr.find_element_by_id("id_Host").send_keys(Keys.ARROW_DOWN)
        dr.find_element_by_id("id_Cycle").send_keys(Keys.ARROW_DOWN)
        dr.find_element_by_id("id_Cycle").send_keys(Keys.ARROW_UP)                               
        dr.find_element_by_id("id_Day").send_keys(Keys.ARROW_UP)
        dr.find_element_by_id("id_Hours").send_keys(Keys.ARROW_DOWN)
        dr.find_element_by_id("id_Minutes").send_keys(Keys.ARROW_UP)
        dr.find_element_by_id("id_Minutes").submit()
        wait(5)
        #修改关机时间
        dr.find_element_by_xpath(u".//a[@title='修改关机设置']").click()
        dr.find_element_by_id("id_Cycle").send_keys(Keys.ARROW_DOWN)
        dr.find_element_by_id("id_Week").send_keys(Keys.ARROW_UP)
        dr.find_element_by_id("id_Week").submit()
        wait(5)
        #删除关机时间
        dr.find_element_by_xpath(".//input[@class='table-row-multi-select']").click()
        dr.find_element_by_id("timing automatic closing physical machine__action_delete").click()                              
        dr.find_element_by_xpath(".//a[@class='btn btn-primary btn-danger']").click()
        locator=(By.XPATH,".//a[@tabindex='1']")
        WebDriverWait(self.driver,20,0.5).until(EC.presence_of_element_located(locator))
        
        #############管理用户################     
        dr.find_element_by_xpath(".//a[@tabindex='5']").click()
        wait(5)
        
        #获取原管理用户
        admin=dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr/td[6]/div/a[1]")
        edit_admin_id=admin.get_attribute("id")
#         print(edit_admin_id)
#         edit_admin_id="users__row_c40ce047747c48d1b22d91da268029cc__action_edit"
        #创建管理用户
        dr.find_element_by_id("users__action_create").click()
        dr.find_element_by_id("id_name").send_keys("Auto-Test")
        dr.find_element_by_id("id_password").send_keys("1")
        dr.find_element_by_id("id_confirm_password").send_keys("1")
        dr.find_element_by_id("id_email").send_keys("3545@qq.com")
        dr.find_element_by_id("id_role_id").send_keys(Keys.ARROW_DOWN)
        dr.find_element_by_id("id_role_id").submit()
        wait(5)
           
        #编辑
        item=dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr[1]/td[6]/div/a[1]")
        if item.get_attribute("id")!=edit_admin_id:
            item.click()
        else:
            dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr[2]/td[6]/div/a[1]").click()
        wait(3)
        dr.find_element_by_id("id_name").clear()
        dr.find_element_by_id("id_name").send_keys("Edit")
        dr.find_element_by_id("id_role").send_keys(Keys.ARROW_UP)
        dr.find_element_by_id("id_role").submit()     
        wait(10)
          
        #修改密码  
        elems=dr.find_elements_by_xpath(".//a[@class='btn btn-default btn-sm dropdown-toggle']")
        item=dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr[1]/td[6]/div/a[1]")
        if item.get_attribute("id")!=edit_admin_id:
            elems[0].click()
        else:
            elems[1].click()
        wait(3)
        dr.find_element_by_xpath(u".//a[@title='修改密码']").click()
        wait(3)
        dr.find_element_by_id("id_password").send_keys("2")
        dr.find_element_by_id("id_confirm_password").send_keys("2")
        dr.find_element_by_id("id_confirm_password").submit()
        wait(5)
        #禁用/激活
        elems=dr.find_elements_by_xpath(".//a[@class='btn btn-default btn-sm dropdown-toggle']")
        item=dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr[1]/td[6]/div/a[1]") 
        if item.get_attribute("id")!=edit_admin_id:
            elems[0].click()
        else:
            elems[1].click()
        dr.find_element_by_xpath(u".//button[@title='禁用用户']").click()
        wait(5)
          
        elems=dr.find_elements_by_xpath(".//a[@class='btn btn-default btn-sm dropdown-toggle']")
        item=dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr[1]/td[6]/div/a[1]") 
        if item.get_attribute("id")!=edit_admin_id:
            elems[0].click()
        else:
            elems[1].click()
        dr.find_element_by_xpath(u".//button[@title='激活用户']").click()
        wait(5)
        
        #删除用户
        elems=dr.find_elements_by_xpath(".//a[@class='btn btn-default btn-sm dropdown-toggle']")
        item=dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr[1]/td[6]/div/a[1]") 
        if item.get_attribute("id")!=edit_admin_id:
            elems[0].click()
        else:
            elems[1].click()
        elems=dr.find_elements_by_xpath(u".//button[@title='删除用户']")
        elems[1].click()
        wait(3)
        dr.find_element_by_xpath(".//a[@class='btn btn-primary btn-danger']").click()
        wait(5)
        
        ############系统设置##########################
        dr.find_element_by_xpath(".//a[@tabindex='6']").click()
        wait(3)
        dr.find_element_by_id("id_language").send_keys(Keys.ARROW_UP)
        dr.find_element_by_name("timezone").send_keys(Keys.ARROW_UP)
        dr.find_element_by_id("id_pagesize").send_keys(Keys.ARROW_UP)
        dr.find_element_by_id("id_instance_log_length").send_keys(Keys.ARROW_UP)
        dr.find_element_by_id("id_instance_log_length").submit()
        wait(10)
        dr.find_element_by_id("id_language").send_keys(Keys.ARROW_DOWN)
        dr.find_element_by_name("timezone").send_keys(Keys.ARROW_DOWN)
        dr.find_element_by_id("id_pagesize").send_keys(Keys.ARROW_DOWN)
        dr.find_element_by_id("id_instance_log_length").send_keys(Keys.ARROW_DOWN)
        dr.find_element_by_id("id_instance_log_length").submit()
        wait(10)
        locator=(By.XPATH,".//a[@tabindex='1']")
        WebDriverWait(self.driver,20,0.5).until(EC.presence_of_element_located(locator))
        
        #############修改管理密码#############################
        dr.find_element_by_xpath(".//a[@tabindex='7']").click()
        wait(3)
        dr.find_element_by_id("id_current_password").send_keys("123qwe")
        dr.find_element_by_id("id_new_password").send_keys("123qwe")
        dr.find_element_by_id("id_confirm_password").send_keys("123qwe")
        dr.find_element_by_id("id_confirm_password").submit()
        locator=(By.ID,"id_username")
        WebDriverWait(dr,30,0.5).until(EC.presence_of_element_located(locator))
        dr.find_element_by_id("id_username").send_keys("admin")
        dr.find_element_by_id("id_password").send_keys("123qwe")
        self.driver.find_element_by_id('loginBtn').click()
        locator=(By.XPATH,"/html/body/div[1]/div[1]/div[2]/ul/li[4]/a")
        WebDriverWait(dr,60,0.5).until(EC.element_to_be_clickable(locator))
        wait(5)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/ul/li[4]/a").click()
        locator=(By.XPATH,".//a[@tabindex='8']")
        WebDriverWait(dr,60,0.5).until(EC.element_to_be_clickable(locator))
        wait(3)
        #############操作记录#############################
        dr.find_element_by_xpath(".//a[@tabindex='8']").click()
        locator=(By.NAME,"operationrecording__filter__q")
        WebDriverWait(dr,20,0.5).until(EC.presence_of_element_located(locator))
        
        dr.find_element_by_name("operationrecording__filter__q").send_keys("admin")
        dr.find_element_by_name("operationrecording__filter__q").send_keys(Keys.ENTER)
        wait(5)
        dr.find_element_by_name("operationrecording__filter__q_field").send_keys(Keys.ARROW_DOWN)
        dr.find_element_by_name("operationrecording__filter__q").clear()
        dr.find_element_by_name("operationrecording__filter__q").send_keys("192.168.20.85")
        dr.find_element_by_name("operationrecording__filter__q").send_keys(Keys.ENTER)
        wait(5)
          
        dr.find_element_by_xpath(".//a[@href='?Page_type=next_page&&Current_page=1']").click()
        wait(10)
        dr.find_element_by_id("jump_page").send_keys("1")
        dr.find_element_by_id("jump_page_sure").click()
        wait(10)
         
        
        js="$(\"input[id='id_start']\").removeAttr('readonly');$(\"input[id='id_start']\").attr('value','2016-11-01')"
        dr.execute_script(js)
        js="$(\"input[id='id_end']\").removeAttr('readonly');$(\"input[id='id_end']\").attr('value','2016-11-08')"
        dr.execute_script(js)
        wait(3)
        dr.find_element_by_xpath(".//button").click()
        wait(5)
        
#     @unittest.skip("test")
    def test_alarm_and_hypevisor(self):
        dr=self.driver
        dr.find_element_by_xpath("/html/body/div[1]/div[1]/div/ul/li[2]/a").click()
        wait(3)
        
        #创建虚拟机    
        dr.find_element_by_id("instances__action_launch").click()
        wait(5)
        dr.find_element_by_id("id_name").send_keys("Auto-Test-for-hypevisor")
        dr.find_element_by_id("id_count").clear()
        dr.find_element_by_id("id_count").send_keys('3')
        dr.find_element_by_id("id_image_id").send_keys(Keys.ARROW_DOWN)
        dr.find_element_by_xpath(".//a[@href='#launch_instance__setnetworkaction']").click()
        items=dr.find_elements_by_xpath(".//input[@name='network']")
        if len(items)>1:
            for item in items:
                item.click()
                item.click()
            items[0].click()
        dr.find_element_by_xpath("/html/body/div[3]/div/form/div/div/div[3]/input").click()
        wait(10)
        locator=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr[1]/td[8]")
        WebDriverWait(dr,300,0,5).until(EC.text_to_be_present_in_element(locator,U'无'))
         
        dr.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/ul/li[4]/a").click()
        wait(3)
        locator=(By.XPATH,".//a[@tabindex='2']")
        WebDriverWait(self.driver,20,0.5).until(EC.presence_of_element_located(locator))
        ##################告警##############
        dr.find_element_by_xpath(".//a[@tabindex='2']").click()
        locator=(By.ID,"alarm__action_create")
        WebDriverWait(dr,30,0.5).until(EC.element_to_be_clickable(locator))
        
        #创建告警
        dr.find_element_by_id("alarm__action_create").click()
        dr.find_element_by_id("id_name").send_keys("Auto-Test")
        dr.find_element_by_id("id_fuzzy_select").click()
        dr.find_element_by_xpath(".//a[@onclick='select(this.text)']").click()
        dr.find_element_by_id("id_meter").send_keys(Keys.ARROW_DOWN)
        dr.find_element_by_id("id_meter").send_keys(Keys.ARROW_DOWN)
        dr.find_element_by_id("id_meter").send_keys(Keys.ARROW_DOWN)
        dr.find_element_by_id("id_meter").send_keys(Keys.ARROW_UP)
        dr.find_element_by_id("id_email").send_keys("8946@qq.com")
        dr.find_element_by_id("id_comparison_operator").send_keys(Keys.ARROW_DOWN)
        dr.find_element_by_id("id_threshold").send_keys(Keys.ARROW_UP)
        dr.find_element_by_id("id_threshold").send_keys(Keys.ARROW_UP)
        dr.find_element_by_id("id_evaluation_periods").send_keys(Keys.ARROW_UP)
        dr.find_element_by_id("id_evaluation_periods").submit()
        wait(10)
        #修改告警
        dr.find_element_by_xpath(u".//a[@title='修改告警']").click()
        dr.find_element_by_id("id_name").clear()
        dr.find_element_by_id("id_name").send_keys("Auto-Test-Edit")
        dr.find_element_by_id("id_name").submit()
        wait(5)
         
        #禁用/激活告警
        dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/form/table/tbody/tr/td[7]/div/a[2]").click()
        dr.find_element_by_xpath(u".//button[@title='禁用 告警']").click()
        wait(3)
        dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/form/table/tbody/tr/td[7]/div/a[2]").click()
        dr.find_element_by_xpath(u".//button[@title='激活 告警']").click()
        wait(3)
         
        #修改邮件地址
        dr.find_element_by_xpath(u".//a[@title='修改邮件地址']").click()
        wait(3)
        dr.find_element_by_id("id_email").clear()
        dr.find_element_by_id("id_email").send_keys("1111@qq.com")
        dr.find_element_by_id("id_email").submit()
        wait(5)
         
        #删除告警
        dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/form/table/tbody/tr/td[7]/div/a[2]").click()
        wait(1)
        dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/form/table/tbody/tr/td[7]/div/ul/li[1]/button").click()
        wait(3)
        dr.find_element_by_xpath(".//a[@class='btn btn-primary btn-danger']").click()
        wait(5)
        
        #主机监控
        dr.find_element_by_xpath(".//a[@tabindex='3']").click()
        wait(3)
        dr.find_element_by_id("host_monitor__action_Refresh").click()
        wait(1)
        dr.find_element_by_xpath(".//input[@type='submit']").click()
        wait(3)
        
        dr.find_element_by_xpath(".//a[@href='?tab=host_monitor__vm_monitor_tab']").click()
        wait(3)
        for i in range(1,4):
            dr.find_element_by_xpath(u".//button[@title='监控 虚拟机']").click()
            wait(10)
        for i in range(1,4):
            dr.find_element_by_xpath(u".//button[@title='取消监控 虚拟机']").click()
            wait(10)    
        
        #删除虚拟机
        url=dr.current_url
        while url !="http://192.168.20.215/dashboard/instances_manager/":
            dr.find_element_by_xpath("/html/body/div[1]/div[1]/div/ul/li[2]/a").click()
            wait(10)
            url=dr.current_url
        items=dr.find_elements_by_xpath("//input[@class='table-row-multi-select']")
        while len(items)<4:
            dr.refresh()
            wait(5)
            items=dr.find_elements_by_xpath("//input[@class='table-row-multi-select']")
        items[1].click()
        items[2].click()
        items[3].click()
        dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/thead/tr[1]/th/div/div[2]/a").click()
        wait(3)
        dr.find_element_by_id("instances__action_terminate").click()
        wait(2)    
        dr.find_element_by_xpath(".//a[@class='btn btn-primary btn-danger']").click()       
        url= dr.current_url    
        while url != "http://192.168.20.215/dashboard/instances_manager/trash":
            dr.find_element_by_id("instances__action_trash").click()
            wait(5)
            url= dr.current_url
        wait(3)
        dr.refresh()
        wait(10)
        locator=(By.XPATH,".//input[@class='table-row-multi-select']")
        WebDriverWait(dr,30,0.5).until(EC.element_to_be_clickable(locator))
        dr.find_element_by_xpath(".//input[@class='table-row-multi-select']").click()
        dr.find_element_by_id("trash__action_trashinstance").click()
        wait(1)
        dr.find_element_by_xpath(".//a[@class='btn btn-primary btn-danger']").click()
        wait(10)
if __name__ == "__main__":
    unittest.main()
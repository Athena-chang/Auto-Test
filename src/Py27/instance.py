# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.common.keys import Keys   
from django.conf.global_settings import SEND_BROKEN_LINK_EMAILS
 
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
        self.driver = webdriver.Firefox()
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
        driver.find_element_by_id("id_name").send_keys("Auto-Test-1")
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
        WebDriverWait(driver,60,0,5).until(EC.text_to_be_present_in_element(locator,U'无'))
        driver.find_element_by_id("instances__action_launch").click()
        wait(5)
        driver.find_element_by_id("id_name").send_keys("Auto-Test-2")
        driver.find_element_by_id("id_image_id").send_keys(Keys.ARROW_DOWN)
        driver.find_element_by_xpath(".//a[@href='#launch_instance__setnetworkaction']").click()
        items=driver.find_elements_by_xpath(".//input[@name='network']")
        if len(items)>1:
            for item in items:
                item.click()
            items[0].click()
        driver.find_element_by_xpath("/html/body/div[3]/div/form/div/div/div[3]/input").click()
        wait(3)
        locator=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr[1]/td[8]")
        WebDriverWait(driver,60,0,5).until(EC.text_to_be_present_in_element(locator,U'无'))
        wait(3)
          
        #编辑虚拟机
        driver.find_element_by_xpath(u".//a[@title='编辑虚拟机']").click()
        wait(1)
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id('id_name').send_keys('Auto-Test-3')
        driver.find_element_by_id('id_name').submit()
        wait(3)
        #删除虚拟机
        driver.find_element_by_xpath(".//button[@title='删除虚拟机' and @class='btn btn-default btn-sm btn-danger btn-confirm']").click()
        wait(1)
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
        driver.find_element_by_id("instances__action_trash").click() 
        wait(3)
        driver.refresh()
        wait(3)
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
        items=driver.find_elements_by_xpath(".//input[@class='form-control']")
        for item in items:
            item.send_keys('Auto-Test-2')
        driver.find_element_by_id("id_source_type").click()
        driver.find_element_by_id("id_source_type").send_keys(Keys.ARROW_DOWN)
        driver.find_element_by_id("id_image_file").click()
        driver.find_element_by_id("id_image_file").send_keys(u'D:\\软件\cirros')
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
        
    
if __name__ == "__main__":
    unittest.main()
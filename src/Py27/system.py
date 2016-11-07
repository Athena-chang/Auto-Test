# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.common.keys import Keys   
from selenium.webdriver.common.alert import Alert
def wait(seconds):
    time.sleep(seconds)
class system_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(u"系统管理测试开始")
    @classmethod
    def tearDownClass(cls):
        print(u"系统管理测试结束")
    def setUp(self):
        #完成登录
        self.driver = webdriver.Firefox()
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
        dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr[2]/td[6]/div/a[1]").click()
        wait(3)
        dr.find_element_by_id("id_name").clear()
        dr.find_element_by_id("id_name").send_keys("Edit")
        dr.find_element_by_id("id_role").send_keys(Keys.ARROW_UP)
        dr.find_element_by_id("id_role").submit()
        wait(5)
        #修改密码  禁用用户
        items=dr.find_elements_by_xpath(".//a[@class='btn btn-default btn-sm dropdown-toggle']")
        items[1].click()
        wait(1)
        items=dr.find_elements_by_xpath(u".//a[@title='修改密码']")
        items[1].click()
        dr.find_element_by_id("id_password").send_keys("2")
        dr.find_element_by_id("id_confirm_password").send_keys("2")
        dr.find_element_by_id("id_confirm_password").submit()
        wait(5)
        
        items=dr.find_elements_by_xpath(".//a[@class='btn btn-default btn-sm dropdown-toggle']")
        items[1].click()
        wait(1)
        dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr[2]/td[6]/div/ul/li[2]/button").click()
        wait(5)
        
        items=dr.find_elements_by_xpath(".//a[@class='btn btn-default btn-sm dropdown-toggle']")
        items[1].click()
        wait(1)
        dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr[2]/td[6]/div/ul/li[2]/button").click()
        wait(5)
        
        dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/tbody/tr[2]/td[1]/input").click()
        dr.find_element_by_id("users__action_delete").click()
        wait(2)
        dr.find_element_by_xpath(".//a[@class='btn btn-primary btn-danger']").click()
        locator=(By.XPATH,".//a[@tabindex='1']")
        WebDriverWait(self.driver,20,0.5).until(EC.presence_of_element_located(locator))
        
        ############系统设置##########################
        dr.find_element_by_xpath(".//a[@tabindex='6']").click()
        wait(3)
        dr.find_element_by_id("id_language").send_keys(Keys.ARROW_UP)
        dr.find_element_by_name("timezone").send_keys(Keys.ARROW_UP)
        dr.find_element_by_id("id_pagesize").send_keys(Keys.ARROW_UP)
        dr.find_element_by_id("id_instance_log_length").send_keys(Keys.ARROW_UP)
        dr.find_element_by_id("id_instance_log_length").submit()
        wait(3)
        dr.find_element_by_id("id_language").send_keys(Keys.ARROW_DOWN)
        dr.find_element_by_name("timezone").send_keys(Keys.ARROW_DOWN)
        dr.find_element_by_id("id_pagesize").send_keys(Keys.ARROW_DOWN)
        dr.find_element_by_id("id_instance_log_length").send_keys(Keys.ARROW_DOWN)
        dr.find_element_by_id("id_instance_log_length").submit()
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
        locator=(By.XPATH,"/html/body/div[1]/div[1]/div[2]/ul/li[4]/a" )
        WebDriverWait(self.driver,20,0.5).until(EC.presence_of_element_located(locator))
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/ul/li[4]/a").click()
        locator=(By.XPATH,".//a[@tabindex='1']")
        WebDriverWait(self.driver,20,0.5).until(EC.presence_of_element_located(locator))
        
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
        for i in range(1,3):
            dr.find_element_by_xpath(u".//button[@title='监控 虚拟机']").click()
            wait(10)
        for i in range(1,3):
            dr.find_element_by_xpath(u".//button[@title='取消监控 虚拟机']").click()
            wait(10)    
        
        #删除虚拟机
        dr.find_element_by_xpath("/html/body/div[1]/div[1]/div/ul/li[2]/a").click()
        wait(3)
        items=dr.find_elements_by_xpath("//input[@class='table-row-multi-select']")
        items[1].click()
        items[2].click()
        items[3].click()
        dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div[2]/form/table/thead/tr[1]/th/div/div[2]/a").click()
        wait(3)
        dr.find_element_by_id("instances__action_terminate").click()
        wait(1)    
        dr.find_element_by_xpath(".//a[@class='btn btn-primary btn-danger']").click()       
        wait(5)
        dr.find_element_by_id("instances__action_trash").click() 
        wait(3)
        dr.find_element_by_xpath(".//input[@class='table-row-multi-select']").click()
        dr.find_element_by_id("trash__action_trashinstance").click()
        wait(1)
        dr.find_element_by_xpath(".//a[@class='btn btn-primary btn-danger']").click()
        wait(10)
        
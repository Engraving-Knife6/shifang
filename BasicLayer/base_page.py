from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, drive:webdriver.Chrome):
        self.driver = drive
        self.wait = WebDriverWait(drive, 10)


     # 定位单个元素，定位失败抛出异常
    def find_element(self, locator):
        try:
            return self.wait.until(ec.visibility_of_element_located(locator))
        except Exception as e:
            print(f"定位元素{locator}失败,错误{e}")
            raise


    # 定位多个元素,定位失败返回空列表
    def find_elements(self, locator):
        try:
            return self.wait.until(ec.presence_of_all_elements_located(locator))
        except Exception as e:
            return []


    # 单击操作
    def click(self, locator):
        element = self.find_element(locator)
        #  普通点击
        # element.click()
        #  替换成 JS 点击（无视遮挡，最稳）
        self.driver.execute_script("arguments[0].click();",element)


    # 输入操作
    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)
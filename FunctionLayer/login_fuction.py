from BasicLayer.base_page import BasePage
from DataLayer.ElementLocatorData.page_locators import LoginLocators


class LoginFunction:
    def __init__(self, driver):
        self.driver = driver
        self.login_func = BasePage(driver)  # 依赖基础层实例，实例化对象

    def input_username(self, username):
        self.login_func.send_keys(LoginLocators.username, username)


    def input_password(self, password):
        self.login_func.send_keys(LoginLocators.password, password)

    def click_loginbut(self):
        self.login_func.click(LoginLocators.loginbut)

    def click_rember(self):
        self.login_func.click(LoginLocators.rembut)


    # 获取异常提示
    def get_error_msg(self, *error_locator):
        error_texts = []
        for locator in error_locator:
            element = self.login_func.find_element(locator)
            error_texts.append(element.text)
            """
            获取文本：从 element（网页元素 / 标签对象）中提取纯文本内容（element.text）
            添加数据：将提取到的文本追加到 error_texts 这个列表的末尾
            """
        return error_texts
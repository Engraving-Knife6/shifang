from BasicLayer.base_page import BasePage
from FunctionLayer.login_fuction import LoginFunction
from DataLayer.ElementLocatorData.page_locators import LoginLocators


class LoginBusiness(BasePage):  #类LoginBusiness继承类BasePage
    def __init__(self, driver):
        super().__init__(driver)  # 调用父类 BasePage 的 __init__ 方法，初始化 wait 等属性
        self.driver = driver
        self.loginfunc = LoginFunction(driver)

    # 合法登录
    def login_with_valid_uesr(self, usrname, password, remember = False):
        self.loginfunc.input_username(usrname)
        self.loginfunc.input_password(password)

        if remember:
            self.loginfunc.click_rember()

            usrname_element = self.find_element(LoginLocators.username)
            password_element = self.find_element(LoginLocators.password)
            self.loginfunc.click_loginbut()
            # 获取输入框值
            return usrname_element.get_attribute("value"), password_element.get_attribute("value")

        self.loginfunc.click_loginbut()

    # 非法登录
    def login_with_error_scenario(self, username = None, password = None, *error_locator):
        # 设计一个login_with_error_scenario通用方法，将差异项作为参数传入，实现“一法多用”，使用可变参数用于不确定需要传递参数的数量
        """
             通用错误场景登录方法：处理各类登录失败场景（参数化差异项）
        :param username: 用户名（可为None，表示不输入/为空）
        :param password: 密码（可为None，表示不输入/为空）
        :param error_locator: 该场景对应的错误提示元素定位器
        :param expected_msg: 该场景预期的错误提示文本
        :return: 校验结果（True/False）
        """

        # 1.输入用户名（若部位None则输入，否则输入）
        if username is not None:
            self.loginfunc.input_username(username)

        # 2.输入密码
        if password is not None:
            self.loginfunc.input_password(password)

        # 3.点击登录
        self.loginfunc.click_loginbut()

        # 4.获取实际错误提示
        error_msg = self.loginfunc.get_error_msg(*error_locator)
        return error_msg

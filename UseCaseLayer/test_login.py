import time
import pytest
import allure
from BusinessLayer.login_business import LoginBusiness
from Common.Utils.data_reader import read_login_data
from DataLayer.ElementLocatorData.page_locators import LoginLocators


@allure.feature("用户登录模块")
@pytest.mark.usefixtures("init_login_page", "capture_screenshot")
class TestLogin:
    datas, param_data = read_login_data()
    # 登录功能的测试用例层
    @allure.story("合法用户登录")
    @allure.title("使用正确的用户名和密码登录")
    def test_login_with_valid_credentials(self, browser):
        """测试用例1：合法用户登录后应跳转到首页"""

        login = LoginBusiness(browser)
        data = self.datas["success_login"]
        username, password = data["username"], data["password"]
        remember = True  # 字段remember值为True验证记住密码功能（场景），为False时，只进行登录成功测试
        getusername, getpassword = login.login_with_valid_uesr(username, password, remember)
        time.sleep(2)

        # 2. 业务判断：登录成功的标志（如URL包含“home”）
        if 'home' in browser.current_url:
            print(f"业务结果；{username}登录成功")
        else:
            print(f"业务结果：{username}登录失败")

        if remember:
            browser.delete_all_cookies()  # 清空cookie值
            browser.get("http://10.61.60.71:6075/login")
            time.sleep(2)
            assert username == getusername, f"记住密码功能失效，预期[{username}]，实际[{getusername}]"
            assert password == getpassword, f"记住密码功能失效，预期[{password}]，实际[{getpassword}]"
            print("业务结果：记住账号功能正常")

    @allure.story("密码错误登录")
    @allure.title("使用正确用户名和错误密码登录")
    @pytest.mark.parametrize("username, password, expected_msg", [
        param_data[3]])  # param_data[3]使用这个格式，因为param_data取得就是invalid_credentials的值，不需要再使用[invalid_credentials]
    def test_login_with_invalid_password(self, username, password, expected_msg, browser):
        # parametrize的参数名需要与est_login_with_invalid_password的参数名一致
        """测试用例2：密码错误时应提示正确的错误信息（数据驱动）"""
        login = LoginBusiness(browser)
        # 调用业务层的密码错误登录方法
        actual_msg = login.login_with_error_scenario(username, password, LoginLocators.wrongpas)
        print(actual_msg, type(actual_msg))
        # 断言：业务层返回True（表示错误提示符合预期）,使用[actual_msg]去做断言，因为expected_msg是list类型
        assert [actual_msg[0]] == expected_msg, f"密码错误时提示异常，预期：[{expected_msg}]，实际[{actual_msg}]"
        print(f"业务结果：[{expected_msg}]密码错误提示正确")

    @allure.story("用户名空登录")
    @allure.title("用户名为空时登录")
    @pytest.mark.parametrize("username, password, expected_msg", [param_data[0]])
    def test_login_with_empty_username(self, username, password, expected_msg, browser):
        """测试用例3：用户名为空时应提示'请输入用户名'"""
        login = LoginBusiness(browser)
        actual_msg = login.login_with_error_scenario(username, password, LoginLocators.empty_username_err)
        # expected_msg = str(expected_msg)
        # 断言：错误提示与预期一致
        assert [actual_msg[0]] == expected_msg, f"用户名为空时提示异常，预期：[{expected_msg}]，实际[{actual_msg}]"
        print(f"业务结果：[{expected_msg}]用户名为空提示正确")

    @allure.story("密码空登录")
    @allure.title("密码为空时登录")
    @pytest.mark.parametrize("username, password, expected_msg", [param_data[1]])
    def test_login_with_empty_password(self, username, password, expected_msg, browser):
        """测试用例3：用户名为空时应提示'请输入用户名'"""
        login = LoginBusiness(browser)
        actual_msg = login.login_with_error_scenario(username, password, LoginLocators.empty_password_err)
        # 断言：错误提示与预期一致
        assert [actual_msg[0]] == expected_msg, f"密码为空时提示异常，预期：[{expected_msg}]，实际[{actual_msg}]"
        print(f"业务结果：[{expected_msg}]密码为空提示正确")

    @allure.story("用户名和密码均空登录")
    @allure.title("用户名和密码为均空时登录")
    @pytest.mark.parametrize("username, password, expected_msg", [param_data[2]])
    def test_login_with_empty_password_usenrame(self, username, password, expected_msg, browser):
        """测试用例3：用户名为空时应提示'请输入用户名'"""
        login = LoginBusiness(browser)
        actual_msg = login.login_with_error_scenario(username, password,
                                                     LoginLocators.empty_username_err, LoginLocators.empty_password_err)
        # 断言：错误提示与预期一致
        assert actual_msg == expected_msg, f"用户名和密码为均空时提示异常，预期：[{expected_msg}]，实际[{actual_msg}]"
        print(f"业务结果：[{expected_msg}]用户名和密码均为空提示正确")

    @allure.story("用户名不存在时登录")
    @allure.title("用户名不存在时登录")
    @pytest.mark.parametrize("username, password, expected_msg", [param_data[4]])
    def test_login_with_username_notexist(self, username, password, expected_msg, browser):
        """测试用例3：用户名为空时应提示'请输入用户名'"""
        login = LoginBusiness(browser)
        actual_msg = login.login_with_error_scenario(username, password, LoginLocators.usename_notexist)
        # 断言：错误提示与预期一致
        assert [actual_msg[0]] == expected_msg, f"用户名不存在时，预期：[{expected_msg}]，实际[{actual_msg}]"
        print(f"业务结果：[{expected_msg}]用户名不存在提示正确")

    @allure.story("用户账号禁用时登录")
    @allure.title("用户账号禁用时登录")
    @pytest.mark.parametrize("username, password, expected_msg", [param_data[5]])
    def test_login_with_accountsuspension(self, username, password, expected_msg, browser):
        """测试用例3：用户名为空时应提示'请输入用户名'"""
        login = LoginBusiness(browser)
        actual_msg = login.login_with_error_scenario(username, password, LoginLocators.accountsuspension)
        # 断言：错误提示与预期一致
        assert [actual_msg[0]] == expected_msg, f"用户账号禁用时，预期：[{expected_msg}]，实际[{actual_msg}]"
        print(f"业务结果：[{expected_msg}]用户账号禁用时提示正确")


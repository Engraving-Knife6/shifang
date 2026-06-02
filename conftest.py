import pytest
import allure
from datetime import datetime
import os
from selenium import webdriver
import sys
from FunctionLayer.login_fuction import LoginFunction
from Common.Utils.data_reader import read_login_data
from BusinessLayer.login_business import LoginBusiness
from  Common.Fixtures.disasesubtype import homep_disase
from  Common.Fixtures.handle import orginal_handle

# 获取当前工作空间根目录（Jenkins 工作空间路径）
root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))  # 根据脚本层级调整
sys.path.append(root_dir)

# 验证路径是否生效
print("python模块搜索路径", sys.path)

"""使用 scope="function" 的 Fixture将 browser 和 init_login_page 的 scope 设置为 function，这样每个测试用例都会有独立的浏览器实例和登录页实例。
function实现每个测试类单独执行,session实现所有测试类在一个会话（浏览器）中执行"""
@pytest.fixture(scope="function")
def browser():
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach",True)
    option.add_argument('--start-maximized')
    option.add_experimental_option("excludeSwitches", ['enable-automation'])
    #chromedriver_path = r"D:\ChromeDriver\chromedriver-win64_145\chromedriver-win64\chromedriver.exe"
    #service = Service(executable_path=chromedriver_path)
    #driver = webdriver.Chrome(service=service, options=option)
    driver = webdriver.Chrome(options=option)

    driver.delete_all_cookies()
    driver.refresh()
    yield  driver  # 返回驱动给测试函数


# 1. 使用 scope="function" 的 Fixture将 browser 和 init_login_page 的 scope 设置为 function，这样每个测试用例都会有独立的浏览器实例和登录页实例。
@pytest.fixture(scope="function")
def init_login_page(browser):
    login_page = LoginFunction(browser)
    browser.get('http://10.61.60.71:6075/')
    return login_page  # 返回初始化好的登录页对象


"""
@pytest.hookimpl：pytest 的装饰器，用于定义钩子函数（钩子函数是 pytest 提供的扩展点，可自定义测试执行过程）。
tryfirst=True：指定该钩子函数优先于其他同名钩子执行（确保结果被优先处理）。
hookwrapper=True：标记该钩子为 “包装器钩子”，可以捕获其他钩子的执行结果（通过 yield 获取）。
"""
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """标记测试用例的执行结果，供截图fixture判断是否失败
        定义钩子函数 pytest_runtest_makereport，这是 pytest 内置的钩子，用于生成测试用例的执行报告。
        参数说明：
        item：测试用例对象（包含用例名称、所在模块等信息）。
        call：测试用例的调用对象（包含用例执行的相关数据，如开始时间、结束时间、异常信息等）。
        """
    # 获取钩子方法的调用结果
    outcome = yield
    # outcome：接收 yield 返回的结果对象，包含测试用例的执行报告数据。
    rep = outcome.get_result()
    # 将测试结果存到 item 的属性中（供 capture_screenshot fixture 使用）;rep 包含测试用例的执行状态（如 passed/failed/skipped）、执行时间、错误信息等。
    setattr(item, "rep_call", rep)
    """
    setattr(item, "rep_call", rep)：给测试用例对象（item）动态添加一个 rep_call 属性，值为测试报告（rep）。
    作用：让其他组件（如 capture_screenshot fixture）可以通过 item.rep_call 获取测试结果（例如用 item.rep_call.failed 判断是否失败）。
    """

# 从 Python 标准库导入 datetime 类，用于生成时间戳（确保截图文件名唯一）。
# 导入 os 模块，用于处理文件路径（创建目录、拼接路径等）。
@pytest.fixture(scope="function")
def capture_screenshot(browser, request):

    """用例失败时自动截图
    定义 fixture 函数 capture_screenshot，参数说明：
    browser：依赖其他 fixture（通常是浏览器驱动实例），用于调用截图方法。
    request：pytest 内置 fixture，用于获取测试用例的相关信息（如用例名称、执行结果）。
    """
    yield  # 测试用例执行前等待
    # 用例执行后，判断是否失败
    if request.node.rep_call.failed:
        """
        用例执行后，通过 request.node.rep_call.failed 判断用例是否失败：
        request.node：表示当前测试用例对象。
        rep_call：存储用例的执行结果（需配合 pytest_runtest_makereport 钩子函数获取，见前文）。
        failed：布尔值，True 表示用例失败，False 表示成功。
        """
        # 生成截图文件名（包含用例名和时间戳，避免重复）
        case_name = request.node.name
        # request.node.name 获取当前测试用例的名称（如 test_login_with_invalid_credentials[case0]），用于截图命名。

        valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-"
        filtered_case_name = ''.join(c for c in case_name if c in valid_chars)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        # 生成当前时间的时间戳（格式：年 - 月 - 日_时 - 分 - 秒，如 20240729_163025），确保同一用例多次失败时截图文件名不重复。

        screenshot_name = f"{filtered_case_name}_{timestamp}.png"

        # screenshot_name = f"{case_name}_{timestamp}.png"
        # 拼接截图文件名，格式为「用例名_时间戳.png」（如 test_login[case0]_20240729_163025.png）。
        # 确保截图目录存在（如不存在则创建）
        screenshot_dir = os.path.join(os.getcwd(), "screenshots")
        # 定义截图保存目录：当前项目根目录下的 screenshots 文件夹（os.getcwd() 获取当前工作目录）。
        os.makedirs(screenshot_dir, exist_ok=True)
        """
        创建截图目录：
        os.makedirs 递归创建目录（支持多级目录）。
        exist_ok=True：若目录已存在则不报错，避免重复创建时的异常
        """

        # 保存截图到目录
        screenshot_path = os.path.join(screenshot_dir, screenshot_name)
        # 拼接完整的截图路径（如 项目根目录/screenshots/test_login[case0]_20240729_163025.png）。

        browser.save_screenshot(screenshot_path)  # 调用浏览器截图方法

        # 新增将截图附加到allure报告
        """
        以二进制读取模式（"rb"） 打开截图文件（screenshot_path 是截图的本地保存路径）。
        with 语句确保文件使用后自动关闭，避免资源泄露。
        f 是文件对象，用于读取图片的二进制数据。
        allure.attach(...)
        这是 Allure 报告工具的核心方法，用于向测试报告中添加附件（如图片、日志等），参数含义：
        f.read()：读取截图文件的二进制数据，作为附件的内容。
        name=f"失败截图_{case_name}"：设置附件在报告中的显示名称，通过 f-string 动态包含用例名（case_name），方便区分不同用例的截图（例如 “失败截图_test_login_with_invalid_credentials”）。
        attachment_type=allure.attachment_type.PNG：指定附件类型为 PNG 图片，确保报告能正确解析并显示图片（而非二进制乱码）。
        """
        with open(screenshot_path, "rb") as f:
            allure.attach(
                f.read(),
                name=f"失败截图_{case_name}",  #附件名称
                attachment_type=allure.attachment_type.PNG  # 附件类型
            )
        print(f"\n测试用例失败，截图已保存至：{screenshot_path}")


@pytest.fixture(scope="function")
def login(init_login_page, browser):
    datas, param_data = read_login_data()  # 获取read_login_data()函数的返回值
    login = LoginBusiness(browser)  # 初始化业务层实例
    data = datas["success_login"]
    username, password = data["username"], data["password"]
    remember = False  # 字段remember值为True验证记住密码功能（场景），为False时，只进行登录成功测试
    login.login_with_valid_uesr(username, password, remember)

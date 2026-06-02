import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(scope="function")
# 将句柄权限转移到新的标签页上
def orginal_handle(browser):
    orginal_handkes = browser.window_handles  # 获取当前窗口所有句柄
    #print(f"输出所有句柄{orginal_handkes}")
    #orginal_count = len(orginal_handkes)
    """WebDriverWait(browser, 10).until(
        lambda d: len(browser.window_handles) == orginal_count + 1
    )"""
    #all_handels = browser.window_handles
    # 将当前操作焦点切换到浏览器中最后打开的那个窗口
    current_handle = browser.switch_to.window(orginal_handkes[-1])
    #print(f"输出当前句柄{orginal_handkes[-1]}")
    return orginal_handkes[-1]  # 可能只需要执行all_handels[-1]就够了"""




"""class Handle:
    def __init__(self, drive:webdriver.Chrome):
        self.drive = drive


    # 统计操作前的原始句柄数量
    def orginal_handle(self):
        orginal_handkes = self.drive.window_handles  # 获取当前窗口所有句柄
        orginal_count = len(orginal_handkes)
        return orginal_count

    # 将句柄权限转移到新的标签页上
    def operation_handle(self):
        orginal_count = self.orginal_handle()  #再次调用self.orginal_handle()时获取到的句柄数量是最近一次的值，不是期待值，因此采用参数获取期待值
        WebDriverWait(self.drive, 10).until(
            lambda d: len(self.drive.window_handles) == orginal_count+1
        )
        all_handels = self.drive.window_handles
        # 将当前操作焦点切换到浏览器中最后打开的那个窗口
        current_handle =  self.drive.switch_to.window(all_handels[-1])
        return current_handle  #可能只需要执行all_handels[-1]就够了"""


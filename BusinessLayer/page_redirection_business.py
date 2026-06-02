import time

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from BasicLayer.base_page import BasePage
from DataLayer.ElementLocatorData.page_locators import NavigationMenuItemLocators


class PageRedirectionBusiness:
    def __init__(self, drive):
        self.drive = drive
        self.redire_bus = BasePage(drive)
        # 把需要测试的试航菜单项，统一整理成列表，方便循环调用
        self.menu_items = [
            ("首页", NavigationMenuItemLocators.homepage2, "首页"),  # 第二个首页为预期首页的关键词
            ("临床试验", NavigationMenuItemLocators.clinical_trial, "我创建的"),
            ("患者管理", NavigationMenuItemLocators.patient_management, "患者管理"),
            ("疗程管理", NavigationMenuItemLocators.treatment_management, "疗程管理"),
            ("方案管理", NavigationMenuItemLocators.solution_management, "方案管理"),
            ("基础管理", NavigationMenuItemLocators.basic_management, "疾病分型")
        ]

    def enter_platform_menu(self):
        """ 统一封装，点击左侧平台菜单，展开试航子菜单"""
        #self.redire_bus.click(NavigationMenuItemLocators.platform)
        """点击平台菜单，展开试航子菜单"""
        locator = NavigationMenuItemLocators.platform
        element = self.redire_bus.wait.until(ec.presence_of_element_located(locator))

        # 1. 强制滚动到元素，确保它在可视区域内
        self.redire_bus.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.2)

        # 2. 用JS强制点击，无视任何遮挡
        self.redire_bus.driver.execute_script("arguments[0].click();", element)



    def redirect_to_menu_item(self, locator, expected_keyword):
        """
        单个菜单项的跳转+校验逻辑
        :param locator: 菜单项的定位器
        :param expected_keyword: 跳转后页面的预期关键词
        """
        # 点击菜单项
        self.redire_bus.click(locator)
        # ！！！获取所有句柄,涉及到页面跳转需要切换句柄，否则会导致定位失败
        handles = self.redire_bus.driver.window_handles
        print(handles)
        self.redire_bus.driver.switch_to.window(handles[-1])
        print(handles[-1])
        time.sleep(1)

        try:
            # ✅ 等待标题出现预期关键词，最多等10秒

            WebDriverWait(self.drive, 10).until(
                lambda d:expected_keyword in d.title
                #lambda d: expected_keyword in d.current_url
            )
            print(f"[{expected_keyword}]校验通过！")
        except:
            # 超时后主动失败，并打印当前标题

            assert False, f"【{expected_keyword}】跳转失败，预期包含关键词：[{expected_keyword}],当前标题:[{self.redire_bus.driver.title}]"

        print(expected_keyword)
        # 校验跳转是否成功
        #assert expected_keyword in self.redire_bus.driver.title, \
        #f"【{expected_keyword}】跳转失败，预期包含关键词：[{expected_keyword}],当前标题:[{self.redire_bus.driver.title}]"

    def test_all_menu_items_redirect(self):
        """主业务流程，循环测试试航下的所有菜单项跳转"""
        # 第一步：进入平台菜单，展开试航菜单
        self.enter_platform_menu()

        n=1
        # 第二步：循环测试每个菜单项
        for menu_name, locator, expected_keyword in self.menu_items:
            with allure.step(f"测试试航菜单项:{menu_name}"):
                print(f"第{n}次点击平台按钮")
                n=n+1

                print(f"正在测试试航菜单项:[{menu_name}]")
                # 执行跳转+校验
                self.redirect_to_menu_item(locator, expected_keyword)
                time.sleep(1)


                # 第三步，测试完成后，返回平台菜单，准备下一次测试
                self.enter_platform_menu()





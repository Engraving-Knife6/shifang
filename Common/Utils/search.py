import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from BasicLayer.base_page import BasePage


class Search:
    def __init__(self, driver):
        self.driver = driver
        self.search = BasePage(driver)

    def public_search_function(self, search_input_locator ,  search_term, search_button_locator = False):
        """
        公共搜索函数，适用于多个模块
        :param search_input_locator: 搜索输入框定位器
        :param search_button_locator: 搜索按钮定位器

        :param search_term: 搜索关键词
        """

        self.search.send_keys(search_input_locator, search_term)
        if search_button_locator:
            self.search.click(search_button_locator)

        """WebDriverWait(self.driver, 10).until(
                ec.visibility_of_element_located(result_locator)
            )
    """

    def get_first_search_result(self, result_locator):
        """
         :param result_locator: 搜索结果定位器
        获取搜索结果中的第一条疾病名称
        :return: 第一条疾病名称文本
        """
        """ WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(result_locator)
        )"""
        time.sleep(1)
        result_element = self.search.find_element(result_locator)
        print(result_element.text)
        return result_element.text
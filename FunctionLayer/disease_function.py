import time
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Common.Utils.search import Search
from Common.Utils.match import DataComparator


from BasicLayer.base_page import BasePage
from DataLayer.ElementLocatorData.disease_element import DiseaseElements


# 疾病分型功能
class DiseaseFunction:
    def __init__(self, driver):
        self.driver = driver
        self.disease_func = BasePage(driver)
        self.search = Search(driver)
        self.datacompartor = DataComparator(driver)

    # 新增搜索功能


    # 可选：获取搜索结果中的第一条疾病名称（用于断言）
    """  def get_first_search_result(self):
        
        #获取搜索结果中的第一条疾病名称
        #:return: 第一条疾病名称文本
        
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(DiseaseElements.search_result)
        )
        time.sleep(1)
        result_element = self.disease_func.find_element(DiseaseElements.search_result)
        print(result_element.text)
        return result_element.text"""

    # 功能1：新增疾病分型
    def add_disease(
            self,
            disease_abb: str=None,
            disease_name: str=None,
            parent_abb: bool=False,
            eng_name: str =None,
            abbreviation: str = None,
            other_name: str = None,
            disease_coding: bool = False
    ):
        # 点击新增疾病按钮
        with allure.step("步骤：点击新增按钮"):
            self.disease_func.click(DiseaseElements.insert_but)
        """新增疾病分型"""
        # 1.判断参数是否存在，有值才操作
        if disease_abb:
            with allure.step("步骤：输入疾病简称"):
                self.disease_func.send_keys(DiseaseElements.disease_abb_value, disease_abb)
        if disease_name:
            with allure.step("步骤：输入疾病名称"):
                self.disease_func.send_keys(DiseaseElements.disease_name_value, disease_name)
        if parent_abb:
            with allure.step("步骤：选择父级简称"):
                self.disease_func.click(DiseaseElements.parent_abb_value)
                self.disease_func.click(DiseaseElements.top)
        if eng_name:
            with allure.step("步骤：输入英文名称"):
                self.disease_func.send_keys(DiseaseElements.eng_name_value, eng_name)
        if abbreviation:
            with allure.step("步骤：输入缩写"):
                self.disease_func.send_keys(DiseaseElements.abbreviation_value, abbreviation)
        if other_name:
            with allure.step("步骤：输入其他名称"):
                self.disease_func.send_keys(DiseaseElements.other_name_value, other_name)
        if disease_coding:
            with allure.step("步骤：选择ICD10编码"):
                self.disease_func.click(DiseaseElements.disease_coding_key)

        # 2.提交保存
        with allure.step("步骤：点击确认"):
            self.disease_func.click(DiseaseElements.confirm)


    def search_disease(self, search_input_locator,disease_name: str, result_locator):
        """
        通过疾病名称进行搜索
        :param disease_name: 要搜索的疾病名称
        """
        self.search.public_search_function(search_input_locator, disease_name)
        reulst = self.search.get_first_search_result(result_locator)
        return reulst

    def insert_match(self):
        values = self.disease_func.find_elements(DiseaseElements.first_row_cells)
        print(values)
        text_valu = [element.text for element in values]
        print(f"第一行数据为：{text_valu}")
        # 获取表头
        #headers = driver.find_elements(By.XPATH, '//thead//tr//th')
        # 获取首行所有单元格
        #first_row_cells = driver.find_elements(By.XPATH, '//tbody//tr[1]//td')
        # 字段-元素映射
        #field_map = {h.text: cell for h, cell in zip(headers, first_row_cells)}

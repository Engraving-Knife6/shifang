from selenium.common import TimeoutException
from FunctionLayer.disease_function import DiseaseFunction
from DataLayer.ElementLocatorData.disease_element import DiseaseElements
from BasicLayer.base_page import BasePage
from Common.Utils.search import Search
from Common.Utils.match import DataComparator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class DiseaseBusiness(BasePage):
    def __init__(self, driver):
        super().__init__(driver)  # 调用父类 BasePage 的 __init__ 方法，初始化 wait 等属性
        self.driver =driver
        # 初始化功能层对象
        self.disease_busi = DiseaseFunction(driver)
        self.search = Search(driver)
        self.datacompartor = DataComparator(driver)
        # 基础操作实例（用于业务层内的校验操作）
        #self.base_page = self.disease_busi.disease_busi

    # ------------------------------
    # 业务场景1：新增疾病分型（主流程+统一校验）
    # ------------------------------
    def add_disease_business(self,
                             disease_abb: str = None,
                             disease_name: str = None,
                             parent_abb: bool = False,
                             eng_name: str = None,
                             abbreviation: str = None,
                             other_name: str = None,
                             disease_coding: bool = False):
        """
        新增疾病分型完整业务流程
        包含：调用功能层新增操作 + 统一校验结果
        """
        # 1. 调用功能层的新增方法
        self.disease_busi.add_disease(
            disease_abb=disease_abb,
            disease_name=disease_name,
            parent_abb=parent_abb,
            eng_name=eng_name,
            abbreviation=abbreviation,
            other_name=other_name,
            disease_coding=disease_coding
        )

        # 2. 业务层统一校验（所有用例共用）
        self._check_add_success()





    # ------------------------------
    # 业务场景2：新增必填项校验（可复用的异常场景）
    # ------------------------------
    def add_disease_required_check(self,
                                   disease_abb: str = None,
                                   disease_name: str = None,
                                   parent_abb: bool = False
                                   ):
        """
        校验新增疾病分型时，必填项为空是否会提示错误
        """
        # 调用功能层操作（不传必填参数）
        self.disease_busi.add_disease(
            disease_abb=disease_abb,
            disease_name=disease_name,
            parent_abb = parent_abb
        )

        # 校验必填项提示
        self._check_required_tips(disease_abb, disease_name, parent_abb)

    # ------------------------------
    # 公共校验方法（所有业务场景共用）
    # ------------------------------
    def _check_add_success(self):
        """校验新增成功（所有新增用例共用）"""
        # 示例：校验成功提示、列表数据
        try:
            # 1. 等待提示元素出现并获取文本
            megs_element = WebDriverWait(self.driver, timeout=10).until(
                ec.presence_of_element_located(DiseaseElements.insert_megs)
            )
            megs = megs_element.text.strip()  # 加strip()处理前后空格更稳妥

            # 2. 校验文本是否符合预期
            if megs == "添加成功":
                print("新增疾病分型操作成功！")
                return True
            else:
                # 文本不匹配，直接抛出断言错误
                assert False, f"新增疾病分型操作失败，当前提示消息为[{megs}], 期待消息为【添加成功】"

        except TimeoutException:
            # 元素找不到/超时的场景
            assert False, "新增疾病分型操作失败：未找到操作结果提示消息"



    def _check_required_tips(self, disease_abb, disease_name, parent_abb):
        """校验必填项提示（所有必填项用例共用）"""
        if disease_abb == None:
            megs = self.find_element(DiseaseElements.disease_abb_value_check).text
            assert "不能为空" ==  megs,f"[疾病简称]必填项为空时，缺少提示"

        if disease_name == None:
            megs = self.find_element(DiseaseElements.disease_name_value_check).text
            assert "不能为空" ==  megs,f"[疾病名称]必填项为空时，缺少提示"

        if disease_name == False:
            megs = self.find_element(DiseaseElements.parent_abb_value_check).text
            assert "不能为空" ==  megs,f"[父级简称]必填项为空时，缺少提示"

        #assert self.base_page.is_element_present(DiseaseElements.required_tips, timeout=5), "未找到必填项提示"

    # 还需要校验列表页，用唯一字段搜索，不要直接拿第一条,，来确认新增数据是否出现在列表页。记得先执行刷新操作
    # 校验列表页是否匹配到新增数据。记得刷新页面

    def search_disease_business(self, search_input_locator,disease_name: str, result_locator):

        """
        业务层封装搜索功能
        """

        result = self.disease_busi.search_disease(search_input_locator,disease_name, result_locator)
        # result = self.disease_busi.get_first_search_result()
        assert disease_name in result, f"搜索结果中未找到疾病名称 [{disease_name}]"

    #def insert_macth(self, list_elements, expected_data=None):
    def insert_macth(self, except_data):
        result = self.disease_busi.insert_match(except_data)
        if result:
            print("页面输入数据与页面显示数据一致")
        #actual_data = self.datacompartor.get_first_list_item(list_elements)
        #print(actual_data)
        #self.datacompartor.compare_data(expected_data, actual_data)
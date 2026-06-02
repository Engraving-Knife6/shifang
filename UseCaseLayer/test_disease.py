import pytest
import allure
from BusinessLayer.disease_business import DiseaseBusiness
from Common.Utils.data_reader_new import read_module_data
from DataLayer.ElementLocatorData.disease_element import DiseaseElements


allure.feature("疾病分型模块")
@pytest.mark.usefixtures("capture_screenshot", "homep_disase")
class TestDisease:
    # 读取疾病模块的新增疾病数据
    all_data = read_module_data("disease")["disease_add_data"]
    """
    用 pytest 标记，只跑特定数据（适合长期维护）
    给你要跑的那条数据加个标记，在 yaml 里加个字段：
    """
    test_data = [item for item in all_data if item.get("run", False)]
    # 参数化;用多组数据（test_data）自动跑同一个测试函数，每组数据算一条用例；ids 给每条用例起个好认的名字。
    @pytest.mark.parametrize("case", test_data, ids=[x["case_name"] for x in test_data])
    @allure.story("新增疾病分型")
    @allure.title("填写疾病分型所有字段数据")
    def test_add_disease(self, browser, orginal_handle, case):
        # 初始化业务层
        business = DiseaseBusiness(browser)
        # 直接调用业务层方法，自动完成操作+校验
        """business.add_disease_business(
            disease_abb="GXY",
            disease_name="高血压",
            eng_name="Hypertension",
            parent_abb= True
        )"""
        business.add_disease_business(
            disease_abb=case["disease_abb"],
            disease_name=case["disease_name"],
            parent_abb=case["parent_abb"],
            eng_name=case["eng_name"],
            abbreviation = case["abbreviation"],
            other_name = case["other_name"],
            disease_coding = case["disease_coding"]
        )


    """def test_add_disease_required(disease_page_fixture):
        business = DiseaseBusiness(disease_page_fixture)
        # 校验必填项为空的场景
        business.add_disease_required_check(disease_abb="GXY")"""

    # 读取疾病模块的搜索测试数据
    all_data = read_module_data("disease")["search_data"]
    test_data = [item for item in all_data if item.get("run", False)]
    @pytest.mark.parametrize("case", test_data, ids=[x["case_name"] for x in test_data])
    @allure.story("搜索疾病分型")
    @allure.title("通过疾病名称搜索")
    def test_search_disease(self, browser, orginal_handle, case):
        business = DiseaseBusiness(browser)
        disease_name = case["disease_name"]

        # 执行搜索
        business.search_disease_business(DiseaseElements.search_input, disease_name, DiseaseElements.search_result)
        # business.disease_busi.search_disease(disease_name)
        #business.disease_func.search_disease(disease_name)

        # 获取搜索结果并断言
        """result = business.disease_busi.get_first_search_result()
        assert disease_name in result, f"搜索结果中未找到疾病名称 [{disease_name}]"
"""



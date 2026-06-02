import pytest
import allure
from BusinessLayer.page_redirection_business import PageRedirectionBusiness


@allure.feature("试航菜单项")
@pytest.mark.usefixtures("capture_screenshot")
class Testpageredirec:
    @allure.story("菜单项跳转校验")
    def test_page_redirection(self, browser, login):
        redirection = PageRedirectionBusiness(browser)
        # 需要将下边步骤放在循环中执行
        redirection.test_all_menu_items_redirect()
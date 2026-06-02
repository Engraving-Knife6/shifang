import pytest
from BasicLayer.base_page import BasePage
from DataLayer.ElementLocatorData.page_locators import NavigationMenuItemLocators


# 疾病分型页面夹具
@pytest.fixture(scope="function")
def homep_disase(browser, login):
    homedis = BasePage(browser)
    homedis.click(NavigationMenuItemLocators.basic_management)
    return homedis


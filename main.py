import pytest
"""
为保证conftest生效，需要在main函数下运行测试用例代码
"""


def run_lgon_test_case():
    """运行 deprecate_test_loginpytest.py 中的测试用例"""
    # 定义 pytest 运行参数（列表格式）
    # -v: 详细模式（显示每个用例的执行结果）
    # -s: 显示测试中的 print 输出（若有）
    # "UseCaseLayer/login_function.py": 要运行的测试文件路径
    pytest_args = ["-v", "-s", "UseCaseLayer/test_login.py"]

    # 调用 pytest 主函数执行测试
    pytest.main(pytest_args)

def run_redirection_test_case():
    """运行 deprecate_test_loginpytest.py 中的测试用例"""
    # 定义 pytest 运行参数（列表格式）
    # -v: 详细模式（显示每个用例的执行结果）
    # -s: 显示测试中的 print 输出（若有）
    # "UseCaseLayer/login_function.py": 要运行的测试文件路径
    pytest_args = ["-v", "-s", "UseCaseLayer/test_page_redirection.py"]

    # 调用 pytest 主函数执行测试
    pytest.main(pytest_args)


def run_disease_test_case():
    """运行 deprecate_test_loginpytest.py 中的测试用例"""
    # 定义 pytest 运行参数（列表格式）
    # -v: 详细模式（显示每个用例的执行结果）
    # -s: 显示测试中的 print 输出（若有）
    # "UseCaseLayer/login_function.py": 要运行的测试文件路径
    pytest_args = ["-v", "-s", "UseCaseLayer/test_disease.py"]

    # 调用 pytest 主函数执行测试
    pytest.main(pytest_args)
# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    #run_lgon_test_case()
    #run_redirection_test_case()
    run_disease_test_case()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助

import yaml
import os

def read_yaml(file_path):
    """读取任意 yaml 文件"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"文件不存在：{file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

# 快捷方法：按模块名读取
def read_module_data(module_name):
    """
    module_name: disease / user / order / common
    """
    path = os.path.join("DataLayer/TestData", f"{module_name}_data.yaml")
    return read_yaml(path)
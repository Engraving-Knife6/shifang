import yaml
from pathlib import Path


def read_login_data():
    # 定义一个名为 read_login_data 的函数，用于封装读取登录测试数据的逻辑。
    """
    __file__：当前脚本（data_reader.py）的绝对路径。
    Path(__file__).parent：当前脚本所在的目录（父目录）。
    .parent.parent：当前脚本目录的上一级目录（祖父目录）。
    / "DataLayer" / "login_data.yaml"：拼接路径，指向 项目根目录/DataLayer/login_data.yaml（假设 data_reader.py 在 Utils 文件夹中，符合方案一的结构）。
    最终 data_path 是 YAML 数据文件的绝对路径，确保无论从哪个目录执行脚本，都能正确找到数据文件。
    """
    data_path = Path(__file__).parent.parent.parent/"DataLayer"/"TestData"/"test_data.yaml"
    with open(data_path, "r", encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        """
                调用 yaml.safe_load(f) 解析文件内容：
                f：打开的 YAML 文件对象。
                safe_load：安全地加载 YAML 数据（避免执行恶意代码），返回一个 Python 字典（或列表，根据 YAML 结构而定）。
                datas：存储解析后的测试数据（例如包含 success_login、invalid_credentials 等键的字典）。
        """

        # 将字典列表转换为参数化所需的列表（按参数名顺序提取值）
        param_data = [
            (item["username"], item["password"], item["expected_msg"])
            for item in datas["invalid_credentials"]
        ]

        return datas, param_data


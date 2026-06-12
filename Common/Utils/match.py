from BasicLayer.base_page import BasePage
class DataComparator:
    """
    数据比较工具类，用于验证列表页数据与预期值是否一致
    支持动态字段比较、格式处理和详细错误提示
    """

    def __init__(self, driver, ignore_case=False, strip_whitespace=False):
        """
        初始化比较器配置
        :param ignore_case: 是否忽略大小写比较
        :param strip_whitespace: 是否去除首尾空格
        """
        self.compare = BasePage(driver)
        self.ignore_case = ignore_case
        self.strip_whitespace = strip_whitespace

    # 数据格式化预处理
    def normalize_value(self, value):
        """
        格式化值（核心处理逻辑）
        :param value: 原始值
        :return: 格式化后的值,类型为字符串
        """
        # 格式化处理流程
        if isinstance(value, str):
            if self.strip_whitespace:
                value = value.strip()  # value去除首位空格
            if self.ignore_case:
                value = value.lower()  # value改成小写
        return value

    def get_first_list_item(self, headerlocated, cellocated):
        """
        从UI元素中提取第一条数据（示例实现）
        :return: 第一条数据的字段字典
        """
        # 获取表头元素的文本，并存储在列表中
        headers = self.compare.find_elements(headerlocated)
        text_headers = [element.text for element in headers]
        # 获取行元素的文本，并存储在列表中
        cells = self.compare.find_elements(cellocated)
        text_cell = [element.text for element in cells]


        field_map = {h.text : cell.text for h, cell in zip(headers,cells)}
        """  # 动态获取所有字段值（需根据实际UI实现）
        for field in first_item.get_all_fields():  # get_all_fields()：获取这条数据所有的字段名
            actual_data[field] = first_item.get_field_value(field)  # 获取当前字段的真实值"""

        return field_map

    # 核心功能：新增输入数据与列表显示数据匹配
    def compare_data(self, expected_data, actual_data, field_map):
        """
        核心比较方法
        :param expected_data: 新建时的预期数据（字典格式）
        :param actual_data: 列表页实际数据（字典格式）
        :return: 一致返回True，否则抛出AssertionError
        """
        mismatches = []

        # 1. 过滤预期字段：只保留页面会显示的字段,生成新字典
        filtered_expected = {
            field: expected_data[field]  # 每次遍历生成的键值对
            for field in field_map.keys()  # 遍历字典key值
            if field in expected_data  # 过滤条件：只有当这个 field 确实存在于 expected_data 中时，才保留它。
        }

        # 2. 转换实际数据的key：页面表头转化成业务字段名
        converted_actual = {}
        for business_field, display_field in field_map.items():  # items会获取字典的key和value分别赋值给business_field, display_field
            if display_field in actual_data:
                converted_actual[business_field] = actual_data[display_field]  # 把取到的值，用业务 key 存进新字典

        # 遍历所有预期字段进行比较；.items()：遍历字典，每次同时拿到字段名（key）和预期值（value）。field = 当前字段名（如 "name"）
        for field, expected_value in filtered_expected.items():
            # 获取页面字典的value
            actual_value = converted_actual.get(field)
            """
            .get(field)：安全取值：存在该字段 → 返回实际值;不存在 → 返回 None，不抛 KeyError。
            """

            # 格式化预期值和实际值
            normalized_expected = self.normalize_value(expected_value)
            normalized_actual = self.normalize_value(actual_value) if converted_actual is not None else None
            """
            如果实际值不是 None：同样用 normalize_value() 清洗，得到清洗后的实际值；
            如果实际值是 None：直接赋值 None，防止 None 调用方法抛异常。
            """

            # 预期 False / 空字符串 → 转成 -，其中经过格式化后False变成"False"，需要判断的是"False"；is 只用于判断 True/False/None
            if normalized_expected == "False" or normalized_expected == "":
                normalized_expected = "-"

            # 比较逻辑
            if normalized_actual != normalized_expected:
                mismatches.append({  # .append({})：往列表里添加一个字典
                    'field': field,  # 记录：业务字段名（英文）
                    'display_field': field_map[field],  # 记录：页面显示的表头（中文）
                    'expected': expected_value,  # 记录：预期的值（你输入的数据）
                    'actual': actual_value  # 记录：实际的值（页面上的值）
                })

        # 处理不匹配结果
        if mismatches:
            error_msg = "数据不匹配字段:\n"
            for mismatch in mismatches:
                error_msg += f"- 业务字段: {mismatch['field']} (页面表头: {mismatch['display_field']}): 预期 {mismatch['expected']} vs 实际 {mismatch['actual']}\n"
            raise AssertionError(error_msg)

        return True


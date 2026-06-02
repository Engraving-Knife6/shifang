class DataComparator:
    """
    数据比较工具类，用于验证列表页数据与预期值是否一致
    支持动态字段比较、格式处理和详细错误提示
    """

    def __init__(self, ignore_case=False, strip_whitespace=False):
        """
        初始化比较器配置
        :param ignore_case: 是否忽略大小写比较
        :param strip_whitespace: 是否去除首尾空格
        """
        self.ignore_case = ignore_case
        self.strip_whitespace = strip_whitespace

    def normalize_value(self, value):
        """
        格式化值（核心处理逻辑）
        :param value: 原始值
        :return: 格式化后的值
        """
        # 格式化处理流程
        if isinstance(value, str):
            if self.strip_whitespace:
                value = value.strip()  # value去除首位空格
            if self.ignore_case:
                value = value.lower()  # value改成小写
        return value

    def compare_data(self, expected_data, actual_data):
        """
        核心比较方法
        :param expected_data: 新建时的预期数据（字典格式）
        :param actual_data: 列表页实际数据（字典格式）
        :return: 一致返回True，否则抛出AssertionError
        """
        mismatches = []

        # 遍历所有预期字段进行比较；.items()：遍历字典，每次同时拿到字段名（key）和预期值（value）。field = 当前字段名（如 "name"）
        for field, expected_value in expected_data.items():
            # 获取实际值并格式化
            actual_value = actual_data.get(field)
            """
            .get(field)：安全取值：存在该字段 → 返回实际值;不存在 → 返回 None，不抛 KeyError。
            """

            # 格式化预期值和实际值
            normalized_expected = self.normalize_value(expected_value)
            normalized_actual = self.normalize_value(actual_value) if actual_value is not None else None
            """
            如果实际值不是 None：同样用 normalize_value() 清洗，得到清洗后的实际值；
            如果实际值是 None：直接赋值 None，防止 None 调用方法抛异常。
            """
            # 比较逻辑
            if normalized_actual != normalized_expected:
                mismatches.append({
                    'field': field,
                    'expected': expected_value,
                    'actual': actual_value
                })

        # 处理不匹配结果
        if mismatches:
            error_msg = "数据不匹配字段:\n"
            for mismatch in mismatches:
                error_msg += f"- {mismatch['field']}: 预期 {mismatch['expected']} vs 实际 {mismatch['actual']}\n"
            raise AssertionError(error_msg)

        return True

    def get_first_list_item(self, list_elements):
        """
        从UI元素中提取第一条数据（示例实现）
        :param list_elements: 列表页元素对象（需实现get_field_value方法）
        :return: 第一条数据的字段字典
        """
        if not list_elements:
            raise ValueError("列表为空，未找到数据项")

        first_item = list_elements[0]
        actual_data = {}

        # 动态获取所有字段值（需根据实际UI实现）
        for field in first_item.get_all_fields():  # get_all_fields()：获取这条数据所有的字段名
            actual_data[field] = first_item.get_field_value(field)  # 获取当前字段的真实值

        return actual_data

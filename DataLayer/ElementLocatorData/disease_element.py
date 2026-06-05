from selenium.webdriver.common.by import By


class DiseaseElements:
    # 定位疾病分型模块元素
    insert_but = (By.XPATH, "//span[normalize-space (text()) = '新增']")  # 新增疾病分型按钮;匹配时去除文本前后空格，再定位
    insert_pop_title = (By.XPATH, "//div[text() = '新增疾病分型']")       # 新增弹窗标题
    close_but = (By.XPATH, "//button[@aria-label = 'close']")  # 弹窗关闭按钮定位；aria-label="close" 是专门给屏幕阅读器用的语义化属性，不会因为样式变化而改变，是这类无文本按钮的首选定位方式。
    cancel = (By.XPATH, "//span[text() = '取消']")  # 弹窗取消按钮
    confirm = (By.XPATH, "//span[text() = '确认']")  # 弹窗确认按钮
    disease_abb_key = (By.XPATH, "//label[.//span[text() = '疾病简称']]//span[@class = 'n-form-item-label__asterisk']")  #逻辑：先找到包含 “疾病简称” 文本的 label，再从这个 label 内部定位星号的 span。
    disease_abb_value = (By.XPATH, "//input[@placeholder = '请输入不超过50字的简称']")  # 疾病简称输入框
    disease_name_key = (By.XPATH, "//label[.//span[text() = '疾病名称']]//span[@class = 'n-form-item-label__asterisk']")
    disease_name_value = (By.XPATH, "//input[@placeholder = '请输入不超过50字的名称']")  # 疾病名称输入框
    parent_abb_key = (By.XPATH, "//label[.//span[text() = '父级简称']]//span[@class = 'n-form-item-label__asterisk']")
    parent_abb_value = (By.XPATH, "//div[text() = '父级简称']")  # 定位父级简称下拉框
    eng_name_key = (By.XPATH, "//span[@class='n-form-item-label__text' and  text() = '英文名称']")  #定位英文名称字段
    eng_name_value = (By.XPATH, "//input[@placeholder = '英文名称']")  #定位英文名称输入框
    abbreviation_key = (By.XPATH, "//span[@class='n-form-item-label__text' and  text() = '缩写']")  #定位缩写字段
    abbreviation_value = (By.XPATH, "//input[@placeholder = '缩写']")  #定位缩写输入框
    other_name_key = (By.XPATH, "//span[@class='n-form-item-label__text' and  text() = '其他名称']")  #定位其他名称字段
    other_name_value = (By.XPATH, "//input[@placeholder = '其他名称']")  #定位其他名称输入框
    disease_coding_key = (By.XPATH, "//span[@class='n-form-item-label__text' and  text() = '关联ICD疾病编码']")  #定位疾病编码字段
    disease_coding = (By.XPATH, "//div[text() = 'ICD编码']")  #定位疾病编码输入框
    insert_megs = (By.XPATH, "//div[text() = '添加成功']")  #定位新增成功的提示消息
    # 疾病简称为空时的提醒校验。//label[.//span[text() = '疾病简称']]表示查找包含span[text() = '疾病简称'的label的标签；
    # /following-sibling::div表示查询当前节点后面div的兄弟节点
    disease_abb_value_check = (By.XPATH, "//label[.//span[text() = '疾病简称']]/following-sibling::div//div[text()='不能为空']")
    # 疾病名称为空时的提醒校验
    disease_name_value_check = (By.XPATH, "//label[.//span[text() = '疾病名称']]/following-sibling::div//div[text()='不能为空']")
    # 父级简称为空时的提醒校验
    parent_abb_value_check = (By.XPATH, "//label[.//span[text() = '父级简称']]/following-sibling::div//div[text()='不能为空']")
    top = (By.XPATH, "//div[text() = '顶级']")  # 父级简称“顶级“菜单项定位

    # 搜索框定位及搜索结果定位
    search_input = (By.XPATH, "//input[@placeholder = '请输入疾病名称']")  # 搜索框定位
    #search_button = (By.XPATH, "//span[text() = '搜索']")  # 搜索按钮定位
    search_result = (By.XPATH, "//div[contains(@class, 'n-data-table')]//td[3]")  # 搜索结果定位（疾病名称在第3列）
    first_row_cells = (By.XPATH, "//tbody//tr[1]//td[position()>=2 and position()<=8]")
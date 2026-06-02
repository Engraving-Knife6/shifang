from selenium.webdriver.common.by import By


class LoginLocators:
    #登录页面元素定位
    username = (By.XPATH, "//input[starts-with(@placeholder,'请输入用户名')]")  # 用户名输入框
    password = (By.XPATH, "//input[starts-with(@placeholder,'请输入密码')]")      # 密码输入框
    loginbut = (By.XPATH, "//span[text()='登录']")
    rembut = (By.XPATH, "//span[@class = 'ep-checkbox__inner']")
    loginass = (By.XPATH, "//img[@alt = 'logo']")
    #wrongpas = (By.XPATH, "//p[text() = '用户名或密码错误，请重新输入']")
    wrongpas = (By.XPATH, "//p[@class = 'ep-message__content']")
    empty_username_err = (By.XPATH, "//div[contains(text(),'请输入用户名')]")  # 用户名为空的提示
    empty_password_err = (By.XPATH,"//div[contains(text(),'请输入密码')]")  # 密码为空的提示
    usename_notexist = (By.XPATH, "//p[text() = '用户名不存在，请重新输入']")
    accountsuspension = (By.XPATH, "//p[text() = '您的账号已被停用，请联系管理员']")
    title = (By.XPATH, "//h1[text() = ' 账号登录 ']")

class NavigationMenuItemLocators:
    # 系统一级导航菜单项和二级菜单项定位
    catalogue = (By.XPATH, "//span[text()='目录']")
    homepage = (By.XPATH, "//span[text()='主页']")
    platform = (By.XPATH, "//span[text()='平台']")
    persionalsettings = (By.CSS_SELECTOR, 'div.utility-item.p-1:nth-of-type(4)')  # 基础设置页面按钮
    homepage2 = (By.XPATH, "//div[text()='首页']")
    clinical_trial = (By.XPATH, "//div[text()='临床试验']")
    patient_management = (By.XPATH, "//div[text()='患者管理']")
    treatment_management = (By.XPATH, "//div[text()='疗程管理']")
    solution_management = (By.XPATH, "//div[text()='方案管理']")
    basic_management = (By.XPATH, "//div[text()='基础数据']")

    # 校验元素
    homepage_chek = (By.XPATH, "//span[text() = '简洁回答']")

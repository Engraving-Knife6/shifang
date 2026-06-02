from selenium import webdriver


#配置Google浏览器
def confige():
    """webdriver.ChromeOptions是Selenium WebDriver库中的一个类，用于配置Chrome浏览器的选项。通过这个类，
    可以设置Chrome浏览器的启动参数、扩展程序、代理、用户数据等，从而实现更加灵活的自动化测试，提高测试效率和可靠性‌"""
    option=webdriver.ChromeOptions()


    #设置浏览器自动关闭
    option.add_experimental_option("detach",True)
    #浏览器最大化
    option.add_argument('--start-maximized')
    #保证打开的浏览器是当前使用的配置，不是初始化的配置
    option.add_argument(r'--user-data-dir=D:\mychromedata')
    #当浏览器存在禁止自动化检测时，使用如下代码通过禁止
    option.add_experimental_option("excludeSwitches",['enable-automation'])

    #将配置完成的对象实例化，同时将配置参数传递
    driver=webdriver.Chrome(options=option)


    #打开浏览器时先清除浏览器存在的cookie信息
    driver.delete_all_cookies()
    driver.get('http://10.61.60.71:6075/')

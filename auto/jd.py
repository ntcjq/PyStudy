from selenium import webdriver
from selenium.webdriver.support.ui import Select

options = webdriver.ChromeOptions()
#执行完不关闭浏览器
options.add_experimental_option('detach', True)
#最大化界面
options.add_argument("--start-maximized")

def main():
    browser = webdriver.Chrome(options)  # 打开Chrome浏览器
    browser.get('https://www.jd.com')  # 打开京东官网
    login_link = browser.find_element_by_link_text('你好，请登录')  # 找到登录链接
    login_link.click()  # 点击登录链接
    username = browser.find_element_by_id('loginname')  # 找到用户名输入框
    username.send_keys('your username')  # 在用户名输入框输入用户名
    password = browser.find_element_by_id('nloginpwd')  # 找到密码输入框
    password.send_keys('your password')  # 在密码输入框输入密码
    submit_btn = browser.find_element_by_id('loginsubmit')  # 找到提交按钮
    submit_btn.click()  # 点击提交按钮

    search_input = browser.find_element_by_id('key')  # 找到搜索框
    search_input.send_keys('iPhone 13')  # 在搜索框中输入要购买的商品
    search_btn = browser.find_element_by_class_name('button')  # 找到搜索按钮
    search_btn.click()  # 点击搜索按钮

    # 进入商品页面，以下代码以第一个搜索结果为例
    search_result = browser.find_element_by_class_name('gl-item')
    search_result_link = search_result.find_element_by_css_selector('.p-name a')  # 找到商品链接
    search_result_link.click()  # 点击商品链接

    # 选择商品规格和购买数量
    spec_select = Select(browser.find_element_by_id('choose-type'))  # 找到商品规格下拉框
    spec_select.select_by_visible_text('金色/官方标配')  # 选择金色/官方标配
    quantity_input = browser.find_element_by_id('buy-num')  # 找到购买数量输入框
    quantity_input.clear()  # 清空输入框中原有的数量
    quantity_input.send_keys('2')  # 在输入框中输入购买数量

    # 加入购物车
    add_to_cart_btn = browser.find_element_by_id('InitCartUrl')  # 找到加入购物车按钮
    add_to_cart_btn.click()  # 点击加入购物车按钮

    # 进入购物车页面
    cart_link = browser.find_element_by_class_name('msku-cart')  # 找到购物车链接
    cart_link.click()  # 点击购物车链接

    # 结算并提交订单
    settlement_btn = browser.find_element_by_class_name('submit-btn')  # 找到结算按钮
    settlement_btn.click()  # 点击结算按钮

    submit_order_btn = browser.find_element_by_id('order-submit')  # 找到提交订单按钮
    submit_order_btn.click()  # 点击提交订单按钮

if __name__ == "__main__":
    main()
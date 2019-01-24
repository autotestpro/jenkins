import allure


def test_a():
    print("aaa")
    assert 1


@allure.step(title="测试步骤001")
def test_b():
    allure.attach('输入用户名', '我是测试步骤001的描述～～～')
    print("用户名")
    allure.attach('输入密码', '我是测试步骤002的描述～～～')
    print("密码")
    allure.attach('点击登陆', '我是测试步骤003的描述～～～')
    print("登陆")
    assert 0
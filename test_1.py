import yaml
import time

from conftest import exp_res1, exp_res2, save_btn_selector

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


class TestNegative:
    def test_step1(self, site, x_selector1, x_selector2, x_selector3, btn_selector, exp_res1):
        input1 = site.find_element("xpath", x_selector1)
        input1.send_keys("test")
        input2 = site.find_element("xpath", x_selector2)
        input2.send_keys("test")
        btn = site.find_element("css", btn_selector)
        btn.click()
        err_label = site.find_element("xpath", x_selector3)
        text = err_label.text
        assert text == exp_res1


class TestPositive:
    def login(self, site, x_selector1, x_selector2, btn_selector):
        input1 = site.find_element("xpath", x_selector1)
        input1.clear()
        input1.send_keys(testdata["username"])
        input2 = site.find_element("xpath", x_selector2)
        input2.clear()
        input2.send_keys(testdata["password"])
        btn = site.find_element("css", btn_selector)
        btn.click()

    def test_step1(self, site, x_selector1, x_selector2, x_selector4, btn_selector, exp_res2):
        self.login(site, x_selector1, x_selector2, btn_selector)
        user_label = site.find_element("xpath", x_selector4)
        text = user_label.text
        assert text == exp_res2

    def test_step2(self, site, x_selector1, x_selector2, btn_selector, plus_btn_selector, x_selector5,
                   save_btn_selector,
                   post_title_selector, exp_res3):
        self.login(site, x_selector1, x_selector2, btn_selector)
        plus_btn = site.find_element("xpath", plus_btn_selector)
        plus_btn.click()
        input5 = site.find_element("xpath", x_selector5)
        input5.clear()
        input5.send_keys(testdata["title"])
        save_btn = site.find_element("xpath", save_btn_selector)
        save_btn.click()
        time.sleep(5)
        post_title = site.find_element("xpath", post_title_selector)
        text2 = post_title.text
        assert text2 == exp_res3

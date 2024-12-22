import pytest
from module import Site
import yaml

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

name = testdata["username"]


@pytest.fixture()
def site():
    site_instance = Site(testdata["address"])
    yield site_instance
    site_instance.quit()


@pytest.fixture()
def x_selector1():
    return """//*[@id="login"]/div[1]/label/input"""


@pytest.fixture()
def x_selector2():
    return """//*[@id="login"]/div[2]/label/input"""


@pytest.fixture()
def x_selector3():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""


@pytest.fixture()
def btn_selector():
    return """button"""


@pytest.fixture()
def exp_res1():
    return "401"


@pytest.fixture()
def x_selector4():
    return """//*[@id="app"]/main/nav/ul/li[3]/a"""


@pytest.fixture()
def exp_res2():
    return f"Hello, {name}"


@pytest.fixture()
def plus_btn_selector():
    return """//*[@id="create-btn"]"""


@pytest.fixture()
def x_selector5():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""


@pytest.fixture()
def save_btn_selector():
    return """//*[@id="create-item"]/div/div/div[7]/div/button/span"""


@pytest.fixture()
def post_title_selector():
    return """//*[@id="app"]/main/div/div[1]/h1"""


@pytest.fixture()
def exp_res3():
    return testdata["title"]

import pytest
from _pytest.fixtures import fixture
from selenium.webdriver import Keys

from pages.home_page import HomePage


@fixture(scope='module')
def get_key_presses_page(get_app):
    app = get_app
    app.home_page.key_presses_link.click()
    yield app


tests_1 = [(chr(i), chr(i)) for i in range(0, 128)]


@pytest.mark.parametrize('key, expected_text', tests_1)
def test_key_press_01(get_key_presses_page, key, expected_text):
    app = get_key_presses_page

    assert app.key_presses_page.input.is_displayed()

    app.key_presses_page.input.click()
    app.key_presses_page.input.send_keys(key)

    assert app.key_presses_page.result.text == f"You entered: {expected_text}"


# tests_2 = [(name, name) for name, value in vars(Keys).items() if not name.startswith('_')]
tests_2 = [(Keys.ESCAPE, "ESCAPE"),
           (Keys.F10, "F10"),
           (Keys.UP, "UP"),
           (Keys.DOWN, "DOWN"),
           ]


@pytest.mark.parametrize('key, expected_text', tests_2)
def test_key_press_02(get_key_presses_page, key, expected_text):
    app = get_key_presses_page

    assert app.key_presses_page.input.is_displayed()

    app.key_presses_page.input.click()
    app.key_presses_page.input.send_keys(key)

    assert app.key_presses_page.result.text == f"You entered: {expected_text}"

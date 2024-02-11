import pytest

from settings import BASE_URL


@pytest.mark.parametrize('code', [200, 301, 404, 500])
def test_status_codes_page(get_app, code):
    app = get_app
    app.home_page.status_codes_link.click()
    app.status_codes_page.code_number(code).click()
    assert app.status_codes_page.get_url() == BASE_URL + f'status_codes/{code}'
    assert f"This page returned a {code} status code." in app.status_codes_page.content.text

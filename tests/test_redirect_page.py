def test_redirect_page(get_app):
    app = get_app
    app.home_page.redirect_link.click()
    app.redirector_page.redirect_link.click()
    assert app.status_codes_page.code_200.is_displayed()
    assert app.status_codes_page.page_name.text == "Status Codes"

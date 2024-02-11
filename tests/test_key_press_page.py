def test_key_press(get_app):
    app = get_app
    app.home_page.key_presses_link().click()
    # assert app.key_presses_page.input.is_displayed()

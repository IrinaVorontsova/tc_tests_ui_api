from selene import have


class SwitchToWindow:

    @staticmethod
    def get_main_window(setup_browser):
        return setup_browser.current_window_handle

    @staticmethod
    def get_all_window(setup_browser):
        return setup_browser.window_handles

    @staticmethod
    def switch_new_window(setup_browser, element, text):

        old_window = setup_browser.driver().current_window_handle
        element.click()

        list_handles = setup_browser.driver().window_handles

        if list_handles[0] == old_window:
            new_window = list_handles[1]
        else:
            new_window = list_handles[0]

        setup_browser.driver().switch_to.window(new_window)
        element.should(have.text(text))
        setup_browser.close()

        setup_browser.driver().switch_to.window(old_window)

    @staticmethod
    def switch_to_windows_selene(setup_browser, element, text):
        element.click()
        setup_browser.switch_to_next_tab()
        element.should(have.text(text))
        setup_browser.close_current_tab()
        setup_browser.switch_to_previous_tab()



class SwitchToWindow:

    def __init__(self, setup_browser):
        self.setup_browser = setup_browser

    @staticmethod
    def get_main_window(setup_browser):
        return setup_browser.current_window_handle

    @staticmethod
    def get_all_window(setup_browser):
        return setup_browser.window_handles

    def switch_new_window(self, setup_browser):
        main_window = self.get_main_window(setup_browser)
        list_handles = self.get_all_window(setup_browser)

        for handle in list_handles:
            if(handle != main_window):
                setup_browser.switch_to.window(handle)

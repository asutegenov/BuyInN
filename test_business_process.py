from pages.main_page import MainPage
from datetime import datetime
from pages.business_process import CheckBusinessProcess

class TestCheckSearchPanel():
    def test_check_search_panel(self, browser):
        start_time = datetime.now().timestamp()

        link = "https://buy-in-10-seconds.company.site/search"
        page = MainPage(browser, link)
        page.open()

        business_process = CheckBusinessProcess(browser, browser.current_url)

        business_process.search_page()
        business_process.basket_page()

        print('::-> ТЕСТ УСПЕШНО ПРОЙДЕН <-::')
        print("ВРЕМЯ ВЫПОЛНЕНИЯ::{:.3f}s".format(datetime.now().timestamp() - start_time))

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.locators import SearchLocators, BasketLocators
import time

class CheckBusinessProcess(BasePage):
    name_select_items = ''
    def search_page(self):

        temp_duration = self.browser.execute_script('return performance.getEntriesByName(window.location)[0].duration;')/1000
        duration_time = (temp_duration * 10 ** 10 // 10 ** (10 - 3) / 10 ** 3)
        print(f"::ВРЕМЯ ЗАГРУЗКИ СТРАНИЦЫ: {duration_time:.1f}s")

        input_search = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((*SearchLocators.INPUT_SEARCH,)))
        input_search.send_keys('товар')
        input_search.send_keys(Keys.ENTER)

        time.sleep(.5)

        input_from_cost = self.browser.find_element(*SearchLocators.INPUT_FROM_COST)
        input_from_cost.send_keys('1')

        input_to_cost = self.browser.find_element(*SearchLocators.INPUT_TO_COST)
        input_to_cost.send_keys('4')
        input_to_cost.send_keys(Keys.ENTER)

        time.sleep(.5)

        input_in_stock = self.browser.find_element(*SearchLocators.INPUT_IN_STOCK)
        input_in_stock.click()

        self.browser.implicitly_wait(5)
        
        try:
            check_hight_and_low_cost = self.browser.find_element(*SearchLocators.INPUT_COST_HIGH_LOW)
            check_hight_and_low_cost.click()
        except Exception as e:
            click_on_sort = self.browser.find_element(*SearchLocators.SORT_OPEN)
            try:
                click_on_sort.click()
            except Exception as a:
                self.browser.execute_script('arguments[0].click();', click_on_sort)

            check_hight_and_low_cost = self.browser.find_element(*SearchLocators.INPUT_COST_HIGH_LOW)
            check_hight_and_low_cost.click()
        
        time.sleep(.5)

        copy_items_name = self.browser.find_element(*SearchLocators.FIRST_ITEMS_NAME)
        self.name_select_items = copy_items_name.text
        print(self.name_select_items)

        click_on_first_element = self.browser.find_element(*SearchLocators.SELECT_FIRST_ITEMS)
        click_on_first_element.click()

        self.browser.implicitly_wait(5)
    
    def basket_page(self):
        click_on_in_basket = WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((*BasketLocators.IN_BASKET,)))
        click_on_in_basket.click()

        self.browser.implicitly_wait(5)

        click_on_basket_icon = self.browser.find_element(*BasketLocators.GO_TO_BASKET)
        self.browser.execute_script('arguments[0].click();', click_on_basket_icon)

        self.browser.implicitly_wait(5)

        name_items = WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((*BasketLocators.NAME_ITEM_SELECT_BASKET,)))

        assert name_items.text == self.name_select_items, 'Название выбранного товара не совпадает с названием товара в корзине!'

from selenium.webdriver.common.by import By

class SearchLocators():
    INPUT_SEARCH = (By.XPATH, '//*[@id="ecwid-products"]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div[3]/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/input')
    INPUT_FROM_COST = (By.XPATH, '//*[@id="ecwid-products"]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div[3]/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/input')
    INPUT_TO_COST = (By.XPATH, '//*[@id="ecwid-products"]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div[3]/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div[1]/div[3]/input')
    INPUT_IN_STOCK = (By.XPATH, '//*[@id="checkbox-in_stock"]')
    SORT_OPEN = (By.XPATH, '//*[@id="ecwid-products"]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div[3]/div[6]/div[1]/div/div/div[1]')
    INPUT_COST_HIGH_LOW = (By.XPATH, '//*[@id="ecwid-products"]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div[3]/div[6]/div[2]/div/div[1]/div/div[2]/div/div/label[4]/div')
    FIRST_ITEMS_NAME = (By.XPATH, '//*[@id="ecwid-products"]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/a[2]/div')
    SELECT_FIRST_ITEMS = (By.XPATH, '//*[@id="ecwid-products"]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]')

class BasketLocators():
    IN_BASKET = (By.XPATH, '//*[@id="ecwid-products"]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div[3]/div[4]/div[2]/div/div[1]/div/div[2]/button')
    GO_TO_BASKET = (By.XPATH, '//*[@id="ecwid_body"]/div[3]/div[2]/div/div[1]/div[1]/div')
    NAME_ITEM_SELECT_BASKET = (By.XPATH, '//*[@id="ecwid-products"]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/a')
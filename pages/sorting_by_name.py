from selenium.webdriver.support.select import Select


class SortingResultsByName:

    def __init__(self, driver):
        self.driver = driver
        self.select_product_sort_id = "selectProductSort"
        self.switch_to_list_css = ".icon-th-list"
        self.product_names_xpath = "//h5[@itemprop='name']//a"

    def select_sorting_by(self, sort_type):
        self.driver.find_element_by_id(self.select_product_sort_id).click()
        select = Select(self.driver.find_element_by_id(self.select_product_sort_id))
        select.select_by_visible_text(sort_type)

    def switch_to_list(self):
        self.driver.find_element_by_css_selector(self.switch_to_list_css)

    def get_product_names(self):
        products = self.driver.find_elements_by_xpath(self.product_names_xpath)
        products_names = [product.get_attribute("text").strip() for product in products]
        return products_names







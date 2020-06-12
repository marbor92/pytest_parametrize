class SearchProduct:

    def __init__(self, driver):
        self.driver = driver
        self.product_name_input_css = "input[name=search_query]"
        self.product_search_submit_name = "submit_search"
        self.search_result_desc_css = ".lighter"

    def product_search(self, product_name):
        self.driver.find_element_by_css_selector(self.product_name_input_css).send_keys(product_name)
        self.driver.find_element_by_name(self.product_search_submit_name).click()

    def find_product_name(self):
        found_product = self.driver.find_element_by_css_selector(self.search_result_desc_css)
        return found_product.get_attribute("textContent")


import pytest
from pages.search_product import SearchProduct
from pages.sorting_by_name import SortingResultsByName


@pytest.mark.usefixtures("setup")
class TestProductSortBy:
    test_data = [
        ('Product Name: A to Z', 0, 0),
        ('Product Name: Z to A', 0, -1),
    ]

    @pytest.mark.parametrize("sort_type, index1, index2", test_data, ids=["A_to_Z", "Z_to_A"])
    def test_sorting_by_name(self, sort_type, index1, index2):
        self.driver.get("http://automationpractice.com/index.php")
        search_product_page = SearchProduct(self.driver)
        search_product_page.product_search("dress")
        product_sorting = SortingResultsByName(self.driver)
        product_sorting.select_sorting_by(sort_type)
        product_sorting.switch_to_list()
        product_names = product_sorting.get_product_names()
        sorted_products_names = sorted(product_names)

        assert product_names[index1] == sorted_products_names[index2]

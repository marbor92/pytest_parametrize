import pytest
from pages.search_product import SearchProduct


@pytest.mark.usefixtures("setup")
class TestProductSearch:

    @pytest.mark.parametrize(
        "product_name, result",
        [
            ('t-shirt', 't-shirt'),
            pytest.param('dress', 'dress', marks=pytest.mark.basic, id="product_found"),
            pytest.param('jeans', 'jeans', marks=[pytest.mark.basic, pytest.mark.xfail], id="product_not_found"),
        ],
    )
    def test_product_search(self, product_name, result):
        self.driver.get("http://automationpractice.com/index.php")
        search_product_page = SearchProduct(self.driver)
        search_product_page.product_search(product_name)
        search_result = search_product_page.find_product_name()

        assert result in search_result

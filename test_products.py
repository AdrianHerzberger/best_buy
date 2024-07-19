import pytest
from products import Product, LimitedProduct, NonStockedProduct
from product_promotions import Promotion, PercentDiscount, SecondHalfPrice, ThirdOneFree
from store import Store


def test_create_product_with_invalid_details():
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)
        
def test_product_reaches_zero_quantity():
    product = Product("Mac Book Air M2", price=1450, quantity=1)
    product.buy(1)
    assert product.quantity == 0
    assert not product.is_active()

def test_product_purchase_multiple():
    product = Product("Mac Book Air M2", price=1450, quantity=10)
    total_price = product.buy(3)
    assert product.quantity == 7
    assert total_price == 1450 * 3
    
    
def test_product_purchase_larger_quantity():
    product = Product("Mac Book Air M2", price=1450, quantity=10)
    with pytest.raises(ValueError):
        product.buy(11)
        
def test_apply_promotion_and_order():
    product = Product("MacBook Air M2", price=1450, quantity=10)
    promotion = PercentDiscount("Percent Discount", 20)
    product.set_promotion(promotion)
    assert product.get_total_price(2) == 1450 * 2 * 0.8
    assert product.buy(2) == 1450 * 2 * 0.8
    assert product.quantity == 8
    
    
